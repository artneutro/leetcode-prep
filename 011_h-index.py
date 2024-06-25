# https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the list to check backwards
        sorted_citations = sorted(citations)
        # Start in the last element
        index = len(sorted_citations)-1
        # Current value
        cur_h = 0
        # Current max h-index
        max_h = 0
        # Case [0]*n
        if sorted_citations[index] == 0 :
            return 0
        # Case [1]
        if len(sorted_citations) == 1 :
            return 1
        # Iterate over the values
        while (index >= 0) :
            cur_h = sorted_citations[index]
            # Case [1,1]
            if cur_h > 0 and max_h == 0 :
                max_h = 1
            if cur_h == 0 :
                return max_h
            while (index >= 0) :
                if sorted_citations[index] == cur_h :
                    index = index-1
                else :
                    index = index+1
                    break
            # Case [1,1]
            if index < 0 :
                index = 0
            size_so_far = len(sorted_citations)-index
            if cur_h >= size_so_far :
                max_h = size_so_far
            else :
                # Case [2,2,2]
                if max_h < cur_h :
                    max_h = cur_h
            index = index-1
        if index <= 0 :
            return max_h
