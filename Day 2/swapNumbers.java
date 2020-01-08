public class swapNumbers
{
    public void swapper(int a, int b){
        System.out.println("Input Numbers: " + a + " and " + b);
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("After Swapping: " + a + " and " + b);
    }

    public static void main(String args[]){
        try{
            new swapNumbers().swapper(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        }catch(NumberFormatException e){
            System.out.println("ERROR: Integers expected");
        }
        catch(ArrayIndexOutOfBoundsException ae){
            System.out.println("ERROR: please enter atleast two integers");
        }
    }
}