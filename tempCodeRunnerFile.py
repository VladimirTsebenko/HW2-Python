
number = int(input("Enter Fibonacci length: "))
print ("Fibonacci number of: ", number, "is; ", round(((5**(0.5)+1)/2)**number/(5**(0.5))))

p = range(number+1)

fibonacci = []

for i in p:
    
    if(i == 0):
        n = 0
        fibonacci.append(n)
    elif(i == 1):
        n = 1
        fibonacci.append(n)
    elif(i > 1):
        n = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(n)

print("Fibonacci sequence is: ", fibonacci)