"""
Problem: 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
Difficulty: Medium
URL: https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
"""

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        out = []
        alerts = {}
        
        for i in range(len(keyName)):
            seconds = int(keyTime[i][:2]) * 60 + int(keyTime[i][-2:])
            if keyName[i] in alerts:
                alerts[keyName[i]].append(seconds)
            else:
                alerts[keyName[i]] = [seconds]
        
        for name, time in alerts.items():
            for i in range(len(time) - 2):
                time = sorted(time)
                if time[i+1] - time[i] <= 60 and time[i+2] - time[i] <= 60:
                    if name not in out:
                        out.append(name)
        
        return sorted(out)