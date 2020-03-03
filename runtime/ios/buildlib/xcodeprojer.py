#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Michael Krause ( http://krause-software.com/ ).
#
# You are free to use this code under the MIT license:
# http://opensource.org/licenses/MIT

# xcoderprojer.py is a script for converting project.pbxproj files
# that represent Xcode projects into one of three formats,
# commented Plist, XML and JSON.
#
# It can also be used to simply check if a project file is in the
# correct form via the lint option.
#
# Xcode uses global ids (strings of 24 hex digits) as references
# in project files. These ids are only partially random
# and they have a structure that can be constructed
# or taken apart with this script.

from __future__ import print_function

__version__ = '0.1'

import sys

if (((sys.version_info.major == 2) and (sys.version_info.minor < 7))
        or ((sys.version_info.major == 3) and (sys.version_info.minor < 2))):
    sys.stderr.write("Error: Python 2.7 or when running on Python 3 at least Python 3.2 is required to run xcodeprojer\n")
    sys.exit(1)

import os
import re
import argparse
# import unicodedata
import time
import random
import json
import datetime
import difflib
import tempfile
import codecs
from operator import xor
from io import BytesIO

from collections import OrderedDict

try:
    import xml.etree.cElementTree as ETree
except ImportError:
    import xml.etree.ElementTree as ETree


__all__ = ['parse', 'unparse', 'report_parse_status', 'projectname_for_path',
           'print_diff', 'is_global_id', 'find_projectfiles',
           'UniqueXcodeIDGenerator', 'gidfields']

PBXPROJNAME = 'project.pbxproj'

OK = 0
ERROR = 1
PARSING_FAILED = 1

LINT_DIFFERENCES = 1
LINT_FAILED = 2

CONVERT_OUTPUT_FAILED = 2


LATEST_OBJECT_VERSION = 46

STDIN = None
STDOUT = '-'

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

args_info = set([])
args_debug = set([])
args_verbose = set([])


if PY2:
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes
    unichr = chr


def unistr(text):
    if not isinstance(text, text_type):
        text = text.decode('utf-8')
    return text


def bytestr(text):
    if not isinstance(text, binary_type):
        text = text.encode('utf-8')
    return text


INFO_TIME = 'time'
INFO_BACKTRACKS = 'backtracks'
INFO_ALL = [INFO_TIME, INFO_BACKTRACKS]

verbose_categories = {
    1: [INFO_TIME],
    2: [INFO_BACKTRACKS],
}

DEBUG_OPTIONS = 'options'
DEBUG_ALL = [DEBUG_OPTIONS]


re_unescape = re.compile(r'\\\\|\\"|\\a|\\b|\\t|\\v|\\f|\\n|(?:\\U[0-9a-f]{4})')
unescape_dict = {
    '\\\\': '\\',
    '\\"': '"',
    '\\a': '\a',
    '\\b': '\b',
    '\\t': '\t',
    '\\v': '\v',
    '\\f': '\f',
    '\\n': '\n',
}

re_escape = re.compile(r'[\x00-\x1f"\\]')
escape_dict = {v: k for k, v in unescape_dict.items()}


# In comparison with unquotedstring in r_tokenize Xcode quotes
# some characters even when they are accepted in unquoted strings.
r_quoteworthy = re.compile(r'[^a-zA-Z0-9$./_]|___')
r_gid = re.compile(r'\A[0-9A-Z]{24}\Z')
r_ws = re.compile(r'\s*')

# Here we have the tokenizing expression that splits any Xcode plist
# into its tokens. We do not create tokens for whitespace because we
# don't need them and it would significantly slow the parsers down.
r_tokenize = re.compile(r"""
            (?:
              (?P<linecomment>//.*$)                      # linecomment
            | (?P<comment>/\*.*?\*/)                      # comment
                                                          # unquoted values can contain slashes so we must handle the two comment forms
                                                          # before unquotedstring.
            | (?P<unquotedstring>[$./:_a-zA-Z0-9-]+)      # unquotedstring which might be an Xcode global id (24 hex digits)
            | (?P<equals>=)                               # equals
            | (?P<semicolon>;)                            # key-value pair terminator
            | (?P<quotedstring>"(?:\\"|[^"])*")            # a doule-quoted string
            | (?P<dictionary>\{)                          # start of a dictionary
            | (?P<dictionaryend>\})                       # end of a dictionary
            | (?P<comma>,)                                # array element terminator
            | (?P<array>\()                               # start of an array
            | (?P<arrayend>\))                            # end of an array
            )
            \s*                                           # skip whitespace after each token
    """, re.MULTILINE | re.VERBOSE)


rule_mapping = r_tokenize.groupindex
rulenumber_to_name = dict((vnr, kname) for (kname, vnr) in rule_mapping.items())
rule_names = [rulenumber_to_name.get(groupnr, 'dummy') for groupnr in range(r_tokenize.groups + 1)]

RULE_COMMENT = rule_mapping['comment']
RULE_LINECOMMENT = rule_mapping['linecomment']
RULE_UNQUOTEDSTRING = rule_mapping['unquotedstring']
RULE_EQUALS = rule_mapping['equals']
RULE_SEMICOLON = rule_mapping['semicolon']
RULE_QUOTEDSTRING = rule_mapping['quotedstring']
RULE_DICTIONARY = rule_mapping['dictionary']
RULE_DICTIONARYEND = rule_mapping['dictionaryend']
RULE_COMMA = rule_mapping['comma']
RULE_ARRAY = rule_mapping['array']
RULE_ARRAYEND = rule_mapping['arrayend']


def parse(text, format=None, dictionarytype=dict, parsertype='normal'):
    """Parses the Xcode project as binary text
    and creates the tree of nested dicts, arrays and strings
    that represents the original structure.

    :param text: the content of a project.pbxproj.
    :param format: one of 'xcode', 'xml', 'json' or None for automatic detection.
    :param dictionarytype: should be dict or OrderedDict.
    :param parsertype: normal: parse plists via syntax transformation by the fast JSON parser
                               and use the classic parser if the JSON parser failed.
                       fast: only parse with the fast JSON parser.
                       classic: only parse plists with the classic parser.
    :return: the tuple (rootnode, parseinfo).
    """
    text = unistr(text)

    root, parseinfo = None, None
    can_only_be_xml = text.startswith('<?xml')
    if format == 'xml' or (format is None and can_only_be_xml):
        return parse_xcodeproject_xml(text, dictionarytype=dictionarytype)

    if format in [None, 'json']:
        root, parseinfo = parse_xcodeproject_json(text, dictionarytype=dictionarytype)
        if root is not None or format == 'json':
            return root, parseinfo

    prev_parseinfo = parseinfo
    root, parseinfo = parse_xcodeproject_plist(text, dictionarytype=dictionarytype, parsertype=parsertype)
    if prev_parseinfo is not None:
        parseinfo['prev_parseinfo'] = prev_parseinfo
    return root, parseinfo


def parse_xcodeproject_plist(text, dictionarytype=dict, parsertype='normal'):
    text = unistr(text)

    if parsertype in ['normal', 'fast']:
        # Try the JSON based plist parser first
        root, parseinfo = parse_xcodeproject_plist_via_json(text)
        if root is not None or parsertype == 'fast':
            return root, parseinfo

    if parsertype in ['normal', 'classic']:
        # If the faster JSON based plist parser failed for whatever reason we try again
        # with the classic parser which has error reporting about where the parse failed.
        root, parseinfo = parse_xcodeproject_plist_direct(text, dictionarytype=dictionarytype)
        if root is not None and parsertype == 'normal':
            # The JSON parser failed after rewriting the plist syntax
            # but the plist parser succeeded. This is strance and we register this.
            parseinfo.setdefault('warnings', []).append('Warning: the fast xcode parser failed where the classic parser succeeded.'
                                                        ' This should not happen and it would be helpful if you could report this project file.')
        return root, parseinfo
    else:
        raise ValueError("Unknown parsertype: %s" % parsertype)


def parse_xcodeproject_plist_via_json(text, dictionarytype=dict):
    """The CPython implementation comes with a fast JSON parser that is written in C.
    Instead of simply parsing the Plist we can split it into tokens with a regular expression
    and do a plist-to-json syntax transformation.
    This gives us about 80% faster parsing over our classic recursive descent parser.
    """
    t0 = time.time()
    text = unistr(text)
    tokens = []
    emit = tokens.append
    jsondumps = json.JSONEncoder().encode

    formatdesc = 'Xcode plist via JSON'
    prjname = None
    pos = skip_whitespace(text)
    for m in r_tokenize.finditer(text, pos):
        if m.start() != pos:
            # The found fragments must be contiguous for a valid parse
            return None, error_report_dict(text, m.start(), m.end(), formatdesc)

        pos = m.end()

        # For our few rules a simple if-sequence ordered by probability is faster than
        # a lookup table with associated function calls.
        # The averaged measured probabilities for the rules we are interested in were:
        # UNQUOTEDSTRING:35% SEMICOLON:20% EQUALS:20% COMMENT:9% DICTIONARY:4%
        #   DICTIONARYEND:4% COMMA:4% QUOTEDSTRING:3% ARRAY:1% ARRAYEND:1%

        # This parser variant should be fast so we leave out almost
        # all error checks which results in a very liberal parser.
        # If this plist is accepted by the JSON based parser it still might not parse in Xcode.

        rulenr = m.lastindex
        if rulenr == RULE_UNQUOTEDSTRING:
            emit('"')
            emit(m.group(rulenr))
            emit('"')
        elif rulenr == RULE_SEMICOLON:
            emit(',')
        elif rulenr == RULE_EQUALS:
            emit(':')
        elif rulenr == RULE_COMMENT:
            if prjname is None:
                prjname = projectname_from_comment(m.group(rulenr))
            continue
        elif rulenr == RULE_DICTIONARY:
            emit('{')
        elif rulenr == RULE_DICTIONARYEND:
            if tokens[-1] == ',':
                # This was probably a semicolon terminator that was transformed into a comma.
                tokens.pop()
            elif tokens[-1] != '{':
                # Neither a preceding terminator nor an empty list.
                return None, error_report_dict(text, m.start(), m.end(), formatdesc)
            emit('}')
        elif rulenr == RULE_COMMA:
            emit(',')
        elif rulenr == RULE_QUOTEDSTRING:
            emit(jsondumps(unescape_str(m.group(rulenr))))
        elif rulenr == RULE_ARRAY:
            emit('[')
        elif rulenr == RULE_ARRAYEND:
            if tokens[-1] == ',':
                tokens.pop()
            emit(']')

    try:
        jsontext = ''.join(tokens)
        root = json.loads(jsontext, object_pairs_hook=dictionarytype)
    except ValueError as e:
        linenr, column, errortext = error_report_from(formatdesc, jsontext, text_type(e))
        return None, {'error_column': column,
                      'error_line_number': linenr,
                      'error_text': errortext}

    parseinfo = {
        'format': 'xcode',
        'parsetime': time.time() - t0,
        'parser': 'fast',
    }
    if prjname is not None:
        parseinfo['projectname'] = prjname
    return root, parseinfo


def skip_whitespace(text, pos=0):
    m = r_ws.match(text, pos)
    if m is not None:
        return m.end()
    return pos


def decode_utf8_or_sys(s):
    try:
        return unistr(s)
    except UnicodeDecodeError:
        return s.decode(sys.getfilesystemencoding())


def projectname_from_comment(text):
    if text.startswith('/* Build configuration list for PBXProject'):
        qstart = text.find('"')
        qend = text.rfind('"')
        if qstart >= 0 and qend >= 0 and qstart + 1 < qend:
            return text[qstart+1:qend]
    return None


def projectname_for_path(filename):
    name, ext = os.path.splitext(os.path.basename(os.path.dirname(filename)))
    if ext not in ['.xcodeproj', '.xcode', '.pbproj', '.pbxproj']:
        return None
    return decode_utf8_or_sys(name)


def is_global_id(node):
    return r_gid.match(node) is not None


def escape_str(text):
    def replace(m):
        char = m.group(0)
        return escape_dict.get(char) or ('\\U%04x' % ord(char))

    return re_escape.sub(replace, text)


def unescape_str(s):
    def replace(m):
        txt = m.group(0)
        c = unescape_dict.get(txt)
        if c is not None:
            return c
        if s.startswith('\\U'):
            return unichr(int(txt[2:], 16))
        else:
            raise ValueError('unknown escape sequence: %s' % repr(s))

    return re_unescape.sub(replace, s[1:-1])


def quoted_string(s):
    # Xcode always quotes strings containing a triple underscore
    # because these strings are destined for textual replacement
    # with strings that may contain spaces and other quoteworthy characters.
    if not s:
        return '""'
    if r_quoteworthy.search(s) is not None:
        return '"' + escape_str(s) + '"'
    return s


def parse_xcodeproject_json(text, dictionarytype=dict):
    try:
        text = unistr(text)
        root = json.loads(text, object_pairs_hook=dictionarytype)
        parseinfo = {'format': 'json'}
        return root, parseinfo
    except ValueError as e:
        linenr, column, errortext = error_report_from('JSON', text, text_type(e))
        parseinfo = {'error_column': column,
                     'error_line_number': linenr,
                     'error_text': errortext}
        return None, parseinfo


def parse_xcodeproject_plist_direct(text, dictionarytype=dict):
    t0 = time.time()
    text = unistr(text)

    tokenrules = []
    tokentexts = []
    offsets = []
    num_comments = 0

    prjname = None
    pos = skip_whitespace(text)
    for m in r_tokenize.finditer(text, pos):
        if m.start() != pos:
            # The found fragments must be contiguous for a valid parse
            break
        rule_number = m.lastindex
        # Only count comments to eventually unparse the file
        # with or without comments depending on if there were comments.
        if rule_number == RULE_COMMENT:
            # The unparser needs the project name which should be known from the filename
            # or from a parameter that was passed in. Pulling the project name
            # out of a comment is our only other chance but still it might be wrong.
            if prjname is None:
                prjname = projectname_from_comment(m.group(rule_number))
            num_comments += 1
        elif rule_number == RULE_LINECOMMENT:
            pass
        else:
            tokenrules.append(rule_number)
            tokentexts.append(m.group(rule_number))
            offsets.append(pos)

        pos = m.end()

    lastpos = pos

    parseinfo = {'num_comments': num_comments}
    success, root = parse_tokens(tokenrules, tokentexts,
                                 dictionarytype=dictionarytype)

    if not success:
        tokenpos = errortokenpos(root)
        if tokenpos < len(tokenrules):
            errstart = offsets[tokenpos]
            errstop = errstart + len(tokentexts[tokenpos])
        else:
            errstart = errstop = lastpos
        parseinfo.update(error_report_dict(text, errstart, errstop, 'Xcode plist classically'))
        return None, parseinfo

    parseinfo = {
        'format': 'xcode',
        'parsetime': time.time() - t0,
        'parser': 'classic',
    }
    if prjname is not None:
        parseinfo['projectname'] = prjname
    return root, parseinfo


