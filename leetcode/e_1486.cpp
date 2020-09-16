/*
Problem: 1486 - XOR Operation in an Array
Difficulty: Easy
URL: https://leetcode.com/problems/xor-operation-in-an-array/
*/

#include <vector>

class Solution
{
public:
    int xorOperation(int n, int start)
    {
        std::vector<int> nums;
        
        for (int i = 0; i < n; i++)
        {
            nums.push_back(start + 2*i);
        }
        
        int aggXor = nums.at(0);
        
        for (int i = 1; i < nums.size(); i++)
        {
            aggXor ^= nums.at(i);
        }
        
        return aggXor;
    }
};