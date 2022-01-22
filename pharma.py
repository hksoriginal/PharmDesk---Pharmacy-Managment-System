
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ctypes
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import ttk

from matplotlib.pyplot import text


class pharmacy_management:
    def __init__(self, root):
        self.root = root
        self.root.title("PharmDesk - Pharmacy Management System")
        self.root.geometry("1550x900+0+0")
        self.root.iconbitmap('icon.ico')

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
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white")
        btnAddData.grid(padx=5, row=0, column=0)

        btnUpdateData = Button(Buttonframe, text=" Update", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white",width=9)
        btnUpdateData.grid(padx=5, row=0, column=1)

        btnDeleteData = Button(Buttonframe, text="Delete", font=(
            "Trebuchet MS", 14, "bold"), bg="#C1272D", fg="white",width=9)
        btnDeleteData.grid(padx=5, row=0, column=4)

        btnResetData = Button(Buttonframe, text="Reset", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white",width=9)
        btnResetData.grid(padx=5, row=0, column=2)

        btnExitData = Button(Buttonframe, text="Exit", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white",width=9)
        btnExitData.grid(padx=5, row=0, column=10)
############# Search By########################
        lablSearch = Label(Buttonframe, text="Search By", bg="#333333",
                           fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablSearch.grid(padx=5, row=0, column=5, sticky=W)

        search_combo = ttk.Combobox(Buttonframe, text="Search", width=12, font=(
            "Trebuchet MS", 12), state="readonly")
        search_combo["values"] = ("Ref No.", "Medicine", "Lot")
        search_combo.grid(padx=2, row=0, column=6, sticky=W)
        search_combo.current(0)

        txtSearch = Entry(Buttonframe, relief=RIDGE,
                          width=20, font=("Trebuchet MS", 14))
        txtSearch.grid(padx=2, row=0, column=7)

        searchBtn = Button(Buttonframe, text="Search", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white",width=9)
        searchBtn.grid(padx=5, row=0, column=8)

        showAllBtn = Button(Buttonframe, text="Show All", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white")
        showAllBtn.grid(padx=5, row=0, column=9)
############################## LAbels & Entry ########################

##########Dataframe Left###############################################

# referemce no
        lablref = Label(DataframeLeft, text="Reference No.", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        lablref.grid(padx=10, row=0, column=0, sticky=W)

        ref_combo = ttk.Combobox(DataframeLeft, text="Search", width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        ref_combo["values"] = ("Ref No.", "Medicine", "Lot")
        ref_combo.grid(padx=2, row=0, column=1, sticky=W)
        ref_combo.current(0)
# Company
        lablcompany = Label(DataframeLeft, text="Company Name", bg="#333333",
                            fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        lablcompany.grid(padx=10, row=1, column=0, sticky=W)

        company_combo = ttk.Combobox(DataframeLeft, text="Search", width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        company_combo["values"] = ("Ref No.", "Medicine", "Lot")
        company_combo.grid(padx=2, row=1, column=1, sticky=W)
        company_combo.current(0)
# Type
        labltype = Label(DataframeLeft, text="Medicine Type", bg="#333333",
                         fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        labltype.grid(padx=10, row=2, column=0, sticky=W)

        type_combo = ttk.Combobox(DataframeLeft, text="Search", width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        type_combo["values"] = ("Ref No.", "Medicine", "Lot")
        type_combo.grid(padx=2, row=2, column=1, sticky=W)
        type_combo.current(0)
# med name
        lablmedname = Label(DataframeLeft, text="Medicine Name.", bg="#333333",
                            fg="white", font=("Trebuchet MS", 14, "bold"), padx=2, pady=6)
        lablmedname.grid(padx=10, row=3, column=0, sticky=W)

        medname_combo = ttk.Combobox(DataframeLeft, text="Search", width=30, font=(
            "Trebuchet MS", 12), state="readonly")
        medname_combo["values"] = ("Ref No.", "Medicine", "Lot")
        medname_combo.grid(padx=2, row=3, column=1, sticky=W)
        medname_combo.current(0)
# lot no
        labllot = Label(DataframeLeft, text="Lot No.", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        labllot.grid(padx=10, row=4, column=0, sticky=W)

        txtlot = Entry(DataframeLeft, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtlot.grid(padx=2, pady=6, row=4, column=1)
# exp date
        lablexp = Label(DataframeLeft, text="Exp Date", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablexp.grid(padx=10, row=5, column=0, sticky=W)

        txtexp = Entry(DataframeLeft, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtexp.grid(padx=2, pady=6, row=5, column=1)
# issue date
        lablissue = Label(DataframeLeft, text="Issue Date", bg="#333333",
                          fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablissue.grid(padx=10, row=6, column=0, sticky=W)

        txtissue = Entry(DataframeLeft, relief=RIDGE,
                         width=26, font=("Trebuchet MS", 14))
        txtissue.grid(padx=2, pady=6, row=6, column=1)
# uses
        labluses = Label(DataframeLeft, text="Uses", bg="#333333",
                         fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        labluses.grid(padx=10, row=0, column=3, sticky=W)

        txtuses = Entry(DataframeLeft, relief=RIDGE,
                        width=26, font=("Trebuchet MS", 14))
        txtuses.grid(padx=2, pady=6, row=0, column=4)
# side_effects
        lablSideEffect = Label(DataframeLeft, text="Side Effects", bg="#333333",
                               fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablSideEffect.grid(padx=10, row=1, column=3, sticky=W)

        txtSideEffect = Entry(DataframeLeft, relief=RIDGE,
                              width=26, font=("Trebuchet MS", 14))
        txtSideEffect.grid(padx=2, pady=6, row=1, column=4)
# dosage
        lablDosage = Label(DataframeLeft, text="Dosage", bg="#333333",
                           fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablDosage.grid(padx=10, row=2, column=3, sticky=W)

        txtDosage = Entry(DataframeLeft, relief=RIDGE,
                          width=26, font=("Trebuchet MS", 14))
        txtDosage.grid(padx=2, pady=6, row=2, column=4)
# Price
        lablPrice = Label(DataframeLeft, text="Price", bg="#333333",
                          fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablPrice.grid(padx=10, row=3, column=3, sticky=W)

        txtPrice = Entry(DataframeLeft, relief=RIDGE,
                         width=26, font=("Trebuchet MS", 14))
        txtPrice.grid(padx=2, pady=6, row=3, column=4)
# Quantity
        lablQty = Label(DataframeLeft, text="Quantity", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablQty.grid(padx=10, row=3, column=3, sticky=W)

        txtQty = Entry(DataframeLeft, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtQty.grid(padx=2, pady=6, row=3, column=4)


##########Dataframe Right###############################################
        
        #entry frame
        entry_frame = Frame(DataframeRight,width=610,bg="#333333",height=200)
        entry_frame.place(x=10,y=10)

    #ref no
        lablrefno = Label(entry_frame, text="Ref No.", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablrefno.grid(padx=10,row=0, column=0)

        txtrefno = Entry(entry_frame, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtrefno.grid(padx=2,pady=6,row=0, column=1)
    #med name    
        lablmedName = Label(entry_frame, text="Medicine Name", bg="#333333",
                        fg="white", font=("Trebuchet MS", 14, "bold"), padx=2)
        lablmedName.grid(padx=10,row=1, column=0)

        txtmedName = Entry(entry_frame, relief=RIDGE,
                       width=26, font=("Trebuchet MS", 14))
        txtmedName.grid(padx=2,pady=6,row=1, column=1)
        ########side Frame################################
        side_frame = Frame(DataframeRight,bd=0,relief=RIDGE,bg="white")
        side_frame.place(x=20,y=100,width=420, height=180)

        scrollSide_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        scrollSide_x.pack(side=BOTTOM, fill=X)
        scrollSide_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        scrollSide_y.pack(side=RIGHT, fill=Y)
         
        self.med_table = ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=scrollSide_x.set,yscrollcommand=scrollSide_y.set)

        scrollSide_x.config(command=self.med_table.xview)
        scrollSide_y.config(command=self.med_table.yview)

        self.med_table.heading("ref",text="Reference No")
        self.med_table.heading("medname",text="Medicine Name")

        self.med_table["show"]="headings"
        self.med_table.pack(fill=BOTH,expand=1)
        self.med_table.column("ref",width=100)
        self.med_table.column("medname",width=100)
        ###########med add button################################
        bt_frame = Frame(DataframeRight,bd=0,relief=RIDGE,bg="#333333")
        bt_frame.place(x=450,y=100,width=120,height=180)

        addMedBtn = Button(bt_frame, text="+ Add", font=(
            "Trebuchet MS", 14, "bold"), bg="#009D3D", fg="white",width=9)
        addMedBtn.grid(padx=10,pady=1 ,row=0, column=0)

        updateMedBtn = Button(bt_frame, text="Update", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white",width=9)
        updateMedBtn.grid(padx=10,pady=1 ,row=1, column=0)

        deleteMedBtn = Button(bt_frame, text="Delete", font=(
            "Trebuchet MS", 14, "bold"), bg="#C1272D", fg="white",width=9)
        deleteMedBtn.grid(padx=10,pady=1 ,row=3, column=0)

        clrMedBtn = Button(bt_frame, text="Clear", font=(
            "Trebuchet MS", 14, "bold"), bg="#0071BC", fg="white",width=9)
        clrMedBtn.grid(padx=10,pady=1 ,row=2, column=0)

#########################Frame Details############################

        frameDetail = Frame(self.root, bd=0, relief=RIDGE,bg="#333333")
        frameDetail.place(x=10, y=620, width=1530, height=270)
################Main Table Frame#################

        frameTablemain = Frame(frameDetail, bd=0, relief=RIDGE,bg="#333333")
        frameTablemain.place(x=0, y=1, width=1530, height=260)

        scrollTable_x = ttk.Scrollbar(frameTablemain, orient=HORIZONTAL)
        scrollTable_x.pack(side=BOTTOM, fill=X)
        scrollTable_y = ttk.Scrollbar(frameTablemain, orient=VERTICAL)
        scrollTable_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(frameTablemain, column=("ref", "companyname", "medname", "type", "lotno", "expdate",
                                           "uses", "sideeffects", "dosage", "price", "qty"), xscrollcommand=scrollTable_x.set, yscrollcommand=scrollTable_y.set)
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
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("medname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffects",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("qty",width=100)
        




if __name__ == "__main__":
    root = Tk()
    obj = pharmacy_management(root)
    root.resizable(False, False)
    root.mainloop()
