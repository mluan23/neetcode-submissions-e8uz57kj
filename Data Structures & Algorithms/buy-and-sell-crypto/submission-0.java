class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int left = 0;
        int right = 1;
        int max = 0;
        while(right < n){
            int buyprice = prices[left];
            int sellprice = prices[right];
            max = Math.max(max, sellprice-buyprice);
            if(buyprice > sellprice){
                left++;
            }
            else{
                right++;
            }
        }
        return max;
    }
}
