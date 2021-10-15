# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        Left = 1
        Right = n

        while Left <= Right:

                Mid = Left + (Right -Left)//2
                print("Printing Mid",Mid)
                if isBadVersion(Mid) and not isBadVersion(Mid-1):
                    return Mid
                elif not isBadVersion(Mid):
                    Left = Mid + 1
                else:
                    Right = Mid-1
                    print("Printing Right in", Right)


def isBadVersion(version):
    if version >= 1702766719:
        return True
    else:
        return False

print(Solution.firstBadVersion(1,2126753390))
