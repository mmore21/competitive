/*
Problem: 1512 - Number of Good Pairs
Difficulty: Easy
URL: https://leetcode.com/problems/number-of-good-pairs/
*/


#include <vector>

class Solution
{
public:
    int numIdenticalPairs(std::vector<int>& nums)
    {
        int good_pairs = 0;
        for (int i = 0; i < nums.size() - 1; i++)
        {
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[i] == nums[j])
                {
                    good_pairs++;
                }
            }
        }
        return good_pairs;
    }
};