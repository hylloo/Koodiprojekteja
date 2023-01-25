public class BottleDispenser {
    private int bottles;
    private int money;
    
    public BottleDispenser() {
        bottles = 5;
        money = 0;
    }
    
    public void addMoney() {
        money += 1;
        System.out.println("Klink! Added more money!");
    }
    
    public void buyBottle() {
        if (money < 1) {
            System.out.println("Add money first!");
        }else{
        money -= 1;
            if (bottles < 1){
                System.out.println("ei pulloja");
            }else{
            bottles -= 1;

            System.out.println("KACHUNK! A bottle came out of the dispenser!");
    }}}
    
    public void returnMoney() {
        money = 0;
        System.out.println("Klink klink. Money came out!");
    }
}
