from tkinter import *
from tkinter import ttk
from threading import *
import os

def delete():
    passwordFailure.destroy()

def delete1():
    usernameFailure.destroy()

def search_function():
    searchGet = userSearch.get()

    if searchGet in files:
        file = open(searchGet, "r")
        user = file.readlines(100)
        textbox2.insert(INSERT, user)
    else:
        Label(searchScreen, text="User not found.", fg="red").pack()

def search_user():
    global searchScreen

    searchScreen = Toplevel(homeScreen)

    searchScreen.title("Narrabundah Alumni - Search")
    searchScreen.geometry("1920x1080")

    global userSearch
    userSearch = StringVar()

    Label(searchScreen, text="Search Full Name: ").pack()
    Entry(searchScreen, textvariable=userSearch).pack()
    Button(searchScreen, text="Search", font=("Calibri", 15), width=10, height=1, command=search_function).pack()

    horScrollbar = Scrollbar(searchScreen, orient=HORIZONTAL)
    horScrollbar.pack(side=BOTTOM, fill=X)

    vertScrollbar = Scrollbar(searchScreen)
    vertScrollbar.pack(side=RIGHT, fill=Y)

    global textbox2
    textbox2 = Text(searchScreen, wrap=NONE, xscrollcommand=horScrollbar.set, yscrollcommand=vertScrollbar.set, width=100, height=20, bd=10, bg="grey")
    textbox2.pack()

    horScrollbar.config(command=textbox2.xview)
    vertScrollbar.config(command=textbox2.yview)

def password_edit2():
    newPassGet = newPass.get()
    replaceFile = open(userEditGet, "r")
    replaceLine = replaceFile.readlines()
    replaceLine[6] = newPassGet+"\n"
    replaceFile = open(userEditGet, "w")
    replaceFile.writelines(replaceLine)
    replaceFile.close()
    Label(adminScreen2, text="Password successfully changed.", fg="green").pack()

def password_edit():
    global newPass
    newPass = StringVar()
    Label(adminScreen2, text="Enter new password: ").pack()
    Entry(adminScreen2, textvariable=newPass).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=password_edit2).pack()

def uni_edit2():
    newUniGet = newUni.get()
    replaceFile = open(userEditGet, "r")
    replaceLine = replaceFile.readlines()
    replaceLine[5] = newUniGet+"\n"
    replaceFile = open(userEditGet, "w")
    replaceFile.writelines(replaceLine)
    replaceFile.close()
    Label(adminScreen2, text="University successfully changed.", fg="green").pack()

def uni_edit():
    global newUni
    newUni = StringVar()
    Label(adminScreen2, text="Enter new university/career: ").pack()
    Entry(adminScreen2, textvariable=newUni).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=uni_edit2).pack()

def number_edit2():
    newNumberGet = newNumber.get()
    replaceFile = open(userEditGet, "r")
    replaceLine = replaceFile.readlines()
    replaceLine[4] = newAddressGet+"\n"
    replaceFile = open(userEditGet, "w")
    replaceFile.writelines(replaceLine)
    replaceFile.close()
    Label(adminScreen2, text="Number successfully changed.", fg="green").pack()

def number_edit():
    global newNumber
    newNumber = StringVar()
    Label(adminScreen2, text="Enter new number: ").pack()
    Entry(adminScreen2, textvariable=newNumber).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=number_edit2).pack()

def email_edit2():
    newEmailGet = newEmail.get()
    replaceFile = open(userEditGet, "r")
    replaceLine = replaceFile.readlines()
    replaceLine[3] = newEmailGet+"\n"
    replaceFile = open(userEditGet, "w")
    replaceFile.writelines(replaceLine)
    replaceFile.close()
    Label(adminScreen2, text="Email successfully changed.", fg="green").pack()

def email_edit():
    global newEmail
    newEmail = StringVar()
    Label(adminScreen2, text="Enter new email: ").pack()
    Entry(adminScreen2, textvariable=newEmail).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=email_edit2).pack()

