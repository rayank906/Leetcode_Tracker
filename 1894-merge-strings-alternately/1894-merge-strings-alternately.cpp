class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string alt = "";
        if (word1.size() > word2.size()){
            for (int i = 0; i < word1.size(); i++){
                while (i < word2.size()){
                    for (int j = 0; j < word2.size(); j++){
                        alt += word1[j];
                        alt += word2[j];
                        i++;
                    }
                }
                alt += word1[i];
            }
        }
        else if (word2.size() > word1.size()){
            for (int i = 0; i < word2.size(); i++){
                while (i < word1.size()){
                    for (int j = 0; j < word1.size(); j++){
                        alt += word1[j];
                        alt += word2[j];
                        i++;
                    }
                }
                alt += word2[i];
            }
        }
        else {
            for (int i = 0; i < word1.size(); i++){
                alt += word1[i];
                alt += word2[i];
            }
        }
        return alt;
    }
};