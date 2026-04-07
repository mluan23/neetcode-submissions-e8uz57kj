class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int left = 0;
        int right = n-1;
        int[] ret = new int[2];
        while(left < right){
            int num = numbers[left] + numbers[right];
            if(num == target){
                ret[0] = left+1;
                ret[1] = right+1;
                return ret;
            }
            else if(num > target){
                right--;
            }
            else{
                left++;
            }
        }
        return null;
    }
}
