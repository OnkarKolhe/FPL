from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import MySQLdb

root = Tk()
root.geometry("5100x4750")
root.minsize(5100, 4750)
global e1, e2, e3, tms, ID, e4, e5, e6, e7, e8, e9, e10, dt, e11, e12, e13, e14, e15, e16, e17, st, e18, e19, upm, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, pmp, e37, e38, e39, e40, e41, e42, e43, e44, e45, e46, e47, e48, e49, matches, e50, e51, e52, e53, e54


def Teams_show():
    global tms
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BD0606@com",
        database='EPL',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from team")
    r = mycursor.fetchall()
    l5 = Label(tms, text="Teams Table", font="time 20 bold",
               bg="blue", fg="white", padx=75, pady=10)
    l5.grid(row=0, column=0, columnspan=30)
    l5.place(x=1000, y=50)
    l6 = Label(tms, text="Team ID", font="time 15 bold")
    l6.grid(row=1, column=0, padx=20, pady=20)
    l6.place(x=990, y=150)
    l7 = Label(tms, text="Team Name", font="time 15 bold")
    l7.grid(row=1, column=1, padx=20, pady=20)
    l7.place(x=1200, y=150)

    num = 2
    p = 50
    for i in r:
        ID = Label(tms, text=i[0], font="time 12 bold", fg='Blue')
        ID.grid(row=num, column=0, padx=10, pady=10)
        ID.place(x=990, y=200+p)
        Name = Label(tms, text=i[1], font="time 12 bold", fg='Blue')
        Name.grid(row=num, column=1, padx=10, pady=10)
        Name.place(x=1200, y=200+p)
        p = p+50
        num = num+1


