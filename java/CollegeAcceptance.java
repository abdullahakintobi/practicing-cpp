import java.util.Scanner;

public class CollegeAcceptance {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Prompt user for their name
        System.out.print("Enter your full name: ");
        String fullName = scanner.nextLine();
        
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        
        System.out.print("Enter your high school CGPA: ");
        double cgpa = scanner.nextDouble();        
        
        // Admission criteria check
        if (age < 16 || cgpa < 2.0) {
            System.out.println("\nWe're sorry, " + fullName + ". You're not accepted.");
        } else {
            System.out.println("\nCongratulations, " + fullName + "! You're accepted!");
        }

        // Close the scanner once
        scanner.close();
    }
}
