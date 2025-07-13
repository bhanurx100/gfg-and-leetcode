class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def dfs(first, second, player_count):

            # base1; they are the same player
            if first == second:  
                return (1, 1)

            # action; swap the recursion when the order is violated
            if first > second:   
                return dfs(second, first, player_count)

            # seen before
            if (first, second, player_count) in memo:
                return memo[(first, second, player_count)]

            # otherwise; calculate memo[(first, second, player_count)]
            half = (player_count + 1) // 2

            min_val, max_val = float('inf'), float('-inf')

            # current list of numbers; [1, ..., first, ..., second, ..., player_count]
            # explore every number prior to first including first; [1: first + 1]
            for i in range(1, first + 1):

                # for every fix i number, the lowest possible pair is first - (i - 1)
                # and the maximum is seond - i 
                # explore the second number in [first - (i - 1): seond - (i - 1)], use i - 1 as i starts with 1
                # the with total second - first possibilities
                for j in range(first - (i - 1), second - (i - 1)):
                    # pair i & j
                    summ = i + j

                    # pass; not valid
                    if first + second - player_count // 2 > summ or summ > half:
                        continue 
                    
                    # recur on i, j 
                    x, y = dfs(i, j, half)
                       
                    # update bounds; include current round (1) with x & y values
                    min_val = min(min_val, 1 + x)
                    max_val = max(max_val, 1 + y)

            memo[(first, second, player_count)] = (min_val, max_val)
                        
            return memo[(first, second, player_count)]

        # memo[(i, j, player_count)] := (min_round, max_round) to reach player i from left and player j from right (i.e., competes against each other) when the total number of players are player_count
        memo = dict()

        # run dfs (left_setp, right_step, player_count)
        return dfs(firstPlayer, n - (secondPlayer - 1), n)