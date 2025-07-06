#include <iostream>

// Recursive function to calculate factorial
int factorial(int n) {
    if (n <= 1)  // base case: factorial of 0 or 1 is 1
        return 1;
    else
        return n * factorial(n - 1);  // recursive call
}

int main() {
    int num;
    std::cout << "Enter a non-negative integer: ";
    std::cin >> num;

    if (num < 0) {
        std::cout << "Factorial is not defined for negative numbers." << std::endl;
    } else {
        std::cout << "Factorial of " << num << " is " << factorial(num) << std::endl;
    }

    return 0;
}