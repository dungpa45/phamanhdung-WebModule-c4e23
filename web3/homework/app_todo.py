import mlab
from todo import Add_todo

mlab.connect()

todo = ["New todo","View all Todos","Mark a Todo COMPLETED ","Delete a Todo","Exit"]

for i in range(len(todo)):
    print(i+1,todo[i],sep='. ')

while True:
    chon=int(input("Enter your command ? "))
    if chon == 1:
        n = input("Name: ")
        d = input("Description: ")
        c = "No"
        add = Add_todo(name=n,description=d,completed=c)
        add.save()

    elif chon == 2:
        todo_list = Add_todo.objects()
        print("====================================")
        x=0
        for t in todo_list:
            x+=1 
            print(x," Name:",t.name)
            print("Description:",t.description)
            print("Completed: ",t.completed)
            print()

        print("====================================")

    elif chon == 3:
        chon_todo = int(input("Which one ? "))
        todo_list = Add_todo.objects()
        so = 0
        for i in todo_list:
            so+=1
            if chon_todo == so :
                i.completed = "Yes"
                i.save()
                print("Updated !!")
                
    elif chon == 4:
        chon_todo = int(input("Which one ? "))
        todo_list = Add_todo.objects()
        so = 0
        for i in todo_list:
            so += 1
            if chon_todo == so:
                i.delete()
                print("Deleted !!")

    elif chon == 5:
        print("Press Enter to continue ...")
        break
