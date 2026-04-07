class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();

        if(n != m){
            return false;
        }

        Map<Character, Integer> table = new HashMap<>();

        for(int i = 0; i < 26; i++){
            table.put((char)('a' + i), 0);
        }

        for(int i = 0; i < n; i++){
            table.put(s.charAt(i), table.get(s.charAt(i))+1);
        }

        for(int i = 0; i < m; i++){
            table.put(t.charAt(i), table.get(t.charAt(i))-1);
        }

        for(char c : table.keySet()){
            System.out.println(table.get(c));
            if(table.get(c) != 0){
                return false;
            }
        }
        return true;
    }
}
