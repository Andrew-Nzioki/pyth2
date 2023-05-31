#dictionaries associate keys and values
friend_ages={"Rolf":24,"Adam":30,"Anne":27}

# print(friend_ages["Adam"])

friends=[
    {"name":"Rolf","Age":24},
    {"name":"Adam","Age":30},
    {"name":"Anne","Age":27}

]

# print(friends[2]["name"])
student_attendance={"Rolf":24,"Adam":30,"Anne":27}
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

#alternative for looping through dictionaries

for student in friends:
    for student,attendance in student.items():
        print(f"{student} : {attendance}")

for student,attendance in student_attendance.items():
    print(f"{student}: {attendance}")