def Teams_submit():
    global e1, e2, ID
    ID = e1.get()
    Name = e2.get()
    if(ID == ''):
        messagebox.showinfo("Error", "Cannot insert!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()

            mycursor.execute("insert into team values (%s,%s)", (ID, Name))
            mydb.commit()
            messagebox.showinfo("Information", "Record Inserted!")
        except:
            messagebox.showinfo("Error", "Foriegn key violation!")


def Teams_delete():
    global e3
    deleteID = e3.get()
    if(deleteID == ''):
        messagebox.showinfo("Error", "Nothing to delete!!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("delete from team where team_id = " + deleteID)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted!")


def Teams_update():
    global e4, e5
    updateID = e4.get()
    updatedname = e5.get()

    if(updateID == '' or updatedname == ''):
        messagebox.showinfo("Error", "Wrong input!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute(
            "update team set name = %s where team_id = %s", (updatedname, updateID))
        mydb.commit()
        messagebox.showinfo("Information", "Record Updated!")


def Teams():

    global e1, e2, e3, e4, e5, tms
    tms = Tk()
    tms.geometry("5100x4750")
    tms.minsize(5100, 4750)
    button7 = Button(tms, text="Back", fg="white",
                     bg="red", font="time 15 bold")
    button7.place(x=30, y=30, width=250)
    l2 = Label(tms, text="Participating Teams", font='time 20 bold')
    l2.place(x=30, y=100)
    l3 = Label(tms, text="Team ID", font='time 20 bold')
    l3.place(x=30, y=200)
    e1 = Entry(tms, width=30, bd=3)
    e1.place(x=200, y=200)
    l4 = Label(tms, text="Team Name", font='time 20 bold')
    l4.place(x=30, y=270)
    e2 = Entry(tms, width=30, bd=3)
    e2.place(x=270, y=270)
    button12 = Button(tms, text="Submit", fg="white", bg="blue",
                      font="time 15 bold", command=Teams_submit)
    button12.place(x=30, y=340, width=250)
    button13 = Button(tms, text="Show", fg="white", bg="blue",
                      font="time 15 bold", command=Teams_show)
    button13.place(x=30, y=410, width=250)
    button14 = Button(tms, text="Delete", fg="white",
                      bg="blue", font="time 15 bold", command=Teams_delete)
    button14.place(x=30, y=480, width=250)
    e3 = Entry(tms, width=30, bd=3)
    e3.place(x=300, y=480)
    l5 = Label(tms, text="Update", font="time 20 bold")
    l5.place(x=30, y=570)
    button15 = Button(tms, text="ID", fg="white",
                      bg="blue", font="time 15 bold", command=Teams_update)
    button15.place(x=30, y=640, width=250)
    e4 = Entry(tms, width=30, bd=3)
    e4.place(x=300, y=640)
    e5 = Entry(tms, width=30, bd=3)
    e5.place(x=300, y=710)


def Details_update():
    global e25, e26, e27, e28
    pID = e25.get()
    name = e26.get()
    val = e27.get()
    pos = e28.get()

    if(pID == '' or name == '' or val == '' or pos == ''):
        messagebox.showinfo("Error", "Wrong input!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()
            mycursor.execute(
                "update player set name = %s,current_value = %s,position = %s where player_id = %s", (name, val, pos, pID))
            mydb.commit()
            messagebox.showinfo("Information", "Record Updated!")
        except:
            messagebox.showinfo("Error", "Foriegn key Violation")


def Details_show():
    global dt
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BD0606@com",
        database='EPL',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from player")
    r = mycursor.fetchall()
    l14 = Label(dt, text="Players", font="time 20 bold",
                bg="blue", fg="white", padx=75, pady=10)
    l14.grid(row=0, column=0, columnspan=30)
    l14.place(x=930, y=50)
    l15 = Label(dt, text="Player ID", font="time 15 bold")
    l15.grid(row=1, column=0, padx=20, pady=20)
    l15.place(x=700, y=150)
    l16 = Label(dt, text="Player Name", font="time 15 bold")
    l16.grid(row=1, column=1, padx=20, pady=20)
    l16.place(x=850, y=150)
    l17 = Label(dt, text="Team ID", font="time 15 bold")
    l17.grid(row=1, column=1, padx=20, pady=20)
    l17.place(x=1020, y=150)
    l18 = Label(dt, text="Value", font="time 15 bold")
    l18.grid(row=1, column=1, padx=20, pady=20)
    l18.place(x=1170, y=150)
    l19 = Label(dt, text="Position", font="time 15 bold")
    l19.grid(row=1, column=1, padx=20, pady=20)
    l19.place(x=1300, y=150)

    num = 2
    p = 50
    for i in r:
        playerID = Label(dt, text=i[0], font="time 12 bold", fg='Blue')
        playerID.grid(row=num, column=0, padx=10, pady=10)
        playerID.place(x=700, y=200+p)
        Pname = Label(dt, text=i[1], font="time 12 bold", fg='Blue')
        Pname.grid(row=num, column=1, padx=10, pady=10)
        Pname.place(x=850, y=200+p)
        tID = Label(dt, text=i[2], font="time 12 bold", fg='Blue')
        tID.grid(row=num, column=0, padx=10, pady=10)
        tID.place(x=1020, y=200+p)
        curr_v = Label(dt, text=i[3], font="time 12 bold", fg='Blue')
        curr_v.grid(row=num, column=0, padx=10, pady=10)
        curr_v.place(x=1170, y=200+p)
        pos = Label(dt, text=i[4], font="time 12 bold", fg='Blue')
        pos.grid(row=num, column=0, padx=10, pady=10)
        pos.place(x=1300, y=200+p)
        p = p+50
        num = num+1


def Details_submit():
    global e6, e7, e8, e9, e10
    playerID = e6.get()
    Pname = e7.get()
    tID = e8.get()
    curr_v = e9.get()
    pos = e10.get()
    if(playerID == '' or tID == ''):
        messagebox.showinfo("Error", "Cannot insert!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()

            mycursor.execute("insert into player values (%s,%s, %s,%s,%s)",
                             (playerID, Pname, tID, curr_v, pos))
            mydb.commit()
            messagebox.showinfo("Information", "Record Inserted!")
        except:
            messagebox.showinfo("Error", "Foriegn key violation")


def Details_delete():
    global e11
    pID = e11.get()
    if(pID == ''):
        messagebox.showinfo("Error", "Nothing to delete!!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("delete from player where player_id = " + pID)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted!")


def Details():
    global e6, e7, e8, e9, e10, e11, dt, e25, e26, e27, e28
    dt = Tk()
    dt.geometry("5100x4750")
    dt.minsize(5100, 4750)
    button9 = Button(dt, text="Back", fg="white",
                     bg="red", font="time 15 bold")
    button9.place(x=30, y=30, width=250)
    l8 = Label(dt, text=" Players' Details", font="time 20 bold")
    l8.place(x=30, y=100)
    l9 = Label(dt, text=" Player ID ", font="time 15 bold")
    l9.place(x=30, y=170)
    e6 = Entry(dt, width=30, bd=3)
    e6.place(x=210, y=170)
    l10 = Label(dt, text=" Name ", font="time 15 bold")
    l10.place(x=30, y=250)
    e7 = Entry(dt, width=30, bd=3)
    e7.place(x=210, y=250)
    l11 = Label(dt, text=" Team ID ", font="time 15 bold")
    l11.place(x=30, y=330)
    e8 = Entry(dt, width=30, bd=3)
    e8.place(x=210, y=330)
    l12 = Label(dt, text=" Current Value ", font="time 15 bold")
    l12.place(x=30, y=410)
    e9 = Entry(dt, width=30, bd=3)
    e9.place(x=210, y=410)
    l13 = Label(dt, text=" Position ", font="time 15 bold")
    l13.place(x=30, y=490)
    e10 = Entry(dt, width=30, bd=3)
    e10.place(x=210, y=490)
    button16 = Button(dt, text="Submit", fg="white", bg="blue",
                      font="time 15 bold", command=Details_submit)
    button16.place(x=30, y=570, width=250)
    button17 = Button(dt, text="Delete", fg="white", bg="blue",
                      font="time 15 bold", command=Details_delete)
    button17.place(x=30, y=650, width=250)
    e11 = Entry(dt, width=30, bd=3)
    e11.place(x=290, y=650)
    button18 = Button(dt, text="Show", fg="white", bg="blue",
                      font="time 15 bold", command=Details_show)
    button18.place(x=30, y=730, width=250)
    button26 = Button(dt, text="Update ID", fg="white", bg="blue",
                      font="time 15 bold", command=Details_update)
    button26.place(x=30, y=810, width=250)
    e25 = Entry(dt, width=30, bd=3)
    e25.place(x=290, y=810)
    l43 = Label(dt, text=" Edited Name ", font="time 15 bold")
    l43.place(x=30, y=890)
    e26 = Entry(dt, width=30, bd=3)
    e26.place(x=290, y=890)
    l44 = Label(dt, text=" Value ", font="time 15 bold")
    l44.place(x=30, y=940)
    e27 = Entry(dt, width=30, bd=3)
    e27.place(x=290, y=940)
    l45 = Label(dt, text="position ", font="time 15 bold")
    l45.place(x=30, y=990)
    e28 = Entry(dt, width=30, bd=3)
    e28.place(x=290, y=990)


def Stats_update():
    global e29, e30, e31, e32, e19
    pID = e19.get()
    goals = e29.get()
    Assists = e30.get()
    rc = e31.get()
    yc = e32.get()
    if(pID == '' or goals == '' or Assists == '' or rc == '' or yc == ''):
        messagebox.showinfo("Error", "Wrong input!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()
            mycursor.execute(
                "update player_stats set goal = %s,assist = %s,red_card = %s,yellow_card = %s where player_id = %s", (goals, Assists, rc, yc, pID))
            mydb.commit()
            messagebox.showinfo("Information", "Record Updated!")
        except:
            messagebox.showinfo("Error", "Foriegn key violation!")


def Stats_show():
    global st
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BD0606@com",
        database='EPL',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from player_stats")
    r = mycursor.fetchall()
    l27 = Label(st, text="Player Statistics", font="time 20 bold",
                bg="blue", fg="white", padx=75, pady=10)
    l27.grid(row=0, column=0, columnspan=30)
    l27.place(x=950, y=50)
    l28 = Label(st, text="Serial no.", font="time 15 bold")
    l28.grid(row=1, column=0, padx=20, pady=20)
    l28.place(x=600, y=150)
    l29 = Label(st, text="Player ID", font="time 15 bold")
    l29.grid(row=1, column=1, padx=20, pady=20)
    l29.place(x=800, y=150)
    l30 = Label(st, text="Goals", font="time 15 bold")
    l30.grid(row=1, column=1, padx=20, pady=20)
    l30.place(x=1000, y=150)
    l31 = Label(st, text="Assists", font="time 15 bold")
    l31.grid(row=1, column=1, padx=20, pady=20)
    l31.place(x=1200, y=150)
    l31 = Label(st, text="Red Cards", font="time 15 bold")
    l31.grid(row=1, column=1, padx=20, pady=20)
    l31.place(x=1400, y=150)
    l32 = Label(st, text="Yellow Cards", font="time 15 bold")
    l32.grid(row=1, column=1, padx=20, pady=20)
    l32.place(x=1600, y=150)

    num = 2
    p = 50
    for i in r:
        serialID = Label(st, text=i[0], font="time 12 bold", fg='Blue')
        serialID.grid(row=num, column=0, padx=10, pady=10)
        serialID.place(x=600, y=200+p)
        PID = Label(st, text=i[1], font="time 12 bold", fg='Blue')
        PID.grid(row=num, column=1, padx=10, pady=10)
        PID.place(x=800, y=200+p)
        goal = Label(st, text=i[2], font="time 12 bold", fg='Blue')
        goal.grid(row=num, column=0, padx=10, pady=10)
        goal.place(x=1000, y=200+p)
        Assists = Label(st, text=i[3], font="time 12 bold", fg='Blue')
        Assists.grid(row=num, column=0, padx=10, pady=10)
        Assists.place(x=1200, y=200+p)
        rc = Label(st, text=i[4], font="time 12 bold", fg='Blue')
        rc.grid(row=num, column=0, padx=10, pady=10)
        rc.place(x=1400, y=200+p)
        yc = Label(st, text=i[5], font="time 12 bold", fg='Blue')
        yc.grid(row=num, column=0, padx=10, pady=10)
        yc.place(x=1600, y=200+p)
        p = p+50
        num = num+1


def Stats_submit():
    global e12, e13, e14, e15, e16, e17, e29, e30, e31, e32
    serialID = e12.get()
    PID = e13.get()
    goal = e14.get()
    Assists = e15.get()
    rc = e16.get()
    yc = e17.get()
    if(PID == '' or serialID == ''):
        messagebox.showinfo("Error", "Cannot insert!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()

            mycursor.execute("insert into player_stats values (%s,%s, %s,%s,%s,%s)",
                             (serialID, PID, goal, Assists, rc, yc))
            mydb.commit()
            messagebox.showinfo("Information", "Record Inserted!")
        except:
            messagebox.showinfo("Error", "Foriegn key violation!")


def Stats_delete():
    global e18
    sno = e18.get()
    if(sno == ''):
        messagebox.showinfo("Error", "Nothing to delete!!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("delete from player_stats where ID = " + sno)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted!")


def Stats():
    global e12, e13, e14, e15, e16, e17, st, e18, e19, e29, e30, e31, e32
    st = Tk()
    st.geometry("5100x4750")
    st.minsize(5100, 4750)
    button8 = Button(st, text="Back", fg="white",
                     bg="red", font="time 15 bold")
    button8.place(x=30, y=30, width=250)
    l20 = Label(st, text=" Players' Statistics", font="time 20 bold")
    l20.place(x=30, y=100)
    l21 = Label(st, text=" Serial No. ", font="time 15 bold")
    l21.place(x=30, y=170)
    e12 = Entry(st, width=30, bd=3)
    e12.place(x=210, y=170)
    l22 = Label(st, text=" Player ID ", font="time 15 bold")
    l22.place(x=30, y=250)
    e13 = Entry(st, width=30, bd=3)
    e13.place(x=210, y=250)
    l23 = Label(st, text=" Goals Scored ", font="time 15 bold")
    l23.place(x=30, y=330)
    e14 = Entry(st, width=30, bd=3)
    e14.place(x=210, y=330)
    l24 = Label(st, text=" Assists ", font="time 15 bold")
    l24.place(x=30, y=410)
    e15 = Entry(st, width=30, bd=3)
    e15.place(x=210, y=410)
    l25 = Label(st, text=" Red Cards ", font="time 15 bold")
    l25.place(x=30, y=490)
    e16 = Entry(st, width=30, bd=3)
    e16.place(x=210, y=490)
    l26 = Label(st, text=" Yellow Cards ", font="time 15 bold")
    l26.place(x=30, y=570)
    e17 = Entry(st, width=30, bd=3)
    e17.place(x=210, y=570)

    button19 = Button(st, text="Submit", fg="white", bg="blue",
                      font="time 15 bold", command=Stats_submit)
    button19.place(x=30, y=650, width=250)
    button20 = Button(st, text="Delete S n.", fg="white", bg="blue",
                      font="time 15 bold", command=Stats_delete)
    button20.place(x=30, y=730, width=250)
    e18 = Entry(st, width=30, bd=3)
    e18.place(x=290, y=730)
    button21 = Button(st, text="Show", fg="white", bg="blue",
                      font="time 15 bold", command=Stats_show)
    button21.place(x=30, y=810, width=250)
    button22 = Button(st, text="Update ID", fg="white", bg="blue",
                      font="time 15 bold", command=Stats_update)
    button22.place(x=30, y=890, width=250)
    e19 = Entry(st, width=30, bd=3)
    e19.place(x=290, y=890)
    l46 = Label(st, text=" Goals ", font="time 10 bold")
    l46.place(x=30, y=940)
    l47 = Label(st, text=" Assists ", font="time 10 bold")
    l47.place(x=100, y=940)
    l48 = Label(st, text=" RedCards ", font="time 10 bold")
    l48.place(x=200, y=940)
    l48 = Label(st, text=" YellowCards ", font="time 10 bold")
    l48.place(x=300, y=940)
    e29 = Entry(st, width=5, bd=3)
    e29.place(x=30, y=980)
    e30 = Entry(st, width=8, bd=3)
    e30.place(x=100, y=980)
    e31 = Entry(st, width=10, bd=3)
    e31.place(x=200, y=980)
    e32 = Entry(st, width=10, bd=3)
    e32.place(x=300, y=980)


def UpMatch_update():
    global e33, e34, e35, e36
    matchID = e33.get()
    t1ID = e34.get()
    t2ID = e35.get()
    week = e36.get()
    if(t1ID == '' or t2ID == '' or week == ''):
        messagebox.showinfo("Error", "Wrong input!")
    else:
        try:
        	mydb = mysql.connector.connect(
        	        host="localhost",
        	        user="root",
        	        password="BD0606@com",
        		database='EPL',
                	auth_plugin='mysql_native_password')

       		mycursor = mydb.cursor()
        	mycursor.execute(
            	"update fixture set team1_id = %s,team2_id = %s,week = %s where f_id = %s", (t1ID, t2ID, week, matchID))
        	mydb.commit()

        	messagebox.showinfo("Information", "Record Updated!")
        except:
            	messagebox.showinfo("Error", "Foriegn key violation!")


def UpMatch_delete():
    global e24
    matchID = e24.get()
    if(matchID == ''):
        messagebox.showinfo("Error", "Nothing to delete!!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("delete from fixture where f_id = " + matchID)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted!")


def UpMatch_show():
    global upm
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BD0606@com",
        database='EPL',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from fixture")
    r = mycursor.fetchall()
    l38 = Label(upm, text="Fixtures", font="time 20 bold",
                bg="blue", fg="white", padx=75, pady=10)
    l38.grid(row=0, column=0, columnspan=30)
    l38.place(x=950, y=50)
    l39 = Label(upm, text="Match ID", font="time 15 bold")
    l39.grid(row=1, column=0, padx=20, pady=20)
    l39.place(x=700, y=150)
    l40 = Label(upm, text="Team1 ID", font="time 15 bold")
    l40.grid(row=1, column=1, padx=20, pady=20)
    l40.place(x=900, y=150)
    l41 = Label(upm, text="Team2 ID", font="time 15 bold")
    l41.grid(row=1, column=1, padx=20, pady=20)
    l41.place(x=1100, y=150)
    l42 = Label(upm, text="Week No.", font="time 15 bold")
    l42.grid(row=1, column=1, padx=20, pady=20)
    l42.place(x=1300, y=150)

    num = 2
    p = 50
    for i in r:
        matchID = Label(upm, text=i[0], font="time 12 bold", fg='Blue')
        matchID.grid(row=num, column=0, padx=10, pady=10)
        matchID.place(x=700, y=200+p)
        t1ID = Label(upm, text=i[1], font="time 12 bold", fg='Blue')
        t1ID.grid(row=num, column=1, padx=10, pady=10)
        t1ID.place(x=900, y=200+p)
        t2ID = Label(upm, text=i[2], font="time 12 bold", fg='Blue')
        t2ID.grid(row=num, column=0, padx=10, pady=10)
        t2ID.place(x=1100, y=200+p)
        week = Label(upm, text=i[3], font="time 12 bold", fg='Blue')
        week.grid(row=num, column=0, padx=10, pady=10)
        week.place(x=1300, y=200+p)

        p = p+50
        num = num+1


def UpMatch_submit():
    global e20, e21, e22, e23
    matchID = e20.get()
    t1ID = e21.get()
    t2ID = e22.get()
    week = e23.get()
    if(t1ID == '' or t2ID == ''or matchID == ''):
        messagebox.showinfo("Error", "Cannot insert!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()

            mycursor.execute("insert into fixture values (%s,%s,%s,%s)",
                             (matchID, t1ID, t2ID, week))
            mydb.commit()
            messagebox.showinfo("Information", "Record Inserted!")
        except:
            messagebox.showinfo("Error", "Foriegn key Violation")


def UpMatch():
    global upm, e20, e21, e22, e23, e24, e33, e34, e35, e36
    upm = Tk()
    upm.geometry("5100x4750")
    upm.minsize(5100, 4750)
    button10 = Button(upm, text="Back", fg="white",
                      bg="red", font="time 15 bold")
    button10.place(x=30, y=30, width=250)
    l33 = Label(upm, text="Upcoming Matches", font="time 20 bold")
    l33.place(x=30, y=100)
    l34 = Label(upm, text=" Match ID ", font="time 15 bold")
    l34.place(x=30, y=170)
    e20 = Entry(upm, width=30, bd=3)
    e20.place(x=210, y=170)
    l35 = Label(upm, text=" Team1 ID", font="time 15 bold")
    l35.place(x=30, y=250)
    e21 = Entry(upm, width=30, bd=3)
    e21.place(x=210, y=250)
    l36 = Label(upm, text=" Team2 ID ", font="time 15 bold")
    l36.place(x=30, y=330)
    e22 = Entry(upm, width=30, bd=3)
    e22.place(x=210, y=330)
    l37 = Label(upm, text=" Week ", font="time 15 bold")
    l37.place(x=30, y=410)
    e23 = Entry(upm, width=30, bd=3)
    e23.place(x=210, y=410)
    button23 = Button(upm, text="Submit", fg="white", bg="blue",
                      font="time 15 bold", command=UpMatch_submit)
    button23.place(x=30, y=490, width=250)
    button24 = Button(upm, text="Show", fg="white", bg="blue",
                      font="time 15 bold", command=UpMatch_show)
    button24.place(x=30, y=570, width=250)
    button25 = Button(upm, text="Delete", fg="white", bg="blue",
                      font="time 15 bold", command=UpMatch_delete)
    button25.place(x=30, y=650, width=250)
    e24 = Entry(upm, width=30, bd=3)
    e24.place(x=290, y=650)
    button27 = Button(upm, text="Update", fg="white", bg="blue",
                      font="time 15 bold", command=UpMatch_update)
    button27.place(x=30, y=730, width=250)
    e33 = Entry(upm, width=30, bd=3)
    e33.place(x=290, y=730)
    l49 = Label(upm, text=" Team1 ID ", font="time 15 bold")
    l49.place(x=30, y=810)
    l50 = Label(upm, text=" Team2 ID ", font="time 15 bold")
    l50.place(x=30, y=870)
    l51 = Label(upm, text=" Week ", font="time 15 bold")
    l51.place(x=30, y=930)
    e34 = Entry(upm, width=20, bd=3)
    e34.place(x=290, y=810)
    e35 = Entry(upm, width=20, bd=3)
    e35.place(x=290, y=870)
    e36 = Entry(upm, width=20, bd=3)
    e36.place(x=290, y=930)


def PMP_update():
    global e42, e43, e44, e45
    serialno = e42.get()
    points = e43.get()
    pID = e44.get()
    matchID = e45.get()
    if(serialno == '' or points == '' or pID == '' or matchID == ''):
        messagebox.showinfo("Error", "Wrong input!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()
            mycursor.execute("update player_match_point set point = %s,player_id = %s,match_id = %s where p_id = %s",
                             (points, pID, matchID, serialno))
            mydb.commit()
            messagebox.showinfo("Information", "Record Updated!")
        except:
            messagebox.showinfo("Error", "Foreign key violation!")


def PMP_delete():
    global e41
    serialno = e41.get()
    if(serialno == ''):
        messagebox.showinfo("Error", "Nothing to delete!!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute(
            "delete from player_match_point where p_id = " + serialno)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted!")


def PMP_submit():
    global pmp, e37, e38, e39, e40
    serialno = e37.get()
    points = e38.get()
    pID = e39.get()
    mID = e40.get()
    if(pID == ''or mID == '' or serialno == ''):
        messagebox.showinfo("Error", "Cannot insert!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()

            mycursor.execute(
                "insert into player_match_point values (%s,%s,%s,%s)", (serialno, points, pID, mID))
            mydb.commit()
            messagebox.showinfo("Information", "Record Inserted!")
        except:
            messagebox.showinfo("Error", "Foriegn key violation! ")


def PMP_show():
    global pmp
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BD0606@com",
        database='EPL',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from player_match_point")
    r = mycursor.fetchall()
    l60 = Label(pmp, text="Player Match Points", font="time 20 bold",
                bg="blue", fg="white", padx=75, pady=10)
    l60.grid(row=0, column=0, columnspan=30)
    l60.place(x=950, y=50)
    l61 = Label(pmp, text="Serial No", font="time 15 bold")
    l61.grid(row=1, column=0, padx=20, pady=20)
    l61.place(x=800, y=150)
    l62 = Label(pmp, text="Points", font="time 15 bold")
    l62.grid(row=1, column=1, padx=20, pady=20)
    l62.place(x=1000, y=150)
    l63 = Label(pmp, text="Player ID", font="time 15 bold")
    l63.grid(row=1, column=1, padx=20, pady=20)
    l63.place(x=1200, y=150)
    l64 = Label(pmp, text="Match ID", font="time 15 bold")
    l64.grid(row=1, column=1, padx=20, pady=20)
    l64.place(x=1400, y=150)

    num = 2
    p = 50
    for i in r:
        serialNo = Label(pmp, text=i[0], font="time 12 bold", fg='Blue')
        serialNo.grid(row=num, column=0, padx=10, pady=10)
        serialNo.place(x=800, y=200+p)
        points = Label(pmp, text=i[1], font="time 12 bold", fg='Blue')
        points.grid(row=num, column=1, padx=10, pady=10)
        points.place(x=1000, y=200+p)
        pID = Label(pmp, text=i[2], font="time 12 bold", fg='Blue')
        pID.grid(row=num, column=0, padx=10, pady=10)
        pID.place(x=1200, y=200+p)
        matchID = Label(pmp, text=i[3], font="time 12 bold", fg='Blue')
        matchID.grid(row=num, column=0, padx=10, pady=10)
        matchID.place(x=1400, y=200+p)

        p = p+50
        num = num+1


def PMP():
    global pmp, e37, e38, e39, e40, e41, e42, e43, e44, e45
    pmp = Tk()
    pmp.geometry("5100x4750")
    pmp.minsize(5100, 4750)
    button11 = Button(pmp, text="Back", fg="white",
                      bg="red", font="time 15 bold")
    button11.place(x=30, y=30, width=250)
    l52 = Label(pmp, text="Player Match Points", font="time 20 bold")
    l52.place(x=30, y=100)
    l53 = Label(pmp, text=" Serial no. ", font="time 15 bold")
    l53.place(x=30, y=170)
    e37 = Entry(pmp, width=30, bd=3)
    e37.place(x=210, y=170)
    l54 = Label(pmp, text=" Points ", font="time 15 bold")
    l54.place(x=30, y=250)
    e38 = Entry(pmp, width=30, bd=3)
    e38.place(x=210, y=250)
    l55 = Label(pmp, text=" Player ID ", font="time 15 bold")
    l55.place(x=30, y=330)
    e39 = Entry(pmp, width=30, bd=3)
    e39.place(x=210, y=330)
    l56 = Label(pmp, text=" Match ID ", font="time 15 bold")
    l56.place(x=30, y=410)
    e40 = Entry(pmp, width=30, bd=3)
    e40.place(x=210, y=410)
    button28 = Button(pmp, text="Submit", fg="white", bg="blue",
                      font="time 15 bold", command=PMP_submit)
    button28.place(x=30, y=490, width=250)
    button29 = Button(pmp, text="Show", fg="white", bg="blue",
                      font="time 15 bold", command=PMP_show)
    button29.place(x=30, y=570, width=250)
    button30 = Button(pmp, text="Delete", fg="white", bg="blue",
                      font="time 15 bold", command=PMP_delete)
    button30.place(x=30, y=650, width=250)
    e41 = Entry(pmp, width=30, bd=3)
    e41.place(x=290, y=650)
    button31 = Button(pmp, text="Update", fg="white", bg="blue",
                      font="time 15 bold", command=PMP_update)
    button31.place(x=30, y=730, width=250)
    e42 = Entry(pmp, width=30, bd=3)
    e42.place(x=290, y=730)
    l57 = Label(pmp, text=" Points ", font="time 15 bold")
    l57.place(x=30, y=810)
    l58 = Label(pmp, text=" Player ID ", font="time 15 bold")
    l58.place(x=30, y=870)
    l59 = Label(pmp, text=" Match ID ", font="time 15 bold")
    l59.place(x=30, y=930)
    e43 = Entry(pmp, width=20, bd=3)
    e43.place(x=290, y=810)
    e44 = Entry(pmp, width=20, bd=3)
    e44.place(x=290, y=870)
    e45 = Entry(pmp, width=20, bd=3)
    e45.place(x=290, y=930)


def Matches_update():
    global e50, e51, e52, e53
    matchID = e50.get()
    t1ID = e51.get()
    t2ID = e52.get()
    week = e53.get()
    if(t1ID == '' or t2ID == '' or week == ''):
        messagebox.showinfo("Error", "Wrong input!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()
            mycursor.execute(
                "update matches set team1_id = %s,team2_id = %s,week = %s where match_id = %s", (t1ID, t2ID, week, matchID))
            mydb.commit()
            messagebox.showinfo("Information", "Record Updated!")
        except:
            messagebox.showinfo("Error", "Foriegn key Violation!")


def Matches_delete():
    global e54
    matchID = e54.get()
    if(matchID == ''):
        messagebox.showinfo("Error", "Nothing to delete!!")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="BD0606@com",
            database='EPL',
            auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        mycursor.execute("delete from matches where match_id = " + matchID)
        mydb.commit()
        messagebox.showinfo("Information", "Record Deleted!")


def Matches_show():

    global matches
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BD0606@com",
        database='EPL',
        auth_plugin='mysql_native_password'
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from matches")
    r = mycursor.fetchall()
    l73 = Label(matches, text="Past Matches", font="time 20 bold",
                bg="blue", fg="white", padx=75, pady=10)
    l73.grid(row=0, column=0, columnspan=30)
    l73.place(x=950, y=50)
    l74 = Label(matches, text="Match ID", font="time 15 bold")
    l74.grid(row=1, column=0, padx=20, pady=20)
    l74.place(x=700, y=150)
    l75 = Label(matches, text="Team1 ID", font="time 15 bold")
    l75.grid(row=1, column=1, padx=20, pady=20)
    l75.place(x=900, y=150)
    l76 = Label(matches, text="Team2 ID", font="time 15 bold")
    l76.grid(row=1, column=1, padx=20, pady=20)
    l76.place(x=1100, y=150)
    l77 = Label(matches, text="Week No.", font="time 15 bold")
    l77.grid(row=1, column=1, padx=20, pady=20)
    l77.place(x=1300, y=150)

    num = 2
    p = 50
    for i in r:
        matchID = Label(matches, text=i[0], font="time 12 bold", fg='Blue')
        matchID.grid(row=num, column=0, padx=10, pady=10)
        matchID.place(x=700, y=200+p)
        t1ID = Label(matches, text=i[1], font="time 12 bold", fg='Blue')
        t1ID.grid(row=num, column=1, padx=10, pady=10)
        t1ID.place(x=900, y=200+p)
        t2ID = Label(matches, text=i[2], font="time 12 bold", fg='Blue')
        t2ID.grid(row=num, column=0, padx=10, pady=10)
        t2ID.place(x=1100, y=200+p)
        week = Label(matches, text=i[3], font="time 12 bold", fg='Blue')
        week.grid(row=num, column=0, padx=10, pady=10)
        week.place(x=1300, y=200+p)

        p = p+50
        num = num+1


def Matches_submit():
    global e46, e47, e48, e49
    matchID = e46.get()
    t1ID = e47.get()
    t2ID = e48.get()
    week = e49.get()
    if(t1ID == '' or t2ID == '' or matchID == ''):
        messagebox.showinfo("Error", "Cannot insert!")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="BD0606@com",
                database='EPL',
                auth_plugin='mysql_native_password'
            )

            mycursor = mydb.cursor()

            mycursor.execute("insert into matches values (%s,%s,%s,%s)",
                             (matchID, t1ID, t2ID, week))
            mydb.commit()
            messagebox.showinfo("Information", "Record Inserted!")
        except:
            messagebox.showinfo("Error", "Foriegn key Violation!")


def Matches():
    global e46, e47, e48, e49, e50, e51, e52, e53, e54, matches
    matches = Tk()
    matches.geometry("5100x4750")
    matches.minsize(5100, 4750)
    button11 = Button(matches, text="Back", fg="white",
                      bg="red", font="time 15 bold")
    button11.place(x=30, y=30, width=250)
    l65 = Label(matches, text="Past Matches", font="time 20 bold")
    l65.place(x=30, y=100)
    l66 = Label(matches, text=" Match ID ", font="time 15 bold")
    l66.place(x=30, y=170)
    e46 = Entry(matches, width=30, bd=3)
    e46.place(x=210, y=170)
    l67 = Label(matches, text=" Team1 ID ", font="time 15 bold")
    l67.place(x=30, y=250)
    e47 = Entry(matches, width=30, bd=3)
    e47.place(x=210, y=250)
    l68 = Label(matches, text=" Team2 ID ", font="time 15 bold")
    l68.place(x=30, y=330)
    e48 = Entry(matches, width=30, bd=3)
    e48.place(x=210, y=330)
    l69 = Label(matches, text=" Week No", font="time 15 bold")
    l69.place(x=30, y=410)
    e49 = Entry(matches, width=30, bd=3)
    e49.place(x=210, y=410)
    button32 = Button(matches, text="Submit", fg="white", bg="blue",
                      font="time 15 bold", command=Matches_submit)
    button32.place(x=30, y=490, width=250)
    button33 = Button(matches, text="Show", fg="white", bg="blue",
                      font="time 15 bold", command=Matches_show)
    button33.place(x=30, y=570, width=250)
    button34 = Button(matches, text="Delete", fg="white", bg="blue",
                      font="time 15 bold", command=Matches_delete)
    button34.place(x=30, y=650, width=250)
    e54 = Entry(matches, width=30, bd=3)
    e54.place(x=290, y=650)
    button35 = Button(matches, text="Update", fg="white", bg="blue",
                      font="time 15 bold", command=Matches_update)
    button35.place(x=30, y=730, width=250)
    e50 = Entry(matches, width=30, bd=3)
    e50.place(x=290, y=730)
    l70 = Label(matches, text=" Team1 ID ", font="time 15 bold")
    l70.place(x=30, y=810)
    l71 = Label(matches, text=" Team2 ID ", font="time 15 bold")
    l71.place(x=30, y=870)
    l72 = Label(matches, text=" Week ", font="time 15 bold")
    l72.place(x=30, y=930)
    e51 = Entry(matches, width=20, bd=3)
    e51.place(x=290, y=810)
    e52 = Entry(matches, width=20, bd=3)
    e52.place(x=290, y=870)
    e53 = Entry(matches, width=20, bd=3)
    e53.place(x=290, y=930)


img = Image.open("p1.jpg")
img = img.resize((500, 350))
my = ImageTk.PhotoImage(img)
label = Label(root, image=my)
label.place(x=700, y=10)

img1 = Image.open("p2.jpg")
img1 = img1.resize((300, 400))
my1 = ImageTk.PhotoImage(img1)
label1 = Label(root, image=my1)
label1.place(x=50, y=20)

img2 = Image.open("p3.jpg")
img2 = img2.resize((300, 400))
my2 = ImageTk.PhotoImage(img2)
label2 = Label(root, image=my2)
label2.place(x=1500, y=600)

l1 = Label(root, text="Fantasy Premier League 2020", font='time 20 bold')
l1.place(x=730, y=400)

button = Button(root, text="Participating Teams", fg="white",
                bg="blue", font="time 15 bold", command=Teams)
button.place(x=800, y=500, width=300)

button2 = Button(root, text="Players Statistics", fg="white",
                 bg="blue", font="time 15 bold", command=Stats)
button2.place(x=800, y=550, width=300)

button3 = Button(root, text="Player Details", fg="white",
                 bg="blue", font="time 15 bold", command=Details)
button3.place(x=800, y=600, width=300)

button4 = Button(root, text="Upcoming Matches", fg="white",
                 bg="blue", font="time 15 bold", command=UpMatch)
button4.place(x=800, y=650, width=300)

button5 = Button(root, text="Player Match Points", fg="white",
                 bg="blue", font="time 15 bold", command=PMP)
button5.place(x=800, y=700, width=300)

button6 = Button(root, text="Past Matches", fg="white",
                 bg="blue", font="time 15 bold", command=Matches)
button6.place(x=800, y=750, width=300)


button6 = Button(root, text="Exit", fg="white", bg="red",
                 font="time 15 bold", command=root.quit)
button6.place(x=800, y=850, width=300)

root.mainloop()
