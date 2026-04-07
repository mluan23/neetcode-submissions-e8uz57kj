class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();
        if(n != m){
            return false;
        }

        HashMap<Character, Integer> cts = new HashMap<>();
        for(int i = 0 ; i < n;i++){
            char c = s.charAt(i);
            cts.put(c, cts.getOrDefault(c,0) + 1);
        }
        for(int i = 0 ; i < n;i++){
            char c = t.charAt(i);
            cts.put(c, cts.getOrDefault(c,0) - 1);
        }
        for(Integer i : cts.values()){
            if(i != 0){
                return false;
            }
        }
        return true;
    }
}
