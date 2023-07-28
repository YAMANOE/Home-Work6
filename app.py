# list1=[1,'a',3.5,4.4,5,6,7.3,'8',9,'10']
# changeToint=0
# newList=[]
# for i in list1:
#     if type(i)==str:
#         changeToint=int(i)
#         newList.append(changeToint)
#     else:
#         newList.append(i)
# print(newList)
# print("the sum of list : ",sum(newList))
# avaregeOflist=sum(newList)/len(newList)
# print("the avarege of list : ",avaregeOflist)
# print('the max value in list : ',max(newList),"\n",'the min value in list : ',min(newList))
# print("the index of max value : ",newList.index(max(newList)),"\n",
#       "the indax of min value : ",newList.index(min(newList)))
# for i in list1:
#      try:
#          changeToint+=int(i)
#      except ValueError:
#           print("rowng value")    
     
# print(newList)
# -------------------------------------------
# person={'name':'yaman',
#         'age':22,
#         'city':'irbid'
# }
# person['name']='saleem'
# person['job']='data centice'
# print(person)

# for i in person:
    # print(i,end=" : ")
    # print(person[i])
# -------------------------------
# clear : 
# person.clear() 
# print(person)
# ------------------------------   
# copy:
# newdec={}
# newdec=person.copy()
# print(newdec)
# ---------------------------------
# items:
# print(person.items())
# ------------------------------
# kyse
# print(person.keys())
# ------------------------------
# valus
# print(person.values())
# ------------------------------
# pop
# person.pop('job')
# -------------------------------
classRoom={
    "yaman":{
        'name':'yaman',
         'city':'irbid',
        'age':22,
         'bhone number':123456
        }  ,  
    'kaled':{
        'name':"kaled",
        'city':"amman",
        'age':33,
        'phone number':56677
    },
    'mohammad':{,
        'name':"mohmad",
        'city':'hartha',
        'age':33,
        "phone number":56789,
    },
    'noor':{,
        'name':"noor",
        'city':'salt',
        'age':38,
        "phone number":567119,
    },
    "adnan":{,
        'name':"adnan",
        'city':'hartha',
        'age':33,
        "phone number":56789,
    },
}
    
 
print(classRoom["yaman"])







    

    




