/*
Problem: 1431 - Kids With the Greatest Number of Candies
Difficulty: Easy
URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
*/

#include <vector>
#include <algorithm>

class Solution
{
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies)
    {     
        int max = *max_element(std::begin(candies), std::end(candies));
        
        std::vector<bool> possibleMaxCandies;
        
        for (std::vector<int>::const_iterator it = candies.begin(); it != candies.end(); it++)
        {
            possibleMaxCandies.push_back(*it + extraCandies >= max);
        }
        
        return possibleMaxCandies;
    }
};