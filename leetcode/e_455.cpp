

/*
Problem: 455 - Assign Cookies
Difficulty: Easy
URL: https://leetcode.com/problems/assign-cookies/
*/

#include <algorithm>
#include <vector>

class Solution
{
public:
    int findContentChildren(std::vector<int>& g, std::vector<int>& s)
    {
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());
        
        int count = 0;
        
        int j = 0;
        for (int i = 0; i < g.size(); i++)
        {
            if (j >= s.size())
            {
                break;
            }
            else if (s[j] >= g[i])
            {
                count++;
            }
            else
            {
                i--;
            }
            j++;
        }
        
        return count;
    }
};