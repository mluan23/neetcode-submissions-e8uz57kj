class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length();
        HashMap<Character, Integer> counts = new HashMap<>();
        for(int i =  0; i  < s1.length(); i++){
            counts.put(s1.charAt(i), counts.getOrDefault(s1.charAt(i),0)+1);
        }
        int left = 0;
        int right = n-1;
        while(right < s2.length()){
            boolean dnr = true;
            HashMap<Character, Integer> copy = new HashMap<>();
            copy.putAll(counts);
            String s = s2.substring(left, right+1);
            System.out.println(s);
            for(int i = 0 ; i < s.length(); i++){
                char c = s.charAt(i);
                if(copy.getOrDefault(c, 0) == 0){
                    dnr = false;
                    break;
                }
                else{
                    copy.put(c,copy.get(c)-1);
                }
            }
            System.out.println(dnr);

            if(dnr){
                return true;
            }
            right++;
            left++;
        }
        return false;
    }
}
