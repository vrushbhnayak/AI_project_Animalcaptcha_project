from tkinter import *
from PIL import ImageTk,Image
#from typing import Counter, no_type_check_decorator
import random

from tkinter import messagebox
root = Tk()
root.geometry("700x700")



image_list ={

    "cat" : [
              
             'images\\1.jpg',
             'images\\8.jpg',
             'images\\7.jpg',
             'images\\6.jpg',
             'images\\9.jpg',
             'images\\3.jpg',
             'images\\4.jpg',
             'images\\5.jpg',
             'images\\2.jpg'
    ],
    "dog" : [
              
             'images\\1.jpg',
             'images\\8.jpg',
             'images\\10.jpg',
             'images\\11.jpg',
             'images\\9.jpg',
             'images\\3.jpg',
             'images\\4.jpg',
             'images\\12.jpg',
             'images\\2.jpg'
    ],

    "tiger":[
             
             'images\\1.jpg',
             'images\\8.jpg',
             'images\\14.jpg',
             'images\\15.jpg',
             'images\\9.jpg',
             'images\\3.jpg',
             'images\\4.jpg',
             'images\\16.jpg',
             'images\\2.jpg'

    ]
 }
right_image_list={

    "cat":    ['images\\5.jpg',
              'images\\6.jpg',
              'images\\7.jpg'],


    "dog":    ['images\\10.jpg',
              'images\\11.jpg',
              'images\\12.jpg' ],

     "tiger": ['images\\14.jpg',
              'images\\15.jpg',
              'images\\16.jpg' ]

}

dictkey = list(image_list.keys())
print(dictkey)
randomkey = random.choices(dictkey)[0]
print(randomkey)
display_image = image_list[randomkey]
print(display_image)
right_image = set(right_image_list[randomkey])
print(right_image)


# image_list=[
#              'images\\1.jpg',
#              'images\\8.jpg',
#              'images\\7.jpg',
#              'images\\6.jpg',
#              'images\\9.jpg',
#              'images\\3.jpg',
#              'images\\4.jpg',
#              'images\\5.jpg',
#              'images\\2.jpg'
# ]

# right_image_list={
#               'images\\5.jpg',
#               'images\\6.jpg',
#               'images\\7.jpg'
# }

image_set=set()
count=0

def fun1(selectlable,imagename):
    global image_set
    global count
    image_set.remove(imagename)
    selectlable.config(borderwidth=0,command=lambda:fun2(selectlable,imagename))
    count=count-1
    
def check():
    global image_set
    global right_image
    global submit
    global count
   
    
    if(count<3  or count>3):
       print(count)
       messagebox.showinfo('WARNING','PLEASE SELECT THREE IMAGES') 
       return
    print("hiii")
    print(right_image)
    print(image_set)
        
    if (image_set==right_image):
        True
        messagebox.showinfo('SUCCESS','CAPTCHA IS  VERIFY')
        submit.config(state=DISABLED)
        root.destroy()
    else:
        False
        messagebox.showinfo('FAILED','CAPTCHA IS NOT VERIFY')
        submit.config(state=NORMAL)



def fun2(lb1,imagename):
    global l3
    global image_set
    global count
    print("Hello World")
    #l3.config(borderwidth=0,command=fun2)
    #l1.config(borderwidth=0,command=fun2)
    print(count)
    count=count+1
    if imagename not in image_set:
        image_set.add(imagename)
        print("images name",image_set)
    print("Hello World..")
    print(lb1)
    print(imagename)
    lb1.config(bg="yellow",fg="gray",borderwidth=10,relief=SUNKEN,command=lambda:fun1(lb1,imagename))
   # l2.config(bg="green",fg="gray",borderwidth=10,relief=SUNKEN,command=fun1)
    #l3.config(bg="green",fg="gray",borderwidth=10,relief=SUNKEN,command=fun1)
    
header_label = Label(root,text="CAPTCHA",borderwidth=15,font="Timesnewroman 27 bold",bg="red",pady=10,relief=SUNKEN)
header_label.pack(pady=10,fill=X)

