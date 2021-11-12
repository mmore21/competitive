/*
Problem: 1470 - Shuffle the Array
Difficulty: Easy
URL: https://leetcode.com/problems/shuffle-the-array/
*/

#include <vector>

class Solution
{
public:
    std::vector<int> shuffle(std::vector<int>& nums, int n)
    {
        std::vector<int> shuffled_nums;
        
        for (int i = 0; i < n; i++)
        {
            shuffled_nums.push_back(nums.at(i));
            shuffled_nums.push_back(nums.at(n+i));
        }
        
        return shuffled_nums;
    }
};