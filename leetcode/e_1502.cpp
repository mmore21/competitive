/*
Problem: 1502 - Can Make Arithmetic Progression From Sequence
Difficulty: Easy
URL: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
*/

#include <algorithm>
#include <vector>

class Solution
{
public:
    bool canMakeArithmeticProgression(std::vector<int>& arr)
    {
        std::sort(arr.begin(), arr.end());
        int difference = arr.at(0) - arr.at(1);
        for (int i = 0; i < arr.size() - 1; i++)
        {
            if (arr.at(i) - arr.at(i + 1) != difference)
            {
                return false;
            }
        }
        return true;
    }
};