/*
Problem: 1480 - Running Sum of 1d Array
Difficulty: Easy
URL: https://leetcode.com/problems/running-sum-of-1d-array/
*/

 // Reduces runtime.
int *runningSum(int *nums, int numsSize, int *returnSize)
{
    int *res = malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    int sum = 0;
    
    for (int i = 0; i < numsSize; i++)
    {
        sum += nums[i];
        res[i] = sum;
    }
    
    return res;
}

 // Reduces memory.
int *runningSum(int *nums, int numsSize, int *returnSize)
{
    *returnSize = numsSize;
    
    for (int i = 1; i < numsSize; i++)
    {
        nums[i] += nums[i-1];
    }
    
    return nums;
}