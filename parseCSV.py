import tkinter as tk
from tkinter import filedialog
import os
import csv
import re
# Create the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a dialog for selecting a folder/directory
selected_folder = filedialog.askdirectory()
files_in_folder = os.listdir(selected_folder)
csv_files = [file for file in files_in_folder if file.endswith('.csv')]
dest_path=selected_folder+"/"+"output.csv"
for fl in csv_files:
    print(fl)
    file=open(selected_folder+"/"+fl,'r')
    data=list(file.read().split(","))
    file.close()
    print("Writing...")
    dest_file=open(dest_path,"a+")
    writer=csv.writer(dest_file)
    heading=["NAME","UPI","NUMBER"]
    writer.writerow(heading)
    total=[]
    for i in data:
        if "UPI" in i:
            out=[]
            req=i[5:]
            h=req.find("-")
            a=req.find("@")
            name=req[:h]
            upi=req[h+1:a]+"@"+re.findall(r'@([^@-]+)-',req)[0]
            match=re.search(r'\b\d{10}\b',upi)
            number=" "
            if match:
                number=match.group(0)
            out.append(name)
            out.append(upi)
            out.append(number)
            total.append(out)
    for i in total:
        writer.writerow(i)
    dest_file.close()
    
    print("Done")
