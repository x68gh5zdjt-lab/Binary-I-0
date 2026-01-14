import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Scanner;
 
/*
Afton Pate 
1/14/2026
Exercise17_14
*/

public class main {
    public static void main(String[] args) {
        Scanner sus = new Scanner(System.in);       
        System.out.println("read in from this file - ");
        String source = sus.nextLine();
        System.out.println("Write out to this fiel - ");
        String destination = sus.nextLine();
 
        try {
            FileInputStream input = new FileInputStream(source);
            FileOutputStream output = new FileOutputStream(destination);
            for (int i = input.read(); i != -1; i = input.read()) {
                output.write(i - 5);
            }
            System.out.println("don");
        } catch (Exception e) {
            System.out.println("retry");
        }
    }
}
