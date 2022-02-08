
from optparse import Values
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
import mysql.connector
import sys


class pharmacy_management:
    def __init__(self, root):
        self.root = root
        self.root.title("PharmDesk - Pharmacy Management System")
        self.root.geometry("1550x900+0+0")
        self.root.iconbitmap('icon.ico')

        ###########Add med variables###########
        self.addmed_var = StringVar()
        self.refMed_var = StringVar()
        ##############main text variables #########################
        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.medName_var = StringVar()
        self.typeMed_var = StringVar()
        self.lot_var = StringVar()
        self.expdate_var = StringVar()
        self.issuedate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.qty_var = StringVar()

        # background 009D3D
        background = Image.open('bg.png')
        background = background.resize((1550, 900), Image.ANTIALIAS)
        self.ph_bg = ImageTk.PhotoImage(background)
        label_bg = Label(self.root, image=self.ph_bg)
        label_bg.place(x=0, y=0, width=1550, height=900)
##########Dataframe#############
        Dataframe = Frame(self.root, bd=0, relief=RIDGE,
                          padx=20, pady=20, bg="#333333")
        Dataframe.place(x=10, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=2, relief=RIDGE, padx=20, pady=20,
                                   text="Medicine Information", fg="white", bg="#333333", font=("Trebuchet MS", 18, "bold"))
        DataframeLeft.place(x=0, y=5, width=870, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=2, relief=RIDGE, padx=20, pady=20,
                                    text="Medicine Add Department", fg="white", bg="#333333", font=("Trebuchet MS", 18, "bold"))
        DataframeRight.place(x=880, y=5, width=610, height=350)
#############Button Frame############################
        Buttonframe = Frame(self.root, bd=0, relief=RIDGE,
                            padx=20, pady=20, bg="#333333")
        Buttonframe.place(x=10, y=530, width=1530, height=80)

