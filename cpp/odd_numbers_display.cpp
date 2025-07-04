#include <iostream>

int main() {
    int num = 0;
    while (num < 10) {
        num++;
        if (num % 2 == 0) { // If num is even
            continue;       // Skip to the next iteration
        }
        std::cout << "Odd number: " << num << std::endl;
    }
    return 0;
}
