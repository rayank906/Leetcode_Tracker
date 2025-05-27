class MyStack {
private:
    list<int> my_stack;
public:
    MyStack() {
        
    }
    
    void push(int x) {
        my_stack.push_back(x);
    }
    
    int pop() {
        int var = my_stack.back();
        my_stack.pop_back();
        return var;
    }
    
    int top() {
        return my_stack.back();
    }
    
    bool empty() {
        return my_stack.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */