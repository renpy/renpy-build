/*

Copyright 2019-2021  Sylvain Beucler
Copyright 2022 Teyut <teyut@free.fr>
Copyright 2019-2022 Tom Rothamel <pytom@bishoujo.us>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

(function () {

  // The div containing the status and progress bar.
  let statusDiv = document.getElementById("statusDiv");
  let statusTextDiv = document.getElementById("statusTextDiv");
  let statusProgress = document.getElementById("statusProgress");

  // The timeout before the status div hides itself.
  let statusTimeout = null;

  // The status message.
  let statusText = "";

  // How long before the status div starts hiding, in seconds.
  const STATUS_TIMEOUT = 2500;

  /**
   * Hide the status div. Once it's hidden, clears the status text.
   */
  function hideStatus() {
      statusDiv.classList.remove("visible");
      statusDiv.classList.add("hidden");

      statusTimeout = setTimeout(() => {
          statusText = "";
      }, 250);
  }

  /**
   * Show the status div.
   */
  function showStatus() {
      statusDiv.classList.remove("hidden");
      statusDiv.classList.add("visible");
      statusTextDiv.scrollTop = statusTextDiv.scrollHeight;
      statusProgress.style.display = "none";
  }

  /**
   * Cancels the timeout that hides the status div.
   */
  function cancelStatusTimeout() {
      if (statusTimeout) {
          clearTimeout(statusTimeout);
          statusTimeout = null;
      }
  }

  /**
   * Start the timeout that hides the status div.
   */
  function startStatusTimeout() {
      cancelStatusTimeout();
      statusTimeout = setTimeout(hideStatus, STATUS_TIMEOUT);
  }

  /**
   * Reports an error that will persist.
   */
  function reportError(s) {
      cancelStatusTimeout();

      if (statusText) {
          statusText += "<br>";
      }

      if (s == "\n") {
          statusText = "";
          s = "";
      }

      s = String(s);
      s = s.replace(/&/g, "&amp;");
      s = s.replace(/</g, "&lt;");
      s = s.replace(/>/g, "&gt;");
      s = s.replace('\n', '<br />', 'g');

      statusText += s;
      statusTextDiv.innerHTML = statusText;

      showStatus();
  }

  /**
   * Reports a message that will eventually be hidden.
   */
  function printMessage(s)
  {
      reportError(s);
      startStatusTimeout();
  }

  /**
   * Updates the progress bar.
   */
  function progress(done, total) {
      _cancelStatusTimeout();
      showStatus();
      statusProgress.value = done;
      statusProgress.max = total;
      statusProgress.style.display = "block";
      startStatusTimeout();
  }

  Module.print = printMessage;
  Module.printErr = printMessage;

  Module.setStatus = function (s) {
    console.log(s);
  }

  /*
  var Module = {
      preRun: [],
      postRun: [],
      print: (function() {
        var element = document.getElementById('output');
        if (element) element.value = ''; // clear browser cache
        return function(text) {
          if (arguments.length > 1) text = Array.prototype.slice.call(arguments).join(' ');
          // These replacements are necessary if you render to raw HTML
          //text = text.replace(/&/g, "&amp;");
          //text = text.replace(/</g, "&lt;");
          //text = text.replace(/>/g, "&gt;");
          //text = text.replace('\n', '<br>', 'g');
          console.log(text);
          if (element) {
            element.value += text + "\n";
            element.scrollTop = element.scrollHeight; // focus on bottom
          }
        };
      })(),
      canvas: (function() {
        var canvas = document.getElementById('canvas');

        // As a default initial behavior, pop up an alert when webgl context is lost. To make your
        // application robust, you may want to override this behavior before shipping!
        // See http://www.khronos.org/registry/webgl/specs/latest/1.0/#5.15.2
        canvas.addEventListener("webglcontextlost", function(e) { alert('WebGL context lost. You will need to reload the page.'); e.preventDefault(); }, false);

        return canvas;
      })(),
      setStatus: function(text) {
        if (!Module.setStatus.last) Module.setStatus.last = { time: Date.now(), text: '' };
        if (text === Module.setStatus.last.text) return;
        var m = text.match(/([^(]+)\((\d+(\.\d+)?)\/(\d+)\)/);
        var now = Date.now();
        if (m && now - Module.setStatus.last.time < 30) return; // if this is a progress update, skip it if too soon
        Module.setStatus.last.time = now;
        Module.setStatus.last.text = text;
        if (m) {
          text = m[1];
          progressElement.value = parseInt(m[2])*100;
          progressElement.max = parseInt(m[4])*100;
          progressElement.hidden = false;
          spinnerElement.hidden = false;
        } else {
          progressElement.value = null;
          progressElement.max = null;
          progressElement.hidden = true;
          if (!text) spinnerElement.style.display = 'none';
        }
        statusElement.innerHTML = text;
      },
      totalDependencies: 0,
      monitorRunDependencies: function(left) {
        this.totalDependencies = Math.max(this.totalDependencies, left);
        Module.setStatus(left ? 'Preparing... (' + (this.totalDependencies-left) + '/' + this.totalDependencies + ')' : 'All downloads complete.');
      }
    };
    Module.setStatus('Downloading...');
    window.onerror = function(event) {
      // TODO: do not warn on ok events like simulating an infinite loop or exitStatus
      Module.setStatus('Exception thrown, see JavaScript console');
      spinnerElement.style.display = 'none';
      Module.setStatus = function(text) {
        if (text) console.error('[post-exception status] ' + text);
      };
    };
  */


  window.presplashEnd = () => {
  }


  /** Set up the canvas. */
  let canvas = document.getElementById('canvas');
  canvas.addEventListener("webglcontextlost", function(e) { alert('WebGL context lost. You will need to reload the page.'); e.preventDefault(); }, false);
  canvas.addEventListener('mouseenter', function(e) { window.focus() });
  canvas.addEventListener('click', function(e) { window.focus() });
  Module.canvas = canvas;

  /**
   * Initializes the runtime environment before the game starts.
   */
  function init() {
      // Set up the canvas.

      // Create the save directory, and mount the IDBFS filesystem.
      try {
          FS.mkdir('/home/web_user/.renpy');
          FS.mount(IDBFS, {}, '/home/web_user/.renpy');
      } catch(e) {
          reportError(`Could not create ~/.renpy/: ${e.message}`);
      }
  }

  Module['preRun'].push(function() {
      init();
  });

})();
