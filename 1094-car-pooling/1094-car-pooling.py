class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = []
        curcap = 0
        for trip in trips:
            numpass,start,end = trip
            while heap and heap[0][0] <= start:
                curcap -= heap[0][1]
                heapq.heappop(heap)
            curcap += numpass
            heapq.heappush(heap,(end,numpass))
            if curcap > capacity:
                return False
        return True