#include "Python.h"

{% for name in modules %}
PyMODINIT_FUNC init{{ name.replace(".", "_") }} (void);
{% endfor %}

static struct _inittab inittab[]  = {
{% for name in modules %}
    { "{{ name }}", init{{ name.replace(".", "_") }} },
{% endfor %}
    { NULL, NULL },
};

void init_librenpy(void) {
    PyImport_ExtendInittab(inittab);
}
