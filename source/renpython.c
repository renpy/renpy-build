#include "Python.h"

void init_librenpy(void);

int main(int argc, char **argv) {
    init_librenpy();

    return Py_Main(argc, argv);
}
