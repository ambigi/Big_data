import numpy as np
from collections import defaultdict
def Question_1():
    arr=np.array([1,2,3,6,4,5])
    arr=arr[::-1]
    print(arr)
def Question_2():
    arr1=np.array([[1,2],[3,4]])
    arr2=np.array([[1,2],[3,4]])
    print(np.array_equal(arr1,arr2))


def Question_3():

    def frequency(arr):
        freq = defaultdict(list)
        for i in range(0,arr.size):
            if arr[i] not in freq:
                freq[arr[i]]=[1,i]
            else:
                freq[arr[i]][0]+=1
                freq[arr[i]].append(i)
        max=0;index=[];number =0
        for i in freq:
            if(freq[i][0]>max):
                max=freq[i][0]
                number =i
                index=freq[i][1:]
        print("max value: ",number," indexes: ",index)

    x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
    y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
    frequency(x)
    frequency(y)
def Question_4():
    gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
    print("sum is: ",np.sum(gfg))
    print("row wise sum is: ",np.sum(gfg, 1))
    print("column wise sum is: ",np.sum(gfg, 0))

#call the function corresponding to the Question
Question_4()



