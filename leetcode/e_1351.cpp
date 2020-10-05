/*
Problem: 1351 - Count Negative Numbers in a Sorted Matrix
Difficulty: Easy
URL: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
*/

#include <vector>

class Solution
{
public:
    int countNegatives(std::vector<std::vector<int>>& grid)
    {
        int negativeCount = 0;
        
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[i].size(); j++)
            {
                if (grid[i][j] < 0)
                {
                    negativeCount++;
                }
            }
        }
        
        return negativeCount;
    }
};
