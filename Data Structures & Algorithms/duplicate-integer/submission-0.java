class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n = nums.length;
        Set<Integer> dupes = new HashSet<>();
        for(int i = 0; i < n; i++){
            if(dupes.contains(nums[i])){
                return true;
            }
            dupes.add(nums[i]);
        }
        return false;
    }
}
