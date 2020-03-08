def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]: 
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_backtrack(seq, x, k,s,count):
		
		if k>=len(seq): 
			x.append(count)
			return
		

		if(k==0 or count==0):
			LIS_backtrack(seq, x, k+1,s+1,count)
			count=count+1
			LIS_backtrack(seq, x, k+1,s,count)
			
		
		#LIS_backtrack(seq, x, k+1,s+1,count)
		
		if(seq[s]<seq[k]):
			LIS_backtrack(seq, x, k+1,k,count+1)
		LIS_backtrack(seq, x, k+1,s,count)
		#LIS_backtrack(seq, x, k+1,s,count)
			
seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis = 0
x = [] 
LIS_backtrack(seq, x, 0,0,0)
print(max(x))