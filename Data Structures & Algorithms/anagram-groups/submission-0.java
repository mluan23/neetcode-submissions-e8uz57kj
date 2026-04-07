class Solution {

    // use a frequency array; i guess this is important pattern
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> slns = new HashMap<>();
        // for(String s : strs){
        //     // now what?
        //     // the main issue is we have to do n^2 comparisons; is there a better way?
        // }
        // another hashmap?
        for(int i = 0; i < strs.length; i++){
            int[] letterCounts = new int[26];

            for(int j = 0 ; j < strs[i].length(); j++){
                char letter = strs[i].charAt(j);
                letterCounts[letter - 'a']++;
            }
            String w = Arrays.toString(letterCounts);
            System.out.println(w);
            if(!slns.containsKey(w)){
                slns.put(w, new ArrayList<String>(Arrays.asList(strs[i])));
            }
            else{
                slns.get(w).add(strs[i]);
            }
            //return new ArrayList<>(slns.values());
        }
        return new ArrayList<>(slns.values());
    }

    // public void combineAnagrams(String str1, String str2, List<String> all){
    //     if(isAnagram(str1, str2)){
    //         if(!all.contains(str1)){
    //             all.add(str1);
    //         }
    //         if(!all.contains(str2)){
    //             all.add(str2);
    //         }
    //     }
    // }

    // public boolean isAnagram(String str1, String str2){
    //     if(strl.length() != str2.length()){
    //         return false;
    //     }
    //     HashMap<Character, Integer> s1 = new HashMap<>();
    //     HashMap<Character, Integer> s2 = new HashMap<>();

    //     for(int i = 0; i < str1.length(); i++){
    //         s1.put(str1.charAt(i), s1.getOrDefault(str1.charAt(i),0));
    //         s2.put(str2.charAt(i), s2.getOrDefault(str2.charAt(i),0));
    //     }
    //     return s1.equals(s2);
    // }
}
