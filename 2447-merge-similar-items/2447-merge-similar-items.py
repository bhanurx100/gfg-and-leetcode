class Solution:
	def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

		merge_item = items1 + items2

		d = defaultdict(int)

		for i in merge_item:
			value,weight = i
			d[value] = d[value] + weight

		result = []

		for j in sorted(d):
			result.append([j,d[j]])

		return result