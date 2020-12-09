# 1189. Maximum Number of Balloons
# Easy

# 332

# 37

# Add to List

# Share
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 10^4
# text consists of lower case English letters only.



def maxNumberOfBalloons(text):
        return min(min(text.count(x) for x in "ban"),text.count("l")//2, text.count("o")//2)

print(maxNumberOfBalloons("nlaebolkonlaebolk"))


# def maxNumberOfBalloons(self, text: str) -> int:
#     h=dict({'b':0,'a':0,'l':0,'o':0,'n':0})
#     for i in text: 
#         if i in ['b','a','l','o','n']:
#             h[i]+=1
#     h['o']//=2
#     h['l']//=2
#     return min(h.values())