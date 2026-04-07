class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> all = new ArrayList<>();
        backtrack(all, 0, 0, "", n);
        return all;
    }
    public void backtrack(List<String> all, int n_left, int n_right, String cur, int n){
        if(cur.length() == n*2 && isValid(cur) && !all.contains(cur)){
            all.add(cur);
            return;
        }
        if(cur.length() > n*2){
            return;
        }
        System.out.println(cur);
        backtrack(all, n_left+1, n_right, cur+"(", n);
        backtrack(all, n_left, n_right+1, cur+")", n);

    }
    public boolean isValid(String cur){
        List<Character> s = new ArrayList<>();
        for(int i = 0 ; i < cur.length(); i++){
            if(cur.charAt(i) == '('){
                s.add('(');
            }
            else{
                if(s.isEmpty()){
                    return false;
                }
                s.remove(s.size()-1);
            }
        }
        return s.isEmpty();
    }
}
/**
looks like some backtracking type of thing
i think need to keep track of placed open/closed parens

so can always start with (
add a ( or )
*/