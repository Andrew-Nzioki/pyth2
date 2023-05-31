numbers=[1,2,3,4]
doubled=[]
for num in numbers:
    doubled.append(num*2)

doubled2=[n*2 for n in numbers if n%2==0]
#namedList=[do something ,for loop, if condition]
# print(doubled2)
# print(doubled)

friends=["Rolf'S","Sam","Samantha","Saurabh","Jen"]
starts_s=[]
for friend in friends:
    if friend.endswith("S") or friend.startswith("S"):
        starts_s.append(friend)
# print(starts_s)

starts_s_list_comprehension=[friend for friend in friends if friend.startswith("S")]
print(starts_s_list_comprehension)