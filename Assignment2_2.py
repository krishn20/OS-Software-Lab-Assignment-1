def duplicate(list1):
  list2=[]
  c=0
  for i in list1:
    if list1.count(i) > 1:
      c = i
      if c not in list2:
        list2.append(c)
      
  print(list2)
  
list1 = [1,1,1,2,2,3]
duplicate(list1)
