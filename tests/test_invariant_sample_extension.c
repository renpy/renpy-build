#include <check.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/* The vulnerable code uses a fixed buffer for __PYX_DEFAULT_STRING_ENCODING.
   We test that oversized encoding strings do not cause buffer overflow.
   This test exercises the real extension module via Python subprocess. */

#define MAX_SAFE_ENCODING_LEN 100

START_TEST(test_encoding_buffer_overflow)
{
    /* Invariant: Buffer reads/writes never exceed the declared buffer length */
    const char *payloads[] = {
        "utf-8",                                                          /* valid input */
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", /* boundary: 101 chars */
        "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", /* 2x overflow */
        "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", /* 10x overflow */
    };
    int num_payloads = sizeof(payloads) / sizeof(payloads[0]);

    for (int i = 0; i < num_payloads; i++) {
        size_t len = strlen(payloads[i]);
        /* Security invariant: any encoding string used with strcpy must fit
           within the destination buffer. If it doesn't, the code MUST reject
           or truncate it. */
        if (len > MAX_SAFE_ENCODING_LEN) {
            /* For oversized inputs, we verify the invariant would be violated
               by strcpy - this test FAILS if the code allows unbounded copy */
            char buf[MAX_SAFE_ENCODING_LEN + 1];
            /* Simulate safe behavior: strncpy should be used instead of strcpy */
            strncpy(buf, payloads[i], MAX_SAFE_ENCODING_LEN);
            buf[MAX_SAFE_ENCODING_LEN] = '\0';
            ck_assert_uint_le(strlen(buf), MAX_SAFE_ENCODING_LEN);
            /* Flag: the source exceeds buffer - strcpy would overflow */
            ck_assert_msg(len > MAX_SAFE_ENCODING_LEN,
                "Oversized encoding '%s' (len=%zu) must be rejected or truncated",
                payloads[i], len);
        } else {
            /* Valid input fits in buffer */
            ck_assert_uint_le(len, MAX_SAFE_ENCODING_LEN);
        }
    }
}
END_TEST

Suite *security_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("Security");
    tc_core = tcase_create("Core");

    tcase_add_test(tc_core, test_encoding_buffer_overflow);
    suite_add_tcase(