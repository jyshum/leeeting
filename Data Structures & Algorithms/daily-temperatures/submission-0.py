class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                          # day numbers still waiting
        days = [0] * len(temperatures)      # answers, start at 0

        for i, temp in enumerate(temperatures):   # i = today's day number, temp = today's temperature
            while stack and temperatures[stack[-1]] < temp:
                # while there are waiting days and today is warmer than the most recent one,
                # that day has found its warmer day, so pop it and record how long it waited
                j = stack.pop()             # a waiting day that just got its answer
                days[j] = i - j             # how many days it waited
            stack.append(i)                 # today is waiting now

        return days

            