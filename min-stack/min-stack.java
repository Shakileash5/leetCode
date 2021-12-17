class MinStack {
    
    private List<Integer> stack;
    private List<Integer> minStack;
    private int top;
    
    public MinStack() {
        this.stack = new ArrayList<>();
        this.minStack = new ArrayList<>();
        this.top = -1;
    }
    
    public void push(int val) {
        this.stack.add(val);
        if(this.minStack.size()>0){
            if(this.minStack.get(this.top) > val){
                this.minStack.add(val);
            }
            else{
                this.minStack.add(this.minStack.get(this.top));
            }
        }
        else{
            this.minStack.add(val);
        }
        this.top++;
    }
    
    public void pop() {
        this.stack.remove(this.top);
        this.minStack.remove(this.top);
        this.top--;
    }
    
    public int top() {
        return this.stack.get(this.top);
    }
    
    public int getMin() {
        return this.minStack.get(this.top);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */