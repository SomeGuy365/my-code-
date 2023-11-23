#include <iostream>
#include <unordered_map>
#include <cmath>

int main() {
    std::unordered_map<std::string, float> converter; 
  
    converter["euro"] = 1.1495; 
    converter["usd"] = 1.25354; 
    converter["yen"] = 187.518; 

    std::string currency;
    float currencyamount;
    std::cout << "yay" << std::endl;
    std::cin >> currencyamount >> currency;
    std::cout << "\x9C" << currencyamount << " : " << floor((converter[currency]*currencyamount)) << " " << currency;
    return 0;
}