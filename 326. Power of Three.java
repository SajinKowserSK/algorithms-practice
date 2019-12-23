class Solution {
    public boolean isPowerOfThree(double n) {
        if (n == 1.00) return true;
        else if (n < 3 && n != 1.00) return false;
        else return isPowerOfThree(n/3);    
    }
}