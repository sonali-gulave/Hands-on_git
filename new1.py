def outer(num1):
	def inner_increment(num1):
		return num1+1
	num2 = inner_increment(num1)
	print(num1,num2)
        inner_increment(10)
if __name__=='__main__':
	outer(10)
	pass
