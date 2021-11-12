/*
Problem: 1561 - Maximum Number of Coins You Can Get
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
*/

#include <algorithm>
#include <vector>

class Solution
{
public:
    int maxCoins(std::vector<int>& piles)
    {
        int sum = 0;
        std::sort(piles.begin(), piles.end(), std::greater<int>());
        
        int pileLen = piles.size();
        for (int i = 1; i < pileLen; i += 2)
        {
            sum += piles.at(i);
            pileLen--;
        }
        
        return sum;
    }
};