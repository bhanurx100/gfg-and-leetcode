class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # maintain 2 lists
        l1 = list() # one for storing XOR elements
        l2 = list() # other for storing non xor elements

        for num in nums:
            if num ^ k > num:
                l1.append(num^k)
            else:
                l2.append(num)

        # If length of the XOR array is even then simply return the sum of both arrays
        if len(l1) % 2 == 0:
            return sum(l1)+sum(l2)

        # If length of XOR arrays is not even the try every possibility by removing one element from XOR array or Adding 1 element to XOR array to make the length even
        else:
            ans = 0
            l1_sum = sum(l1)
            l2_sum = sum(l2)
            total = l1_sum+l2_sum
            for i in l1:
                ans = max(ans, total - (i) + (i^k))
            for i in l2:
                ans = max(ans, total + (i^k) - i)
            return ans
      