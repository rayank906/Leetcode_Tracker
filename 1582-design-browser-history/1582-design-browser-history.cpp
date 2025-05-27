class BrowserHistory {
private:
    list<string> history;
    list<string>::iterator page;
public:
    BrowserHistory(string homepage) {
        history.push_back(homepage);
        page = history.begin();
    }
    
    void visit(string url) {
        auto it = page;
        it++;
        if (it == history.end()) {
            page = history.insert(it, url);
        }
        else {
            history.erase(it, history.end());
            page = history.insert(history.end(), url);
        }
    }
    
    string back(int steps) {
        int dist_to_front = distance(history.begin(), page);
        if (steps >= dist_to_front) {
            page = history.begin();
        }
        else {
            for (int i = 0; i < steps; i++) {
                --page;
            }
        }
        return *page;
    }
    
    string forward(int steps) {
        int dist_to_back = distance(page, history.end());
        if (steps >= dist_to_back) {
            page = prev(history.end());
        }
        else {
            for (int i = 0; i < steps; i++) {
                ++page;
            }
        }
        return *page;
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */

 /*
    - keep track of page [iterator to curr obj], number of steps moved [num steps obj], pages visited [doubly linked list]
    - bh: initialize list and insert homepage, then assign iterator to page
    - visit: insert url if at the back, push back, else erase forward hist and push back
    - back: if steps > possible moves, return first element
        else loop step times and increment rbegin it until you get to desired element
    - forward: if steps > possible moves, return last element
        else loop step times from and increment begin
 */