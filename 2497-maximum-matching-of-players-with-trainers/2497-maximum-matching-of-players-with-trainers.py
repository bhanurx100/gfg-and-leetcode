class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n,m=len(players),len(trainers)        
        players.sort()
        trainers.sort()
        l,r=0,0
        while l<n and r<m:
            if players[l]<=trainers[r]:
                l+=1
            r+=1
        return l