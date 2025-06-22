// Practice for loop in Java
public class Main {

    public static void main(String[] args) {
        System.out.println("Practicing Loop:");
        
        System.out.print("x = [");

        for(int x=2; x<=20; x+=2) {
            System.out.print(x);
            
            if(x<20) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}