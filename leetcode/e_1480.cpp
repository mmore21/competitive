/*
Problem: 1480 - Running Sum of 1d Array
Difficulty: Easy
URL: https://leetcode.com/problems/running-sum-of-1d-array/
*/

#include <vector>

class Solution
{
public:
    std::vector<int> runningSum(std::vector<int>& nums)
    {
        int i = 1;
        while (i < nums.size())
        {
            nums[i] += nums[i-1];
            i++;
        }
        return nums;
    }
};