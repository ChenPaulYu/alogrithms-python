import math
unsortlist = [4,2,5,3,0,2,3,0,3]


def countingSort(List):
	size = max(List)+1
	countingList = [ List.count(i) for i in range(0,size)]
	newList = [0 for i in range(0,len(List))]
	for i in range(0,size):
		if i>0:
			countingList[i] = countingList[i-1]+countingList[i]

	for i in range(0,len(List)):
		temp = List[len(List)-i-1]
		# print(temp,countingList[temp],countingList)
		newList[countingList[temp]-1] = temp 
		countingList[temp] = countingList[temp] - 1 
	return newList
	



def main():
	List = countingSort(unsortlist)
	print(List)
if __name__ == "__main__":
    main()