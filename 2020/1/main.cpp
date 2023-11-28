#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

int main() {
        std::ifstream file("input.txt");
        std::unordered_map<int, int> first_complements;
        std::unordered_map<int, int> second_complements;
        std::string line;

        while (std::getline(file, line)){
                // read a number from the file.
                int number = std::stoi(line);
                // iterator
                auto iterator = first_complements.find(2020-number);
                // check if the number is already in the map
                if (iterator != first_complements.end()) {
                        std::cout << "Key:" << iterator->first << ", Value:" << iterator->second << std::endl;
                        // return the product
                        int product = iterator->first * iterator->second;
                        // part one: 
                        std::cout << "Product:" << product << std::endl;
                }
                // add the number and the compliment to the map.
                else first_complements[number] = 2020-number;
        }
        file.clear(); // clear any error flags
        file.seekg(0, std::ios::beg);
        
        for (auto it = first_complements.begin(); it != first_complements.end(); ++it) {
                int value = it->second;
                int key = it->first;
        
                while (std::getline(file, line)) {
                        int difference = std::stoi(line)- value;
                        auto x = first_complements.find(difference);
                        if (x != first_complements.end()) {
                            int a = key;
                            int b = value - std::stoi(line);
                            int c = std::stoi(line);
                            std::cout << "a+b+c"<< a <<","<< b <<","<< c << std::endl;
                        } 
                        else std::cout << "No luck "<< std::endl;
                }
        }

        file.close();

        return 0;
}