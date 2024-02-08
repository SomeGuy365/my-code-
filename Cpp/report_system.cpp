#include <iostream>

using namespace std;

int main() {
    string student_name = "john doe";
    string subjects[6] = {"English","Maths","Science","Geography","CS","History"}; 
    int scores[6] = {5,4,6,2,6,7};

    string user_inp = "";

    cout << "Student report system" << endl
         << "What Student?" << endl;
    cin >> user_inp;
    cout << student_name<<":"<<endl<<endl;
    
    if (student_name == "john doe") {
        for (int i = 0; i < (sizeof(scores)/4) ; i++)
        {
            cout<< subjects[i] << ":" << scores[i] << endl;
        }
        
    }
    return 0;
}