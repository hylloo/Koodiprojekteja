import java.util.Scanner;

public class Dog {

    private String dogname = "";
    private String says = "";

    public Dog(String name) {

     dogname = name;

        if (dogname.isEmpty()) {
         dogname = "Doge";
        }
        System.out.println("Hey, my name is " + dogname);
    }
    public void speak(String say) {

        Scanner scan = new Scanner(System.in);
        
        //System.out.println(dogname + ": " + says);
        System.out.print("What does a dog say: ");
        String teksti = scan.nextLine();
        //System.out.println(teksti);

        String[] words = teksti.split("[ ]");
            for ( String ss : words) {
               
                if (ss.contains("true")) {
                    System.out.println("Such boolean: "+ss);

                    }

                else if (ss.contains("false")) {
                    System.out.println("Such boolean: "+ss);
                    }

                else if (ss.matches("[0-9].*")){
                    System.out.println("Such integer: "+ss);
                    }

                else {
                    System.out.println(ss);
                }
            }


                
                }
                }
       
        
        
        //System.out.print(dogname + ": " + says);
    


