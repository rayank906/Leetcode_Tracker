class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int current_num = 0;
        int while_i = 0;

        // override all duplicates
        for (int i = 0; i < nums.size(); i=while_i) {
            current_num = nums[i];
            while_i = ++i;
            while (while_i < nums.size() && nums[while_i] == current_num) {
                nums[while_i] = -101;
                while_i++;
            }
        }

        // shift all elements that aren't -101 to the start
        int unique_idx = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != -101) {
                nums[unique_idx] = nums[i];
                unique_idx++;
            }
        }
        
        return unique_idx;
    }
};