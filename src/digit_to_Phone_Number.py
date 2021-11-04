
#
# Complete the 'getWordsFromPhoneNumber' function below.
#
# The function accepts STRING phoneNumber as parameter.
# The function is expected to return a STRING_ARRAY.
#


'''
Words From Phone Number

Given a seven-digit phone number, return all the character combinations that can be generated according to the following mapping:



Return the combinations in the lexicographical order.

Example

Input: “1234567”

Output: [

“adgjmp”,

“adgjmq”,

“adgjmr”,

“adgjms”,

“adgjnp”,

...

“cfilns”,

“cfilop”,

“cfiloq”,

“cfilor”,

“cfilos”]

First string “adgjmp” in the first line comes from the first characters mapped to digits 2,3,4,5,6 and 7 respectively. Since digit 1 maps to nothing, nothing is appended before 'a'. Similarly, the fifth string “adgjnp” generated from first characters of 2,3,4,5, second character of 6 and first character of 7. All combinations generated in such a way must be returned in the lexicographical order.

Notes

Input Parameters: The function has one parameter, a string of exactly seven digit characters.

Output: Return an array of the generated string combinations in the lexicographical order. If nothing can be generated, return an array with one string "-1".

Constraints:

Input string is 7 characters long; each character is a digit.
Digits 0 and 1 map to nothing. Other digits map to either three or four different characters each.

Custom Input

Input Format: One line containing the string phoneNumber.

Output Format: Each line represents one generated combination. If nothing can be generated, push only one element "-1" into the resultant array.
'''

digit_to_chars = {
    '1' : "",
    '2' : "abc",
    '3' : "def",
    '4' : "ghi",
    '5' : "jkl",
    '6' : "mno",
    '7' : "pqrs",
    '8' : "tuv",
    '9' : "wxyz",
    '0' : ""
}


def getWordsFromPhoneNumber(phoneNumber):
    results = []
    def helper(phone_number, i, slate):
        if i == len(phone_number):
            if len(slate) > 0:
                results.append("".join(slate))
        else:
            chars = digit_to_chars[phone_number[i]]
            if chars:
                for x in chars:
                    slate.append(x)
                    helper(phone_number, i + 1, slate)
                    slate.pop()
            else:
                helper(phone_number, i + 1, slate)
    helper(phoneNumber, 0, [])
    if results:
        return results
    else:
        return ["-1"]
