/*
Problem: 1528 - Shuffle String
Difficulty: Easy
URL: https://leetcode.com/problems/shuffle-string/
*/

#include <vector>
#include <string>

class Solution
{
public:
    std::string restoreString(std::string s, std::vector<int>& indices)
    {
        std::string shuffled = s;
        for (int i = 0; i < indices.size(); i++)
        {
            shuffled[indices[i]] = s[i];
        }
        return shuffled;
    }
};