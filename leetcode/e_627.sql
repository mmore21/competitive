-- Problem: 627 - Swap Salary
-- Difficulty: Easy
-- URL: https://leetcode.com/problems/swap-salary/

UPDATE salary
SET sex = CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;