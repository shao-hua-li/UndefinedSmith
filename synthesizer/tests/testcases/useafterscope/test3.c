#include<stdio.h>
int g1, *g2;

int foo(int p) {
    int a = 1;
    int *b = &g1;
    g2 = &g1;
    int d[2] = {1, 2};
    if (p>a) {
        int c = 1;
        a++;
    }
    a = a +1;
    return *g2;
}

int main() {
    int x;
    x = foo(2);
    printf("checksum = %d\n", x);
}
