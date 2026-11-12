class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            
            if start <= last_end:
                merged[-1][1] = max(last_end, end)   # overlap: extend the end
            else:
                merged.append([start, end])          # no overlap: new interval

        return merged