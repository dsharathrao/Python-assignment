3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters.
   If yes return True else False.


Code :

def isSubSequence(str1,str2,m,n): 
	j = 0 
	i = 0  
	while j<m and i<n: 
		if str1[j] == str2[i]:	 
			j = j+1	
		i = i + 1
	return j==m 
str1 = "ee"
str2 = input("Enter a string")
m = len(str1) 
n = len(str2) 
print ("Yes" if isSubSequence(str1,str2,m,n) else "No")


