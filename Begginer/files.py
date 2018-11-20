# f = open("data.txt",'r')
# print(f)
# f.close()

# try:
#     f = open('dada.tct')
#     print(f)
# finally:
#     print("err")
#     f.cose()

with open("C:/Users/skandikonda2/Desktop/Learning/python/Begginer/data/data.txt") as f:
    # print(f.read())
    # print(f.read(1))
    print(f.readlines())
