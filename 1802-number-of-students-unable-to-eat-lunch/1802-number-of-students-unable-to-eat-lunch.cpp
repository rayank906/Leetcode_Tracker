class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int stud_z = 0;
        int stud_o = 0;
        int res = sandwiches.size();
        
        for (int i = 0; i < students.size(); i++) {
            if (students[i] == 0) { stud_z++; }
            else { stud_o++; }
        }

        for (int i = 0; i < sandwiches.size(); i++) {
            if (sandwiches[i] == 1) {
                if (stud_o > 0) {
                    res--;
                    stud_o--;
                }
                else {
                    return res;
                }
            }
            else {
                if (stud_z > 0) {
                    res--;
                    stud_z--;
                }
                else {
                    return res;
                }
            }
        }

        return res;
    }
};

/*
*/