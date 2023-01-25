

public class BottleDispenser {
    private int bottles;
    // The array for the Bottle-objects
    private Bottle[] bottle_array;
    private int money;
    public String name = "Pepsi Max";
    public String manufacturer = "Pepsi";
    public String total_energy = "0";
    public BottleDispenser() {
        bottles = 50;
        money = 0;
        
        // Initialize the array
        bottle_array = new Bottle[bottles];
        // Add Bottle-objects to the array
        for(int i = 0;i<bottles;i++) {
            // Use the default constructor to create new Bottles
            bottle_array[i] = new Bottle();
            System.out.println(bottle_array[i]);
        }
        
    }
    
    public void addMoney() {
        money += 1;
        System.out.println("Klink! Money was added into the machine!");
    }
    
    public void buyBottle() {
        bottles -= 1;
        System.out.println("KACHUNK! Bottle appeared from the machine!");
    }
    
    public void returnMoney() {
        money = 0;
        System.out.println("Klink klink. All money gone!");
    }
}