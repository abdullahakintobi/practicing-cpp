// Generate and display even numbers in a list format
#include <stdio.h>

int main() {
    printf("x = [");
    
    for(int x = 2; x <= 10; x += 2 ) {
        printf("%d", x);
            
        if(x < 10) {
            printf(", ");
        }
    }
    printf("]\n");
    
    return 0;
}