# 2534. Time Taken to Cross the Door
# https://leetcode.com/problems/time-taken-to-cross-the-door/submissions/1431389787/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        # n persons numbered 0 to n-1
        # can enter/exit once taking 1 second
        # arrival array -> non-decreasing, arrival time for ith person at door
        # state array -> state of ith person -> 0: enter, 1: exit

        # Return array -> answer : answer[i] = second at which person i crosses the door
        # Only one person can cross the door at each second.

        # Person arrival status answer
        #   0       0       0       0
        #   1       1       1       3
        #   2       1       0       1
        #   3       2       0       2
        #   4       4       1       4


         # Person arrival status answer
        #   0       0       1       0
        #   1       0       0       2
        #   2       0       1       1
     

        # Validation checks:
        # Same len of arrival and status
        # # 
    
        # if len(arrival) != len(state):
        #     return res

        # n = len(arrival)
        # answer = [-1] * n # to store the result array
        # curr_t = 0 # start from time 0
        # # maintain queues for entry and exit
        # entry_q, exit_q = deque(), deque()
        # prev_state = -1  # Track the direction used in the previous second (-1 = no usage, 0 = entry, 1 = exit)
        # i = 0  # Pointer to iterate over people based on arrival


        # while i < n or entry_q or exit_q:   
        #     # Add people arriving at the current time to their respective queues
        #     while i < n and arrival[i] <= curr_t:
        #         if state[i] == 0:
        #             entry_q.append(i)
        #         elif state[i] == 1:
        #             entry_q.append(i)
        #         i += 1

        #     # check who gets to use the door
        #     # If the door was not used in the previous second, then the person who wants to exit goes first.
        #     if prev_state == 1:
        #         if exit_q:
        #             answer[exit_q.popleft()] == curr_t
        #         elif entry_q:
        #             answer[entry_q.popleft()] == curr_t
        #             prev_state = 0

        #     else:
        #         if entry_q:
        #             answer[entry_q.popleft()] == curr_t
        #         elif exit_q:
        #             answer[exit_q.popleft()] == curr_t
        #             prev_state = 1
        #         else:
        #             prev_state = 1


        #     curr_t += 1  # Move to the next second

        # return answer

        enter_pool, exit_pool = deque(),deque()
        cur_time = 0
        prev_state = 1
        i = 0
        ans = [0 for _ in range(len(arrival))]
        while i < len(arrival) or enter_pool or exit_pool:
            while i < len(arrival) and arrival[i] <= cur_time:
                if state[i] == 0:
                    enter_pool.append(i)
                else:
                    exit_pool.append(i)
                i += 1
            if prev_state == 1:
                if exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                elif enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                    prev_state = 0
            else:
                if enter_pool:
                    ans[enter_pool.popleft()] = cur_time
                elif exit_pool:
                    ans[exit_pool.popleft()] = cur_time
                    prev_state = 1
                else:
                    prev_state = 1
            cur_time += 1
        return ans





            


            
