/*
Problem: 1309 - Decrypt String from Alphabet to Integer Mapping
Difficulty: Easy
URL: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
*/

#include <string>

class Solution
{
public:
    string freqAlphabets(std::string s)
    {
        std::string alpha;
        for (int i = s.length() - 1; i >= 0; i--)
        {
            if (s[i] == '#')
            {
                int idx = std::stoi(s.substr(i-2, 2));
                char letter = 96 + idx;
                alpha.insert(alpha.begin(), letter);
                i -= 2;
            }
            else
            {
                int idx = s[i] - '0';
                char letter = 96 + idx;
                alpha.insert(alpha.begin(), letter);
            }
        }
        return alpha;
    }
};