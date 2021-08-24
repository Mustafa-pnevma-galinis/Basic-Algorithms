#بسم اللّه و الصلاة و السلام على جميع الأنبياء و المرسلين و آل بيوتهم الطاهرين المقربين و على من تبعهم بإحسانٍ إلى يوم الدين
# ◙◙ (α) Merge Sort Algorithm
count = 0

lst = [4,6,8,1,3,2,5,7]
sectorA = lst[0:4]
sectorB = lst[4:8]

# ◘◘@Note: to allocate the size of the array before initialisation.
#sortedArray = [][:5]
sortedArray = []
count = 0


# ◘◘@Note: to print the entire array elements without for loop.
'''print(*sectorA,sep ="\n")
print('\n'.join(map(str, sectorA)))'''



'''for i in range(1):
    if (sectorA[-1] < sectorA[0] and sectorA[-1] < sectorA[1] and sectorA[-1] < sectorA[2]):
        sortedArray.append(sectorA[-1])
    if(sectorA[0] < sectorA[1] and sectorA[0] < sectorA[2] ):
        sortedArray.append(sectorA[0])
    if(sectorA[1] < sectorA[2]):
        sortedArray.append(sectorA[1])
    sortedArray.append(sectorA[2])
'''

'''for i in sectorA:
    if(sectorA[-1] < i):
        sortedArray.append(sectorA[-1])
    if(sectorA[0] < i):
        sortedArray.append(sectorA[0])
    if (sectorA[1] < i):
        sortedArray.append(sectorA[1])
        sortedArray.append(sectorA[2])
'''


# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# ◙◙                            {Select Sorting Algorithms}
#───────────────────────────────────────────────────────────────────────────────────
#◘◘@Note: to sort a list we need firstly to set the minimum number {declare a new variable} as the first index on the list; either it is the minimum or not, 
#         then compare that number with the rest numbers on the list, after getting the {real minimum number}, set it to be the first index on the list.

unsortedLst = [7,11,8,1,4,2,3,9,12,10]
for i in range(len(unsortedLst)):
      
    # Find the minimum element in remaining 
    # unsorted array

    min_number = i

    for j in range(i+1, len(unsortedLst)):


        if unsortedLst[min_number] > unsortedLst[j]:


            min_number = j


    # Swap the found minimum element with 
    # the first element 
           
    unsortedLst[i], unsortedLst[min_number] = unsortedLst[min_number], unsortedLst[i]

'''print(unsortedLst)'''
	
# ◘◘Select Sorting Algorithm illustration;
'''
    ◘ for i in range (11):
        min_number = 0
        
        for j in range(1,11):
            if (unsortedLst[0] > unsortedLst[1]):
                min_number = 1
        
        ▬# Then Swapping indices, The min_number will get in-place
            of the higher_number; That process will continuosly occured till
            the array got arranged.
'''

# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

# ◙◙                            {Bubble Sorting Algorithms}
#───────────────────────────────────────────────────────────────────────────────────
def bubbleSort(array):
    n = len(array)

    for i in range(n-1): # ◘◘ {n-1} because the last element has the index No. [(len(array)-1)]. 
        for j in range(0,n-i-1):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array
    '''
    # ◘◘Illustration: ▬ On first iteration
            for i in range(7):
                for j in range(0,6): # On first iteration i = 0
                    if (array[1] > array[2]): # ▬ if True >  then swap the indices values.
                        array[1], array[2] = array[2],array[1]
    '''
'''print(bubbleSort([1,3,4,5,8,6,7,2]))'''

# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


# ◙◙                            {Insertion Sorting Algorithms}
#───────────────────────────────────────────────────────────────────────────────────

L = [4,5,8,9,2,1,3,7,6]
for i in range(1,len(L)):
    k = L[i]
    j = i - 1
    while (j >= 0 and L[j] > k):
        L[j+1] = L[j]
        j = j - 1
    L[j+1] = k

'''Algorithm Analysis'''
'''k = L[0]
j = 0'''
# if {Ture} then looping 
'''while (1 >= 0 and 4 > 5):
    L[2] = L[1]
    j = 0 '''
# if False then keep it in its index.
'''L[j+1] = k ◘◘ As {j+1 = 1}
'''

# ◘ get the integer value of division. » use (//) ▬ for example: {//2}. 
'''print(len(L) //2)'''


# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬


