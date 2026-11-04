// 1. Buffer Overflow using strcat()

#include <stdio.h>
#include <string.h>

int main() {
    char str[10];
    char add[20];

    printf("Enter first string: ");
    scanf("%9s", str);

    printf("Enter second string: ");
    scanf("%19s", add);

    strcat(str, add);

    printf("String: %s\n", str);
    return 0;
}


// 2. Buffer Overflow using sprintf()

#include <stdio.h>

int main() {
    char str[5];
    char input[50];

    printf("Enter a string: ");
    scanf("%49s", input);

    sprintf(str, "%s", input);

    printf("String: %s\n", str);
    return 0;
}