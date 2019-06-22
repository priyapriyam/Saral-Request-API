import requests
import json
import os

saral_url = "http://saral.navgurukul.org/api/courses"

var = requests.get(saral_url)

#print(var.content)

with open("courses.json","w") as file:

    file.write(var.text)

resonse = var.json()

a = "shubhangi"
print 
if os.path.exists("./courses.json"):
    a = open("courses.json","r")
    b = a.read()
    #print (b)
else:
    with open("/.courses.json","w") as shubhangi:
       zeba.write(var.content)
    s = (var.json)
    #print (s)
    
i = 0
while i <len((resonse["availableCourses"])):
    course = resonse["availableCourses"][i]["name"]
    print i+1,course
    i = i + 1


new = []
i = 0
while i <len((resonse["availableCourses"])):
    new.append(resonse["availableCourses"][i]["id"])
    i = i + 1

#print new
user = int(raw_input("enter your id"))
var = new[user-1]
print var
var1 = saral_url+"/"+str(var)+"/exercises"
print var1
z = requests.get(var1)
#print(z.content)   

resonse1 = z.json()
i = 0
while i <len((resonse1["data"])):
    course1 = resonse1["data"][i]["name"]
    print i+1,course1
    i = i + 1


resonse2 = z.json()
new1 = []
i = 0
while i <len((resonse2["data"])):
    data1 = resonse2["data"][i]
    storedata = data1["childExercises"]
    new1.append(storedata)
    i = i + 1

#print new1

new_2 = []
new_3 = []
user_1 = int(raw_input("enter your number"))
course_4 = new1[user_1-1]
j=0
while j <len(course_4):
    course3 = course_4[j]["name"]
    print course3
    course5 = course_4[j]["id"]
    var_3 = course_4[j]["slug"]
    new_2.append (course5)
    new_3.append (var_3)
    j=j+1
#print new_2
#print new_3

user_2 = int(raw_input("enter your slug"))
ID = new_2[user_2]
SLUG = new_3[user_2]

saral_1 = "http://saral3.navgurukul.org/api/courses/"+str(ID)+"/exercise/getBySlug?slug="+str(SLUG)
var_6 = requests.get(saral_1)
print(var_6.text)