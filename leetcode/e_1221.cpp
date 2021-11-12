/*
Problem: 1221 - Split a String in Balanced Strings
Difficulty: Easy
URL: https://leetcode.com/problems/split-a-string-in-balanced-strings/
*/

#include <string>

class Solution
{
public:
    int balancedStringSplit(std::string s)
    {
        int balancedCount = 0;
        
        int rCount = 0;
        int lCount = 0;
        
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == 'R')
            {
                rCount++;
            }
            else
            {
                lCount++;
            }
            
            if (rCount == lCount)
            {
                balancedCount++;
                rCount = 0;
                lCount = 0;
            }
        }
        
        return balancedCount;
    }
};