#include <iostream>
#include <list>

using namespace std;


int main() {
    string input;
    int pasnum;
    int num1,num2;
    list<char> operators{};
    cout << "Enter you equation:";
    cin >> input;
    for (auto i:input) {
        operators.push_back(i);
    };

    int n = size(operators);
    list<char>::iterator its = operators.begin();
    list<char>::iterator itm = operators.begin();
    list<char>::iterator ite = operators.begin();
    advance(itm,1);
    advance(ite,2);
    
    for (int b = 0;b < n+1;b++) {

        switch(*itm)
        {
        case '+':
            cout << endl << "addition" << endl << *its << endl << *itm << endl << *ite;
            num1 = *its - '0';
            num2 = *ite - '0';
            break;
        case '-':
            cout << "subtract";
            break;
        default:
            break;
        }

        advance(its,2);
        advance(itm,2);
        advance(ite,2);
    }

    cout << "Output:";
    for (auto c:operators) {
        cout << c;
    }
    
    return 0;
}