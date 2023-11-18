#include <iostream>

using namespace std;

int main() {
    string input1 = "please";
    int num1 = 0;
    int num2 = 0;
    cout << "what you wanna do>" << endl << "1:add" << endl << "2:subtract" << endl << "3:multiply" << endl;
    cin >> input1;
    cout << "enter num 1:";
    cin >> num1;
    cout << "enter num 2:";
    cin >> num2;
    if (input1 == "1") {
        cout << num1+num2 << endl;
    } else if (input1 == "2") {
        cout << num1-num2 << endl;
    } else if (input1 == "3") {
        cout << num1*num2 << endl;
    };
    return 0;
}