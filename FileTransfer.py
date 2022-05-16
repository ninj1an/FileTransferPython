import os, shutil
import pandas as pd

os.getcwd()
#read in the weekly edited mxd file and convert it to a list
df = pd.read_csv("MXDDetailCircles.csv")
changed_mxd = df['MXD'].tolist()

#create a new list to change the .mxd files to pdf extentions
new_list = []
new_list = [i[:-4] for i in changed_mxd]

#Create the list of PDFs to find in the folder
pdf_list = [x + '.pdf' for i, x in enumerate(new_list)]

#Loop through listed PDFs to find and move to the repair folder
f = 0
e = []
while i < len(pdf_list):
    try:
        src_path = "K:/PDFRequestor/PRODRepository/pdf/in/" + pdf_list[f]
        dst_path = "Z:/Maps/WebPDF/Repair/" + pdf_list[f]
        shutil.move(src_path,dst_path)
    except:
        e.append(pdf_list[f])
        pass
    finally:
        i = f + 1
#The try/except/finally handles any 'file not found' errors by storing the missing PDF name and then moving on.

#Create a data frame to export missing PDFs to a CSV
missingPDF = {'PDF Not Found' : e}
df = pd.DataFrame(missingPDF)

#Saves the CSV
df.to_csv('MissingPDF.csv', index = False)

print("All found files moved to repair folder.")
print("Missing files: " + e)
