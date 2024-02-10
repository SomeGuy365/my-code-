#include <iostream>
//vigenere cipher

int main() {
    //base variables
    std::string alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
    std::string key = "houghton";
    std::string inp;
    int mode;
    char* keypoint, letter;
    char* point;
    //input
    std::cout << "1:Encrypt\n2:Decrypt\n";
    std::cin >> mode;
    std::cout << "Enter phrase:";
    std::getline(std::cin >> std::ws, inp);
    std::cout << "Enter keyword:";
    std::cin >> key;
    std::cout << inp << " : ";
    //pointers
    point = &inp[0];
    keypoint = &key[0];
    
    for (int i=0;i<inp.length();i++) {

        if (*point != ' ') {
            //letter indexing/ forward or backwards based on mode
            if (mode == 1) {
                letter = alpha[alpha.find(*point)+alpha.find(*keypoint)];
            } else {
                letter = alpha[(alpha.find(*point)+26)-alpha.find(*keypoint)];
            }
            //reset keyword or next letter of keyword
            if (*keypoint != key[(key.length())-1]) {
                keypoint++;
            } else {
                keypoint = &key[0];
            };
        } else {
            letter = ' ';
        };

        std::cout << letter;
        point++;
    };
    return 0;
}