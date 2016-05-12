# C edition, see Insertion_Sort.c
def insertion_sort(A,n):
	for j in range(1,n):
		t=j-1
		key=A[j]
		while (t>=0 and A[t]>key):
			A[t+1]=A[t]
			t=t-1
		A[t+1]=key

aList=[8,2,5,3,4,9]
n=6
insertion_sort(aList,n)
print(aList)