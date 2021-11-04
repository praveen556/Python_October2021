
# Complete the function below.
# The function accepts a STRING as parameter and is expected to return a STRING ARRAY.

# Complete the function below.
# The function accepts a STRING as parameter and is expected to return a STRING ARRAY.
def get_distinct_subsets(str):
    str = sorted(str)
    result = []

    def helper(slate, i):
        result.append(slate)
        if i == len(str):
            return

        unique = {}
        for k in range(i, len(str)):
            if str[k] not in unique:
                unique[str[k]] = 1
                helper(slate + str[k], k + 1)

    helper("", 0)
    return result

print(get_distinct_subsets("aab"))