def errortokenpos(tokenoffset):
    """Find the root cause in the chain of parser errors
    and return the token position where the parser could
    no longer advance.
    """
    if isinstance(tokenoffset, ParserError):
        for prevexc in iter(lambda: tokenoffset.prevexc, None):
            tokenoffset = prevexc
        tokenoffset = tokenoffset.pos
    return tokenoffset


def error_report_dict(text, errstart, errstop, formatdesc):
    linenr, column, errortext = parse_error_report(text, errstart, errstop, formatdesc)
    return {'error_column': column,
            'error_line_number': linenr,
            'error_text': errortext}


def linenr_column_line(text, offset):
    """Return line number, column and the whole line
    in which text[offset] lies.
    Line number and column are in one-based indexing.
    Each tab is counted as one column.
    """

    offset = min(max(0, offset), len(text))
    textbegin = text[:offset]
    if not textbegin:
        return 1, 1, None
    lines = textbegin.splitlines(True)
    linenr, column = max(1, len(lines)), len(lines[-1]) + 1
    line = lines[-1]
    nlpos = text.find('\n', offset)
    if nlpos >= 0:
        line += text[offset:nlpos+1]
    else:
        line += text[offset:]
    return linenr, column, line


def parse_error_report(text, errstart, errstop, formatdesc):
    errmsg = 'Error: parsing %s failed' % formatdesc

    linenr, column, line = linenr_column_line(text, errstart)
    if line is None:
        return 1, 1, errmsg

    if errstop >= len(text):
        return linenr, column, errmsg + ', reached end of text before completing the grammar'

    # Use a line in which all printables are replaced by spaces
    # as a prefix to position the caret under the error position.
    blankline = re.sub(r'\S', ' ', line)
    blankline = blankline[:column-1]

    # We count each tab as four spaces and report the
    # column number after this expansion as this is common
    # in the column display of text editors.
    countingline = blankline.replace('\t', '    ')
    column = len(countingline) + 1

    # Draw squiggles under the offending token that
    # follows after the error position.
    errtoken = text[errstart:errstop]
    errtoken = errtoken.replace('\t', '    ')
    caretline = blankline + '^' + '~' * (len(errtoken) - 1)
    errortext = line.rstrip() + '\n' + caretline + '\n'
    errortext += errmsg

    return linenr, column, errortext


def error_report_from(format, text, errortext):
    """XML and JSON parse error texts look like this:
          not well-formed (invalid token): line 155, column 8
      or  Expecting ':' delimiter: line 14 column 32 (char 303)

    Extract the line and column information to report the offending
    line with a caret positioned under the shady character.
    """
    linepos = errortext.rfind('line')
    errmsg = 'Error: parsing %s failed' % format
    standard_error = 1, 1, errmsg
    if linepos == -1:
        return standard_error
    errortext = errortext[linepos:]
    numbers = [int(x) for x in re.split(r"[^\d]+", errortext) if x]
    if len(numbers) not in [2, 3]:  # Do we have line, column, [char]?
        return standard_error
    linenr, column = numbers[:2]

    errstart = 0
    for idx, line in enumerate(text.splitlines(True)):
        if idx + 1 == linenr:
            errstart += column - 1
            break
        errstart += len(line)
    else:
        # If the line containing the error wasn't found
        # no extended error report is genenerated
        return linenr, column, errmsg

    return parse_error_report(text, errstart, errstart, format)


class ParserError(Exception):

    def __init__(self, text, pos, prevexc=None):
        super(ParserError, self).__init__(text)
        self.pos = pos
        self.prevexc = prevexc


def parse_tokens(tokenrules, tokentexts, dictionarytype=dict):

    def inc(pos):
        return pos + 1

    def rule_at(pos):
        try:
            return tokenrules[pos]
        except IndexError:
            raise ParserError('Expecting more tokens', pos)

    def text_at(pos):
        try:
            return tokentexts[pos]
        except IndexError:
            raise ParserError('Expecting more tokens', pos)

    def skip_literal(pos, rulenr):
        if rule_at(pos) == rulenr:
            return inc(pos)
        return pos

    def musthave_literal(pos, s):
        nextpos = skip_literal(pos, s)
        if nextpos == pos:
            raise ParserError("Expecting '%s'" % s, pos)
        return nextpos

    def sequence(pos, *args):
        elements = []
        for element in args:
            if callable(element):
                r = element(pos)
                v, pos = r
                elements.append(v)
            else:
                pos = musthave_literal(pos, element)
        return elements, pos

    def zero_or_more(pos, func, nextelem):
        elements = []
        while True:
            try:
                v, pos = func(pos)
                elements.append(v)
            except ParserError as e:
                try:
                    musthave_literal(pos, nextelem)
                except ParserError as e2:
                    e2.prevexc = e
                    raise e2
                return elements, pos
        return elements, pos

    def anystring(pos):
        rulenr = rule_at(pos)
        if rulenr == RULE_UNQUOTEDSTRING:
            return unquotedstring(pos)
        elif rulenr == RULE_QUOTEDSTRING:
            return quotedstring(pos)
        raise ParserError('Expecting string', pos)

    def value(pos):
        rulenr = rule_at(pos)
        if rulenr == RULE_UNQUOTEDSTRING:
            return unquotedstring(pos)
        elif rulenr == RULE_DICTIONARY:
            return dictionary(pos)
        elif rulenr == RULE_QUOTEDSTRING:
            return quotedstring(pos)
        elif rulenr == RULE_ARRAY:
            return array(pos)
        raise ParserError('Expecting value', pos)

    def arrayvalue(pos):
        rulenr = rule_at(pos)
        if rulenr == RULE_UNQUOTEDSTRING:
            return unquotedstring(pos)
        elif rulenr == RULE_QUOTEDSTRING:
            return quotedstring(pos)
        elif rulenr == RULE_DICTIONARY:
            return dictionary(pos)
        raise ParserError('Expecting array value', pos)

    def arrayelements(pos):
        try:
            return zero_or_more(pos, arrayelement, RULE_ARRAYEND)
        except RuntimeError as exc:
            if str(exc).startswith('maximum recursion depth exceeded'):
                raise ParserError("Exceeded maximum recursion", pos)

    def arrayelement(pos):
        v, pos = arrayvalue(pos)

        p2 = skip_literal(pos, RULE_COMMA)
        if p2 > pos:
            # There is a comma after the array element
            return v, p2

        # No comma after an array element is also fine in case
        # a closing paren follows which we don't consume.
        musthave_literal(pos, RULE_ARRAYEND)
        return v, pos

    def array(pos):
        v, pos = sequence(pos, RULE_ARRAY, arrayelements, RULE_ARRAYEND)
        return v[0], pos

    def kvpair(pos):
        k, p = anystring(pos)
        p = musthave_literal(p, RULE_EQUALS)
        v, p = value(p)
        p = musthave_literal(p, RULE_SEMICOLON)
        return (k, v), p

    def kvpairs(pos):
        return zero_or_more(pos, kvpair, RULE_DICTIONARYEND)

    def dictionary(pos):
        try:
            v, pos = sequence(pos, RULE_DICTIONARY, kvpairs, RULE_DICTIONARYEND)
            return dictionarytype(v[0]), pos
        except RuntimeError as exc:
            if str(exc).startswith('maximum recursion depth exceeded'):
                raise ParserError("Exceeded maximum recursion", pos)

    def quotedstring(pos):
        v, pos = named_rule(pos, RULE_QUOTEDSTRING)
        return unescape_str(v), pos

    def unquotedstring(pos):
        return named_rule(pos, RULE_UNQUOTEDSTRING)

    def named_rule(pos, rulenr):
        if rule_at(pos) != rulenr:
            raise ParserError('Expecting rule %d' % rulenr, pos)
        return text_at(pos), inc(pos)

    def parse_xcodeplist_tokens(pos):
        try:
            root = dictionary(pos)
        except ParserError as e:
            return False, e
        if root is None:
            return False, None

        v, pos = root
        if pos != len(tokenrules):
            return False, ParserError("there are still tokens left after parsing", pos)
        return True, v

    success, root = parse_xcodeplist_tokens(0)
    return success, root


