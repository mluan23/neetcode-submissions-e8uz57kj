class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // k buckets, max of nums elements
        int n = nums.length;
        HashMap<Integer, ArrayList<Integer>> buckets = new HashMap<>();
        HashMap<Integer, Integer> frequencies = new HashMap<>();
        int[] res = new int[k];
        // counts the frequencies
        for(int i = 0; i < n; i++) {
            frequencies.put(nums[i], frequencies.getOrDefault(nums[i], 0) + 1);
            buckets.put(i, new ArrayList<>());
        }
        buckets.put(n, new ArrayList<>());
        for(Integer key : frequencies.keySet()) {
            // System.out.println(frequencies);
            int value = frequencies.get(key);
                        // System.out.println(buckets);

            buckets.get(value).add(key);
        }
        int kCount = 0;
        for(int i = n; i >= 0; i--){
            // System.out.print(buckets);
            // System.out.print(frequencies);
            if(buckets.containsKey(i)) {
                for (Integer num : buckets.get(i)) {
                    res[kCount] = num;
                    kCount++;
                    if(kCount == k) return res;
                }
            }
        }
        return res;
    }
}
