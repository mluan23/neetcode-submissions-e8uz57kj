class Solution {
    // please revisit
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        HashSet<Integer> se = new HashSet<>();
        HashSet<Integer> starts = new HashSet<>();
        for(int i = 0 ; i < n; i++){
            se.add(nums[i]);
        }
        for(int i = 0 ; i < n ; i++){
            int nn = nums[i];
            if(!se.contains(nn-1)){
                starts.add(nn);
            }
        }
        int max = 0;
        for(Integer i : starts){
            int ii = i;
            int count = 1;
            while(se.contains(ii+1)){
                count++;
                ii++;
            }
            if(count > max){
                max = count;
            }
        }
        return max;
    }
}
