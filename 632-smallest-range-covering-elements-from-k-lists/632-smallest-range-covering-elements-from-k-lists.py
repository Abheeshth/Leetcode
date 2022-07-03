class Solution:
    def smallestRange(self, A: List[List[int]]) -> List[int]:
        '''
        # let's male a heap
        Range = [[float('-inf'),float('inf')]]
        xRange = float('inf')
        heap = [[nums[i][0],i,0] for i in range(len(nums))]
        maxi = max([nums[i][0] for i in range(len(nums))])
        heapify(heap)
        p = 0
        while p<=len(nums[0]):
            #print(heap)
            mini,row,index = heappop(heap)
            #print(mini,maxi,xRange)
            if maxi - mini < xRange:
                #print('yahaa')
                xRange = maxi-mini
                Range.pop(0)
                Range.append([mini,maxi])
            if index+1 >= len(nums[row]):
                break
            index+=1
            heappush(heap,[nums[row][index],row,index])
            if nums[row][index] > maxi:
                maxi = nums[row][index]
            p = index
            #print(Range)
            #print(heap)
        
        #print(Range)
        return Range[0]
                '''
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in A)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(A[i]):
                return ans
            v = A[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))

        #return ans
            
            
            
        