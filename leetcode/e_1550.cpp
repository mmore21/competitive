/*
Problem: 1550 - Three Consecutive Odds
Difficulty: Easy
URL: https://leetcode.com/problems/three-consecutive-odds/
*/

#include <vector>

class Solution
{
public:
    bool threeConsecutiveOdds(std::vector<int>& arr)
    {
        if (arr.size() < 3)
        {
            return false;
        }
        else
        {
            for (int i = 0; i < arr.size() - 2; i++)
            {
                if (arr.at(i+2) % 2 == 0)
                {
                    i+=2;
                }
                else if (arr.at(i+1) % 2 == 0)
                {
                    i += 1;
                }
                else if (arr.at(i+1) % 2 == 0)
                {
                    continue;
                }
                else
                {
                    return true;
                }
            }
            return false;
        }

    }
};

class Solution
{
public:
    bool threeConsecutiveOdds(std::vector<int>& arr)
    {
        int count = 0;
        for (std::vector<int>::const_iterator it = arr.begin(); it != arr.end(); it++)
        {
            count = *it % 2 == 0 ? 0 : count + 1;
            if (count == 3)
            {
                return true;
            }
        }
        return false;
    }
};