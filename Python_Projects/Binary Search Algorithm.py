def binary_search(list,element):
    start = 0
    middle = 0
    steps = 0
    end = len(list)
    
    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1]))
        
        steps+=1
        middle = (start+end) //2
    
        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle-1
        else:
            start = middle+1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12
binary_search(my_list,target)