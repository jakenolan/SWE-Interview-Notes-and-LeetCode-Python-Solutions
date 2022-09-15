class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort list by custom sorting equation (distance formula)
        points.sort(key=self.distance_formula)
        
        # Return k smallest
        return points[:k]
    
    def distance_formula(self, point: List[int]):
        return sqrt((point[0]**2) + (point[1]**2))