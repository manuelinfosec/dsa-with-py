"""
1876. Substrings of Size Three with Distinct Characters
Easy
Topics
Companies
Hint
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence 
should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
"""


def countGoodSubStrings(s: str):
    # Number of characters to use in the sliding window
    window = 3
    # Counter for "good" substrings found
    good_sub_string = 0

    # Iterate through the given string
    for idx in range(len(s)):
        # Sliding Window: Collect substring across the window
        substring = s[idx : idx + window]
        # Initialize a data structure for storing the frequency
        # of characters in the subset
        count_set = set()

        # Work with only three characters in the window
        if len(substring) < 3:
            break

        # Iterate through the substring
        for ichar in substring:
            # Check if the inner character is in the DS or..
            if ichar not in count_set:
                count_set.add(ichar)
            # If an occurence is found, this substring is not considered "good"
            else:
                # Of to collect the next substring from the window
                break
        # A "good" substring was found if no characters occurred more than once
        else:
            good_sub_string += 1

    # Return the number of "good" substrings found
    return good_sub_string


print(countGoodSubStrings("aababcabc"))
