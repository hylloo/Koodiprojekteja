import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Mainclass {
    
    public static void main(String args[]) {

        String n1 = "";
        String s1 = "";

        System.out.print("Give a name to the dog: ");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try {
            n1 = br.readLine();
        } catch (IOException ex) {
        }

        Dog dog1 = new Dog(n1);

        //System.out.print("What does a dog say: ");

        //try {
         //   s1 = br.readLine();
        //} catch (IOException ex) {
       // }
        dog1.speak(s1);
        System.out.print("\n");


    }
    
}

