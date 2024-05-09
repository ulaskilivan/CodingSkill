'''Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.'''

def longestPalindrome(s):
    maxLen=0
    palindrome="No palindrome word!"
    firstIndex=0
    
    for i in range(0,len(s)-1):
        firstIndex=0
        for lastIndex in range(i+2,len(s)+1):
            tmpStr=s[firstIndex:lastIndex]
            if tmpStr==tmpStr[::-1]:
                palindrome=tmpStr
            firstIndex+=1
    return palindrome

print(longestPalindrome("abbcbbcc"))