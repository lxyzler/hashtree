list=[[1,2,4],[1,2,9],[1,3,5],[1,3,9],[1,4,7],[1,5,8],[1,6,7],[1,7,9],[1,8,9],
    [2,3,5],[2,4,7],[2,5,6],[2,5,7],[2,5,8],[2,6,7],[2,6,8],[2,6,9],[2,7,8],
    [3,4,5],[3,4,7],[3,5,7],[3,5,8],[3,6,8],[3,7,9],[3,8,9],
    [4,5,7],[4,5,8],[4,6,7],[4,6,9],[4,7,8],
    [5,6,7],[5,7,9],[5,8,9],[6,7,8],[6,7,9]]
result=[]
def conf(list2d,k):
    list=[]
    list1=[]
    list2=[]
    list3=[]
    if len(list2d)>3:
        for i in range(len(list2d)):
                if list2d[i][k]%3==1:
                    list1.append(list2d[i])
                elif list2d[i][k]%3==2:
                    list2.append(list2d[i])
                else:
                    list3.append(list2d[i])
        list.append(list1) 
        list.append(list2)
        list.append(list3)
    return list
list1=conf(list,0)
i=0
j=0
for i in range(3):
    result1=[]
    list2=[]
    if len(list1[i])>3:
        list2=conf(list1[i],1)
       # print("h",list2)
        for j in range(3):
            list3=[]
            if len(list2[j])>3:
                list3=conf(list2[j],2)
               # print(list3)
                result1.append(list3)
            else:
               # print(list2[j])
                result1.append(list2[j])
    result.append(result1)
print(result)
#print(len(result[2]))
