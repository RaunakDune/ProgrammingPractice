public class calculateFactors
{   
    /**
     * Returns the Lowest Common Multiple of the two inut ingers
     * 
     * To be more efficient, used the result from the calculateGCD function
     *  
     * @param a     First Input integer
     * @param b     Second Input integer
     * @return      Lowest Common Denominator
     */
    public int calculateLCM(int a, int b){
        return ((a * b) / calculateGCD(a,b));
    }

    /**
     * Returns the Greatest Common Divisor or Highest Common Factor of the two input integers.
     * 
     * To optimize complexity, does not Euclidean recusrive method 
     * 
     * @param a     First Input integer
     * @param b     Second Input integer
     * @return      Greatest Common Divisor or Highest Common Factor
     */
    public int calculateGCD(int a, int b){


        int lower = (a < b) ? a : b;

        if ((a % lower) == 0 && (b % lower) == 0){
            return lower;
        }

        for (int iter = (lower / 2); iter >= 2; iter--){
            if ( (a % iter == 0) && (b % iter == 0) ){
                return iter;
            }
        }

        //Base Case:
        return 1;
    }

    public static void main(String args[]){
        try{
            int a = Integer.parseInt(args[1]);
            int b = Integer.parseInt(args[2]);
            int result = 0;
            if (args[0].equalsIgnoreCase("LCM")){
                result = new calculateFactors().calculateLCM(a, b);
            }
            else if (args[0].equalsIgnoreCase("HCF") || args[0].equalsIgnoreCase("GCD")){
                result = new calculateFactors().calculateGCD(a,b);
            }

            System.out.println("Input Numbers: " + a + " and " + b);
            System.out.println(args[0]+" : "+result);
        }catch(NumberFormatException n){
            System.out.println("ERROR: Integers expected");
        }
        catch(ArrayIndexOutOfBoundsException ae){
            System.out.println("ERROR: Input format \n $java calculateFactors <LCM/HCF/GCD> <Input Integer 1> <Input Integer 2>  ");
        }
        catch(Exception e){
            System.out.println("ERROR");
        }
    }
}