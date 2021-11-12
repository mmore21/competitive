/*
Problem: 1475 - Final Prices With a Special Discount in a Shop
Difficulty: Easy
URL: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
*/

#include <vector>

class Solution
{
public:
    std::vector<int> finalPrices(std::vector<int>& prices)
    {
        for (int i = 0; i < prices.size() - 1; i++)
        {
            for (int j = i + 1; j < prices.size(); j++)
            {
                if (prices.at(j) <= prices.at(i))
                {
                    prices[i] -= prices[j];
                    break;
                }
            }
        }
        return prices;
    }
};