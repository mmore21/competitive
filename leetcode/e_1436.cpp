/*
Problem: 1436 - Destination City
Difficulty: Easy
URL: https://leetcode.com/problems/destination-city/
*/

#include <algorithm>
#include <string>
#include <vector>

class Solution
{
public:
    std::string destCity(std::vector<std::vector<std::string>>& paths)
    {
        std::vector<std::string> destinations;
        
        std::vector<std::vector<std::string>>::const_iterator it;
        
        for (it = paths.begin(); it != paths.end(); it++)
        {
            destinations.push_back((*it)[1]);
        }
        
        for (it = paths.begin(); it != paths.end(); it++)
        {
            destinations.erase(std::remove(destinations.begin(), destinations.end(), (*it)[0]), destinations.end());
        }
        
        return destinations.front();
    }
};