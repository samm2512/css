// 1. Buffer Overflow using gets()

#include <stdio.h>

int main() {
    char str[5];

    printf("Enter a string: ");
    gets(str);

    printf("String: %s\n", str);
    return 0;
}


// 2. Buffer Overflow using strcpy()

#include <stdio.h>
#include <string.h>

int main() {
    char dest[5];

    strcpy(dest, "HelloWorld");

    printf("String: %s\n", dest);
    return 0;
}