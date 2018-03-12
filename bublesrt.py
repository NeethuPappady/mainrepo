def insertion():
 for i in range(len(list)):
      for j in range(len(list)):
             if list[i] < list[j]:
                   t=0
                   t=list[i]
                   list[i]=list[j]
                   list[j]=t
def bubblesort(list):
 for i in range(len(list)):
  for j in range(len(list)-1):
   if list[j]>list[j+1]:
    t=0
    t=list[j]
    list[j]=list[j+1]
    list[j+1]=t
def selection(list):
 for i in range(len(list)):
   for j in range(i):
    if list[j] >= list[j+1]:
     t=0
     t=list[j]
     list[j]=list[j+1]
     list[j+1]=t
list=[20,16,7,76,42]
bubblesort(list)
print(list)
list=[20,16,7,76,42]
insertion()
print(list)
list=[20,16,7,76,42]
selection(list)
print(list)
