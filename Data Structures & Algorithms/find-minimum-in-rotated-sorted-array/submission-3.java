class Solution {
    // find the position where it decreases
    public int findMin(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n-1;
        while(left < right){
            int ln = nums[left];
            int rn = nums[right];
            int mid = (left + right)/2;
            int mn = nums[mid];
            if(mn < rn){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        return nums[left];
    }
}
