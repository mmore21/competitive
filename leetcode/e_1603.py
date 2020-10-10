"""
Problem: 1603 - Design Parking System
Difficulty: Easy
URL: https://leetcode.com/problems/design-parking-system/
"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.spots = [self.big, self.medium, self.small]
        

    def addCar(self, carType: int) -> bool:
        self.spots[carType - 1] -= 1
        
        return self.spots[carType - 1] >= 0      