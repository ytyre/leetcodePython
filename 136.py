import collections
from sortedcontainers import SortedDict
class Solution(object):
    def singleNumber(self, nums):
        count = collections.Counter(nums)
        count = SortedDict(count)

        return sorted(count.items(),key=lambda item: item[1]) [0][0]
