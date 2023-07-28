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
# person={"name":'yaman',
#         "age":22,
#         "city":'irbid'}
# print(person)
# person['name']='salem'
# print(person)
# person['job']='data sencine'
# print(person)
# --------------------------------
# list2=[1,2,3,4,5,6,7,'a','8',9,'10']
# sumation=0
# changetoint=0
# for i in list2:
#      try: 
#          sumation+=int(i)
#      except ValueError:
#           print('wrong value')
# print(sumation)

# -------------------------------
# dectrionary:collection of key value pairs 
# person={
#     "name":'yaman',
#     'age':22,
#     "city":'irbid',
# }
# print(person['name'])
# person['name']='sallem'
# print(person['name'])
# person["job"]='data engnaring'
# # print(person)
# person['skills']=['python','c++']
# person['parents']={
#     'father':'kaled',
#     'mather':'doaa'
# }
# print(person)
# for i in person:
#     print(i," : ",person[i])

#  -------------------------------
# method in dectonary
# clear : Clear all contents dectonary  
# person.clear()
# print(person)
# ----------------------------------
#  copy : copy one dectonary to anouther dectonary 
# decnew={}
# decnew=person.copy()
# print(decnew)
# -----------------------------------
# item : get all items in the dectonary 
# print(person.items())
# ----------------------------------
# key : get all key in the dectonary
# print(person.keys())
# ---------------------------------
# valurs :get all valus in the dectonary
# print(person.values())
# --------------------------------
# pop :remove for item inside the dec
# person.pop("job")
# print(person)
# ----------------------------------
# print(person["parents"]['father'])
# ----------------------------------
# popitem
# print(person)
# print()
# print()
# person.popitem()
# print(person)
# --------------------------------
# update
# person.update({'city':'amman'})
# print(person)
# -------------------------------
# skills=[]
# person={'name':' ',
#         'age':22,
#         'city':" ",
#         'skilles':skills}
# for i in person :
#     name=input("inter your name : ")
#     person.update({"name":name})
#     age=int(input('enter your age : '))
#     person.update({"age":age})
#     city=input("inter your city : ")
#     person.update({"city":city})
#     while True:
#          skills1=input('inter your skills : ')
#          skills.append(skills1)
#          print("do you need to contino yes or no : ")
#          a=input("inter your anrwr: ")
#          if a=="yes ":
#               continue
#          if a=="no":
#               break
         
#         # person.update({'skills':skills})    
# print(person )    

# -----------------------------
# person={}
# # i=0
# # m=1
# def addKeys():
#     i=0
#     m=1
#     print("What do you want to add to your dictionary")
#     while i<m:
#         y=input("enter the key : ") 
#         person[y]=" "
#         print("go you want to continue ? ")
#         k=input("inter your answer yes or no : ")
#         if k=="yes":
#             i+=1
#             m+=1
#             continue
#         elif k=="no":
#             break
# def addValue():
#     print("what the ansawr of ypur key ")
#     for i in person :
#         value=input("enter ypour value : ")
#         person[i]=value
#     print(person)    
# addKeys()   
# addValue()

classroom={
    'yaman':{
        'name':"yaman",
        'age':22,
        'city':"irbid",
        'phone number':233455,
    }
    'kaled':{

    }
}




















    

    




