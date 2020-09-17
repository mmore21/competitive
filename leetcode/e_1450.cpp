/*
Problem: 1450 - Number of Students Doing Homework at a Given Time
Difficulty: Easy
URL: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
*/

#include <vector>

class Solution
{
public:
    int busyStudent(std::vector<int>& startTime, std::vector<int>& endTime, int queryTime)
    {
        int busyCount = 0;
        
        for (int i = 0; i < startTime.size(); i++)
        {
            if (queryTime >= startTime.at(i) && queryTime <= endTime.at(i))
            {
                busyCount++;
            }
        }
        
        return busyCount;
    }
};