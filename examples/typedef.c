#!/usr/bin/cscript
#include <string.h>

printf("This is an example involving a function that returns a struct\n");

typedef struct {
    int length;
    char * content;
} String;

String createHelloString()
{
    String result;
    result.length = 5;
    result.content = malloc(6);
    strcpy(result.content, "Hello");
    return result;
}

void deleteString(String string)
{
    free(string.content);
}

String hello = createHelloString();

printf("Why %s there!\n", hello.content);

deleteString(hello);
