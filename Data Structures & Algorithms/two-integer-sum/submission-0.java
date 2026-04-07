class Solution {
    public int[] twoSum(int[] nums, int target) {
       int n = nums.length;

       Map<Integer, Integer> vals =new HashMap<>();

       for(int i = 0; i < n; i++){
        int diff = target-nums[i];
        if(vals.containsKey(diff)){
            int[] a = {vals.get(diff), i};
            return a;
        }
        vals.put(nums[i], i);
       }
       return new int[2];
    }
}
