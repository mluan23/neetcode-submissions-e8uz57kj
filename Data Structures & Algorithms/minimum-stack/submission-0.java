class MinStack {
    List<Integer> stack;
    List<Integer> mins;

    public MinStack() {
        stack = new ArrayList<>();
        mins = new ArrayList<>();
    }
    
    public void push(int val) {
        stack.add(val);
        if(mins.isEmpty() || val <= mins.get(mins.size()-1)){
            mins.add(val);
        }
        
    }
    
    public void pop() {
        if(stack.isEmpty()){
            return;
        }
        int val = stack.get(stack.size()-1);
        stack.remove(stack.size()-1);
        if(val == mins.get(mins.size()-1)){
            mins.remove(mins.size()-1);
        }

    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return mins.get(mins.size()-1);
    }
}