def grad_edit2():
    newGradGet = newGrad.get()
    replaceFile = open(userEditGet, "r")
    replaceLine = replaceFile.readlines()
    replaceLine[2] = newGradGet+"\n"
    replaceFile = open(userEditGet, "w")
    replaceFile.writelines(replaceLine)
    replaceFile.close()
    Label(adminScreen2, text="Graduation year successfully changed.", fg="green").pack()

def grad_edit():
    global newGrad
    newGrad = StringVar()
    Label(adminScreen2, text="Enter new graduation year: ").pack()
    Entry(adminScreen2, textvariable=newGrad).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=grad_edit2).pack()

def address_edit2():
    newAddressGet = newAddress.get()
    replaceFile = open(userEditGet, "r")
    replaceLine = replaceFile.readlines()
    replaceLine[1] = newAddressGet+"\n"
    replaceFile = open(userEditGet, "w")
    replaceFile.writelines(replaceLine)
    replaceFile.close()
    Label(adminScreen2, text="Address successfully changed.", fg="green").pack()

def address_edit():
    global newAddress
    newAddress = StringVar()
    Label(adminScreen2, text="Enter new address: ").pack()
    Entry(adminScreen2, textvariable=newAddress).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=address_edit2).pack()

def user_edit_function():
    global userEditGet
    userEditGet = userEditVar.get()

    if userEditGet in files:
        Label(adminScreen2, text="Are you looking to edit: ").pack()
        Label(adminScreen2, text=" ").pack()
        Button(adminScreen2, text="Address", font=("Calibri", 15), width=10, height=1, command=address_edit).pack()
        Label(adminScreen2, text=" ").pack()
        Button(adminScreen2, text="Graduation year", font=("Calibri", 15), width=20, height=1, command=grad_edit).pack()
        Label(adminScreen2, text=" ").pack()
        Button(adminScreen2, text="Email", font=("Calibri", 15), width=10, height=1, command=email_edit).pack()
        Label(adminScreen2, text=" ").pack()
        Button(adminScreen2, text="Number", font=("Calibri", 15), width=10, height=1, command=number_edit).pack()
        Label(adminScreen2, text=" ").pack()
        Button(adminScreen2, text="University/Career", font=("Calibri", 15), width=20, height=1, command=uni_edit).pack()
        Label(adminScreen2, text=" ").pack()
        Button(adminScreen2, text="Password", font=("Calibri", 15), width=10, height=1, command=password_edit).pack()
    else:
        Label(adminScreen2, text="User not found.", fg="red").pack()

def user_edit():
    global adminScreen2

    adminScreen2 = Toplevel(homeScreen)

    adminScreen2.title("Narrabundah Alumni - Admin")
    adminScreen2.geometry("1920x1080")

    global userEditVar
    userEditVar = StringVar()

    Label(adminScreen2, text="Enter full name: ").pack()
    Entry(adminScreen2, textvariable=userEditVar).pack()
    Button(adminScreen2, text="OK", font=("Calibri", 15), width=10, height=1, command=user_edit_function).pack()

def user_delete():
    userDeleteGet = userDelete.get()
    if userDeleteGet in files:
        file4 = open(userDeleteGet, "w+")
        os.remove(userDeleteGet)
        Label(adminScreen, text="User successfully deleted.", fg="green").pack()
    else:
        Label(adminScreen, text="User not found.", fg="red").pack()

def user_admin():

    global userDelete
    userDelete = StringVar()
    Label(adminScreen, text="Search user to delete: ").pack()
    Entry(adminScreen, textvariable=userDelete).pack()
    Button(adminScreen, text="Delete", font=("Calibri", 15), width=10, height=1, command=user_delete).pack()

def forum_delete():
    forumDeleteGet = forumDelete.get()
    if forumDeleteGet in files:
        file3 = open(forumDeleteGet, "w+")
        os.remove(forumDeleteGet)
        Label(adminScreen, text="Forum successfully deleted.", fg="green").pack()
    else:
        Label(adminScreen, text="Forum not found.", fg="red").pack()

def forum_admin():

    global forumDelete
    forumDelete = StringVar()
    Label(adminScreen, text="Search forum to delete: ").pack()
    Entry(adminScreen, textvariable=forumDelete).pack()
    Button(adminScreen, text="Delete", font=("Calibri", 15), width=10, height=1, command=forum_delete).pack()

def admin_screen():
    global adminScreen

    adminScreen = Toplevel(homeScreen)

    adminScreen.title("Narrabundah Alumni - Admin")
    adminScreen.geometry("1920x1080")

    Label(adminScreen, text="Are you looking to delete user, forum question or edit user?: ").pack()
    Label(adminScreen, text=" ").pack()
    Button(adminScreen, text="Delete Forum", font=("Calibri", 15), width=10, height=1, command=forum_admin).pack()
    Label(adminScreen, text=" ").pack()
    Button(adminScreen, text="Delete User", font=("Calibri", 15), width=10, height=1, command=user_admin).pack()
    Label(adminScreen, text=" ").pack()
    Button(adminScreen, text="Edit User", font=("Calibri", 15), width=10, height=1, command=user_edit).pack()


def admin_function():

    archana = "Archana Aggarwal"

    if usernameLoginGet == archana:
        admin_screen()
    else:
        username_failure()

def answer_function_2():
    answerGet = answer.get()
    answerGet = str(answerGet)

    if questionGet in files:
        topic = open(questionGet, "w+")
        topic.write(questionGet+"\n")
        topic.write(answerGet)
        topic.close()
        textbox1.insert(INSERT, "\n")
        textbox1.insert(INSERT, "Answer: ")
        textbox1.insert(END, answerGet)
        Label(answerScreen, text="Answer stored!", fg="green").pack()

def answer_function():
    global questionGet
    questionGet = question.get()

    if questionGet in files:
        topic = open(questionGet, "r")
        question1 = topic.read()
        textbox1.insert(INSERT, question1)
    else:
        textbox1.insert(INSERT, "\n")
        textbox1.insert(INSERT, "Error detected. Please make sure you entered question exactly as asked in 'Question' page.")

def answer_screen():
    global answerScreen

    answerScreen = Toplevel(homeScreen)

    answerScreen.title("Narrabundah Alumni - Answers")
    answerScreen.geometry("1920x1080")

    global question
    question = StringVar()

    Label(answerScreen, text="Please type in question (exactly as written by yourself or other Alumni in 'Question' page.): ").pack()
    Entry(answerScreen, textvariable=question, width=100).pack()
    Button(answerScreen, text="Send", font=("Calibri", 15), width=10, height=1, command=answer_function).pack()
    Label(answerScreen, text=" ").pack()

    horScrollbar = Scrollbar(answerScreen, orient=HORIZONTAL)
    horScrollbar.pack(side=BOTTOM, fill=X)

    vertScrollbar = Scrollbar(answerScreen)
    vertScrollbar.pack(side=RIGHT, fill=Y)

    global textbox1
    textbox1 = Text(answerScreen, wrap=NONE, xscrollcommand=horScrollbar.set, yscrollcommand=vertScrollbar.set, width=100, height=20, bd=10, bg="grey")
    textbox1.pack()

    horScrollbar.config(command=textbox1.xview)
    vertScrollbar.config(command=textbox1.yview)

    global answer
    answer = StringVar()

    Label(answerScreen, text=" ").pack()
    Label(answerScreen, text="Please type in answer: ").pack()
    Entry(answerScreen, textvariable=answer, width=100).pack()
    Button(answerScreen, text="Send", font=("Calibri", 15), width=10, height=1, command=answer_function_2).pack()

def chatroom_function():
    msgGet = msg.get()
    msgGet = str(msgGet)

    file2 = open(msgGet, "w+")
    file2.write(msgGet)
    file2.close()

    Entry11.delete(0, END)

    textbox.insert(INSERT, "\n")
    textbox.insert(INSERT, "You: ")
    textbox.insert(END, msgGet)

    Label(chatroomScreen, text="Inquiry recieved. Please check 'Answered Questions' to see if your question has been answered.", fg="green").pack(expand=1)

