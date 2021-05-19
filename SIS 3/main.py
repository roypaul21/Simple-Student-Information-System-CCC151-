from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

start_p = Tk()
w = 860
h = 630
start_p.geometry(f'{w}x{h}+{250}+{40}')
start_p.overrideredirect(True)
start_p.iconbitmap(r'sis.ico')
start_p.configure(background="black")
start_p.resizable(False, False)

# sis Gif animation
frameCnt = 10
frames = [PhotoImage(file='loading1.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
            ind = 0
    label.configure(image=frame, bg='black')
    start_p.after(50, update, ind)

label = Label(start_p)
label.place(x=200, y=20)
start_p.after(0, update, 0)

def mp():
    main_p = Tk()
    w = 860
    h = 630
    main_p.geometry(f'{w}x{h}+{250}+{40}')
    main_p.configure(background="#161618")
    main_p.resizable(False, False)
    main_p.iconbitmap(r'sis.ico')
    main_p.overrideredirect(True)

    
    #main page frames
    f = Frame(main_p, width=700, height=0, highlightbackground="white", highlightthickness=4, bg="#161618")
    f.place(x=0, y=470)

    f2 = Frame(main_p, width=700, height=0, highlightbackground="white", highlightthickness=4, bg="#161618")
    f2.place(x=0, y=189)

    f3 = Frame(main_p, width=890, height=0, highlightbackground="white", highlightthickness=4, bg="#161618")
    f3.place(x=0, y=340)

    # sis Gif animation
    frameCnt = 25
    frames = [PhotoImage(file='gifb.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame, bg="#161618")
        main_p.after(50, update, ind)

    label = Label(main_p)
    label.place(x=610, y=200)
    main_p.after(0, update, 0)

    # student list page
    def student_list_p():
        root2 = Tk()
        w = 800
        h = 500
        root2.geometry(f'{w}x{h}+{280}+{110}')
        root2.resizable(False, False)
        root2.configure(background="#161618")
        root2.iconbitmap(r'sis.ico')
        root2.overrideredirect(True)

        f = Frame(root2, width=0, height=510, highlightbackground="white", highlightthickness=4, bg="#161618")
        f.place(x=200, y=0)

        f2 = Frame(root2, width=0, height=510, highlightbackground="white", highlightthickness=4, bg="#161618")
        f2.place(x=500, y=0)

        f3 = Frame(root2, width=0, height=510, highlightbackground="white", highlightthickness=4, bg="#161618")
        f3.place(x=700, y=0)
        idnum = Entry(root2, width=0)
        idnum.place(x=10, y=70)

        ttk.Style().theme_use("clam")
        ttk.Style().configure("Treeview", background="light gray",
                              foreground="black", fieldbackground="gray")
        ttk.Style().map('Treeview', background=[('selected','black')])

        # List Student
        frm = Frame(root2)
        frm.pack(side=LEFT, padx=6, pady=(0, 150))

        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show="headings", height=13)
        tv.pack()

        tv.heading(1, text="Name", anchor=CENTER)
        tv.heading(2, text="ID Number", anchor=CENTER)
        tv.heading(3, text="Gender", anchor=CENTER)
        tv.heading(4, text="Course", anchor=CENTER)

        with open('StudentList.csv') as f:
            reader = csv.DictReader(f, delimiter=',')

            for row in reader:
                name = row['Name']
                id_number = row['ID No.']
                gender = row['Gender']
                course = row['Course']

                tv.insert('', 'end', values=(name, id_number, gender, course))

        # delete function
        def delete():
            if idnum.get() == '':
                return messagebox.showinfo("DELETE INFO", "PLEASE PRESS 'SELECT' BUTTON")

            if messagebox.askyesno("Delete Confirmation", "Do you wanna Delete this Student") == False:
                return

            selected = tv.selection()
            tv.delete(selected)

            lists = []
            with open("StudentList.csv", 'r', newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if idnum.get() != row[1]:

                        lists.append(row)
                        #   print(row)

            with open("StudentList.csv", "w", newline="") as file:
                Writer = csv.writer(file)
                Writer.writerows(lists)
            messagebox.showinfo("Delete info", "Item Successfully Deleted")

            name.delete(0, END)
            idnum.delete(0, END)
            gender.delete(0, END)
            course.delete(0, END)

        #Delete all function
        def del_all():
            for records in tv.get_children():
                tv.delete(records)
            headerList = ['Name','ID No.','Gender','Course']
            with open("StudentList.csv", "w", newline="") as file:
                dw = csv.DictWriter(file, fieldnames=headerList)
                dw.writeheader()
                Writer = csv.writer(file)
                for row_id in tv.get_children():
                    row = tv.item(row_id)['values']
                    Writer.writerows(row)
            messagebox.showinfo("Delete info", "Items Successfully Deleted")



        # Select Button
        def slc():
            name.delete(0, END)
            idnum.delete(0, END)
            gender.delete(0, END)
            course.delete(0, END)

            selected = tv.focus()
            values = tv.item(selected, 'values')

            name.insert(0, values[0])
            idnum.insert(0, values[1])
            gender.insert(0, values[2])
            course.insert(0, values[3])

        # csv function
        def update_csv():
            messagebox.showinfo("Update Info", "Yey you have update successfully")

            data1 = name.get()
            data2 = idnum.get()
            data3 = gender.get()
            data4 = course.get()

            sel = tv.selection()
            tv.item(sel, values=(data1, data2, data3, data4))


            lists = []
            with open("StudentList.csv", 'r', newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if idnum.get() == row[1]:
                        row[0] = name.get()
                        row[2] = gender.get()
                        row[3] = course.get()
                    lists.append(row)

            with open("StudentList.csv", "w", newline="") as f:
                Writer = csv.writer(f, dialect='excel')
                Writer.writerows(lists)

            name.delete(0, END)
            idnum.delete(0, END)
            gender.delete(0, END)
            course.delete(0, END)


        def back():
            root2.destroy()
            mp()



        # delete button
        delete_btn = Button(root2, bg="red4", text="DELETE",fg="white",command=delete)
        delete_btn.place(x=125, y=450)

        delete_all = Button(root2,bg="dark red", text="DELETE ALL",fg="white",command=del_all)
        delete_all.place(x=20, y=450)

        # Update button
        update_btn = Button(root2, bg="dark green", text="UPDATE", command=update_csv,fg="white")
        update_btn.place(x=80, y=400)

        # Select Button
        slc_btn = Button(root2, bg="navy", text="Select", command=slc,fg="white")
        slc_btn.place(x=80, y=350)

        # Back button
        bk = PhotoImage(file="back.bmp.png ")
        back_btn = Button(root2, image=bk, compound=CENTER, bg="#161618",
                   borderwidth=0, activebackground="#161618", command=lambda: [back()])
        back_btn.place(x=740, y=450)

        # Entry update function
        gender = Entry(root2)
        gender.place(x=300, y=380)
        gl= Label(root2,text="GENDER:",bg="#161618", fg="White")
        gl.place(x=245,y=378)

        course = Entry(root2)
        course.place(x=300, y=410)
        cl = Label(root2, text="COURSE:", bg="#161618", fg="White")
        cl.place(x=245, y=408)

        name = Entry(root2, width=20)
        name.place(x=300, y=350)
        nl = Label(root2, text="NAME:", bg="#161618", fg="White")
        nl.place(x=245, y=348)

        root2.mainloop()


    #Search page
    def search_p():
        main_p.destroy()
        root4 = Tk()
        w = 600
        h = 250
        root4.overrideredirect(True)
        root4.geometry(f'{w}x{h}+{390}+{200}')
        root4.resizable(False, False)
        root4.configure(background="#161618")

        def search():
            if srch_entry.get() == "":
               messagebox.showwarning("Search Warning", "Please Input ID Number...")

            else:

                root3 = Tk()
                w = 800
                h = 200
                root3.geometry(f'{w}x{h}+{280}+{200}')
                root3.title('Record')
                root3.iconbitmap(r'sis.ico')
                root3.resizable(False, False)
                root3.configure(background="#161618")
                idnum = Entry(root3, width=0)
                idnum.place(x=200, y=12)

                f = Frame(root3, width=0, height=200, highlightbackground="white", highlightthickness=1, bg="#161618")
                f.place(x=150, y=110)
                f = Frame(root3, width=0, height=200, highlightbackground="white", highlightthickness=1, bg="#161618")
                f.place(x=700, y=110)

                # searched function
                frm1 = Frame(root3)
                frm1.pack(side=LEFT, padx=10, pady=(0, 110))

                tv = ttk.Treeview(frm1, columns=(1, 2, 3, 4), show="headings", height=13)
                tv.pack()

                tv.heading(1, text="Name", anchor=CENTER)
                tv.heading(2, text="ID Number", anchor=CENTER)
                tv.heading(3, text="Gender", anchor=CENTER)
                tv.heading(4, text="Course", anchor=CENTER)

                lists=[]
                with open("studentlist.csv", 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        lists.append(row)

                col = [x[1] for x in lists]

                #print(col)

                if srch_entry.get() in col:
                    for row in range (1, len(lists)):
                        if srch_entry.get() == lists[row][1]:
                            tv.insert('', 'end', values=(lists[row]))
                else:
                    root3.destroy()
                    messagebox.showwarning("Search Info", "Invalid ID Entry or No Student Register")


                def delete():

                    if idnum.get() == '':
                        return messagebox.showinfo("DELETE INFO", "PLEASE PRESS 'SELECT' BUTTON")

                    if messagebox.askyesno("Delete Confirmation", "Do you wanna Delete this Student") == False:
                        return

                    selected = tv.selection()
                    tv.delete(selected)

                    lists = []
                    with open("StudentList.csv", 'r', newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if idnum.get() != row[1]:
                                lists.append(row)
                                #   print(row)

                    with open("StudentList.csv", "w", newline="") as file:
                        Writer = csv.writer(file)
                        Writer.writerows(lists)
                    messagebox.showinfo("Delete info", "Item Successfully Deleted")

                    name.delete(0, END)
                    idnum.delete(0, END)
                    gender.delete(0, END)
                    course.delete(0, END)

                def slc():
                    name.delete(0, END)
                    idnum.delete(0, END)
                    gender.delete(0, END)
                    course.delete(0, END)

                    selected = tv.focus()
                    values = tv.item(selected, 'values')

                    name.insert(0, values[0])
                    idnum.insert(0, values[1])
                    gender.insert(0, values[2])
                    course.insert(0, values[3])

                def update_csv():

                    messagebox.showinfo("Update Info", "Yey you have update successfully")
                    data1 = name.get()
                    data2 = idnum.get()
                    data3 = gender.get()
                    data4 = course.get()

                    sel = tv.selection()
                    tv.item(sel, values=(data1, data2, data3, data4))

                    updatedlist = []
                    with open("StudentList.csv", 'r', newline="") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            if idnum.get() == row[1]:
                                row[0] = name.get()
                                row[2] = gender.get()
                                row[3] = course.get()
                            updatedlist.append(row)

                    with open("StudentList.csv", "w", newline="") as f:
                        Writer = csv.writer(f,dialect='excel')
                        Writer.writerows(updatedlist)

                    name.delete(0, END)
                    idnum.delete(0, END)
                    gender.delete(0, END)
                    course.delete(0, END)


                def back():
                    root3.destroy()

                def des1():
                    root4.destroy()
                    root3.destroy()

                # delete button
                delete_more_btn = Button(root3, bg="dark salmon", text="DELETE", command=delete)
                delete_more_btn.place(x=10,y=167)

                # Update button
                update_btn = Button(root3, bg="light green", text="UPDATE", command=update_csv)
                update_btn.place(x=10,y=134)

                # Select Button
                slc_btn = Button(root3, bg="light blue", text="Select", command=slc)
                slc_btn.place(x=10,y=100)

                rec = Button(root3, text="Records", command=lambda: [des1(), student_list_p()],
                                activebackground="#161618", bg="light blue")
                rec.place(x=737, y=135)
                # back button
                back_btn = Button(root3, borderwidth=5, bg="gray", text="Return", activebackground="#161618",
                                                   command=lambda: [back()])
                back_btn.place(x=740, y=167)

                # Entry update function
                gender = Entry(root3)
                gender.place(x=300, y=135)
                gl = Label(root3, bg='#161618', text='Gender:', fg="white")
                gl.place(x=250, y=135)

                course =Entry(root3)
                course.place(x=300, y=161)
                cl = Label(root3, bg='#161618', text='Course:', fg="white")
                cl.place(x=250, y=161)

                name = Entry(root3, width=20)
                name.place(x=300, y=110)
                nl = Label(root3, bg='#161618', text='Name:', fg="white")
                nl.place(x=250, y=110)

                root3.mainloop()
                         
        #search frame
        f = Frame(root4, width=295, height=40, highlightbackground="white", highlightthickness=1, bg="#161618")
        f.place(x=130, y=110)
        f = Frame(root4, width=0, height=40, highlightbackground="white", highlightthickness=1, bg="#161618")
        f.place(x=373, y=110)

        # Search Entry
        srch_entry = Entry(root4, width=30)
        srch_entry.place(x=180, y=120)

        #Search ID number lbl
        si = Label(root4, text="Type ID Number....", font=("Madelyn", 21, "italic"), fg="white", bg="#161618")
        si.place(x=140, y=30)

        m = PhotoImage(file="mini search.png")
        min_search = Label(root4, image=m,bg="#161618")
        min_search.place(x=140,y=120)

        #search button
        search_btn = Button(root4,text="Search",bg="#161618",fg="white", borderwidth=0,activebackground="#161618", command=search)
        search_btn.place(x=375,y=118)

        def back():
            root4.destroy()
        #back button
        ba = PhotoImage(file="back.bmp.png")

        back_btn = Button(root4, borderwidth=0, image=ba, compound=CENTER, activebackground="#161618",bg="#161618",
                          command=lambda: [back(), mp()])
        back_btn.place(x=500, y=200)
        root4.mainloop()

    # Register student page
    def register_p():
        main_p.destroy()
        root1 = Tk()
        w = 400
        h = 400
        root1.geometry(f'{w}x{h}+{480}+{170}')
        root1.configure(background="#161618")
        root1.resizable(False, False)
        root1.iconbitmap(r'sis.ico')
        root1.overrideredirect(True)

        fa = Frame(root1, width=410, height=340, highlightbackground="white", highlightthickness=1, bg="#161618")
        fa.place(x=20, y=20)

        # Register Function
        def register():
            if name.get() == '':
                return messagebox.showwarning("Warning!", "PLEASE COMPLETE THE INPUT")
            elif idnum.get() == '':
                return messagebox.showwarning("Warning!", "PLEASE COMPLETE THE INPUT")
            elif gender.get() == 'Gender':
                return messagebox.showwarning("Warning!", "PLEASE COMPLETE THE INPUT")
            elif course.get() == 'Course':
                return messagebox.showwarning("Warning!", "PLEASE COMPLETE THE INPUT")

            data1 = name.get()
            data2 = idnum.get()
            data3 = gender.get()
            data4 = course.get()

            with open('StudentList.csv', 'a',newline='') as f:
                w = csv.writer(f, dialect='excel')
                w.writerow([
                    data1,
                    data2,
                    data3,
                    data4])

            name.delete(0, END)
            idnum.delete(0, END)
            gender.set("Gender")
            course.set("Course")
            messagebox.showinfo("Register Confirmation", "Successfully Registered")



        def back():
            root1.destroy()

        # register student entry
        name = Entry(root1, width=30)
        name.place(x=115, y=80)

        idnum = Entry(root1, width=30)
        idnum.place(x=115, y=110)

        gender = StringVar()
        gender.set("Gender")
        drop_g = OptionMenu(root1, gender, "Male", "Female", "Transgender", "Genderqueer", "Gender Neutral", "Others")
        drop_g["menu"].config(bg="light yellow")
        drop_g.place(x=100, y=150)


        course = StringVar()
        course.set("Course")
        drop_c = OptionMenu(root1, course, "Computer Science", "IT", "Biology", "Engineer", "Teacher", "Chemistry",
                            "Nursing", "Psychology", "Economics", "Accountacy", "Political Science", "Sociology")
        drop_c["menu"].config(bg="light yellow")
        drop_c.place(x=230, y=150)


        # register student Label
        register_lbl = Label(root1, bg="#161618", text="REGISTER", font=('Helvetica', 25, 'bold'), fg="White")
        register_lbl.place(x=115, y=5)

        name_lbl = Label(root1, bg="#161618", fg='white', text="Complete Name:", font=('helvetica', 10))
        name_lbl.place(x=7, y=80)

        idnum_lbl = Label(root1, bg="#161618", text="ID Number:", fg='white', font=('helvetica', 10))
        idnum_lbl.place(x=7, y=110)

        # register button
        r = PhotoImage(file="register now.png")
        register_btn = Button(root1, image=r, compound=CENTER, command=register,borderwidth=0, activebackground="#161618",bg="#161618")
        register_btn.place(x=119, y=210)

        # terms and condition button

        # back button
        ba = PhotoImage(file="back.bmp.png")

        b = Button(root1, image=ba, compound=CENTER, bg="#161618",
                            borderwidth=0, activebackground="#161618", command=lambda: [back(), mp()])
        b.place(x=300, y=290)


        root1.mainloop()

        # exit function

    def exit():
        if messagebox.askyesno("Exit", "Are You Sure You Want To Exit?...") == False:
           return
        else:
            main_p.destroy()
    def des():
        main_p.destroy()

    #label
    s = Label(main_p, text="SEARCH", wraplength=1,  fg="white", bg="#161618")
    s.place(x=2, y=80)

    r = Label(main_p, text="REGISTER", wraplength=1,  fg="white", bg="#161618")
    r.place(x=2, y=200)

    l = Label(main_p, text="RECORDS", wraplength=1,  fg="white", bg="#161618")
    l.place(x=2, y=350)

    e = Label(main_p, text="EXIT", wraplength=1,  fg="white", bg="#161618")
    e.place(x=2, y=490)

    #search button
    c2 = PhotoImage(file="search.bmp.png")
    search_btn = Button(main_p, image=c2, compound=CENTER, bg="#161618",
                        borderwidth=0, activebackground="#161618", command=search_p)
    search_btn.place(x=55, y=100)

    #register button
    c = PhotoImage(file="register.bmp.png")
    register_btn = Button(main_p, image=c, compound=CENTER, bg="#161618",borderwidth=0,
                           activebackground="#161618", command= register_p)
    register_btn.place(x=60, y=220)

    #records button
    c3 = PhotoImage(file="records.bmp.png")
    records_btn = Button(main_p, image=c3, compound=CENTER, bg="#161618", borderwidth=0,
                           activebackground="#161618", command=lambda :[des(), student_list_p()])
    records_btn.place(x=35, y=370)

    #exit button
    c4 = PhotoImage(file="exit.bmp.png")
    ex_btn = Button(main_p, image=c4, compound=CENTER, bg="#161618", borderwidth=0
                      , activebackground="#161618", command=exit)
    ex_btn.place(x=40, y=476)

    main_p.mainloop()

def des():
    start_p.destroy()

start_p.after(2000, lambda :(des(), mp()))
start_p.mainloop()
