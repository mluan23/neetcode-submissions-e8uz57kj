class Solution {

// why this works: so when you're passing through the array,
// the map will be empty until you encounter that value
// you try to store the actual value, and then if you can get it 
// through the difference, you get the pair
// [3, 4, 5, 6] target = 8
// so map would be :  {} initially
// iter 1: {3:1}
// iter 2: {4:2}; 8 - 4 = 4
// iter 3: {5:3}; 8 - 5 = 3, so then 5 + 3 = 8

    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] idx = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0 ; i  < n; i++){
            if(map.containsKey(target - nums[i])){
                idx[0] = map.get(target-nums[i]);
                idx[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        return idx;
    }
}
