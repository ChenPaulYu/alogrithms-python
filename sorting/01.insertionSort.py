unsortlist = [8,6,6,9,7,5,2,2,3,4,5,6,]

def insertionSort(unsortlist):
	sortNumber = 1
	for i in unsortlist[1:]:
		key = i
		index = sortNumber
		# print(unsortlist,key,index)
		for x in unsortlist[0:index]:
			# print(key,x)
			if(key<x):
				del unsortlist[index]
				unsortlist.insert(unsortlist.index(x),key)
				# print('insert',unsortlist)
				break
		sortNumber = sortNumber + 1
	return unsortlist


def main():
    list = insertionSort(unsortlist)
    print(list)

if __name__ == "__main__":
    main()

