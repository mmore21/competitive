/*
Problem: 973 - K Closest Points to Origin
Difficulty: Medium
URL: https://leetcode.com/problems/k-closest-points-to-origin/
*/

#include <vector>
#include <queue>
#include <utility>

class Solution
{
public:
    
    typedef std::pair<float, std::vector<int>> piv;
    
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int K)
    {
        std::vector<int> arr;
        std::priority_queue<piv, std::vector<piv>, std::greater<piv>> pq;
        
        for (int i = 0; i < points.size(); i++)
        {
            float dist = sqrt(pow(points[i][0], 2) + pow(points[i][1], 2));
            pq.push(make_pair(dist, points[i]));
        }
        
        std::vector<std::vector<int>> closest;
        
        for (int i = 0; i < K; i++)
        {
            closest.push_back(pq.top().second);
            pq.pop();
        }
        
        return closest;
    }
};