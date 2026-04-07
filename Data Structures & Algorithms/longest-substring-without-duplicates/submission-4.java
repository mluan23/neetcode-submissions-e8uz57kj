class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }
        Set<Character> seen = new HashSet<>();
        int left = 0 ; // start of sequence
        int right = 1; // end of sequecne
        int max = 0;
        seen.add(s.charAt(left));
        while(right < n && left <= right){
            char lc = s.charAt(left);
            char rc = s.charAt(right);
            if(!seen.contains(rc)){
                seen.add(rc);
                right++;
            }
            else{
                left++;
                seen.remove(lc);
            }
            max = Math.max(max, right-left);

        }
        return max;
    }
}
