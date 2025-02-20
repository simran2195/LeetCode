class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)  # Convert binary string to decimal integer
        steps = 0  # Counter for steps

        while n > 1:
            if n % 2 == 0:  # Even case
                n //= 2
            else:  # Odd case
                n += 1
            steps += 1  # Count each operation

        return steps
