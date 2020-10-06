/*
Problem: 1347 - Minimum Number of Steps to Make Two Strings Anagram
Difficulty: Medium
URL: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
*/

#include <unordered_map>

class Solution
{
public:
    
    void countChars(const std::string &s, std::unordered_map<char, int> &sCounts)
    {
        for (int i = 0; i < s.length(); i++)
        {
            sCounts[s.at(i)]++;
        }
    }
    
    int minSteps(std::string s, std::string t)
    {
        int changeCount = 0;
        std::unordered_map<char, int> sCounts;
        std::unordered_map<char, int> tCounts;
        
        countChars(s, sCounts);
        countChars(t, tCounts);
        
        for(auto elem : sCounts)
        {
            if (sCounts[elem.first] > tCounts[elem.first])
            {
                changeCount += sCounts[elem.first] - tCounts[elem.first];
            }
        }
        
        return changeCount;
    }
};