#chkbox = Checkbutton(root,text="Check Me!")
#chkbox.pack()
def fun3():
    global imagename
    global submit
    global var
    global img1
    global l1
    global img2
    global l2
    global img3
    global l3
    global img4
    global l4
    global img5
    global l5
    global img6
    global l6
    global img7
    global l7
    global img8
    global l8
    global img9
    global l9
    global imageFrame
    global mylable
    #global imagename
    if(var.get()):
       global imageFrame
       global c
       c.config(state=DISABLED,foreground='blue')
       imageFrame = Frame(root,borderwidth=10,relief=SUNKEN)
       imageFrame.pack()

       img1 = ImageTk.PhotoImage(Image.open(display_image[0]).resize((100,100)))
       l1 =Button(imageFrame,image = img1,command=lambda:fun2(l1,display_image[0]))
       l1.grid(row=0,column=0)

       img2 = ImageTk.PhotoImage(Image.open(display_image[1]).resize((100,100)))
       l2 = Button(imageFrame,image = img2,command=lambda:fun2(l2,display_image[1]))
       l2.grid(row=0,column=1)

       global l3

       img3 = ImageTk.PhotoImage(Image.open(display_image[2]).resize((100,100)))
       l3 = Button(imageFrame,image = img3,command=lambda:fun2(l3,display_image[2]))
       l3.grid(row=0,column=2)

       img4 = ImageTk.PhotoImage(Image.open(display_image[3]).resize((100,100)))
       l4 = Button(imageFrame,image = img4,command=lambda:fun2(l4,display_image[3]))
       l4.grid(row=1,column=0)

       img5 = ImageTk.PhotoImage(Image.open(display_image[4]).resize((100,100)))
       l5 = Button(imageFrame,image = img5,command=lambda:fun2(l5,display_image[4]))
       l5.grid(row=1,column=1)

       img6 = ImageTk.PhotoImage(Image.open(display_image[5]).resize((100,100)))
       l6 = Button(imageFrame,image = img6,command=lambda:fun2(l6,display_image[5]))
       l6.grid(row=1,column=2)

       img7 = ImageTk.PhotoImage(Image.open(display_image[6]).resize((100,100)))
       l7 = Button(imageFrame,image = img7,command=lambda:fun2(l7,display_image[6]))
       l7.grid(row=2,column=0)
       
       img8 = ImageTk.PhotoImage(Image.open(display_image[7]).resize((100,100)))
       l8 = Button(imageFrame,image = img8,command=lambda:fun2(l8,display_image[7]))
       l8.grid(row=2,column=1)
       
       img9 = ImageTk.PhotoImage(Image.open(display_image[8]).resize((100,100)))
       l9 = Button(imageFrame,image = img9,command=lambda:fun2(l9,display_image[8]))
       l9.grid(row=2,column=2)
       
      
       submit=Button(root,text="Verify",height=1,width=5,font=" Timesnewroman 15 bold",bg="red",borderwidth=10,command=check,relief=SUNKEN)
       submit.pack(pady=10)
       mylable=Label(root,text="").pack()
       
    else:
        
        #for i in imageFrame.winfo_children():
        imageFrame.destroy()
        submit.destroy()
       




# def show():
#     myLable=Label(root,text=var.get()).pack()
# creating header
root.config(background="skyblue")
#Label(root,text="CAPTCHA ",borderwidth=20,font="Castellar 23 bold",bg="blue",pady=10,relief=SUNKEN).pack(pady=10,fill=X)
var = IntVar()
c =Checkbutton(root, text="I AM NOT ROBOT", borderwidth=20,relief=SUNKEN,font="Timesnewroman 15 bold",bg="red",pady=10, variable=var,command=fun3)


c.pack()
Label(root,text="SELECT THE ANIMAL IMAGE ",borderwidth=20,font="Timesnewroman 15 bold",bg="red",relief=SUNKEN).pack(pady=20,padx=20)
#mybutton=Button(root,text="button",command=show).pack()

#myLable= Label(root,text=var.get()).pack()

# image
print(c)
print(var.get())







root.mainloop()


