// Variable initialization and if-else statement in Java

public class Main {

    public static void main(String[] args) {
        // Variables declaration
        String customerFirstName = "Charles";
        char currency = '$';
        double price = 99.99;
        int quantity = 7;
        boolean buy = true;

        // Conditional Statement
        if(!buy) {
            System.out.println("Your selected items will be added to cart.");
        } else {
            System.out.println("Hi, " + customerFirstName + "! 👋");
            System.out.println("Thanks for shopping with us! 😊");
            System.out.print("You have selected " + quantity + " items at ");
            System.out.print(currency + "" + price + " each. ");
            System.out.println("Your total fee is " + currency + (price * quantity));
        }
    }
}
