#!/usr/bin/cscript

int factorial(int argument)
{
    if (argument <= 0) {
        return 1;
    }
    return argument * factorial(argument - 1);
}

if (argc > 1) {
    int x = atoi(argv[1]);
    printf("Factorial(%d): %d\n", x, factorial(x));
}

