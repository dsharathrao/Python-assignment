list1=[1,2,3,4,5]
list2=[6,7,8,9]
list3=[10,11,12,13,14,15,16]
list1.sort()
list1=list1[::-1]
list2.sort()
list2=list2[::-1]
list3.sort()
list3=list3[::-1]
Maxlist=list1[0:2] + list2[0:2] + list3[0:2]
print "Maxlist is ",Maxlist
total=average=0
for i in Maxlist:
  total+=i
average=total/len(Maxlist)
print "average of the Maxlist is ",average

Minlist=[list1[-1],list1[-2],list2[-1],list2[-2],list3[-1],list3[-2]]
print "Minlist is ",Minlist
total=average=0
for i in Minlist:
  total+=i
average=total/len(Maxlist)
print "average of the Minlist is ",average

