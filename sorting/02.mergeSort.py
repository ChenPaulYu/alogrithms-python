import math

unsortlist = [5,2,4,6,1,3,2,6]



def MergeSort(List,start,end):
	if start < end:
		mid = math.floor((start+end)/2)
		# print(start,mid,mid+1,end)
		MergeSort(List,start,mid)
		MergeSort(List,mid+1,end)
		List = Merge(List,start,mid,end)
	# else:
	# 	print('No')
	return List

def Merge(List,start,mid,end):
	Left =  [i for  i in List[start:mid+1]]
	Left.append(10000000)
	Right = [i for  i in List[mid+1:end+1]]
	Right.append(10000000)
	# print(Left,Right)
	L_index = 0
	R_index = 0 
	List_index = 0
	for i in List[start:end+1]:
		# print(start+List_index,L_index,R_index,List)
		if(Left[L_index]<Right[R_index]):
			List[start+List_index] = Left[L_index]
			L_index = L_index + 1
		else:
			List[start+List_index] = Right[R_index]
			R_index = R_index + 1
		List_index = List_index + 1
	# print("Merge",start,end,mid,List)
	return List 

def main():
	List = MergeSort(unsortlist,0,7)
	print(List)

if __name__ == "__main__":
    main()
