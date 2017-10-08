
unsortlist = [2,8,7,1,3,5,6,4,2]

def partition(List,start,end):
	print(start,end,List)
	compareBase = List[end]
	partitionIndex = start-1 # initial is -1
	for x in range(start,end):
		if(List[x]<compareBase):
			partitionIndex = partitionIndex + 1
			List[partitionIndex],List[x] = List[x],List[partitionIndex]

	del List[end]
	List.insert(partitionIndex+1,compareBase)
	
	return partitionIndex+1


def quickSort(List,start,end):
	if start<end:
		mid = partition(List,start,end)
		List = quickSort(List,start,mid-1)
		List = quickSort(List,mid+1,end)
	return List




def main():
	List = quickSort(unsortlist,0,len(unsortlist)-1)
	print(List)

if __name__ == "__main__":
    main()