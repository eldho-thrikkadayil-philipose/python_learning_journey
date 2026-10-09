coeff = []

for i in range(4):
    c = float(input(f"Enter coefficient {i+1}: "))  #{i+1 shows the index of coefficient to user}
    coeff.append(c)

x = float(input("Enter the value for x: "))

def polynomial(x, coeff):
    result = 0  #Python needs result to be defined before we use 'result +='. zero is the additive identity, adding zero does not change a number
     
    result += coeff[0] * x ** 3
    result += coeff[1] * x ** 2
    result += coeff[2] * x 
    result += coeff[3] 

    return result

y = polynomial(x, coeff)

print('Coefficients: ', coeff)
print('f(x): ', y)

    