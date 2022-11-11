from tkinter import *
root = Tk()
root.geometry("900x900")
root.maxsize(900, 400)
root.minsize(200, 300)
root.title("Online Job application Portal")
root.configure(bg="#89CFFD")
# Contact us 

def contactus():
    new = Toplevel()
    new.geometry("900x900")
    new.maxsize(900, 400)
    new.minsize(200, 300)
    new.configure(bg="#D6E4E5")
    f1 = LabelFrame(new, borderwidth=15, relief=SUNKEN, padx=80, pady=60)
    msg = Label(new, text="TOLL FREE NUMBER", font=("arial", 16, 'bold'), anchor=CENTER, fg="#748DA6",bg="#D6E4E5")

  
    num = Label(new, text="                   1456                        ", font=("arial", 12), anchor=CENTER, fg="#748DA6",bg="#D6E4E5")


    email = Label(new, text="For next level of support, mail to: oap@gmail.com",
                  wraplength=300, font=("arial", 12), anchor=CENTER, fg="#748DA6",bg="#D6E4E5")
    msg.pack()
    num.pack()
    email.pack()
    f1.pack()

# about us

def abt():
    new = Toplevel()
    new.geometry("900x900")
    new.maxsize(900, 400)
    new.minsize(200, 300)
    new.configure(bg="#D6E4E5")
    abtus = "This portal aims to search for jobs and hence apply for the available jobs.  It is a one-stop solution that provides a wide array of employment and career related services to the citizens of India. It works towards bridging the gap between jobseekers and employers, candidates seeking training and career guidance, agencies providing training and career counselling."
    s = Label(new, text=abtus, font=('arial', 14),
              wraplength=300, border=90, borderwidth=50, width=90,fg='#748DA6')
    s.pack()


# this function is for calling login/register function when search button is pressed.
def search(job):
    log()

# this is for login
def log():

    base = Toplevel()
    base.geometry("600x600")
    base.configure(bg="#D6E4E5")
    name_in = Label(base, text="Enter Name", width=30,
                    font=("arial", 12), anchor="w",fg='#748DA6',bg="#D6E4E5")
    name_in.grid(row=2, column=1)
    en1 = Entry(base)
    en1.grid(row=2, column=2)

    pass_in = Label(base, text="Enter password", width=30,
                    font=("arial", 12), anchor="w",fg='#748DA6',bg="#D6E4E5")
    pass_in.grid(row=4, column=1)
    en3 = Entry(base)
    en3.grid(row=4, column=2)

    reg = Label(base, text="Haven't registered yet?",
                width=30, font=("arial", 12), anchor="w",fg='#748DA6',bg="#D6E4E5")

    # this button opens window for registering
    reg_button = Button(base, text="Click here to get yourself registered!",
                        width=30, font=("arial", 12), command=to_register,bg="#EEEEEE")
    reg.grid(row=6, column=1)
    reg_button.grid(row=6, column=2)

    # this opens window for navigating back to main window
    erg = Label(base, text="LOGIN", width=30, font=("arial", 12), anchor="w",fg='#748DA6',bg="#D6E4E5")
    erg_button = Button(base, text="LOGIN", width=30, font=(
        "arial", 12), command=successful_login,bg="#EEEEEE")  
    erg.grid(row=7, column=1)
    erg_button.grid(row=7, column=2)

