# identity operators exercise 
a = [1,2,3]
b = a 
result = b is a # is identity operator 
print ("result of",b, "is:",a, "is:",result)

c = [1,2,3]
d = [1,2,3]
result = d is  c # is identity operator 
print ("result of",d, "is:",c, "is:",result)

a = [1,2,3]
b = [1,2,3]
result = b is not  a # is identity operator 
print ("result of",b, "is not :",a, "is:",result)

c = [1,2,3]
d = [1,2,3]
Result = d is  c # is identity operator 
print ("result of",d, "is not :",c, "is:",Result)
