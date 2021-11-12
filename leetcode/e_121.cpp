/*
Problem: 121 - Best Time to Buy and Sell Stock
Difficulty: Easy
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
*/

#include <limits>
#include <vector>

class Solution
{
public:
    int maxProfit(std::vector<int>& prices)
    {
        int minPrice = std::numeric_limits<int>::max();
        int maxProfit = 0;
        
        for (int i = 0; i < prices.size(); i++)
        {
            if (prices[i] < minPrice)
            {
                minPrice = prices[i];
            }
            else if (prices[i] - minPrice > maxProfit)
            {
                maxProfit = prices[i] - minPrice;
            }
        }
        
        return maxProfit;
    }
};