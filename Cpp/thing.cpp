#include <iostream>
#include <vector>
#include <cmath>

//typedef std::vector<std::pair<std::string, int>> pairlist_t;

namespace first{
    //pairlist_t yipee;
    double a = 5;
    double b = 1;
    double c = 1;
}

int main() {
    char op;
    double num1;
    double num2;
    double result;

    std::cout << "enter operator:";
    std::cin >> op;

    std::cout << "enter number 1:";
    std::cin >> num1;

    std::cout << "enter number 2:";
    std::cin >> num2;

    switch (op)
    {
    case '+':
        std::cout << num1+num2;
        break;
    
    case '-':
        std::cout << num1-num2;
        break;
    
    case '/':
        std::cout << num1/num2;
        break;

    case '*':
        std::cout << num1*num2;
        break;
    
    default:
        std::cout << "stop playing :/";
        break;
    }

    return 0;
}