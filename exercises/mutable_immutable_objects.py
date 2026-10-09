#Topic: Passing objects to functions

def change_values(number, number_list):
    number += 10
    #IMMUTABLE OBJECT 'integer'
    # Intergers are immutable
    #This create a new interger value and reassigns the local varibale 'number'.
    #It does NOT change the original variable outside the function.

    number_list[0] += 2
    #MUTABLE OBJECT 'list'
    # lists are mutable.
    # This changes the first element of the original list because number_list refers to the same list object

# Original variables
x = 5
y= [2,3,5]

print('Before function call')
print('x :', x , '|',  'y :', y)

#pass varibales to the function
change_values(x, y)

print('After function call')
print('x :', x , '|', 'y :', y)

y = [2,3,5]

#what happens if we make a copy of list y?
change_values(x,y[:])

print("Function call after making a copy of y")
print('x :', x , '|', 'y :', y)




#how to actually make changes to x?

#Method 1 : Use return (recommended)

def change_values_with_return(num):
    num += 1
    return num

i = 5

print('value of i before function call')
print('i:', i)

i = change_values_with_return(i)       #very important assign the returned value

print('value of i after function call')
print('i:', i)



#Method 2 : Use a mutable container -- eg: list!   but we already implemented it.

#Method 3 : use OOP

class Number:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 10

j = Number(7)

print("Before:", j.value)

j.increase()

print("After:", j.value)
