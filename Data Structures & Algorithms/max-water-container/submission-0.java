class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int left = 0;
        int right = n-1;
        int max = 0;
        while(left <= right){
            int l = heights[left];
            int r = heights[right];
            if(Math.min(l,r) * (right - left) > max){
                max = Math.min(l,r)*(right-left);
            }
            if(l < r){
                left++;
            }
            else{
                right--;
            }
        }
        return max;
    }
}
