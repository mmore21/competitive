/*
Problem: 1929 - Concatenation of Array
Difficulty: Easy
URL: https://leetcode.com/problems/concatenation-of-array/
*/

int *getConcatenation(int *nums, int numsSize, int *returnSize)
{
    int *res = malloc(numsSize * 2 * sizeof(int));
    *returnSize = numsSize * 2;
    
    for (int i = 0; i < numsSize; i++)
    {
        res[i] = nums[i];
        res[numsSize + i] = nums[i];
    }
    
    return res;
}