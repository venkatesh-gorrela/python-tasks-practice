#task-15..only_____ even__places__reverse____ for while list reverse.....
book = " my name is venky hardik "
a = book.split()
n=[]
      
for i in a:
        if i == "name":
            i="name"[::-1]
            n.append(i)
        elif i =="venky":
              i="venky"[::-1]
              n.append(i)
        else:
              n.append(i)
              a=" ".join(n)
              
         
 
print(a)















