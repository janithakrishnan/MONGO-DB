#Creating Connection
from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/)')
#Using Database and collection
db=client['student_data_janitha']
collection=db["New_college"]
#Function for clearing entries
def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    option_entry.delete(0, tk.END)
#Function for inserting documents
def create_doc():
    id=id_entry.get()
    name=name_entry.get()
    city=city_entry.get()
    collection.insert_one({'id':id,'name':name,'city':city})
    messagebox.showinfo("Success", "Document inserted successfully!")
    clear_entries()
#Function for reading documents
def read_doc():
    result=collection.find()
    result_list.delete(0, tk.END)
    for doc in result:
        result_list.insert(tk.END, f"ID: {doc['id']}, Name: {doc['name']}, City: {doc['city']}")
#function for updating documents
def update_doc():
    x=name_entry.get()
    y=city_entry.get()
    z=option_entry.get()
    if z=='one':
        result=collection.update_one({'name':x},{'$set':{'city':y}})
        print(f"\nUPDATED {z} OCCURENCE OF {x}: changed city {y}")
        read_doc()
    else:
        result=collection.update_many({'name':x},{'$set':{'city':y}})
        print(f"\nUPDATED {z} OCCURENCES OF {x}: changed city {y}")
        read_doc()
    clear_entries()
#Function for Deleting documents
def delete_doc():
    x=name_entry.get()
    z=option_entry.get()
    if z=='one':
        result=collection.delete_one({'name':x})
        print(f"\nDELETED {z} OCCURENCE OF {x}")
        read_doc()
    else:
        result=collection.delete_many({'name':x})
        print(f"\nDELETED {z} OCCURENCES OF {x}")
        read_doc()
    clear_entries()
#Tkinter Window
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("CRUD APPLICATION USING TKINTER")
root.geometry("800x400")

#Create tkinter buttons to trigger CRUD
create_button=tk.Button(root,text="Create",command=create_doc)
create_button.grid(row=2,column=0,padx=10,pady=5)
read_button=tk.Button(root,text="Read",command=read_doc)
read_button.grid(row=2,column=1,padx=10,pady=5)
update_button=tk.Button(root,text="Update [name,city,option]",command=update_doc)
update_button.grid(row=3,column=0,padx=10,pady=5)
delete_button=tk.Button(root,text="Delete [name,option]",command=delete_doc)
delete_button.grid(row=3,column=1,padx=10,pady=5)

#TextBoxs for user Entry
id_label = tk.Label(root, text="ID")
id_label.grid(row=0,column=0,padx=3,pady=5)
id_entry=tk.Entry(root)
id_entry.grid(row=0,column=1,padx=3,pady=5)

name_label = tk.Label(root, text="NAME")
name_label.grid(row=0,column=2,padx=3,pady=5)
name_entry=tk.Entry(root)
name_entry.grid(row=0,column=3,padx=10,pady=5)

city_label = tk.Label(root, text="CITY")
city_label.grid(row=1,column=0,padx=3,pady=5)
city_entry=tk.Entry(root)
city_entry.grid(row=1,column=1,padx=10,pady=5)

option_label = tk.Label(root, text="OPTION")
option_label.grid(row=1,column=2,padx=3,pady=5)
option_entry=tk.Entry(root)
option_entry.grid(row=1,column=3,padx=10,pady=5)
# Create a Label to display the result
result_list = tk.Listbox(root, width=50)
result_list.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()