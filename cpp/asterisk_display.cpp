// For loop in C++
#include <iostream>
#include <string>

int main()
{
    std::string astr = "*";
    
    for(int i = 0; i <= 10; i++)
    {
        std::cout << astr << std::endl;
        astr += "*";
    }
    return 0;
}

/* 
Output:

*
**
***
****
*****
******
*******
********
*********
**********
***********

*/
