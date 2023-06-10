#include <iostream>

int main() {
    const double pi = 3.14;

    int a = 1;
    int b = 2;
    int store = b;
    b = a;
    a = store;

    std::cout << a*pi << std::endl;
    std::cout << b*pi << std::endl;
    return 0;
}