def chatroom():
    global chatroomScreen

    chatroomScreen = Toplevel(homeScreen)

    chatroomScreen.title("Narrabundah Alumni - Question")
    chatroomScreen.geometry("1920x1080")

    horScrollbar = Scrollbar(chatroomScreen, orient=HORIZONTAL)
    horScrollbar.pack(side=BOTTOM, fill=X)

    vertScrollbar = Scrollbar(chatroomScreen)
    vertScrollbar.pack(side=RIGHT, fill=Y)

    global textbox

    textbox = Text(chatroomScreen, wrap=NONE, xscrollcommand=horScrollbar.set, yscrollcommand=vertScrollbar.set, width=100, height=35, bd=10, bg="grey")
    textbox.pack()

    horScrollbar.config(command=textbox.xview)
    vertScrollbar.config(command=textbox.yview)

    global msg

    msg = StringVar()

    global Entry11

    Entry11 = Entry(chatroomScreen, textvariable=msg, width=100)
    Entry11.pack(expand=1)

    Button6 = Button(chatroomScreen, text="Send", font=("Calibri", 15), width=10, height=1, command=chatroom_function)
    Button6.pack(expand=1)

def login_success():
    global loginSuccess
    loginSuccess = Toplevel(homeScreen)
    loginSuccess.title("Narrabundah Alumni")
    loginSuccess.geometry("1920x1080")
    Button(loginSuccess, text="Ask Question", font=("Calibri", 20), width=10, command=chatroom).pack(expand=1)
    Button(loginSuccess, text="Answer Question", font=("Calibri", 20), width=15, command=answer_screen).pack(expand=1)
    Button(loginSuccess, text="Search Alumni", font=("Calibri", 20), width=10, command=search_user).pack(expand=1)
    Label(loginSuccess, text=" ").pack()
    Label(loginSuccess, text="Admin authorities only available as 'Archana Aggarwal'").pack()
    Button(loginSuccess, text="Admin", font=("Calibri", 20), width=10, command=admin_function).pack(expand=1)

def password_failure():
    global passwordFailure
    passwordFailure = Toplevel(homeScreen)
    passwordFailure.title("Narrabundah Alumni - Password failure")
    passwordFailure.geometry("1920x1080")
    Label(passwordFailure, text="Incorrect password, please try again.", fg="red", font=("Calibri", 45)).pack(expand=1)
    Button(passwordFailure, text="OK", command=delete).pack(expand=1)

def username_failure():
    global usernameFailure
    usernameFailure = Toplevel(homeScreen)
    usernameFailure.title("Narrabundah Alumni - Username failure")
    usernameFailure.geometry("1920x1090")
    Label(usernameFailure, text="Incorrect name, please try again. Plase enter name as you entered when registering", fg="red", font=("Calibri", 30)).pack(expand=1)
    Button(usernameFailure, text="OK", command=delete1).pack(expand=1)

def register_function():
    firstNameGet = firstName.get()
    addressGet = address.get()
    gradYearGet = gradYear.get()
    emailGet = email.get()
    numberGet = number.get()
    universityGet = university.get()
    passwordGet = password.get()

    file = open(firstNameGet, "w")
    file.write(firstNameGet+"\n")
    file.write(addressGet+"\n")
    file.write(gradYearGet+"\n")
    file.write(emailGet+"\n")
    file.write(numberGet+"\n")
    file.write(universityGet+"\n")
    file.write(passwordGet+"\n")
    file.close()

    Entry1.delete(0, END)
    Entry3.delete(0, END)
    Entry4.delete(0, END)
    Entry5.delete(0, END)
    Entry7.delete(0, END)
    Entry8.delete(0, END)
    Entry9.delete(0, END)

    Label(registerScreen, text="Completed registration, please attempt to login.", fg="green").pack(expand=1)

def login_function():
    global usernameLoginGet
    usernameLoginGet = usernameVerify.get()
    passwordLoginGet = passwordVerify.get()

    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

    global files
    files = os.listdir()
    if usernameLoginGet in files:
        file1 = open(usernameLoginGet, "r")
        verify = file1.read().splitlines()
        if passwordLoginGet in verify:
            login_success()
        elif passwordLoginGet == " ":
            password_failure()
        else:
            password_failure()

    else:
        username_failure()

