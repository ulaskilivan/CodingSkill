'''Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

def lengthOfLongestSubstring(s):
    counter=0
    tempList=[]
    counters=[]
    for letter in s:
        if letter not in tempList:
            counter+=1
            tempList.append(letter)
            counters.append(counter)
        else:
            tempList=[]
            counters.append(counter)
            counter=0
    return max(counters)
        
print(lengthOfLongestSubstring("erce"))