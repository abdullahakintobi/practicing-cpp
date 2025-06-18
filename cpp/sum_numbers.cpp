// Input-Output in C++
#include <iostream>

int main()
{
    std::cout << "Kindly add your numbers:" << std::endl;
    int n1, n2 = 0;
    std::cin >> n1 >> n2;
    int sum = n1 + n2;
    std::cout << "The sum of " << n1 << " and " << n2 << " is " << sum << std::endl;
    return 0;
}


/*
This C++ code collects two integers values, n1 and n2 respectively from user and add it together. It then output the message ”The sum of <n1> and <n2> is <n1+n2>. For instance, if user input 4 as n1 and 7 as n2, the message will be "The sum of 4 and 7 is 11"
*/