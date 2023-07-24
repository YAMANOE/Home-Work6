list1=[1,'2',3.5,4.4,5,6,7.3,'8',9,'10']
changeToint=0
newList=[]
for i in list1:
    if type(i)==str:
        changeToint=int(i)
        newList.append(changeToint)
    else:
        newList.append(i)
print(newList)
avaregeOflist=sum(newList)/len(newList)
print(avaregeOflist)
print('the max value in list : ',max(newList),"\n",'the min value in list : ',min(newList))
print("the index of max value : ",newList.index(max(newList)),"\n",
      "the indax of min value : ",newList.index(min(newList)))



