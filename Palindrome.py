def isPalindrome(string):
	reversedString = ''
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString

# def isPalindrome(string):
# 	return string == string[::-1]

#    def isPalindrome(string):
#     reversedChars-[]
# 	for i in reversed(range(len(string))):
# 		reversedChars.append(string[i])
# 	return string ==''.join(reversedChars)
