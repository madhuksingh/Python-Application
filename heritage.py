import tkinter as t
import tkinter.messagebox as m
from tkinter.ttk import *
from PIL import Image, ImageTk

rt= t.Tk()
d1={"Taj Mahal":["Located in Agra,Uttar Pradesh","Built between 1632 and 1653","Founded by Mughal Emperor Shah Jahan","It was built in the memory of his wife Mumtaz Mahal","For more information,kindly visit www.tajmahal.gov.in"],"Ajanta Caves":["Located in Aurangabad,Maharashtra","Built in 2nd century BC and 6th century BC","The caves were built in two phases, the first phase was built during the reign of Emperor Ashoka while the second was built during the reign of the Gupta dynasty","The Ajanta Caves depict richly decorated fresco paintings, reminiscent of the Silgiriya painting, sculptures of Sri Lanka and many more","For more information,kindly visit www.ancient.eu"],"Agra Fort":["Located in Agra,Uttar Pradesh","Built between 1565 and 1573","Built by the Mughals","The Agra Fort served as the main residence of the Emperors of the Mughal dynasty","For more information kindly,visit agra.nic.in"],"Humayun's Tomb":["Located in Mathura Road,Nizamuddin East,Delhi","Built in 1570","Built by Humayun's first wife,Bega Begum","It was built by Bega Begum in the memory of his deceasd husband, Humayun","For more information,kindly visit www.humayunstomb.com"],"Ellora Caves":["Located in Aurangabad,Maharashtra","These caves date from 600-1000 CE","The Hindu and Buddhist caves were built by the Rashtrakuta Dynasty while the Jain caves were built by the Yadav Dynasty","Ellora Caves served as lodgings to the travelling Buddhist and Jain monks besides being a site for the trade route. There are 17 Hindu caves, 12 Buddhist and five Jain caves with deities, carvings and even monasteries depicting the mythology of each religion."],"Konark Sun Temple":["Located in Puri district,Odisha","Built in 13th century","Built by King Narsingha Deva 1st of the Eastern Ganga Dynasty","The Konark Sun temple is dedicated to the Sun God or Surya.The temple is said to be an attribution to King Narsingha Deva 1st of the Eastern Ganga Dynasty"],"Fatehpur Sikri Fort":["Located in Agra,Uttar Pradesh","Built in 16th century","It was founded by the Mughal Emperor Akbar","Fatehpur Sikri was built by the Mughal Emperor Akbar during the 16th century, who had planned to make this city as the capital of the Mughal Empire"]}
#:["Located in Agra,Uttar Pradesh","Built between 1565 and 1573","Built by the Mughals","The Agra Fort served as the main residence of the Emperors of the Mughal dynasty","For more information kindly,visit agra.nic.in"],"Humayun's Tomb":["Located in Mathura Road,Nizamuddin East,Delhi","Built in 1570","Built by Humayun's first wife,Bega Begum","It was built by Bega Begum in the memory of his deceasd husband, Humayun","For more information,kindly visit www.humayunstomb.com"],"Ellora Caves":["Located in Aurangabad,Maharashtra","These caves date from 600-1000 CE","The Hindu and Buddhist caves were built by the Rashtrakuta Dynasty while the Jain caves were built by the Yadav Dynasty","Ellora Caves served as lodgings to the travelling Buddhist and Jain monks besides being a site for the trade route. There are 17 Hindu caves, 12 Buddhist and five Jain caves with deities, carvings and even monasteries depicting the mythology of each religion."],"Konark Sun Temple":["Located in Puri district,Odisha","Built in 13th century","Built by King Narsingha Deva 1st of the Eastern Ganga Dynasty","The Konark Sun temple is dedicated to the Sun God or Surya.The temple is said to be an attribution to King Narsingha Deva 1st of the Eastern Ganga Dynasty"],"Fatehpur Sikri Fort":["Located in Agra,Uttar Pradesh","Built in 16th century","It was founded by the Mughal Emperor Akbar","Fatehpur Sikri was built by the Mughal Emperor Akbar during the 16th century, who had planned to make this city as the capital of the Mughal Empire"]}
site = t.StringVar()
rt.geometry("1500x1500")
rt.configure(bg="ORANGE")
rt.title ("Tourist spot Details ")
rt.withdraw()
info = t.StringVar()
id = 1
iid = 0

tv = None


rt.photo = ImageTk.PhotoImage(Image.open("m.jpg"))

def display():
    
    s= site.get()
    im= s+".jpg"
    rt.photo=ImageTk.PhotoImage(Image.open(im))
    l4 = t.Label(rt,image=rt.photo)
    
    l4.place( x=550,y=5)
    msg=""
    s1= d1[s]
    
    for i in range (len(s1)):
        msg = msg + s1[i]+"\n"
    info.set(msg) 
    
    
   
def newscreen():
    rt.deiconify()
    
    
    
    
    style = Style()
    style.configure('my.TCombobox', arrowsize=3)
    style.configure('my.TCombobox.Vertical.TScrollbar', arrowsize=3)
            
    l1 = t.Label(rt, anchor='w', text="Welcome to XYZ Tourism",bg ="orange", fg ="Blue",font=("Courier",26,"bold"))
    l4 = t.Label(rt,image=rt.photo)
    l2 = t.Label(rt, width = 20,text="Choose Heritage site ", fg ="Blue")
    x=["Select","Taj Mahal","Ajanta Caves","Agra Fort"]
    c1 = Combobox(rt,textvariable= site,values=x)
                           
    l3 = t.Label(rt, textvariable= info, width = 20,text="", fg ="Blue",font=("Courier", 16,"bold"))
    b1= t.Button(rt, text="Show", command= display)
    l1 .place(height=50, width=500, x=10,y=50)
    l4.place( x=550,y=5)
    l2. place(x=50,y=150)
    
    c1. place(x=200,y=150)
    
    l3. place(height = 200 , width =1500,x=10,y=250)
    b1. place(x=100,y=600)   
    
    
  
    rt.mainloop()



