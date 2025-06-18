// C++ code to calculate a circle's circumference with user input
#include <iostream>
#include <iomanip>

int main() {
    const double PI = 3.14159;
    double radius;
    
    std::cout << "Input radius value (cm): ";
    std::cin >> radius;
    
    if (radius < 0) {
        std::cout << "Radius cannot be negative.";
        return 1;
    }
    
    double circumference = 2 * PI * radius;
    
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "The Circumference of the circle is " << circumference << " cm." << std::endl;
    
    return 0;
}