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
    std::cout << "Enter Gdp:";
    std::cin >> currencyamount;
    std::cout << "Suppoerted currency:" << std::endl << "Euro" << std::endl << "Usd" << std::endl << "Yen" << std::endl;
    std::cout << "Enter currency to convert:";
    std::cin >> currency;
    std::cout << "\x9C" << currencyamount << " : " << floor((converter[currency]*currencyamount)*100)/100 << " " << currency;

    return 0;
}