##########Main Button################################
        btnAddData = Button(Buttonframe, text=" + Add Medicine", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white", command=self.Add_data)
        btnAddData.grid(padx=5, row=0, column=0)

        btnUpdateData = Button(Buttonframe, text=" Update", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white", width=9, command=self.Update)
        btnUpdateData.grid(padx=5, row=0, column=1)

        btnDeleteData = Button(Buttonframe, text="Delete", font=(
            "Trebuchet MS", 14, "bold"), bg="#C1272D", fg="white", width=9, command=self.Delete)
        btnDeleteData.grid(padx=5, row=0, column=4)

        btnResetData = Button(Buttonframe, text="Reset", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white", width=9, command=self.Reset)
        btnResetData.grid(padx=5, row=0, column=2)

        btnExitData = Button(Buttonframe, text="Exit", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white", width=9,command=sys.exit)
        btnExitData.grid(padx=5, row=0, column=10)
############# Search By########################
        lablSearch = Label(Buttonframe, text="Search By", bg="#333333",
                           fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablSearch.grid(padx=5, row=0, column=5, sticky=W)

        # search_var_comboiable
        self.search_var_combo = StringVar()
        search_combo = ttk.Combobox(Buttonframe, textvariable=self.search_var_combo, text="Search", width=12, font=(
            "Trebuchet MS", 12), state="readonly")
        search_combo["values"] = ("Ref_no", "MedName", "LotNo")
        search_combo.grid(padx=2, row=0, column=6, sticky=W)
        search_combo.current(0)

        # textvariable for search entry
        self.search_box_var = StringVar()
        txtSearch = Entry(Buttonframe, relief=RIDGE, textvariable=self.search_box_var,
                          width=20, font=("Trebuchet MS", 14))
        txtSearch.grid(padx=2, row=0, column=7)

        searchBtn = Button(Buttonframe, command=self.Search_data, text="Search", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white", width=9)
        searchBtn.grid(padx=5, row=0, column=8)

        showAllBtn = Button(Buttonframe,command = self.fetch_data ,text="Show All", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white")
        showAllBtn.grid(padx=5, row=0, column=9)
############################## LAbels & Entry ########################

##########Dataframe Left###############################################

# referemce no

        lablref = Label(DataframeLeft, text="Reference No.", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        lablref.grid(padx=10, row=0, column=0, sticky=W)

        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        my_cursor.execute("select Ref from pharma")
        ref_row = my_cursor.fetchall()

        ref_combo = ttk.Combobox(DataframeLeft, textvariable=self.ref_var, width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        ref_combo["values"] = ref_row
        ref_combo.grid(padx=2, row=0, column=1, sticky=W)
        ref_combo.current(0)
# Company
        lablcompany = Label(DataframeLeft, text="Select Company", bg="#333333",
                            fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        lablcompany.grid(padx=10, row=1, column=0, sticky=W)

        company_combo = ttk.Combobox(DataframeLeft, textvariable=self.cmpName_var, width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        company_combo["values"] = ("Select Company", "Sun Pharma", "Cipla", "Dr. Reddy's",
                                   "Biocon", "Torrent", "Lupin", "Glenmark", "Mankind", "Priamal")
        company_combo.grid(padx=2, row=1, column=1, sticky=W)
        company_combo.current(0)
# Type
        labltype = Label(DataframeLeft, text="Medicine Type", bg="#333333",
                         fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        labltype.grid(padx=10, row=2, column=0, sticky=W)

        type_combo = ttk.Combobox(DataframeLeft, textvariable=self.typeMed_var, width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        type_combo["values"] = ("Select Type", "Tablet",
                                "Syrup", "Liquid", "Inhaler", "Injection")
        type_combo.grid(padx=2, row=2, column=1, sticky=W)
        type_combo.current(0)
# med name
        lablmedname = Label(DataframeLeft, text="Medicine Name.", bg="#333333",
                            fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        lablmedname.grid(padx=10, row=3, column=0, sticky=W)

        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        my_cursor.execute("select MedName from pharma")
        med_row = my_cursor.fetchall()

        medname_combo = ttk.Combobox(DataframeLeft, textvariable=self.medName_var, width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        medname_combo["values"] = med_row
        medname_combo.grid(padx=2, row=3, column=1, sticky=W)
        medname_combo.current(0)
# lot no
        labllot = Label(DataframeLeft, text="Lot No.", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        labllot.grid(padx=10, row=4, column=0, sticky=W)

        txtlot = Entry(DataframeLeft, textvariable=self.lot_var, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtlot.grid(padx=2, pady=6, row=4, column=1)
# exp date
        lablexp = Label(DataframeLeft, text="Exp Date", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablexp.grid(padx=10, row=5, column=0, sticky=W)

        txtexp = Entry(DataframeLeft, textvariable=self.expdate_var, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtexp.grid(padx=2, pady=6, row=5, column=1)
# issue date
        lablissue = Label(DataframeLeft, text="Issue Date", bg="#333333",
                          fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablissue.grid(padx=10, row=6, column=0, sticky=W)

        txtissue = Entry(DataframeLeft, relief=RIDGE, textvariable=self.issuedate_var,
                         width=26, font=("Trebuchet MS", 14))
        txtissue.grid(padx=2, pady=6, row=6, column=1)
# uses
        labluses = Label(DataframeLeft, text="Uses", bg="#333333",
                         fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        labluses.grid(padx=10, row=0, column=3, sticky=W)

        txtuses = Entry(DataframeLeft, textvariable=self.uses_var, relief=RIDGE,
                        width=26, font=("Trebuchet MS", 14))
        txtuses.grid(padx=2, pady=6, row=0, column=4)
# side_effects
        lablSideEffect = Label(DataframeLeft, text="Side Effects", bg="#333333",
                               fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablSideEffect.grid(padx=10, row=1, column=3, sticky=W)

        txtSideEffect = Entry(DataframeLeft, textvariable=self.sideEffect_var, relief=RIDGE,
                              width=26, font=("Trebuchet MS", 14))
        txtSideEffect.grid(padx=2, pady=6, row=1, column=4)
# dosage
        lablDosage = Label(DataframeLeft, text="Dosage", bg="#333333",
                           fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablDosage.grid(padx=10, row=2, column=3, sticky=W)

        txtDosage = Entry(DataframeLeft, textvariable=self.dosage_var, relief=RIDGE,
                          width=26, font=("Trebuchet MS", 14))
        txtDosage.grid(padx=2, pady=6, row=2, column=4)
# Price
        lablPrice = Label(DataframeLeft, text="Price", bg="#333333",
                          fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablPrice.grid(padx=10, row=4, column=3, sticky=W)

        txtPrice = Entry(DataframeLeft, textvariable=self.price_var, relief=RIDGE,
                         width=26, font=("Trebuchet MS", 14))
        txtPrice.grid(padx=2, pady=6, row=4, column=4)
# Quantity
        lablQty = Label(DataframeLeft, text="Quantity", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablQty.grid(padx=10, row=3, column=3, sticky=W)

        txtQty = Entry(DataframeLeft, textvariable=self.qty_var, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtQty.grid(padx=2, pady=6, row=3, column=4)


##########Dataframe Right###############################################

        # entry frame
        entry_frame = Frame(DataframeRight, width=610,
                            bg="#333333", height=200)
        entry_frame.place(x=10, y=10)

    # ref no
        lablrefno = Label(entry_frame, text="Ref No.", bg="#333333",
                          fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablrefno.grid(padx=10, row=0, column=0)

        txtrefno = Entry(entry_frame, textvariable=self.refMed_var, relief=RIDGE,
                         width=26, font=("Trebuchet MS", 14))
        txtrefno.grid(padx=2, pady=6, row=0, column=1)
    # med name
        lablmedName = Label(entry_frame, text="Medicine Name", bg="#333333",
                            fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablmedName.grid(padx=10, row=1, column=0)

        txtmedName = Entry(entry_frame, textvariable=self.addmed_var, relief=RIDGE,
                           width=26, font=("Trebuchet MS", 14))
        txtmedName.grid(padx=2, pady=6, row=1, column=1)
        ########side Frame################################
        side_frame = Frame(DataframeRight, bd=0, relief=RIDGE, bg="white")
        side_frame.place(x=20, y=100, width=420, height=180)

        scrollSide_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        scrollSide_x.pack(side=BOTTOM, fill=X)
        scrollSide_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        scrollSide_y.pack(side=RIGHT, fill=Y)

        self.med_table = ttk.Treeview(side_frame, column=(
            "ref", "medname"), xscrollcommand=scrollSide_x.set, yscrollcommand=scrollSide_y.set)

        scrollSide_x.config(command=self.med_table.xview)
        scrollSide_y.config(command=self.med_table.yview)

        self.med_table.heading("ref", text="Reference No")
        self.med_table.heading("medname", text="Medicine Name")

        self.med_table["show"] = "headings"
        self.med_table.pack(fill=BOTH, expand=1)
        self.med_table.column("ref", width=100)
        self.med_table.column("medname", width=100)

        self.med_table.bind("<ButtonRelease-1>", self.Medget_cursor)
        ###########med add button################################
        bt_frame = Frame(DataframeRight, bd=0, relief=RIDGE, bg="#333333")
        bt_frame.place(x=450, y=100, width=120, height=180)

        addMedBtn = Button(bt_frame, text="+ Add", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white", width=9, command=self.AddMed)
        addMedBtn.grid(padx=10, pady=1, row=0, column=0)

        updateMedBtn = Button(bt_frame, text="Update", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white", width=9, command=self.updateMed)
        updateMedBtn.grid(padx=10, pady=1, row=1, column=0)

        deleteMedBtn = Button(bt_frame, text="Delete", font=(
            "Trebuchet MS", 14, "bold"), bg="#C1272D", fg="white", width=9, command=self.deleteMed)
        deleteMedBtn.grid(padx=10, pady=1, row=3, column=0)

        clrMedBtn = Button(bt_frame, text="Clear", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white", width=9, command=self.clr_Med)
        clrMedBtn.grid(padx=10, pady=1, row=2, column=0)

#########################Frame Details############################

        frameDetail = Frame(self.root, bd=0, relief=RIDGE, bg="#333333")
        frameDetail.place(x=10, y=620, width=1530, height=270)
################Main Table Frame#################

        frameTablemain = Frame(frameDetail, bd=0, relief=RIDGE, bg="#333333")
        frameTablemain.place(x=0, y=1, width=1530, height=260)

        scrollTable_x = ttk.Scrollbar(frameTablemain, orient=HORIZONTAL)
        scrollTable_x.pack(side=BOTTOM, fill=X)
        scrollTable_y = ttk.Scrollbar(frameTablemain, orient=VERTICAL)
        scrollTable_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(frameTablemain, column=("ref", "companyname", "medname", "type", "lotno", "expdate",
                                           "uses", "sideeffects", "dosage", "price", "qty", "issuedate",), xscrollcommand=scrollTable_x.set, yscrollcommand=scrollTable_y.set)
        scrollTable_x.pack(side=BOTTOM, fill=X)
        scrollTable_y.pack(side=RIGHT, fill=Y)
        scrollTable_x.config(command=self.pharmacy_table.xview)
        scrollTable_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("ref", text="Reference No.")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("medname", text="Medicine Name")
        self.pharmacy_table.heading("type", text="Medicine Type")
        self.pharmacy_table.heading("lotno", text="Lot No.")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffects", text="Side Effect")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("qty", text="Quantity")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.col_list = ["ref", "companyname", "medname", "type", "lotno",
                         "expdate", "uses", "sideeffects", "dosage", "price", "qty", "issuedate"]

        for i in self.col_list:
            self.pharmacy_table.column(i, width=100)
        self.fetch_data()
        self.fetch_dataMed()
        # self.get_cursor()
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)
############Add Medicine Functionality Declaration######

    def AddMed(self):
        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)", (
            self.refMed_var.get(), self.addmed_var.get()))
        connect.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        connect.close()
        messagebox.showinfo("Success", "Medicine Added Successfully!")

    def fetch_dataMed(self):
        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.med_table.delete(*self.med_table.get_children())
            for i in rows:
                self.med_table.insert("", END, values=i)
                connect.commit()
        connect.close()

################med get cursor##############

    def Medget_cursor(self, event=''):
        cursor_row = self.med_table.focus()
        content = self.med_table.item(cursor_row)
        row_med = content['values']
        self.refMed_var.set(row_med[0])
        self.addmed_var.set(row_med[1])

    def updateMed(self):
        if self.refMed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are Required!")
        else:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="Hkumar@454", database="pharma_management")
            my_cursor = connect.cursor()
            my_cursor.execute("update pharma set MedName = %s where Ref=%s", (
                self.addmed_var.get(), self.refMed_var.get()
            ))
            connect.commit()
            self.fetch_dataMed()
            connect.close()
            messagebox.showinfo("Success", "Medicine Updated")

    def deleteMed(self):
        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        sql = "delete from pharma where Ref=%s"
        val = (self.refMed_var.get(),)
        my_cursor.execute(sql, val)
        connect.commit()
        self.fetch_dataMed()
        connect.close()
        messagebox.showinfo("Success", "Medicine Deleted!!!")

    def clr_Med(self):
        self.refMed_var.set("")
        self.addmed_var.set("")


###################Main Table #####################################


    def Add_data(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are Required")

        else:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="Hkumar@454", database="pharma_management")
            my_cursor = connect.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.ref_var.get(),
                self.cmpName_var.get(),
                self.medName_var.get(),
                self.typeMed_var.get(),
                self.lot_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.qty_var.get(),
                self.issuedate_var.get()
            ))

            connect.commit()
            self.fetch_data()
            connect.close()
            messagebox.showinfo("Success", "Data has been Inserted")

    def fetch_data(self):
        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        my_cursor.execute("select * from pharmacy")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, values=i)
            connect.commit()
        connect.close()

    def get_cursor(self, event=''):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row_med = content['values']

        self.ref_var.set(row_med[0])
        self.cmpName_var.set(row_med[1])
        self.medName_var.set(row_med[2])
        self.typeMed_var.set(row_med[3])
        self.lot_var.set(row_med[4])
        self.expdate_var.set(row_med[5])
        self.uses_var.set(row_med[6])
        self.sideEffect_var.set(row_med[7])
        self.dosage_var.set(row_med[8])
        self.price_var.set(row_med[9])
        self.qty_var.set(row_med[10])
        self.issuedate_var.set(row_med[11])

    def Update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are Required!")
        else:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="Hkumar@454", database="pharma_management")
            my_cursor = connect.cursor()
            my_cursor.execute("update pharmacy set  CmpName = %s,MedName =%s,MedType= %s,LotNo= %s,Exp_Date= %s,Uses= %s,Side_effects= %s,Dosage= %s,Price= %s,Quantity= %s,Issue_Date = %s where Ref_no= %s", (

                self.cmpName_var.get(),
                self.medName_var.get(),
                self.typeMed_var.get(),
                self.lot_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.qty_var.get(),
                self.issuedate_var.get(),
                self.ref_var.get()
            ))
            connect.commit()
            self.fetch_data()
            connect.close()
            messagebox.showinfo("Success", "Data Updated")

    def Delete(self):
        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        sql = "delete from pharmacy where Ref_no=%s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql, val)
        connect.commit()
        self.fetch_data()
        connect.close()
        messagebox.showinfo("Success", "Data Deleted")

    def Reset(self):
        self.cmpName_var.set(""),
        self.lot_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.qty_var.set(""),
        self.issuedate_var.set(""),

    def Search_data(self):
        connect = mysql.connector.connect(
            host="localhost", user="root", password="Hkumar@454", database="pharma_management")
        my_cursor = connect.cursor()
        my_cursor.execute(f"select * from pharmacy where {str(self.search_var_combo.get())} LIKE '{str(self.search_box_var.get())}%'")

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values=i)
            connect.commit()
        connect.close()

    

if __name__ == "__main__":
    root = Tk()
    obj = pharmacy_management(root)
    root.resizable(False, False)
    root.mainloop()
