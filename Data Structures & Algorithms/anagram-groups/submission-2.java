class Solution {

    // use a frequency array; i guess this is important pattern
    public List<List<String>> groupAnagrams(String[] strs) {
        // int n = strs.length;
        // List<List<String>> ret = new ArrayList<>();
        // // since anagrams are just rearranged letters of same word,
        // // we should just count the num letters and group by that
        // char[] counts = new char[26];
        // HashMap<String, List<String>> vals = new HashMap<>();
        // for(String str : strs) {
        //     for(char c : str.toCharArray()) {
        //         counts[c - 'a'] += 1;
        //     }
        //     if(vals.get(new String(counts)) != null) {
        //         vals.get(new String(counts)).add(str);
        //     }
        //     else {
        //         vals.put(new String(counts), new ArrayList<>(List.of(str)));
        //     }
        //     counts = new char[26];
        // }
        // return new ArrayList<>(vals.values());
        int n = strs.length;
        char[] counts = new char[26];
        HashMap<String, List<String>> res = new HashMap<>();
        for(String str : strs) {
            for (char c : str.toCharArray()) {
                counts[c - 'a'] += 1;
            }
            if(res.containsKey(new String(counts))) {
                res.get(new String(counts)).add(str);
            }
            else {
                res.put(new String(counts), new ArrayList<>(List.of(str)));
            }
            counts = new char[26];
        }
        return new ArrayList<>(res.values());
    }
}
