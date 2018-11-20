# import math

# print(math.factorial(3))
# print(math.fabs(-3.55))


file=open("text.txt","r")
file.write("hiii")
file.close()

try:
    with open("text.txt","a+") as ff:
        ff.write("1")
except:
    file=open("text.txt","w")
    file.write("hiii")
    file.close()
note=open("text.txt","r")
print(note.read())

with open("text.txt","a+") as file:
    file.write("\n1 dasgdjgas dgajgdja gdja")

with open("text.txt","r") as file:
    print(file.readlines(3))

for line in file:
    print(line)