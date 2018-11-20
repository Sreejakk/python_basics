student = {"name":"kiran","college":"sarada","hno":503,"phno":23456,"area":"kachiguda","city":"chennai","state":"tn","country":"india"}

# print(student['name'])

for s in student:
#    print(s)
    print("key: {} value: {}".format(s,student[s]))

#values
for v in student.values():
    print(v)
#keys
for v in student.keys():
    print(v)

#values and keys
for k,v in student.items():
    print(k,v)

student['name'] = 'mad'
print(student['name'])