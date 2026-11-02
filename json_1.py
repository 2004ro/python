import json
student_details=[{"roll":101,"name":"John","percent":89},
                 {"roll":102,"name":"Jill","percent":90},
                 {"roll":103,"name":"Jolly","percent":78}]
with open("student3.json","wt") as fh:
    json.dump(student_details,fh,indent=4)


#From the file ,print the names of the students who scored>80
# with open("student3.json","rt") as fh:
#     data=json.load(fh)
# #print(data)

# li=[]
# for i in data:
#     if i["percent"]>80:
#         li.append(i["name"])
# print("Student scored more than 80 % : ",li)

