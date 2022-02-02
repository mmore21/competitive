/*
Problem: 2011 - Final Value of Variable After Performing Operations
Difficulty: Easy
URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
*/

int finalValueAfterOperations(char **operations, int operationsSize)
{
    int x = 0;
    
    for (int i = 0; i < operationsSize; i++)
    {
        operations[i][1] == '+' ? x++ : x--;
    }
    
    return x;
}