def parse_xcodeproject_xml(text, dictionarytype=dict):
    """We parse the XML format by transforming the document into a simplified plist format
    and handing this off to our plist parser.
    """

    structures = {
        'dict': '{};',
        'array': '(),',
    }

    stack = ['dummy']
    tokens = []

    def emit(s):
        tokens.append(s)

    def emit_text(s):
        emit(quoted_string(s))

    def emit_terminator(parent):
        structure_markers = structures.get(parent)
        if structure_markers is not None:
            emit(structure_markers[-1])
            emit('\n')

    def iterxml(buf):
        try:
            for event, elem in ETree.iterparse(buf, events=('start', 'end')):
                tag = elem.tag
                if event == 'start':
                    stack.append(tag)
                else:
                    stack.pop()

                parent = stack[-1]

                if event == 'end':
                    if tag == 'key':
                        emit_text(elem.text)
                        emit('=')
                    elif tag == 'string':
                        emit_text(elem.text)
                        emit_terminator(parent)

                structure_markers = structures.get(tag)
                if structure_markers:
                    if event == 'start':
                        emit(structure_markers[0])
                    else:
                        emit(structure_markers[1])
                        emit_terminator(parent)
        except ETree.ParseError as e:
            linenr, column, errortext = error_report_from('XML', text, text_type(e))
            return {'error_column': column,
                    'error_line_number': linenr,
                    'error_text': errortext}
        return None

    errorparseinfo = iterxml(BytesIO(bytestr(text)))
    if errorparseinfo is not None:
        return None, errorparseinfo

    text = ''.join(tokens)
    root, parseinfo = parse_xcodeproject_plist(text, dictionarytype=dictionarytype)
    if root is not None:
        parseinfo['format'] = 'xml'
    return root, parseinfo


# ---------------------------------------------------------------

def unparse(root, format='xcode', projectname='', disable_comments=False, parseinfo=None):
    """Generate the content of a project.pbxproj.

    :type root: the root node of the tree.
    :type format: 'xcode', 'xml', 'json'.
    :type projectname: basename of the .xcodeproj.
    :type disable_comments: don't add comments after the gids.
    :type parseinfo: if you parsed the project you can pass this from the parse result.
                     we use this to guess if comments should be recreated.
    :return:
    """
    if root is None:
        raise ValueError("root is None")
    unparserclass = unparsers.get(format)
    if unparserclass is None:
        raise ValueError('format must be one of [%s]' % ', '.join(output_formats))
    unparser = unparserclass(root)
    text = unparser.unparse(root, projectname=projectname, disable_comments=disable_comments, parseinfo=parseinfo)
    return bytestr(text)


