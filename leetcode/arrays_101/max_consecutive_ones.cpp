#include <vector>

class Solution
{
public:
    int findMaxConsecutiveOnes(std::vector<int>& nums)
    {
        int max = 0;
        int streak = 0;
        
        for (std::vector<int>::const_iterator it = nums.begin(); it != nums.end(); it++)
        {
            if (*it == 1)
            {
                streak++;
            }
            else
            {
                if (streak > max)
                {
                    max = streak;
                }
                streak = 0;
            }
        }
        
        return max > streak ? max : streak;
    }
};