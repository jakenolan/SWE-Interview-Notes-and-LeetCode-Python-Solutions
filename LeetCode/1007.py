# TOO SLOW
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Create python counter for each list
        # Gets max number of occurences
        self.tops_counter = Counter(tops)
        self.bottoms_counter = Counter(bottoms)
        
        # Loop through occurences in descending order
        while self.tops_counter and self.bottoms_counter:
            # Get max occurence
            self.tops_max = max(self.tops_counter, key=self.tops_counter.get)
            self.bottoms_max = max(self.bottoms_counter, key=self.bottoms_counter.get)
            if self.tops_counter[self.tops_max] > self.bottoms_counter[self.bottoms_max]:
                self.max_ref = ['top', self.tops_max, len(tops) - self.tops_counter[self.tops_max]]
            else:
                self.max_ref = ['bottom', self.bottoms_max, len(bottoms) - self.bottoms_counter[self.bottoms_max]]
            # Check this occurence
            if self.max_ref[0] == 'tops':
                solution_found = self.helper(name='tops', main=tops, other=bottoms)
            else:
                solution_found = self.helper(name='bottoms', main=bottoms, other=tops)
            # If solution found
            if solution_found:
                return self.max_ref[2]
        
        # Cannot be done
        return -1

    def helper(self, name, main, other):
        check = 0
        while check < self.max_ref[2]:
            for i in range(len(main)):
                if main[i] != self.max_ref[1] and other[i] == self.max_ref[1]:
                    check += 1
                elif main[i] != self.max_ref[1] and other[i] != self.max_ref[1]:
                    if name == 'tops':
                        del self.tops_counter[self.max_ref[1]]
                    else:
                        del self.bottoms_counter[self.max_ref[1]]
                    return False
        # If check passes
        return True