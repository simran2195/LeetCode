class MedianFinder:

    def __init__(self):
        self.numbers = []

            
    def addNum(self, num: int) -> None:
        # we need to add in an ordered manner to the array
        self.numbers.append(num)
        

    def findMedian(self) -> float:
        self.numbers.sort()
        l = len(self.numbers)
        if l % 2 == 0:
            # even number of elements. Return mean of middle two elements
            return (self.numbers[int(l/2)] + self.numbers[int(l/2 - 1 )])/2

        else:
            # return mid element
            return self.numbers[l // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()