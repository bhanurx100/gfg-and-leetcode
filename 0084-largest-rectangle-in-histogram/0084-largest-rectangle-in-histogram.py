class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[-1]
        max_area=0
        for i in range(len(heights)):
            while st[-1]!=-1 and heights[i]<=heights[st[-1]]:
                height=heights[st.pop()]
                width=i-st[-1]-1
                max_area=max(max_area,height*width)
            st.append(i)
        while st[-1]!=-1:
            height=heights[st.pop()]
            width=len(heights)-st[-1]-1
            max_area=max(max_area,height*width)
        return max_area