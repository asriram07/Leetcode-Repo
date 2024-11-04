"""
3163. String Compression III
Solved
Medium
Topics
Companies
Hint
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.

 

Example 1:

Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp."""

class Solution:
    def compressedString(self, word: str) -> str:
        finalString = ""
        curr = word[0]
        temp = 0
        i = 0
        n = len(word)
        while(i<n):
            curr = word[i]
            temp = 0
            while(temp<9 and i<n and word[i]==curr):
                temp+=1
                i+=1

            finalString+=(str(temp)+curr)
        return finalString