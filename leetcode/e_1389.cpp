/*
Problem: 1389 - Create Target Array in the Given Order
Difficulty: Easy
URL: https://leetcode.com/problems/create-target-array-in-the-given-order/
*/

#include <vector>

class Solution
{
public:
    std::vector<int> createTargetArray(std::vector<int>& nums, std::vector<int>& index)
    {
        std::vector<int> target;
        for (int i = 0; i < nums.size(); i++)
        {
            std::vector<int>::iterator it = target.begin();
            it += index.at(i);
            target.insert(it, nums.at(i));
        }
        return target;
    }
};