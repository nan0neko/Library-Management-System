from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def listbooks():
        li=ttk.Combobox(second_frame,value=libbook,width=10)
        li.pack()
def borrow():
        Label(second_frame,text="enter your name").pack()
        Entry(second_frame,text=yourname).pack()
        Label(second_frame,text="So, you want to borrow book!").pack()
        Label(second_frame,text="entery the book to borrow").pack()
        Entry(second_frame,text=bookname).pack()
        #return bookname.get()
        Button(second_frame,text="proceed",command=borrow1).pack()
       
        
   
def returnb ():
            Label(second_frame,text="So, you want to return book!").pack()
            Label(second_frame,text="enter your name").pack()
            Entry(second_frame,text=yourname).pack()
            Label(second_frame,text="entery the book to return").pack()
            Entry(second_frame,text=bookname).pack()
            if {yourname.get(): bookname.get()} in track:
             track.remove({yourname.get(): bookname.get()})
             #return self.book
            Button(second_frame,text="proceed",command=returnb1).pack()
            
            ''' messagebox.showinfo("","BOOK RETURNED : THANK YOU! \n")
             libbook.append(bookname.get())'''
       
def donate():       
              Label(second_frame,text="So, you want to donate book!").pack()
             
              Label(second_frame,text="entery the book to donate").pack()
              Entry(second_frame,text=bookname).pack()
              Button(second_frame,text="proceed",command=donate1).pack()
def track1():
               for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        Label(second_frame,text=f"{book} book is taken/issued by {holder}.").pack()
               
               if len(track) == 0:
                    messagebox.showinfo("","NO BOOKS ARE ISSUED!. \n")
        


              
   
  
def borrow1():
    if bookname.get() not in libbook:
            
            messagebox.showinfo("" ,   "\n"+str(bookname.get()) +" BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
    else:
            track.append({yourname.get(): bookname.get()})
            messagebox.showinfo("","BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            libbook.remove(bookname.get())
def returnb1():
    
     messagebox.showinfo("","BOOK RETURNED : THANK YOU! \n")
     libbook.append(bookname.get())
    
def donate1():
     messagebox.showinfo("","BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
     libbook.append(bookname.get())


         

        
        
        

root=Tk()
root.title("library management system")
root.geometry("1200x1200")
main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)

my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))


#second frame
second_frame=Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")


track=[]

libbook=['DIVERGENT','NIGHT SHIFT','SHES WITH ME','SIX OF CROWS']
yourname=StringVar()
bookname=StringVar()
#Button(root,text="**WELCOME TO CHINMIS LIBRARY**",pady=10,padx=10,command=dashboard).pack()
Label(second_frame,text="**WELCOME TO THE LIBRARY**",pady=40,padx=50).pack()
 
user=IntVar()

Label(second_frame,text="***enter your choice").pack()

Button(second_frame,text="list books",command=listbooks).pack()
Button(second_frame,text="borrow",command=borrow).pack()
Button(second_frame,text="return books",command=returnb).pack()
Button(second_frame,text="donate",command=donate).pack()
Button(second_frame,text="track",command=track1).pack()


#Label(second_frame,text="**WELCOME TO CHINMIS LIBRARY**",pady=40,padx=50).pack()
 
 



root.mainloop()
