class MyLinkedList {
private:
    struct Node {
        Node() : val(0), next(nullptr) {}
        int val;
        Node* next;
    };
    int size;
    Node* first;
    Node* last;
public:
    MyLinkedList() : size(0) {
        first = last = new Node();
    }
    
    int get(int index) {
        if (index >= size || size == 0) { return -1; }

        Node* idx = first;
        for (int i = 0; i < index; i++) {
            idx = idx->next;
        }

        return idx->val;
    }
    
    void addAtHead(int val) {
        if (size == 0) {
            first->val = val;
        }
        else {
            Node* add = new Node();
            add->val = val;
            add->next = first;
            first = add;
        }
        size++;
    }
    
    void addAtTail(int val) {
        if (size == 0) {
            last->val = val;
        }
        else {
            Node* add = new Node();
            add->val = val;
            last->next = add;
            last = add;
        }
        size++;
    }
    
    void addAtIndex(int index, int val) {
        if (index > size) { return ;}
        if (index == 0) {
            addAtHead(val);
        }
        else if (index == size) {
            addAtTail(val);
        }
        else {
            Node* idx = first;
            for (int i = 0; i < index - 1; i++) {
                idx = idx->next;
            }

            Node* add = new Node();
            add->val = val;
            add->next = idx->next;
            idx->next = add;

            size++;
        }
    }
    
    void deleteAtIndex(int index) {
        if (index >= size) { return; }
        if (size == 1) { 
            delete first; first = last = new Node();
        }
        else if (index == 0) {
            Node* del = first;
            first = first->next;
            delete del;
        }
        else {
            Node* idx = first;
            for (int i = 0; i < index - 1; i++) {
                idx = idx->next;
            }
            Node* del = idx->next;
            if (del->next) { 
                idx->next = del->next; 
            }
            else {
                idx->next = nullptr;
                last = idx;
            }
            delete del;
        }
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */