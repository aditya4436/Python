list1=["Aditya", 11, "Kumar", 2, "Shah", 3]
print("The original list: ",list1)
key_list=["name", "number"]
n=len(list1)
res=[]
for i in range(0, n, 2):
    res.append({key_list[0]: list1[i], key_list[1]: list1[i+1]})

print(f"The constructed dictionary from the list: {res}")