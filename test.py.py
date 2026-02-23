# Show Info Program

import tkinter
from PIL import Image, ImageTk

class ShowInfoGUI:
    def __init__(self):
        # Create the main window
        self.root = tkinter.Tk()
        self.root.title("Food viewer")
        ##self.root.minsize(300,200)

        # Create two frames
        self.img_frame = tkinter.Frame(self.root)
        self.rbdBtn_frame = tkinter.Frame(self.root)

        self.img1 = Image.open("chicken.jpg")
        self.img1 = self.img1.resize((500, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)
        
        
        self.img2 = Image.open("pie.jpg")
        self.img2 = self.img2.resize((500, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)
        

        self.img3 = Image.open("pizza.jpg")
        self.img3 = self.img3.resize((500, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)
    

        self.img4 = Image.open("steak.jpg")
        self.img4 = self.img4.resize((500, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)
        
        self.myLabel = tkinter.Label(self.img_frame,image= self.imgOne)
        self.myLabel.pack()

        self.selected_option = tkinter.IntVar(value=1)

        self.radio_a = tkinter.Radiobutton(self.rbdBtn_frame,text="chicken",variable=self.selected_option, value=1, command=self.on_radio_select).pack(side="left",padx=10)
        self.radio_b = tkinter.Radiobutton(self.rbdBtn_frame,text="pie", variable=self.selected_option, value=2, command=self.on_radio_select).pack(side="left",padx=10)
        self.radio_c = tkinter.Radiobutton(self.rbdBtn_frame,text="pizza", variable=self.selected_option, value=3, command=self.on_radio_select).pack(side="left",padx=10)
        self.radio_d = tkinter.Radiobutton(self.rbdBtn_frame,text="steak", variable=self.selected_option, value=4, command=self.on_radio_select).pack(side="left",padx=10)

        self.img_frame.pack()
        self.rbdBtn_frame.pack()
        self.root.mainloop()

        
        
    def on_radio_select(self):
        if(self.selected_option.get()==1):
            self.myLabel.config(image=self.imgOne) 
        elif(self.selected_option.get()==2):
            self.myLabel.config(image=self.imgTwo) 
        elif(self.selected_option.get()==3):
            self.myLabel.config(image=self.imgThree)
        elif(self.selected_option.get()==4):
            self.myLabel.config(image=self.imgFour)


if __name__ == '__main__':
    show_info = ShowInfoGUI()
