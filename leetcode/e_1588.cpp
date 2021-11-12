/*
Problem: 1588 - Sum of All Odd Length Subarrays
Difficulty: Easy
URL: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
*/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution
{
public:
    int sumOddLengthSubarrays(std::vector<int>& arr)
    {
        int sum = 0;
        
        for (int i = 1; i <= arr.size(); i+=2)
        {
            for (int j = 0; j <= arr.size() - i; j++)
            {
                std::vector<int>::const_iterator front = arr.begin() + j;
                std::vector<int>::const_iterator end = arr.begin() + i + j;
                std::vector<int> currArr(front, end);
                
                sum += std::accumulate(currArr.begin(), currArr.end(), 0);
            }
            
        }
        
        return sum;
    }
};