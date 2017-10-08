import math

unsortlist = [4,1,3,2,16,15,9,10,14,8,7]


def maxHeapify(List,index):
	Left  = index * 2 + 1 
	Right = index * 2 + 2
	Largest = index
	size = len(List)-1
	# print(Left,Right,index)
	if((Left<=size) and List[Left]>List[Largest]):
		Largest = Left
	if((Right<=size) and List[Right]>List[Largest]):
		Largest = Right
	# print(index,Largest,List[index],List[Largest])
	if(index != Largest):
		List[Largest],List[index] = List[index],List[Largest] 
		maxHeapify(List,Largest)
	# print(Largest,List)
	return List

def buildMaxHeap(List):
	size = len(List)-1
	index = math.ceil(size/2-1) 
	while(index>=0):
		maxHeapify(List,index)
		index = index - 1
	return List

def HeapSort(List):
	List = buildMaxHeap(List)
	newList = []
	for i in range(len(List)):
		size = len(List)-1
		List[0],List[size] = List[size],List[0]
		if (not newList):
			newList.append(List.pop())
		else :
			newList.insert(0,List.pop())
		maxHeapify(List,0)
	return newList

def main():
	List = HeapSort(unsortlist)
	print(List)




if __name__ == "__main__":
    main()