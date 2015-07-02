#!/usr/bin/python3

import cscript, os

assert (cscript.isFunctionDeclaration("int something()"))
assert (not cscript.isFunctionDeclaration("if (x == 7)"))
assert (not cscript.isFunctionDeclaration("gerald = something()"))
assert (cscript.isFunctionDeclaration("(void*) something(char* blah)"))
assert (cscript.isFunctionDeclaration("    (void*) something(char* blah)"))

assert (cscript.isIncludeLine('#include "something.h"'))
assert (cscript.isIncludeLine('#include <something.h>'))
assert (cscript.isIncludeLine('   #include <something.h>'))

assert (cscript.isTypedef('typedef struct {}'))
assert (cscript.isTypedef('   typedef struct {}'))
assert (not cscript.isTypedef('   struct {}'))

os.system('touch firstfile')
os.system('touch secondfile')
assert (cscript.fileIsNewerThan('secondfile', 'firstfile'))

os.system('touch secondfile')
os.system('touch firstfile')
assert (not cscript.fileIsNewerThan('secondfile', 'firstfile'))

os.system('rm secondfile')
os.system('rm firstfile')
print("OK")
