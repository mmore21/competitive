/*
Problem: 1464 - Maximum Product of Two Elements in an Array
Difficulty: Easy
URL: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
*/

#include <algorithm>
#include <vector>

class Solution
{
public:
    int maxProduct(std::vector<int>& nums)
    {
        auto idxMax1 = std::max_element(nums.begin(), nums.end());
        int max1 = *idxMax1;
        nums.erase(idxMax1);
        auto idxMax2 = std::max_element(nums.begin(), nums.end());
        int max2 = *idxMax2;
        
        return (max1 - 1) * (max2 - 1);
    }
};