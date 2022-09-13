'''
Problem:
Xsquare loves to play with strings a lot. Today, he has two strings S1 and S2 both consisting of lower case alphabets.
Xsquare listed all subsequences of string S1 on a paper and all subsequences of string S2 on a separate paper.
Xsquare wants to know whether there exists a string which is listed on both the papers.
Xsquare thinks that this task is pretty boring and handed it to you. Please accomplish this task on his behalf.

Input:
First line of input contains a single integer T denoting the number of test cases. Each test case consists of two lines.
First line of each test case contains a string denoting string S1. Next line of each test case contains a string denoting string S2.

Output:
For each test case, Print Yes if both papers contain a common string otherwise Print No.

'''


tc = int(input())
 
for z in range(tc):
  a = set(input())
  b = set(input())
  if not a&b:
    print('No')
  else:
    print('Yes')
