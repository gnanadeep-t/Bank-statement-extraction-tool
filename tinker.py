import tkinter as tk
from tkinter import filedialog
import os
import csv
import re
import pandas as pd
# Create the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a dialog for selecting a folder/directory
selected_folder = filedialog.askdirectory()
files_in_folder = os.listdir(selected_folder)
xlsx_files = [file for file in files_in_folder if file.endswith('.xlsx')]
dest_path=selected_folder+"/"+"output.csv"
for fl in xlsx_files:
    print(fl)
    path=selected_folder+"/"+fl
    # col=input("Enter column : ")
    print("Loading...")
    df = pd.read_excel(path, usecols="L")
    df=df.values
    total=[]
    for i in df:
        if 'UPI/' in str(i[0]):
            out=[]
            name=" "
            number=" "
            upi=" "
            if "Pay to" in i[0]:
                upi=i[0].split('/')[6]
                upi=re.findall(r'\b([a-zA-Z0-9]+@[^@\s]+)\b', upi)
                if upi==[]:
                    upi=" "
                else:
                    upi=upi[0]
            else:
                upi=i[0]
                upi=re.findall(r'/(?P<extracted_text>[a-zA-Z0-9][^/@]*@[^/]+)', upi)
                if upi==[]:
                    upi=" "
                else:
                    if " " in upi[0]:
                        upi=" "
                    else:
                        upi=upi[0]
            name=str(i[0]).split('/')[3]
            if re.findall(r'/(?P<phone_number>91\d{10})/', str(i[0]))==[]:
                number=" "
            else:
                number=int((re.findall(r'/(?P<phone_number>91\d{10})/', str(i[0]))[0])[2:])
            if name.isdigit()==True and number == " ":
                number=name
                name=" "
            if number==" " and upi!=" ":
                if "@" in upi:
                    temp=upi.split('@')[0]
                    if temp.isdigit():
                        number=temp
            if '@' in name:
                name= " "
            out.append(upi)
            out.append(name)
            out.append(number)
            total.append(out)
                
    print("Writing...")
    file=open(dest_path,"a+")
    writer=csv.writer(file)
    heading=["UPI","NAME","NUMBER"]
    writer.writerow(heading)
    for i in total:
        writer.writerow(i)
    file.close()
    print("Done")

    