# noinspection PySetFunctionToLiteral
class Unparser(object):
    """Creates the text representation from the parsed tree.
    """

    header = '// !$*UTF8*$!\n'
    trailer = '\n'

    keys_without_comments = frozenset([
        'remoteGlobalIDString',
        'TestTargetID',
        'TargetAttributes'
    ])

    pbx_names = {
        'PBXProject': 'Project object',
        'PBXTargetDependency': 'PBXTargetDependency',
        'PBXBuildRule': 'PBXBuildRule',
        'PBXContainerItemProxy': 'PBXContainerItemProxy',
    }

    commentpaths = frozenset(['PBXAggregateTarget.buildConfigurationList',
                              'PBXAggregateTarget.buildPhases',
                              'PBXAggregateTarget.dependencies',
                              'PBXAppleScriptBuildPhase.files',
                              'PBXBuildFile.fileRef',
                              'PBXContainerItemProxy.containerPortal',
                              'PBXCopyFilesBuildPhase.files',
                              'PBXFrameworksBuildPhase.files',
                              'PBXGroup.children',
                              'PBXHeadersBuildPhase.files',
                              'PBXLegacyTarget.buildConfigurationList',
                              'PBXNativeTarget.buildConfigurationList',
                              'PBXNativeTarget.buildPhases',
                              'PBXNativeTarget.buildRules',
                              'PBXNativeTarget.dependencies',
                              'PBXNativeTarget.productReference',
                              'PBXProject.buildConfigurationList',
                              'PBXProject.buildStyles',
                              'PBXProject.mainGroup',
                              'PBXProject.productRefGroup',
                              'PBXProject.projectReferences.ProductGroup',
                              'PBXProject.projectReferences.ProjectRef',
                              'PBXProject.targets',
                              'PBXReferenceProxy.remoteRef',
                              'PBXResourcesBuildPhase.files',
                              'PBXRezBuildPhase.files',
                              'PBXSourcesBuildPhase.files',
                              'PBXTargetDependency.target',
                              'PBXTargetDependency.targetProxy',
                              'PBXVariantGroup.children',
                              'XCBuildConfiguration.baseConfigurationReference',
                              'XCConfigurationList.buildConfigurations',
                              'XCVersionGroup.children',
                              'XCVersionGroup.currentVersion'])

    def __init__(self, root):
        if root is None:
            raise ValueError("root is None")
        self.objects = root.get('objects')
        self.keypath = []
        self.open_section = None
        self.concise_mode = 0

        self.section_for_file = {}
        self.build_configuration_lists = {}
        self.gidcomments = {}

        self.outputbuffer = None
        self.projectname = None
        self.disable_comments = None
        self.version = None
        self.last_userhash = None

    def unparse(self, root, projectname='', disable_comments=False, parseinfo=None):
        if root is None:
            return None
        try:
            self.version = int(root.get('objectVersion'))
        except TypeError:
            return None
        self.outputbuffer = []

        if projectname is not None:
            projectname = decode_utf8_or_sys(projectname)
        self.projectname = projectname

        self.disable_comments = disable_comments
        self.last_userhash = None
        self.set_comment_handling(disable_comments, parseinfo)

        self.create_lookup_tables()
        self.print_root(root, indent=0)
        return self.getoutput()

    def emit(self, s):
        self.outputbuffer.append(s)

    @staticmethod
    def getmember(obj, name):
        try:
            return obj.get(name)
        except AttributeError:
            return None

    def getoutput(self):
        return ''.join(self.outputbuffer)

    def set_comment_handling(self, disable_comments, parseinfo):
        if disable_comments is not None:
            self.disable_comments = disable_comments
            return

        sufficient_num_commented_nodes = 10
        if parseinfo:
            num_present = parseinfo.get('num_comments')
            if num_present is not None and num_present < sufficient_num_commented_nodes:
                self.disable_comments = True

    def print_root(self, root, indent=0):
        if not self.has_comments():
            self.disable_comments = True
        if self.has_utf8_header():
            self.emit(self.header)
        self.emit_node(root, indent)
        self.emit(self.trailer)

    def create_lookup_tables(self):
        """When we generate comments we'd get quadratic behaviour
        to find file sections and buildconfigurations.
        Build lookup tables to avoid this.
        """
        for obj in self.objects.values():
            files = self.getmember(obj, 'files')
            if isinstance(files, list):
                name = self.get_name(obj)
                if name is None:
                    name = self.buildphasename(self.getmember(obj, 'isa'))
                for f in files:
                    self.section_for_file[f] = name
            bcl = self.getmember(obj, 'buildConfigurationList')
            if bcl is not None:
                self.build_configuration_lists[bcl] = obj

    @staticmethod
    def buildphasename(name):
        if name is None:
            return None
        start = 'PBX'
        end = 'BuildPhase'
        if name.startswith(start) and name.endswith(end):
            return name[len(start):-len(end)]
        return None

    def supress_comment(self):
        if len(self.keypath) >= 1 and self.keypath[-1] in self.keys_without_comments:
            return True
        if len(self.keypath) >= 2 and self.keypath[-2] in self.keys_without_comments:
            return True
        return False

    def comment_for_obj(self, obj):
        if self.disable_comments:
            return None

        if self.supress_comment():
            return None

        isa = self.getmember(obj, 'isa')
        return (self.pbx_names.get(isa)
             or self.get_name(obj)
             or self.buildphasename(isa)
             or self.name_for_object(obj))

    def build_configuration(self, bcuuid):
        obj = self.objects.get(bcuuid)
        if obj is None:
            return None
        if obj.get('isa') != 'XCConfigurationList':
            return None

        obj = self.build_configuration_lists.get(bcuuid)
        if obj is not None:
            isa = obj.get('isa')
            name = self.get_name(obj) or self.name_of_first_target(obj)
            if isa == 'PBXProject':
                name = self.projectname or name.strip()
            name = self.transform_to_nfd(name)
            comment = 'Build configuration list'
            if self.has_build_configuration_list_detail():
                comment += ' for %s "%s"' % (isa, name)
            return comment
        return None

    def name_of_first_target(self, obj):
        targets = self.getmember(obj, 'targets')
        if isinstance(targets, list):
            for uuid in targets:
                name = self.name_for_object(self.objects.get(uuid))
                if name is not None:
                    return name
        return None

    def transform_to_nfd(self, text):
        if text is None:
            return None
        if not self.has_nfd_comments():
            return text

        # We should only have ASCII comments in the renios prototype project.

        # return unicodedata.normalize('NFD', text)
        return text

    def get_name(self, obj):
        return self.transform_to_nfd(self.getmember(obj, 'name'))

    def name_for_object(self, obj):
        if obj is None or not isinstance(obj, dict):
            return None
        return (self.get_name(obj)
             or self.getmember(obj, 'path')
             or self.name_for_object(self.objects.get(self.getmember(obj, 'fileRef')))
             or self.name_of_first_target(obj))

    def comment_for_value(self, v):
        if not is_global_id(v):
            return None

        if not self.valid_comment_keypath():
            return None

        comment = self.gidcomments.get(v)
        if comment is not None:
            return comment

        comment = None
        buildconf = self.build_configuration(v)
        if buildconf is not None:
            comment = buildconf
        else:
            obj = self.objects.get(v)
            if obj is not None and isinstance(obj, dict):
                comment = self.comment_for_obj(obj)
                section = self.section_for_file.get(v)
                if section is not None:
                    comment = "%s in %s" % (comment or '(null)', section)

        self.gidcomments[v] = comment or ''
        return comment

    def valid_comment_keypath(self):
        """Adding a comment to every value that looks like a global id
        is incorrect in the improbable case that e.g. a file is named exactly as
        a global id that exists in the same project.
        """
        k = self.keypath
        if k[0] == 'objects':
            if len(k) == 2:
                return True
            elif len(k) >= 3:
                path = [self.get_isa(self.objects.get(x)) or x for x in k[1:]]
                kp = '.'.join(path)
                return kp in self.commentpaths
        # The only other commented keypath is the rootObject.
        return k == ['rootObject']

    def in_fileobj(self, obj):
        return self.getmember(obj, 'isa') in ['PBXBuildFile', 'PBXFileReference']

    def get_isa(self, obj):
        if isinstance(obj, dict):
            return self.getmember(obj, 'isa')
        return None

    def begin_section(self, obj):
        isa = self.get_isa(obj)
        if isa != self.open_section:
            self.close_section()
            self.emit("\n/* Begin %s section */\n" % isa)
            self.open_section = isa
            return True
        return False

    def close_section(self):
        if self.open_section:
            self.emit('/* End %s section */\n' % self.open_section)
            self.open_section = None

    # -----------------------------------------------------------
    # Xcode format version dependent checks

    def has_utf8_header(self):
        return self.version > 30

    def has_userhash_comments(self):
        return 32 < self.version < 40

    def has_ungrouped_objects_sort(self):
        return self.version < 40

    def has_leading_isa(self):
        return self.version >= 40

    def has_concise_format(self):
        return self.version >= 40

    def has_comments(self):
        return self.version >= 40

    def has_build_configuration_list_detail(self):
        return self.version >= 41

    def has_nfd_comments(self):
        """There is a UTF-8 inconsistency in Xcode starting with object version 46.
        Although Xcode uses the composed Unicode form (NFC) almost everywhere,
        some comments are encoded in the decomposed Unicode form (NFD) which
        is probably because the HFS Plus file system stores filenames in NFD.
        """
        return self.version >= 46

    # -----------------------------------------------------------

    @staticmethod
    def objects_sortkey(kv):
        """The 'objects' dict are sorted by isa first. This way we get the
        sections, e.g. /* Begin PBXBuildFile section */.
        The secondary sort key is the gid which creates the proper
        order within the sections.
        """
        try:
            return kv[1].get('isa'), kv[0]
        except AttributeError:
            return kv[0]

    @staticmethod
    def ungrouped_objects_sortkey(kv):
        return kv[0]

    def sorted_items(self, dictionary):
        if self.keypath == ['objects']:
            # This is the 'objects' dict which we sort by (isa, gid) into sections.
            if self.has_ungrouped_objects_sort():
                sortkey = self.ungrouped_objects_sortkey
            else:
                sortkey = self.objects_sortkey
        else:
            sortkey = None
            if self.has_leading_isa():
                isa = dictionary.get('isa')
                if isa is not None:
                    items = [('isa', isa)]
                    items.extend(sorted(x for x in dictionary.items() if x[0] != 'isa'))
                    return items
        return sorted(dictionary.items(), key=sortkey)

    def emit_value(self, v):
        v = quoted_string(v)
        self.emit(v)
        comment = self.comment_for_value(v)
        if comment is not None:
            if not self.disable_comments:
                self.emit_comment(comment)

    def emit_kvpair(self, k, v, indent):
        self.emit_value(k)
        self.emit(' = ')
        self.emit_node(v, 0 if self.concise() else indent)

    def concise(self):
        return self.concise_mode and self.has_concise_format()

    def emit_comment(self, comment):
        if comment:
            self.emit(' /* ')
            self.emit(comment)
            self.emit(' */')

    def emit_prologue(self):
        if not self.concise():
            self.emit('\n')

    def emit_indent(self, indent):
        self.emit('\t' * indent)

    def emit_leading_separator(self, indent):
        self.emit_indent(0 if self.concise() else indent)

    def emit_trailing_separator(self):
        self.emit(' ' if self.concise() else '\n')

    def emit_userhash_comments(self, k):
        if not self.has_userhash_comments():
            return
        if len(self.keypath) != 1:
            return
        if self.keypath[0] != 'objects':
            return
        if self.last_userhash is None:
            self.last_userhash = k
            return
        a = self.last_userhash[:2]
        b = k[:2]
        if a != b:
            self.emit_userhash_range(a)
            self.emit_userhash_range(b)
        self.last_userhash = b

    def emit_userhash_range(self, userhash):
        for i in range(5):
            self.emit('//%s%d\n' % (userhash, i))

    def emit_map(self, node, indent):
        self.emit('{')
        self.emit_prologue()
        began_sections = False
        sections = self.keypath == ['objects'] and not self.disable_comments
        for k, v in self.sorted_items(node):
            self.emit_userhash_comments(k)
            self.keypath.append(k)
            began_sections = sections and (self.begin_section(v) or began_sections)
            self.emit_leading_separator(indent + 1)
            self.emit_kvpair(k, v, indent + 1)
            self.emit(';')
            self.emit_trailing_separator()
            self.keypath.pop()
        if began_sections:
            self.close_section()
        self.emit_leading_separator(indent)
        self.emit('}')

    def emit_list(self, node, indent):
        self.emit('(')
        self.emit_prologue()
        for v in node:
            self.emit_leading_separator(indent + 1)
            self.emit_node(v, indent + 1)
            self.emit(',')
            self.emit_trailing_separator()
        self.emit_leading_separator(indent)
        self.emit(')')

    def emit_node(self, node, indent=0):
        if isinstance(node, dict):
            concise_output = self.in_fileobj(node)
            if concise_output:
                self.concise_mode += 1
            self.emit_map(node, indent)
            if concise_output:
                self.concise_mode -= 1
        elif isinstance(node, (list, tuple)):
            self.emit_list(node, indent)
        else:
            self.emit_value(node)


