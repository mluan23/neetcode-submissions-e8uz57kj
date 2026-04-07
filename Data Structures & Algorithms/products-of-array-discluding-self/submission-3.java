class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        for(int i = 0; i< n; i++){
            prefix[i] = 1;
            suffix[i] = 1;
        }
        for(int i = 1 ; i < n ; i++){
            prefix[i] *= nums[i-1] * prefix[i-1];
            //System.out.println(prefix[i]);

        }
        for(int i = n-2 ; i >= 0 ; i--){
            suffix[i] *= nums[i+1] * suffix[i+1];
            System.out.println(suffix[i]);

        }
        for(int i = 0; i < n; i ++){
            output[i] = prefix[i] * suffix[i];
            //System.out.println(prefix[i]);
        }
        return output;

        // int n = nums.length;
        // int[] output = new int[n];
        // for(int i = 0 ; i < n ;i++){
        //     output[i] = 1;
        //     for(int j = 0; j < n; j++){
        //         if(j == i){
        //             continue;
        //         }
        //         output[i] *= nums[j];
        //     }
        // }
        // return output;
    }
}  
