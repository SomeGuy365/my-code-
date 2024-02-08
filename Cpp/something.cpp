#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;


int main() {
    // data types
    float example = 3.67f;
    long big_num = 90000L;
    char letter = 'a';
    bool valid = true;

    int binary = 0b11111111;
    int hexidec = 0xFF;
    cout << binary << endl << hexidec << endl;

    //random numbers
    srand(time(nullptr));
    int rando = rand() % 10;
    cout << "random:" << rando << endl;

    // circle area calculator
    const double pi = 3.14;
    double radius;
    cout << "enter radius:";
    cin >> radius;
    double area = pi * pow(radius,2);
    cout << area<< endl;

    // fahrenheit to celcius translator
    double inp = 2;
    cout << "enter temp:";
    cin >> inp ;
    double celc = (inp - 32) * 5/9;
    cout << celc << endl;
    return 0;
}