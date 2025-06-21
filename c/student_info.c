// Variables in C
#include <stdio.h>
#include <stdbool.h>

int main() {
    char name[] = "Williams";
    double pi = 3.14159265358979323846;
    int score = 88;
    float gpa = 4.7;
    char grade = 'A';
    bool student = true;
    
    if(student) {
        printf("Hello, %s! 😊\n", name);
        printf("You have correctly approximated π to %.4lf (4 decimal place). Your score, GPA, and grade are %d, %.1f, and %c respectively.\n", pi, score, gpa, grade);
    }
    else {
        printf("Sorry, you're not our student.\n");
    }
    
    return 0;
}