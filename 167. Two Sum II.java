class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // outer for loop
        // inner for loop
        // if numbers[outer] + numbers[inner] == target, return outter, inner
        int [] ret = new int [2];
        for (int x = 0; x < numbers.length; x++){
            for (int y = x+1; y < numbers.length; y++){
                if (numbers[x]+numbers[y] == target){
                    ret[0] = x+1;
                    ret [1] = y+1;
                }
            }
        }
        
        return ret;
        
    }
}