class MyClass:
	a = 10
	def func(self):
		print("hello")
obj = MyClass()
print(MyClass.a)
print(MyClass.func)
obj.func()