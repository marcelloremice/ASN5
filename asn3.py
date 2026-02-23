import tkinter as tk 
from tkinter import messagebox 
 
def displayData(): 
    first = entFirst.get().strip() 
    last = entLast.get().strip() 
    email = entEmail.get().strip() 
    phone = entPhone.get().strip() 
 
    msg = f"""First Name: {first} 
Last Name:  {last} 
Email:      {email} 
Phone:      {phone}""" 
 
    messagebox.showinfo("Personal Information", msg) 
 
def Clear(): 
    entFirst.delete(0, tk.END) 
    entLast.delete(0, tk.END) 
    entEmail.delete(0, tk.END) 
    entPhone.delete(0, tk.END) 
 
root = tk.Tk() 
root.title("Assignment 3 - Personal Information") 
root.geometry("500x300") 
 
lblFrPerson = tk.LabelFrame(root, text="Personal Information") 
lblFrPerson.pack(fill="both", padx=10, pady=10) 
 
lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg="blue", fg="white") 
lblFirst.grid(row=0, column=0, padx=5, pady=5, sticky="e") 
entFirst = tk.Entry(lblFrPerson) 
entFirst.grid(row=0, column=1, padx=5, pady=5, sticky="w") 
 
lblLast = tk.Label(lblFrPerson, text="*Last Name:", bg="blue", fg="white") 
lblLast.grid(row=0, column=2, padx=5, pady=5, sticky="e") 
entLast = tk.Entry(lblFrPerson) 
entLast.grid(row=0, column=3, padx=5, pady=5, sticky="w") 
 
lblEmail = tk.Label(lblFrPerson, text="Email:") 
lblEmail.grid(row=1, column=0, padx=5, pady=5, sticky="e") 
entEmail = tk.Entry(lblFrPerson) 
entEmail.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we") 
 
lblPhone = tk.Label(lblFrPerson, text="Phone:") 
lblPhone.grid(row=2, column=0, padx=5, pady=5, sticky="e") 
entPhone = tk.Entry(lblFrPerson) 
entPhone.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="we") 
 
lblFrPerson.columnconfigure(1, weight=1) 
lblFrPerson.columnconfigure(3, weight=1) 
 
fraButtons = tk.Frame(root) 
fraButtons.pack(pady=10) 
 
btnS = tk.Button(fraButtons, text="Submit", command=displayData) 
btnS.pack(side=tk.LEFT, padx=5) 
 
btnR = tk.Button(fraButtons, text="Reset", width=5, command=Clear) 
btnR.pack(side=tk.LEFT, padx=5) 
 
btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy) 
btnQ.pack(side=tk.LEFT, padx=5) 
 
root.mainloop() 
