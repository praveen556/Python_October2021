'''

Generate All Combinations With Sum Equal to Target



Given an integer array, generate all the unique combinations of the array numbers that sum up to a given target value.



Example One:

Input: [1, 2, 3], 3

Output: [ [1, 2], [3] ]



Example Two:

Input: [1, 1, 1, 1], 2

Output: [ [1, 1] ]



Notes:

Each number in the array can be used exactly once.
All the returned combinations must be different. Two combinations are considered different if their sorted version is different.
The order of combinations and order of the numbers inside a combination does not matter.


Constraints:

1 <= Array Length <= 25.
1 <= Array Values <= 100.
1 <= Target Value <= 2500.


Custom Input:

Input Format:

The first line contains the size of the input array.
The next lines contain the array elements, one in each line.
The last line contains the target value.
Input for “Example One” above would be:

3

1

2

3

3



Output Format:

The output contains each combination in a separate line and the numbers inside a combination must be space-separated.
Output for “Example One” above would be:

1 2

3

'''





'''
    The function takes an INTEGER ARRAY and an INTEGER as inputs
    and is expected to return a 2D INTEGER ARRAY

    Complete the function below.
'''
def generate_all_combinations(arr, target):
    results = []
    arr.sort(reverse =True)
    def helper(i, target, slate):
        #Base Case when combination meets the target
        if target == 0:
            results.append(slate[:])
            return
        #If target is never achieved after reading entire array as well
        if target < 0 or i == len(arr) or sum(arr[i:])<target:
            return
        #Counting duplicates
        count = 0
        for x in range(i, len(arr)):
            if arr[x]!=arr[i]:
                break
            count += 1
        #Skipping all the Duplicates
        helper(i+count, target, slate) #Skipping this step as nothing to do

        #Go through each count
        for x in range(0, count):
            slate.append(arr[i])
            target -= int(arr[i])
            helper(i+count, target, slate) # important as you always want to push the index at end of duplicate
        #poppog all the dups from slate
        for x in range(0,count):
            slate.pop()
    helper(0, target, [])
    return results

print(generate_all_combinations([1,2,4,2,1,5],2))
