def Add(a,b):
	return a+b
def Sub(a,b):
	return a-b
def Mul(a,b):
	return a*b
def Div(a,b):
	return a/b
print ("Tong la:", Add(5, 5))
print ("Hieu la:", Sub(12, 7))
print ("Tich la:", Mul(5, -3))
print ("Thuong la:", Div(24,6))

print()
a = [1,3,5,6,7,1,-3]
print("Mang ban dau: ")
print(a)
def sort_1(a):
	for i in range(0,len(a)):
		for j in range(0 , i +1 ):
			if a[i] < a[j]:
				temp = a[i]
				a[i] = a[j]
				a[j] = temp
a = [1,3,5,6,7,1,-3]
sort_1(a)
print("Mang tang dan: ")
print(a)
print()
print("Mang ban dau: ")
a = [[1,3,0] ,[ 6,7,1]]
print(a)
def sort_2(a):
	row = len(a)
	col = len(a[0])
	#print("row = %d\ncol=%d" %(row , col))
	for i in range(0,row):
		sort_1(a[i])
a = [[1,3,0] ,[ 6,7,1]]
sort_2(a)
print("Mang tang dan: ")
print(a)


