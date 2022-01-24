import tkinter as t
import tkinter.messagebox as m
import heritage as b

root= t.Tk()
root.configure(bg="red")
root.title ("Login Screen")
root.geometry("400x400")


def signin():
    usr= t1.get()
    pswd = t2.get()
    print("values are",usr,pswd)
    if usr=="dpsg" and pswd== "abc":
       
        
        b.newscreen()
    else:
        m.showinfo("Sorry !!" ," Sorry dear, you can try one more time ")
        
l1 = t.Label(root, width = 20,text="Enter User ID", fg ="Blue")
t1 = t.Entry(root, width=30)

l2 = t.Label(root, width = 20,text="Enter Password", fg ="Blue")
t2 = t.Entry(root, width=30,show='*')

b1= t.Button(root, text="Sign in", command= signin)

l1.grid(row= 0, column = 0, padx=10, pady=10)
t1.grid(row= 0, column = 1, pady=10,columnspan =5)
l2.grid(row= 1, column = 0,padx=10, pady=10)
t2.grid(row= 1, column = 1, pady=10)
b1.grid(row= 4, column = 0)



root.mainloop()