# ◙◙                            {Merge Sort Algorithm}
#───────────────────────────────────────────────────────────────────────────────────
# ◘ To define this Algorithm we need to pass through some steps:
#    ○ α) Divide the main array by its length for sub-arrays.
#    ○ ß) Sorting elements.
#    ○ Γ) Merging elements in sub-arrays; finally merge sub-arrays to the final form of array. 
def mergeSort(array):
    if (len(array) > 1):
        mid_length = len(array) //2 # ◘ Get the integer number of the length.
        
        # ◙ Dividing the main array to (2) sectors {Right -- Left}..
        L = array[:mid_length]

        R = array[mid_length:]

        # Then Sorting The Right and Left sector Separately.

        # ◘◘ The Passed array will be divided till reaching out one element of each array to be compared with.
        mergeSort(L)

        mergeSort(R)

        i = j = k = 0
        

        # ◘ Loop till the reaching the length of both arrays and copying the main array elements
            # on both sub-arrays.

            # »» On this step: Dividing the main array to {2 arrays}; while one of these arrays
            #    will contain the smaller valued elements and the other will contain the higher valued elements.
          
        while i < len(L) and j < len(R):
            # ○ Comparing with first elements in both arrays.

               # » If the left side element is smaller than the right side element.
            if (L[i] < R[j]):

                # ◘ Replacing the first element in the main arrays with the smaller number.
                array[k] = L[i]
                i += 1
            
                # » If the Right side element is smaller than the left side element.
            else:
                array[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        return array


'''print(mergeSort([5,6,1,3,2,7,9,8,4]))'''






#────────────────────────────────────important──────────────────────────────────────
# α)
# ▬▬ Check if a String contains an integer number:
'''x = "asdfas5654asd"

for i in range(len(x)):
    try:
        if (isinstance(int(x[i]), int)):
            print("Integer")
    except ValueError:
        print("Not Integer")
'''


# ß)
# ▬▬ Inverting string value.
# ◘ Method_1
'''print(string[::-1])'''

# ◘ Method_2
'''x = ""
count = len(string) -1
for i in string:
    x += string[count]
    count -= 1'''



# Γ)
# ▬▬ getting the absolute number from float value.
'''if int(n) < n:
    print(int(n) + 1)
else:
    print(n)'''



# Σ)
# ▬▬  using enumerate function; Note that {enumerate} will print a type (list) in a form of dictionary {key and values}.
'''lst = ["GTX 1650","GTX 980","GTX 970","RTX 2070"]
for i,j in enumerate(lst):
    print(i,j)
'''


'''    
0 GTX 1650
1 GTX 980
2 GTX 970
3 RTX 2070
'''



# σ)
# ▬▬ using {.round()} function that is mainly used to get the nearest decimals according to the past argument.
''' ◘ Note: that while the the parameter passed to this argument is <-number> » That will return the nearest 100 number.
# ╚ For example: x = 5555.456156187          └ print(round(x,-2)) ▬ returns 5600'''

x = -10
y = 5
#print(min(abs(y),abs(x)))



# µ)
# ▬▬ remove an item from a list and add it to an appended new list.
'''
def remove_item(x):
    if x == 30:
        lst_1.reverse()
        lst.append(lst_1)
        return False
    if x > 30:
        lst.remove(x)
        lst_1.append(x)
        remove_item(x - 1)
    return lst
'''



# τ)
# ▬▬ return a key for the specified value in dictionary.
'''def get_required_item(item_1,item_2,item_3):
    dictionary = {"GTX 1650":item_1,"RTX 2070":item_2,"RTX 3080":item_3}
    for key,value in dictionary.items():
        if value:
            return key'''
#───────────────────────────────────────────────────────────────────────────────────

# Check your answer
#q6.check()
#print(exactly_one_topping(False,True,False))

'''
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
lst = [x for x in l if x > 4]
print(lst)'''

         
dic = {"GTX 1650":2900,"GTX 2060":5700,"RTX 3080":2900}
x = 2900





#print(remove_item(40))



#print(lst)






'''
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    lst = []
    topping_dictionary = {"Ketchup":ketchup,"Mustard":mustard,"Onion":onion}
    for key, value in topping_dictionary.items():
        if value == True:
            lst.append(key)
    return lst
print(exactly_one_topping(True,True,False))
'''



def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) > 2:
        return L[1]
    else:
        return None



