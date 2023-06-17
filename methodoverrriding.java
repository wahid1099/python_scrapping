
package labfinal;
import java.util.Scanner;

class NamePrinter {
    void printName(String name) {
        System.out.println("Name: " + name);
    }
}

class UserInputNamePrinter extends NamePrinter {
    @Override
    void printName(String name) {
        System.out.println("My Name: " + name);
    }
}

public class Labfinal {

     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        UserInputNamePrinter printer = new UserInputNamePrinter();
        printer.printName(name);
    }
}