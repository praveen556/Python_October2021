
#Attend Meetings
#Given a list of meeting intervals where each interval consists of a start and an end time, check if a person can attend all the given meetings such that only one meeting can be attended at a time.
#Example One
#Input = [[1, 5], [5, 8], [10, 15]]
#Output = 1
#As the above intervals are non-overlapping intervals, it means a person can attend all these meetings.
#Example Two
#Input = [[1, 5], [4, 8]]
#Output = 0
#Time 4 - 5 is overlapping in the first and second intervals.
#Notes
#A new meeting can start at the same time the previous one ended.
#Constraints:
#1 <= number of intervals <= 10^5
#0 <= start time < end time <= 10^9
#Custom Input
#Input Format:
#First-line has the number of rows that will be equal to the number of intervals.
#Second-line has the number of columns that will always be equal to 2.
#Each row will be printed in a new line containing 2 space-separated integers where the first integer is the start time and the second integer is the end time.
#Input for “Example One” above would look like:

#3
#2
#1 5
#5 8
#10 15

#Output Format:
#A single line containing 1 if it is possible to attend all the meetings, else 0.
#Output for “Example One” above would look like:

#1
'''
Complete the function below.
The function takes a 2D INTEGER ARRAY as input and is expected to return an INTEGER.
'''
def can_attend_all_meetings(intervals):
    sorted_list = sorted(intervals, key=lambda x: x[0])
    for i in range(len(sorted_list)-1):
        if sorted_list[i][1] > sorted_list[i+1][0]:
            return 0
    return 1
