import customtkinter as ctk
import tkinter as tk
import database1
from tkinter import filedialog
from PIL import Image
from customtkinter import *
import database1 as cdb
from tkinter import messagebox
ap = ctk.CTk()
def main():
    def filedialog1():
        global image_path
        image_path = filedialog.askopenfilename()

    def submit():
        toplevel = messagebox.showwarning(ap,message=" Registered succesfully!")
        global password1
        password1 = entry1.get()
        contact = entry2.get()
        character = entry4.get()
        val = entry5.get()
        cdb.insert(password1, contact,character, val, image_path)

    def log_in():
        datos = []
        data = ()
        image = []
        passw = entry.get()
        for i in cdb.fetch():
            datos.append(i[0])
            if i[0] == passw:
                data += i
                image.append(i[4])
            

        def separator(number):
                x = ""
                char = data[number].split()
                counter = len(char)
            
                for i in range(counter):
                    if i % 3 == 0:
                        x += "\n" + char[i]
                    else:
                        x +=  " " + char[i]
                return x

        if passw in datos:
            ap.destroy()
            root = ctk.CTk()
            def home():
                frameroot1 = ctk.CTkFrame(root)
                frameroot1.configure(fg_color="#cbc5c7" , width = 865, height = 550)
                frameroot1.place(x=1,y=50)
                frame0= ctk.CTkFrame(root)
                frame0.configure(fg_color="#AF90FC" , width = 300, height = 300, corner_radius=150, bg_color="#cbc5c7")
                frame0.place(x=300,y=70)
                framed = ctk.CTkFrame(root)
                framed.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed.place(x=800,y=50)
                framed1 = ctk.CTkFrame(root)
                framed1.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed1.place(x=830,y=50)
                framed2 = ctk.CTkFrame(root)
                framed2.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed2.place(x=770,y=50)
                framed3 = ctk.CTkFrame(root)
                framed3.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed3.place(x=740,y=50)
                

                label = ctk.CTkLabel(frameroot1, text = separator(2),
                                    text_color="Black",
                                    font =('Raillinc', 24 , "bold"),
                                    bg_color= "#D3D3B1",
                                    fg_color="#cbc5c7",
                                    justify = "left"
                                    )
                label.place(x=95,y=250)
                image_original = ctk.CTkImage(light_image=Image.open(image[0]), size=(200,200))

                my_label= ctk.CTkLabel(frame0,text='', image=image_original)
                my_label.place(x=50, y =50)

                root.mainloop()
            def about():
                frameroot1 = ctk.CTkFrame(root)
                frameroot1.configure(fg_color="#cbc5c7" , width = 865, height = 550)
                frameroot1.place(x=1,y=50)
                framed = ctk.CTkFrame(root)
                framed.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed.place(x=800,y=50)
                framed1 = ctk.CTkFrame(root)
                framed1.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed1.place(x=830,y=50)
                framed2 = ctk.CTkFrame(root)
                framed2.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed2.place(x=770,y=50)
                framed3 = ctk.CTkFrame(root)
                framed3.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed3.place(x=740,y=50)
                
                


                label = ctk.CTkLabel(frameroot1, text = separator(3),
                                    text_color="Black",
                                    font =('Raillinc', 18 , "bold"),
                                    bg_color= "green",
                                    fg_color="#cbc5c7",
                                    justify = "left"
                                    )
                label.place(x=0,y=300)
                image_original = ctk.CTkImage(light_image=Image.open('C:/Users/Administrator/Desktop/vince programs/vi.png'), size=(300,300))

                my_label= ctk.CTkLabel(frameroot1,text='', image=image_original)
                my_label.place(x=330, y =20)

                root.mainloop()

            def contact():
                frameroot1 = ctk.CTkFrame(root)
                frameroot1.configure(fg_color="#cbc5c7" , width = 865, height = 550)
                frameroot1.place(x=1,y=50)
                framed = ctk.CTkFrame(root)
                framed.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed.place(x=800,y=50)
                framed1 = ctk.CTkFrame(root)
                framed1.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed1.place(x=830,y=50)
                framed2 = ctk.CTkFrame(root)
                framed2.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed2.place(x=770,y=50)
                framed3 = ctk.CTkFrame(root)
                framed3.configure(fg_color="#AF90FC", width = 12, height = 600)
                framed3.place(x=740,y=50)


                

                label = ctk.CTkLabel(frameroot1, text = f"{data[1]}-----PLEASE CALL ME\n USING THIS NUMBER",
                                    text_color="Black",
                                    font =('Raillinc', 18 , "bold"),
                                    bg_color= "#cbc5c7",
                                    fg_color="#cbc5c7",
                                    justify = "center"
                                    )
                
                label.place(x=95,y=250)
                image_original = ctk.CTkImage(light_image=Image.open('C:/Users/Administrator/Desktop/vince programs/vi2.png'), size=(200,200))

                my_label= ctk.CTkLabel(frameroot1,text='', image=image_original)
                my_label.place(x=130, y =10)

                

                root.mainloop()

            def c():
                global root
                root.destroy()



            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            root.geometry(f"{width}x{height}")
            root.geometry("0+0")
            root.configure(fg_color="#AF90FC")#AF90FC

            frameroot1 = ctk.CTkFrame(root)
            frameroot1.configure(fg_color="#cbc5c7" , width = 865, height = 550)
            frameroot1.place(x=1,y=50)
            frame0= ctk.CTkFrame(root)
            frame0.configure(fg_color="#AF90FC" , width = 300, height = 300, corner_radius=150, bg_color="#cbc5c7")
            frame0.place(x=300,y=70)

            framed = ctk.CTkFrame(root)
            framed.configure(fg_color="#AF90FC", width = 12, height = 600)
            framed.place(x=800,y=50)
            framed1 = ctk.CTkFrame(root)
            framed1.configure(fg_color="#AF90FC", width = 12, height = 600)
            framed1.place(x=830,y=50)
            framed2 = ctk.CTkFrame(root)
            framed2.configure(fg_color="#AF90FC", width = 12, height = 600)
            framed2.place(x=770,y=50)
            framed3 = ctk.CTkFrame(root)
            framed3.configure(fg_color="#AF90FC", width = 12, height = 600)
            framed3.place(x=740,y=50)

            label = ctk.CTkLabel(frameroot1, text = separator(2),
                                    text_color="Black",
                                    font =('Raillinc', 24 , "bold"),
                                    bg_color= "#D3D3B1",
                                    fg_color="#cbc5c7",
                                    justify = "left"
                                    )
            label.place(x=95,y=250)
            image_original = ctk.CTkImage(light_image=Image.open(image[0]), size=(200,200))

            my_label= ctk.CTkLabel(frame0,text='', image=image_original)
            my_label.place(x=50, y =50)

            frameroot2 = ctk.CTkFrame(root)
            frameroot2.configure(fg_color="#cbc5c7" , width = 400, height = 550)#cbc5c7
            frameroot2.pack(pady=0,padx=0)
            frameroot2.place(x=868,y=50)



            Buttonservices = ctk.CTkButton(frameroot2, 
                                text="Contact", 
                                font = ("Lolita Script",18,"bold"),
                                text_color="black",
                                bg_color="#cbc5c7",
                                fg_color="#AF90FC",
                                width=10,
                                corner_radius=50,
                                hover_color="#C0ACF1",
                                command=contact
                                ).place(x= 190,y=12)
            but1 = ctk.CTkButton(frameroot2, 
                                text="home", 
                                font = ("Lolita Script",18,"bold"),
                                text_color="black",
                                bg_color="#cbc5c7",
                                fg_color="#AF90FC",
                                width=10,
                                corner_radius=50,
                                hover_color="#C0ACF1",
                                command=home
                                ).place(x= 20,y=12)#command=home
            but2 = ctk.CTkButton(frameroot2, 
                                text="about", 
                                font = ("Lolita Script",18,"bold"),
                                text_color="black",
                                bg_color="#cbc5c7",
                                fg_color="#AF90FC",
                                width=10,
                                corner_radius=50,
                                hover_color="#C0ACF1",
                                command=about
                                ).place(x= 105,y=12)
            but3 = ctk.CTkButton(root, text="x", font = ("Lolita Script",18,"bold"),text_color="black",bg_color="#AF90FC",fg_color="#922B21", width=10,corner_radius=50, hover_color="#922B21", command=root.destroy ).place(x= 1200,y=12)

            image_original = ctk.CTkImage(light_image=Image.open('C:/Users/Administrator/Desktop/vince programs/Vince2.png'), size=(400,400),)
            my_label= ctk.CTkLabel(frameroot2,text='', image=image_original, width=500,height=500)
            my_label.place(x=-30, y =100)
            root.mainloop()
        else:
                toplevel = messagebox.showwarning(ap,message="Wrong Password!")
                
    ap.title("SIGN UP!")
    ap.geometry("900x900")
    ap.geometry("300+0")
    ap.resizable(width=False,height=False)
    #sign up frame
    frame=ctk.CTkFrame(ap, fg_color="#AF90FC", width=450, height=900 )
    frame.place(x=450,y=0)
    #sign up
    label= ctk.CTkLabel(frame, text="Sign up", font =('Raillinc', 34 , "bold"), bg_color= "#D3D3B1", fg_color="#AF90FC")
    label.place(x=170,y=60)
    #password
    password1 =ctk.CTkLabel(frame, text="C-password", font =('Raillinc', 20 , "bold") )
    password1.place(x=40,y=200)
    entry1= ctk.CTkEntry(frame, height=30, width= 250, corner_radius=50)
    entry1.place(x=180,y=200)
    #contact
    contact =ctk.CTkLabel(frame, text="Contact", font =('Raillinc', 20 , "bold") )
    contact.place(x=80,y=235)
    entry2= ctk.CTkEntry(frame, height=30, width= 250, corner_radius=50)
    entry2.place(x=180,y=235)
    #upload a picture
    pic = ctk.CTkButton(frame, text="PICTURE",font =('Raillinc', 20 , "bold"), corner_radius=50, command = filedialog1)
    pic.place(x=180,y=280)
    pic1 =ctk.CTkLabel(frame, text="Upload", font =('Raillinc', 20 , "bold") )
    pic1.place(x=93,y=280)
    #describe yourself
    about =ctk.CTkLabel(frame, text="Describe yourself", font =('Raillinc', 20 , "bold") )
    about.place(x=125,y=350)
    entry4= ctk.CTkEntry(frame, height=50, width= 300, corner_radius=50)
    entry4.place(x=83,y=380)
    #values
    val =ctk.CTkLabel(frame, text="Your Values", font =('Raillinc', 20 , "bold") )
    val.place(x=155,y=470)
    entry5= ctk.CTkEntry(frame, height=50, width= 300, corner_radius=50)
    entry5.place(x=83,y=500)
    #submit button
    sub = ctk.CTkButton(frame, text="Submit",font =('Raillinc', 24 , "bold"), corner_radius=30, fg_color="green", command= submit)
    sub.place(x=170,y=570)

    #sign in
    label1=ctk.CTkLabel(ap, text="Sign in",  font =('Raillinc', 34 , "bold"),)
    label1.place(x=170,y=60)
    #sign in password
    password =ctk.CTkLabel(ap, text="Password", font =('Raillinc', 20 , "bold") )   
    password.place(x=50,y=200)
    entry= ctk.CTkEntry(ap, height=30, width= 250, corner_radius=50)
    entry.place(x=170,y=200)
    #login
    login = ctk.CTkButton(ap, text="Log in",font =('Raillinc', 24 , "bold"), corner_radius=30 , fg_color="green", command= log_in)
    login.place(x=170,y=350)

    ap.mainloop()

if __name__ == "__main__":
    main()




