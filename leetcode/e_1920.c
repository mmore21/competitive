/*
Problem: 1920 - Build Array from Permutation
Difficulty: Easy
URL: https://leetcode.com/problems/build-array-from-permutation/
*/

int *buildArray(int *nums, int numsSize, int *returnSize)
{
    int *res = malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    
    for (int i = 0; i < numsSize; i++)
    {
        res[i] = nums[nums[i]];
    }
    
    return res;
}