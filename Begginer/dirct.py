import os

# print("Current Working Dir: ",os.getcwd())
# print(os.listdir())
os.chdir("data")
print("Current Working Dir: ",os.getcwd())
# print(os.listdir())
# os.mkdir('test')
# print(os.listdir())

# os.rename('test','new_one')
# print(os.listdir())

os.rmdir('new_one')
print(os.listdir())
