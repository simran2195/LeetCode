class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # count_s, count_t = Counter(s), Counter(t)

        # for c in count_t:
        #     if c not in count_s:
        #         return c
        #     if count_s[c] < count_t[c]:
        #         return c

        # approach 2
        sum_s, sum_t = 0, 0

        for c in s:
            sum_s += ord(c)

        for c in t:
            sum_t += ord(c)

        return chr(sum_t - sum_s)


        