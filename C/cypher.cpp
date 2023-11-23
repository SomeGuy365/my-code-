#include <iostream>
//vigenere cipher

int main() {
    std::string alpha = "abcdefghijklmnopqrstuvwxyz";
    std::string key = "houghton";
    char letter;
    char* keypoint;
    char* point;
    std::string inp;
    inp = "michigan technological university";
    point = &inp[0];
    keypoint = &key[0];
    for (int i=0;i<inp.length();i++) {
        if (*point != ' ') {
            if (alpha.find(*point)+alpha.find(*keypoint) > 26) {
                letter = alpha[(alpha.find(*point)+alpha.find(*keypoint))-27];
            } else {
                letter = alpha[alpha.find(*point)+alpha.find(*keypoint)];
            }
        } else {
            letter = ' ';
        };
        std::cout << letter << " : " << *point << " : " << *keypoint << std::endl;
        point++;
        if (*keypoint != key[(key.length())-1]) {
            keypoint++;
        }
        else {
            keypoint = &key[0];
        };
    };

    return 0;
}