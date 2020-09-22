/*
Problem: 1529 - Bulb Switcher IV
Difficulty: Medium
URL: https://leetcode.com/problems/bulb-switcher-iv/
*/

#include <string>

class Solution
{
public:
    int minFlips(std::string target)
    {
        int count = 0;
        char lights = '0';
        
        for (int i = 0; i < target.size(); i++)
        {
            if (target[i] != lights)
            {
                count++;
                lights = lights == '1' ? '0' : '1';
            }
        }
        
        return count;
    }
};