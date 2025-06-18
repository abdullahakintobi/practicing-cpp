// C++ script that calculates BMI (Body Mass Index) based on user input.
#include <iostream>

int main() {
    double weight, height, bmi;

    // Prompt user for weight in kilograms
    std::cout << "Enter your weight in kilograms: ";
    std::cin >> weight;

    // Prompt user for height in meters
    std::cout << "Enter your height in meters: ";
    std::cin >> height;

    // Calculate BMI
    bmi = weight / (height * height);

    // Output the result
    std::cout << "Your Body Mass Index (BMI) is: " << bmi << std::endl;

    return 0;
}