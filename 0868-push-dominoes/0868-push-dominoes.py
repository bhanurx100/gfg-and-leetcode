class Solution(object):
    def pushDominoes(self,dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # Left to right
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # start with strong force
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Final result
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)
        