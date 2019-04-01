def hinh_vuong(n):
	print("Hinh vuong\n")
	for i in range(0, n):
		for j in range(0, n):
			print("*",end=' ')
		print(" ")
	print(" ")

def hinh_chu_nhat(a,b):
	print("Hinh chu nhat\n")
	for i in range(0, a):
		for j in range(0, b):
			print("*",end=' ')
		print(" ")
	print("\n")
def hinh_tam_giac(n):
	print("Hinh tam giac\n")
	for i in range(n):
		for spaces in range(n-i, 0 , -1):
			print(' ', end=" ")
		for start in range(0,i*2+1,1):
			print("*",end=" ")
		print("\n")
	print("\n")
def tam_giac_vuong(n):
	print("Tam giac vuong")
	for i in range(n):
		for j in range(n):
			if(j<=i):
				print("*",end=' ')
		print("\n")


