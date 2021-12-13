#include "Python.h"

{% for name in modules %}
PyMODINIT_FUNC PyInit_{{ name.replace(".", "_") }} (void);
{% endfor %}

static struct _inittab inittab[]  = {
{% for name in modules %}
    { "{{ name }}", PyInit_{{ name.replace(".", "_") }} },
{% endfor %}
    { NULL, NULL },
};

void init_librenpy(void) {
    PyImport_ExtendInittab(inittab);
}
