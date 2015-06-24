#!/usr/bin/python3

import cscript

assert (cscript.isFunctionDeclaration("int something()"))
assert (not cscript.isFunctionDeclaration("if (x == 7)"))
assert (not cscript.isFunctionDeclaration("gerald = something()"))
assert (cscript.isFunctionDeclaration("(void*) something(char* blah)"))
assert (cscript.isFunctionDeclaration("    (void*) something(char* blah)"))

assert (cscript.isIncludeLine('#include "something.h"'))
assert (cscript.isIncludeLine('#include <something.h>'))
assert (cscript.isIncludeLine('   #include <something.h>'))

assert (cscript.isTypedef(''))

print("OK")
