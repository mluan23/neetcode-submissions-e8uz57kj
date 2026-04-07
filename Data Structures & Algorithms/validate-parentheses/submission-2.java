class Solution {
    public boolean isValid(String s) {
        List<Character> chars = new ArrayList<>();
        for(int i = 0 ; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '(' || c == '{' || c == '['){
                chars.add(c);
            }
            else{
                if(chars.isEmpty()){
                    return false;
                }
                if(c == '}'){
                    if(chars.get(chars.size()-1) != '{'){
                        return false;
                    }
                    chars.remove(chars.size()-1);
                }
                if(c == ']'){
                    if(chars.get(chars.size()-1) != '['){
                        return false;
                    }
                    chars.remove(chars.size()-1);
                }
                if(c == ')'){
                    if(chars.get(chars.size()-1) != '('){
                        return false;
                    }
                    chars.remove(chars.size()-1);
                }
            }
        }
        return chars.isEmpty();
    }
}