def register_screen():

    global registerScreen
    registerScreen = Toplevel(homeScreen)

    registerScreen.geometry("1920x1080")
    registerScreen.title("Narrabundah Alumni - Register")

    global firstName
    global address
    global gradYear
    global email
    global number
    global university
    global password
    global Entry1
    global Entry3
    global Entry4
    global Entry5
    global Entry6
    global Entry7
    global Entry8
    global Entry9
    firstName = StringVar()
    address = StringVar()
    gradYear = StringVar()
    email = StringVar()
    number = StringVar()
    university = StringVar()
    password = StringVar()

    Label2 = Label(registerScreen, text="First and second name: ", font=("Calibri", 10))
    Label2.pack(expand=1)
    Entry1 = Entry(registerScreen, textvariable=firstName)
    Entry1.pack(expand=1)
    Label5 = Label(registerScreen, text="Address: ", font=("Calibri", 10))
    Label5.pack(expand=1)
    Entry4 = Entry(registerScreen, textvariable=address, width=40)
    Entry4.pack(expand=1)
    Label6 = Label(registerScreen, text="Year of Graduation: ", font=("Calibri", 10))
    Label6.pack(expand=1)
    Entry5 = Entry(registerScreen, textvariable=gradYear, width=10)
    Entry5.pack(expand=1)
    Label8 = Label(registerScreen, text="Email Address: ", font=("Calibri", 10))
    Label8.pack(expand=1)
    Entry7 = Entry(registerScreen, textvariable=email, width=30)
    Entry7.pack(expand=1)
    Label9 = Label(registerScreen, text="Mobile Number: ", font=("Calibri", 10))
    Label9.pack(expand=1)
    Entry8 = Entry(registerScreen, textvariable=number)
    Entry8.pack(expand=1)
    Label10 = Label(registerScreen, text="University and career path: ", font=("Calibri", 10))
    Label10.pack(expand=1)
    Entry9 = Entry(registerScreen, textvariable=university)
    Entry9.pack(expand=1)
    Label4 = Label(registerScreen, text="Password: ", font=("Calibri", 10))
    Label4.pack(expand=1)
    Entry3 = Entry(registerScreen, textvariable=password)
    Entry3.pack(expand=1)

    Button3 = Button(registerScreen, text="Register", font=("Calibri", 15), width=10, height=1, command=register_function)
    Button3.pack(expand=1)

def login_screen():

    global loginScreen
    loginScreen = Toplevel(homeScreen)

    loginScreen.geometry("1920x1080")
    loginScreen.title("Narrabundah Alumni - Login")

    global usernameVerify
    global passwordVerify
    global usernameEntry
    global passwordEntry

    usernameVerify = StringVar()
    passwordVerify = StringVar()

    Label11 = Label(loginScreen, text="First and second name: ", font=("Calibri", 10))
    Label11.pack()
    usernameEntry = Entry(loginScreen, textvariable=usernameVerify)
    usernameEntry.pack()
    Label12 = Label(loginScreen, text="Password: ", font=("Calibri", 10))
    Label12.pack()
    passwordEntry = Entry(loginScreen, textvariable=passwordVerify)
    passwordEntry.pack()
    Button4 = Button(loginScreen, text="Login", font=("Calibri", 15), width=10, height=1, command=login_function)
    Button4.pack()

def home_screen():

    global homeScreen
    homeScreen = Tk()

    homeScreen.geometry("1000x700")
    homeScreen.title("Narrabundah Alumni - Home")
    Label1 = Label(text="Welcome to Narrabundah College Alumni System", font=("Calibri", 45))
    Label1.pack(expand=1)
    Label(text=" ").pack
    Button3 = Button(text="Login", font=("Calibri", 20), width=10, command=login_screen)
    Button3.pack(expand=1)
    Button2 = Button(text="Register", font=("Calibri", 20), width=10, command=register_screen)
    Button2.pack(expand=1)

    homeScreen.mainloop()

home_screen()