# this is for registering user.
def to_register():
    base = Toplevel()
    base.geometry("500x500")
    base.title("registration form")

    base.configure(bg="#D6E4E5")

    lb1 = Label(base, text="Enter Name", width=10, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb1.place(x=20, y=120)
    en1 = Entry(base)
    en1.place(x=200, y=120)

    lb3 = Label(base, text="Enter Email", width=10, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb3.place(x=19, y=160)
    en3 = Entry(base)
    en3.place(x=200, y=160)

    lb4 = Label(base, text="Contact Number", width=13, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb4.place(x=19, y=200)
    en4 = Entry(base)
    en4.place(x=200, y=200)

    lb5 = Label(base, text="Select Gender", width=15, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb5.place(x=5, y=240)
    vars = IntVar()
    Radiobutton(base, text="Male", padx=5, variable=vars,
                value=1,fg='#748DA6',bg="#D6E4E5").place(x=180, y=240)
    Radiobutton(base, text="Female", padx=10,
                variable=vars, value=2,fg='#748DA6',bg="#D6E4E5").place(x=240, y=240)
    Radiobutton(base, text="others", padx=15,
                variable=vars, value=3,fg='#748DA6',bg="#D6E4E5").place(x=310, y=240)

    list_of_cntry = ("United States", "India", "Nepal", "Germany")
    cv = StringVar()
    drplist = OptionMenu(base, cv, *list_of_cntry)
    drplist.config(width=15)
    cv.set("United States")
    lb2 = Label(base, text="Select Country", width=13, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb2.place(x=14, y=280)
    drplist.place(x=200, y=275)

    lb6 = Label(base, text="Enter Password", width=13, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb6.place(x=19, y=320)
    en6 = Entry(base, show='*')
    en6.place(x=200, y=320)

    lb7 = Label(base, text="Re-Enter Password", width=15, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    lb7.place(x=21, y=360)
    en7 = Entry(base, show='*')
    en7.place(x=200, y=360)


    # shows user is sucessfully registered
    def sucessful_register():
        lab = Label(base, text="Successfuly registered! Now you search for your job!.",fg='#748DA6',bg="#D6E4E5")
        lab.pack()
    
    Button(base, text="Register", width=10,command=sucessful_register).place(x=200, y=400)

# this helps to navigate back to main window
def successful_login():
    base = Toplevel(bg="#D6E4E5")
    base.geometry("600x600")

    lab = Label(base, text="Successfuly login! Now you search for your job!.",fg='#748DA6',bg="#D6E4E5").pack()
    Button(base, text="GO TO SEARCH WINDOW", width=20,
           command=search_button_clicked).pack(pady=20)
    Button(base, text="Quit", command=base.destroy).pack()

# this shows job you have searched for.
def search_button_clicked():
    t = Toplevel(bg="#D6E4E5")
    t.geometry("900x900")
    t.maxsize(900, 400)
    t.minsize(200, 300)
    loc = loc_in.get()
    pos = pos_in.get()
    text = Label(
        t, text=f"You have shown interest in {pos} and wish to work in {loc} and here are the results.", wraplength=300, width=40, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")

    text.pack()

    hi = [
        ("software engineering", "delhi"),
        ("mechanical engineering", "noida"),
        ("electrical engineering", "gurugram"),
        ("data analyst", "kolkatta"),
        ("web development", "bangalore"),
        ("chef", "bangalore"),
        ("teacher", "delhi"),
        ("writer", "mumbai"),
        ("journalism", "mumbai"),
        ("accountant", "lucknow"),
        ("social media management", "indore")
    ]
    flag = False
    for job, city in hi:
        if loc.lower() == city and job.lower() == pos:

            found = Label(t, text="Congratulations, we found a job as per your request.",fg='#748DA6',bg="#D6E4E5",
                          wraplength=300, width=40, font=("arial", 12))
            found.place(x=270, y=60)
            flag = True
            break
        else:
            foun = Label(t, text="Sorry, no job found.",
                         wraplength=300, width=40, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
            foun.place(x=270, y=60)


    if flag == True:
        name_label = Label(t, text=pos.upper(), font=(
            "arial", 20, 'bold'), anchor=CENTER)

        comp_name = Label(t, text='ABC INDIA', font=(
            "arial", 16), anchor=CENTER)

        loc_label = Label(t, text=loc.upper()+" ,INDIA",
                          font=("arial", 16), anchor=CENTER)

        apply_now = Button(t, text='What you waiting for? ... Apply Now!',
                           width=50, font=("arial", 12), command=apply)

        name_label.place(x=300, y=120)
        comp_name.place(x=300, y=160)
        loc_label.place(x=300, y=200)
        apply_now.place(x=300, y=240)


def successfully_applied():
    
    hi = Toplevel()
    hi.geometry("900x900")
    hi.maxsize(900, 400)
    hi.minsize(200, 300)
    Label(hi, text="Successfully Applied.", width=40,bd=20, font=("arial", 12),fg='#748DA6',bg="#D6E4E5").pack()

# application form
def apply():
    app = Toplevel()
    app.geometry("900x900")
    app.maxsize(900, 400)
    app.minsize(200, 300)
    
    
    app.geometry("900x900")
    app.maxsize(900, 400)
    app.minsize(200, 300)
    # name
    name_label = Label(app, text="NAME", width=10, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    name_label.place(x=20, y=120)
    name_entry = Entry(app)
    name_entry.place(x=200, y=120)
    # address
    address_label = Label(app, text="ADDRESS", width=10, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    address_label.place(x=19, y=160)
    address_entry = Entry(app)
    address_entry.place(x=200, y=160)
    # QUALIFICATION
    qualification_label = Label(app, text="QUALIFICATIONS", width=15, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    qualification_label.place(x=19, y=200)
    qualification_entry = Entry(app,width=60)
    qualification_entry.place(x=200, y=200)
    
    
    # experience
    experience_label = Label(app, text="EXPERIENCE", width=12, font=("arial", 12),fg='#748DA6',bg="#D6E4E5")
    experience_label.place(x=19, y=240)
    experience_entry = Entry(app,width=60)
    experience_entry.place(x=200, y=240)
    
    # apply button
    to_apply = Button(app, text="Apply",width=10,command=successfully_applied)
    to_apply.place(x=400,y=350)
    
'''This is for top access bar'''
f = LabelFrame(root, borderwidth=10, relief=RAISED, padx=50, pady=25, bg="#2192FF")
home = Button(f, text="HOME", bd=5,bg="#DFF6FF")
contact = Button(f, text="CONTACT", bd=5, command=contactus,bg="#DFF6FF")
about = Button(f, text="ABOUT US", bd=5, command=abt,bg="#DFF6FF")
login = Button(f, text="LOGIN/REGISTER", bd=5, command=log,bg="#DFF6FF")
home.grid(row=0, column=1, padx=50, pady=20)
contact.grid(row=0, column=2, padx=50, pady=20)
about.grid(row=0, column=3, padx=50, pady=20)
login.grid(row=0, column=4, padx=50, pady=20)
f.pack()


'''This is for filing position and desired location opt  and searching it'''
f2 = LabelFrame(root, borderwidth=15, relief=SUNKEN, padx=80, pady=60,bg="#47B5FF")
l1 = Label(f2, text="Find A Job That Will Fit To Your Expertise!",
           justify='center', width=35, font=("arial", 12),bg="#47B5FF")
l1.config(justify=CENTER)
l1.place(x=12, y=-30)

pos = Label(f2, text="Postion", width=15, font=("arial", 12),bg="#47B5FF")

pos.grid(row=5, column=0)
pos_in = Entry(f2, width=30)
pos_in.insert(0,"Possition you are looking for")

pos_in.grid(row=9, column=0)

loc = Label(f2, text="Location", width=15, font=("arial", 12),bg="#47B5FF")
# pos.place(x = 0 , y=25 )
loc.grid(row=5, column=8)

job = StringVar()
loc_in = Entry(f2, width=20, textvariable=job)
loc_in.insert(0,"Enter desired location")

loc_in.grid(row=9, column=8)

search_button = Button(
    f2, text='Search', command=lambda: search(job), borderwidth=1, bg="#89CFFD")

search_button.grid(row=9, column=9)


f2.pack(padx=30, pady=30)


root.mainloop()