class XMLUnparser(Unparser):
    header = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
"""
    trailer = '</plist>\n'

    def __init__(self, root):
        super(XMLUnparser, self).__init__(root)
        self.disable_comments = True

    def has_concise_format(self):
        return False

    def has_leading_isa(self):
        return False

    @staticmethod
    def escape_tag_entities(data):
        # For clarity we are not going to import xml.sax.saxutils
        # for these three lines.
        data = data.replace("&", "&amp;")
        data = data.replace(">", "&gt;")
        data = data.replace("<", "&lt;")
        return data

    def emit_value(self, v):
        self.emit('<string>')
        self.emit(self.escape_tag_entities(v))
        self.emit('</string>')

    def emit_kvpair(self, k, v, indent):
        self.emit('<key>')
        self.emit(self.escape_tag_entities(k))
        self.emit('</key>')
        self.emit('\n')
        self.emit_node(v, indent)

    def emit_map(self, node, indent):
        if not node:
            self.emit('<dict/>')
            return
        self.emit('<dict>')
        self.emit('\n')
        for k, v in self.sorted_items(node):
            self.emit_indent(indent + 1)
            self.emit_kvpair(k, v, indent + 1)

        self.emit_indent(indent)
        self.emit('</dict>')

    def emit_list(self, node, indent):
        if len(node) == 0:
            self.emit('<array/>')
            return
        self.emit('<array>')
        self.emit('\n')
        for v in node:
            self.emit_node(v, indent + 1)
        self.emit_leading_separator(indent)
        self.emit('</array>')

    def emit_node(self, node, indent=0):
        self.emit_indent(indent)
        super(XMLUnparser, self).emit_node(node, indent=indent)
        self.emit('\n')


class JSONUnparser(Unparser):
    def __init__(self, root):
        super(JSONUnparser, self).__init__(root)
        self.disable_comments = True

    def unparse(self, root, projectname='', disable_comments=False, parseinfo=None):
        try:
            return json.dumps(root, sort_keys=True,
                                    indent=2,
                                    separators=(',', ':'))
        except ValueError:
            return None


# ---------------------------------------------------------------

unparsers = OrderedDict([
                        ('xcode', Unparser),
                        ('xml', XMLUnparser),
                        ('json', JSONUnparser)])
output_formats = unparsers.keys()

# ---------------------------------------------------------------


class UniqueXcodeIDGenerator(object):
    """This class generates global ids in a schema
    similar to the one Xcode uses.
    The optional keyword arguments allow a deterministic
    generation.
    """

    AbsoluteTimeIntervalSince1970 = 978307200

    def __init__(self, username=None, pid=None, refdatefunc=None):
        if refdatefunc is None:
            refdatefunc = self.reftime
        self.initialseq = 0
        self.lasttime = 0
        self.refdatefunc = refdatefunc
        if pid is None:
            pid = os.getpid()
        self.rndgen = random.Random(xor((pid << 16), refdatefunc()))
        self.userhash = self.user_hash(username)
        self.pidbyte = pid & 0xff
        self.randomconst = self.rndgen.randint(0, (2 ** 31) - 1) & 0x00ffffff
        self.randomseq = self.rndgen.randint(0, (2 ** 31) - 1) & 0xffff

    def generate(self):
        refdate = self.refdatefunc()
        self.randomseq += 1
        self.lasttime = 0
        if refdate > self.lasttime:
            self.initialseq = self.randomseq
            self.lasttime = refdate
        else:
            if self.randomseq == self.initialseq:
                self.lasttime += 1
            refdate = self.lasttime

        return (self.hexbyte(self.userhash) + self.hexbyte(self.pidbyte)
              + self.big_endian_hex(self.randomseq, 2)
              + self.big_endian_hex(refdate, 4)
              + self.big_endian_hex(self.randomconst, 4))

    @staticmethod
    def user_hash(username=None):
        userhash = 0
        hashvalue = 0
        if username is None:
            username = os.getlogin()
        for inp in username:
            cc = UniqueXcodeIDGenerator.five_bit_hash(ord(inp))
            if hashvalue != 0:
                cc = ((cc << hashvalue) >> 8) | (cc << hashvalue)
            hashvalue = hashvalue + 5 & 7
            userhash = xor(userhash, cc)
        return userhash & 255

    @staticmethod
    def five_bit_hash(c):
        if ord('A') <= c <= ord('Z'):
            return c - ord('A')
        elif ord('a') <= c <= ord('z'):
            return c - ord('a')
        elif ord('0') <= c <= ord('9'):
            return ord('Z') - ord('A') + 1 + ((c - ord('0')) % 5)
        else:
            return 31

    @staticmethod
    def hexbyte(c):
        return '%02X' % c

    @staticmethod
    def big_endian_hex(v, size):
        lst = []
        for _ in range(size):
            lst.append(v & 0xff)
            v >>= 8
        lst.reverse()
        return ''.join(UniqueXcodeIDGenerator.hexbyte(c) for c in lst)

    @staticmethod
    def big_endian_number(hexstring):
        sum = 0
        while hexstring:
            sum *= 256
            byte = hexstring[:2]
            sum += int(byte, 16)
            hexstring = hexstring[2:]
        return sum

    @staticmethod
    def reftime(t=None):
        if t is None:
            t = time.time()
        return int(t - UniqueXcodeIDGenerator.AbsoluteTimeIntervalSince1970)

    @staticmethod
    def reftime_to_epoch(t):
        return t + UniqueXcodeIDGenerator.AbsoluteTimeIntervalSince1970


class IDGeneratorClock(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def tick(self):
        self.seconds += 1

    def getseconds(self):
        return self.seconds


def datetime_from_utc(refdate):
    return datetime.datetime.strptime(refdate, '%Y-%m-%dT%H:%M:%SZ')


def generate_gids(num, username=None, pid=None, refdate=None):
    if refdate is not None:
        dt = datetime_from_utc(refdate)
        t = time.mktime(dt.timetuple())
    else:
        t = None
    secs = UniqueXcodeIDGenerator.reftime(t)

    clock = IDGeneratorClock(secs)
    generator = UniqueXcodeIDGenerator(username=username, pid=pid, refdatefunc=clock.getseconds)
    for i in range(num):
        gid = generator.generate()
        # We can only generate 65536 different gids for the same second,
        # then we go on to the next second.
        yield gid
        if i & 0xffff == 0xffff:
            clock.tick()


def iprint(category, *args, **kwargs):
    if category in args_info:
        print(*args, **kwargs)


def dprint(category, *args, **kwargs):
    if category in args_debug:
        print(*args, **kwargs)


def outline(s, fp=None):
    if fp is None:
        fp = sys.stdout
    fp.write(unistr(s + '\n'))

reportmessage = outline

def reporterror(s, fp=None):
    if fp is None:
        fp = sys.stderr
    reportmessage(s, fp=fp)

reportwarning = reporterror

def print_gids(num, username=None, pid=None, refdate=None):
    for g in generate_gids(num, username=username, pid=pid, refdate=refdate):
        outline(unistr(g))
    return OK


def comment_for_gid(giddict, gid):
    if isinstance(giddict, dict):
        comment = giddict.get(gid)
        if comment is not None:
            return comment
    return None


def gidfields(giddict, gid):
    parts = gid[:2], gid[2:4], gid[4:8], gid[8:16], gid[16:24]
    parts = [UniqueXcodeIDGenerator.big_endian_number(x) for x in parts]
    user, pid, seq, date, randomconst = parts
    date = UniqueXcodeIDGenerator.reftime_to_epoch(date)
    date = datetime.datetime.utcfromtimestamp(date)
    date = date.isoformat() + 'Z'
    comment = comment_for_gid(giddict, gid)
    d = OrderedDict([
        ('date', date),
        ('user', user),
        ('pid', pid),
        ('random', randomconst),
        ('seq', seq),
        ('gid', gid)])
    if comment:
        d['comment'] = comment
    return d


def gidsplit(gidseq, format='text', sort=False, buf=None):
    """This function prints a columnar JSON representation of the splitted gids
    with the date in front so one can sort and extract data with the
    usual command line tools as well as read the output as JSON.
    """
    gids = [g for g in gidseq if is_global_id(g)]
    if not gids:
        return

    out = buf
    if out is None:
        out = sys.stdout

    def uniwrite(text):
        out.write(unistr(text))


    if sort:
        gids.sort()
    entries = [gidfields(gidseq, gid) for gid in gids]

    if format == 'json':
        root = {'gids': entries}
        uniwrite(json.dumps(root, sort_keys=True, indent=2, separators=(',', ':')))
        uniwrite('\n')
    elif format == 'text':
        formatstrings = {"date": "%s", "user": "%3d", "pid": "%3d", "random": "%10d",
                         "seq": "%5d", "gid": "%24s", "comment": "%s"}
        jsondumps = json.JSONEncoder().encode
        for d in entries:
            comment = d.get('comment')
            if comment is not None:
                d['comment'] = jsondumps(comment)
            uniwrite(' '.join(formatstrings[k] % v for k, v in d.items()))
            uniwrite('\n')
    return OK


def giddump(args, parser):
    filenames = args.filename
    if len(filenames) > 1:
        parser.error('Please specify no more than one filename to giddump')
        # The return is only reached with a test parser from the unit tests.
        return 1

    filename = (filenames and filenames[0]) or STDIN
    xcodeproj = data_from_filename(filename)
    root, parseinfo = parse(xcodeproj, parsertype=args.parser)
    report_parse_status(root, parseinfo, filename=filename)
    if root is None:
        return PARSING_FAILED

    projectname = projectname_from_args(args, parser, filename, parseinfo.get('projectname'))

    unparser = Unparser(root)
    # Run the unparser to get the table of gidcomments
    _ = unparser.unparse(root, projectname=projectname)

    if args.outputfile is not None and args.outputfile != '-':
        destfilename = args.outputfile
        with codecs.open(destfilename, 'w', encoding='utf-8') as fp:
            gidsplit(unparser.gidcomments, format=args.gid_format, sort=True, buf=fp)
    else:
        gidsplit(unparser.gidcomments, format=args.gid_format, sort=True)

    return OK

# ----------------------------------------------------------------------


def find_projectfiles(rootdir):
    """Iterates recursively over rootdir and yields
    every filename that looks like a credible project.pbxproj.
    """
    validfirstchars = {'/',  # usual header for the plist format: // !$*UTF8*$!
                       '<',  # <?xml version="1.0" encoding="UTF-8"?>
                       '{'   # plist format without the UTF8 header
                       }
    for path, dirs, files in os.walk(rootdir):
        for name in files:
            if name != PBXPROJNAME:
                continue
            filename = os.path.join(path, name)
            with codecs.open(filename, 'r', encoding='utf-8') as f:
                c = f.read(1)
                if c in validfirstchars:
                    yield filename


def unilines(text):
    return unistr(text).splitlines(True)


def print_unified_diff(a, b, fp=None, **kwargs):
    if fp is None:
        fp = sys.stdout
    for line in difflib.unified_diff(unilines(a), unilines(b), **kwargs):
        fp.write(unistr(line))
        if not line.endswith('\n'):
            fp.write(unistr('\n'))


def timestamp():
    return 'projer' + str(time.time()).replace('.', '_')


def print_diff(a, b, difftype='unified', filename=None, fp=None):

    def write_tempfile(data, **kwargs):
        fd, path = tempfile.mkstemp(**kwargs)
        try:
            os.write(fd, bytestr(data))
        finally:
            os.close(fd)
        return path

    if difftype == 'unified':
        print_unified_diff(a, b, fromfile=filename, tofile='', n=3, fp=fp)
    elif difftype == 'html':
        htmldiffer = difflib.HtmlDiff(tabsize=4)
        html = htmldiffer.make_file(unilines(a), unilines(b),
                                    fromdesc=filename,
                                    todesc='',
                                    context=True, numlines=2)
        htmlfilename = write_tempfile(html, suffix='.html', prefix=timestamp())
        reporterror('\nopen "%s"' % htmlfilename, fp=fp)
    elif difftype == 'opendiff':
        outfilename = write_tempfile(b, suffix='.pbxproj', prefix=timestamp())
        reporterror('\nopendiff "%s" "%s"' % (filename, outfilename), fp=fp)
    else:
        raise ValueError("Unknown difftype: '%s'" % difftype)


def farthest_parseinfo(parseinfo):
    """As we might have tried several attempts of parsing different formats
    we have several error reports from the respective parsers.
    The parser that made it the farthest (line, column) probably
    matched the format but failed anyway.
    The error report of this least unsuccessful parser is the only
    one being reported.
    """
    line = parseinfo.get('error_line_number', -1)
    column = parseinfo.get('error_column', -1)
    prev = parseinfo.get('prev_parseinfo')
    if prev is None:
        return line, column, parseinfo
    prevline, prevcolumn, prev = farthest_parseinfo(prev)
    if (prevline, prevcolumn) > (line, column):
        return prevline, prevcolumn, prev
    else:
        return line, column, parseinfo


def report_parse_status(root, parseinfo, filename=None, fp=None):
    # Report warnings after a successful parse.
    if isinstance(parseinfo, dict):
        _warnings = parseinfo.get('warnings', [])
        for w in _warnings:
            reportwarning(w, fp=fp)

    iprint(INFO_TIME, "Parse time:", parseinfo.get('parsetime'))

    if root is not None:
        # We have a parse tree, no errors to report here.
        return

    if filename == STDIN:
        filename = '<stdin>'
    else:
        filename = '%s' % filename
    line, column, parseinfo = farthest_parseinfo(parseinfo)
    parseinfo = parseinfo.copy()
    parseinfo['filename'] = filename
    reporterror('File %(filename)s, line %(error_line_number)d, column %(error_column)d' % parseinfo, fp=fp)
    reporterror(parseinfo.get('error_text'), fp=fp)


def data_from_filename(filename):
    if filename == STDIN:
        return sys.stdin.read()
    else:
        with open(filename, 'rb') as f:
            return f.read()


def projectname_from_args(args, parser, filename, prjname=None):
    if filename == STDIN:
        projectname = args.projectname
        if projectname is None:
            if prjname is not None:
                reportwarning('Warning: We needed to guess "%s" as project name which might not be correct.\n'
                              '         It would be preferable if you could supply the definite project name using --projectname when you read from stdin.' % prjname)
                projectname = prjname
            else:
                parser.error('When we get the project via stdin (-) you must specify the project name with --projectname')
    else:
        projectname = projectname_for_path(filename)
    return projectname


def lint(args, parser):
    filenames = args.filename
    exit_code = OK
    if not filenames:
        filenames = [STDIN]

    for filename in filenames:
        xcodeproj = data_from_filename(filename)
        root, parseinfo = parse(xcodeproj, format=None, parsertype=args.parser)
        report_parse_status(root, parseinfo, filename=filename)
        if root is None:
            exit_code = max(exit_code, LINT_FAILED)
            continue

        if parseinfo['format'] not in ['xcode', 'xml']:
            reportmessage('The project file "%s" is in %s which is nothing that Xcode can read.' % (filename, parseinfo['format']))
            exit_code = max(exit_code, LINT_FAILED)
            continue

        if parseinfo['format'] == 'xml':
            reportmessage('The project file "%s" is in XML which is a clearly a failed lint.' % filename)
            exit_code = max(exit_code, LINT_FAILED)
            continue

        projectname = projectname_from_args(args, parser, filename, parseinfo.get('projectname'))
        proj = unparse(root, projectname=projectname)
        if xcodeproj != proj:
            exit_code = max(exit_code, LINT_DIFFERENCES)
            print_unified_diff(xcodeproj, proj, fromfile=filename)
    return exit_code


def convert(args, parser):
    filenames = args.filename
    if len(filenames) > 1:
        parser.error('Please specify no more than one filename to convert')
        # The return is only reached with a test parser from the unit tests.
        return 1

    filename = (filenames and filenames[0]) or STDIN
    xcodeproj = data_from_filename(filename)
    root, parseinfo = parse(xcodeproj, parsertype=args.parser)
    report_parse_status(root, parseinfo, filename=filename)
    if root is None:
        return PARSING_FAILED

    # Set objectVersion if requested
    if args.objectversion != 'same':
        if args.objectversion == 'latest':
            version = text_type(LATEST_OBJECT_VERSION)
        else:
            version = args.objectversion
        root['objectVersion'] = version

    projectname = projectname_from_args(args, parser, filename, parseinfo.get('projectname'))
    proj = unparse(root,
                   format=args.convert,
                   projectname=projectname,
                   disable_comments=args.comments == 'no',
                   parseinfo=parseinfo)

    if args.outputfile is not None:
        destfilename = args.outputfile
    elif filename == STDIN:
        destfilename = STDOUT
    else:
        destfilename = filename

    if destfilename == STDOUT:
        buf = sys.stdout
        try:
            numbytes = buf.write(proj)
        except TypeError:
            # We are probably writing to a io.StringIO here.
            numbytes = len(proj)
            buf.write(unistr(proj))
    else:
        with open(destfilename, 'wb') as f:
            numbytes = f.write(proj)

    if numbytes is not None and numbytes != len(proj):
        reporterror('Incomplete output, only %d of %d bytes written' % (numbytes, len(proj)))
        return CONVERT_OUTPUT_FAILED

    return OK


# ----------------------------------------------------------------------

def cmdline_parser(parserclass=argparse.ArgumentParser):
    """The option to change the parserclass is used for testing the
    command line options.
    """
    parser = parserclass(description='Convert Xcode project files into different formats.')
    parser.add_argument('-o', '--outputfile', help='output filename or - for stdout')
    parser.add_argument('--projectname', action='store', help='the directory name without the .xcodeproj, necessary for stdin input')
    parser.add_argument('--parser', choices=['normal', 'fast', 'classic'], default='normal')
    # The info and debug options were inspired by rsync.
    parser.add_argument('--info', help='fine-grained informational verbosity')
    parser.add_argument('--debug', help='fine-grained debug verbosity')
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    group = parser.add_argument_group('Convert file formats')
    group.add_argument('-c', '--convert', choices=output_formats, help='convert into a specific format')
    group.add_argument('--objectversion', action='store', default='same', help='output version of plist, e.g.: 30, 46, latest, same')
    group.add_argument('--comments', choices=['yes', 'no', 'same'], default='yes',
                       help='only meaningful for plist output, same means include if input file was commented.')

    lintgroup = parser.add_argument_group('Lint file formats')
    lintgroup.add_argument('--lint', action='store_true', help='checks if the files are in properly commented plist format')

    gidgroup = parser.add_argument_group('Global ids')
    gidgroup.add_argument('--gid', nargs='?', const=1, type=int, default=None, metavar='NUM', help='number of global ids to generate')
    gidgroup.add_argument('--gidsplit', nargs='+', default=None, metavar='GID_TO_INTERPRET', help='transform global ids into readable components')
    gidgroup.add_argument('--giddump', action='store_true', help='representation of commented gids, for software archeologists')
    gidgroup.add_argument('--gid-pid', type=int, default=None, help='pid for the global id generator')
    gidgroup.add_argument('--gid-user', default=None, help='username for the global id generator')
    gidgroup.add_argument('--gid-date', default=None, help='base date for the global id generator, e.g. 2007-01-09T16:41:00Z')
    gidgroup.add_argument('--gid-format', choices=['json', 'text'], default='text', help='output format for gidsplit and giddump')

    parser.add_argument('filename', nargs='*', help='input filename')

    return parser


def set_logging_parameters(args):
    for attr, catset, defaults in (
            ('info', args_info, INFO_ALL),
            ('debug', args_debug, DEBUG_ALL)):
        option = getattr(args, attr)
        if option:
            catset.update(x.lower() for x in option.split(','))
            if 'all' in catset:
                catset.update(defaults)

    if args.verbose is not None:
        for level in sorted(verbose_categories):
            if args.verbose >= level:
                args_info.update(verbose_categories[level])


def run_with_args(args, parser):
    set_logging_parameters(args)

    dprint(DEBUG_OPTIONS, args)

    num_actions = 0
    actions = 'convert lint gid gidsplit giddump'.split()
    for act in actions:
        if getattr(args, act):
            num_actions += 1

    if num_actions != 1:
        parser.error('Please specify exactly one of the options %s.' % ', '.join('--' + x for x in actions))

    ret = 0
    if args.gid is not None:
        ret = print_gids(args.gid, username=args.gid_user, pid=args.gid_pid, refdate=args.gid_date)
    elif args.gidsplit:
        ret = gidsplit(args.gidsplit, format=args.gid_format)
    elif args.giddump:
        ret = giddump(args, parser)
    elif args.lint:
        ret = lint(args, parser)
    elif args.convert:
        ret = convert(args, parser)
    else:
        parser.error('Something is wrong with the options or the handling of them.')

    return ret


def main():
    parser = cmdline_parser()
    args = parser.parse_args()
    run_with_args(args, parser)

if __name__ == '__main__':
    if PY3:
        sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
        sys.stderr = codecs.getwriter('utf8')(sys.stderr.buffer)
    sys.exit(main())
