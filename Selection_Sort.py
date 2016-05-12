def selection_sort(A,n):
	for i in range(0,n-1):
		k=i
		for j in range(i+1,n):
			if(A[j]<A[k]):
				k=j
		if(k!=i):
			t=A[i]
			A[i]=A[k]
			A[k]=t

aList=[8,2,5,3,4,9]
n=6
selection_sort(aList,n)
print(aList)