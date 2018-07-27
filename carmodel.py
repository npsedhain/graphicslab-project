from tkinter import *
import time



class car:
     
     def __init__(self,master):
          
        self.master=master
        self.frame=Frame(master,width=1280,height=720)
        self.frame.grid()

        self.startframe = Frame(master,width=1280, height=720)
        self.startframe.grid()

        self.stopframe = Frame(master,width=1280, height=720)
        self.stopframe.grid()
        
        self.reverseframe = Frame(master,width=1280, height=720)
        self.reverseframe.grid()
        
     def home(self):
          
        self.startframe.grid_forget()
        self.stopframe.grid_forget()
        self.reverseframe.grid_forget()
        
        button1 = Button(self.frame, text = "Go Forward", command = self.animationstart)
        button1.configure(width=40, activebackground = "green")
        button1.pack(side=TOP)
        
        button2 = Button(self.frame, text = "Stop the Car", command = self.animationstop)
        button2.configure(width=40, activebackground = "red")
        button2.pack(side=TOP)
        
        button3 = Button(self.frame, text = "Reverse the Car", command = self.animationreverse)
        button3.configure(width=40, activebackground = "yellow")
        button3.pack(side=TOP)
        
        self.canvas = Canvas(self.frame, width=1280, height=720)
        self.canvas.pack()

        '''self.root = Tk()
        self.canvas = Canvas(self.root, width=1280, height =720 )
        self.canvas.pack()'''

        
        self.carm1 = self.canvas.create_oval(580, 30, 620, 70, outline='#A9A9A9',fill='#A9A9A9')
        self.carm2 = self.canvas.create_oval(630, 30, 670, 70, outline='#A9A9A9', fill='#A9A9A9')
        self.carm3 = self.canvas.create_oval(680, 30, 720, 70, outline='#A9A9A9', fill='#A9A9A9')
        
        self.caroad = self.canvas.create_line(0,390,1300,390, width=4)
        
        self.carb1 = self.canvas.create_line(50,370,90,370,width=3)
        self.carb3 = self.canvas.create_line(130,370,220,370,width=3)
        self.carb5 = self.canvas.create_line(260,370,300,370,width=3)
        self.carb6 = self.canvas.create_line(300,370,300,350,width=3)
        self.carb7 = self.canvas.create_line(300,350,240,330,width=3)
        self.carb8 = self.canvas.create_line(240,330,200,300,width=3)  
        self.carb9 = self.canvas.create_line(200,300,110,300,width=3)
        self.carb10 = self.canvas.create_line(110,300,80,330,width=3)
        self.carb11 = self.canvas.create_line(80,330,50,340,width=3)
        self.carb12 = self.canvas.create_line(50,340,50,370,width=3)
        
        self.carw1 = self.canvas.create_line(165,305,165,330,width=3)
        self.carw2 = self.canvas.create_line(165,330,230,330,width=3)
        self.carw3 = self.canvas.create_line(230,330,195,305,width=3)
        self.carw4 = self.canvas.create_line(195,305,165,305,width=3)
        
        self.carw5 = self.canvas.create_line(160,305,160,330,width=3)
        self.carw6 = self.canvas.create_line(160,330,95,330,width=3)
        self.carw7 = self.canvas.create_line(95,330,120,305,width=3)
        self.carw8 = self.canvas.create_line(120,305,160,305,width=3)
        
        self.carh1 = self.canvas.create_oval(90,350,130,390,width=3,fill='silver')
        self.carh2 = self.canvas.create_oval(220,350,260,390,width=3,fill='silver')
        
        self.canvas.pack()

        self.root.mainloop()

     '''def home(self):
        #self.canvasnew = Canvas(self.root, width=1280, height =720 )
        button1 = Button(self.newcanvas, text = "Start", command = self.animation)
        button1.configure(width=40, activebackground = "#33B5E5")
        button1.pack(side=LEFT) '''          
     
     def animationstart(self):
        '''frame=self.frame
        self.startframe.grid()

        self.canvasstart= Canvas(self.startframe, width=1280, height=720)
        self.canvasstart.pack()'''
        self.carm1 = self.canvas.create_oval(580, 30, 620, 70, outline='#A9A9A9',fill='green')
        self.carm2 = self.canvas.create_oval(630, 30, 670, 70, outline='#A9A9A9', fill='#A9A9A9')
        self.carm3 = self.canvas.create_oval(680, 30, 720, 70, outline='#A9A9A9', fill='#A9A9A9')
        
        for i in range(0,200):
             x =5
             y =0 
             time.sleep(0.025)
             self.canvas.move(self.carb1, x, y)
             self.canvas.move(self.carb3, x, y)
             self.canvas.move(self.carb5, x, y)
             self.canvas.move(self.carb6, x, y)
             self.canvas.move(self.carb7, x, y)
             self.canvas.move(self.carb8, x, y)
             self.canvas.move(self.carb9, x, y)
             self.canvas.move(self.carb10, x, y)
             self.canvas.move(self.carb11, x, y)
             self.canvas.move(self.carb12, x, y)
             self.canvas.move(self.carw1, x, y)
             self.canvas.move(self.carw2, x, y)
             self.canvas.move(self.carw3, x, y)
             self.canvas.move(self.carw4, x, y)
             self.canvas.move(self.carw5, x, y)
             self.canvas.move(self.carw6, x, y)
             self.canvas.move(self.carw7, x, y)
             self.canvas.move(self.carw8, x, y)
             self.canvas.move(self.carh1, x, y)
             self.canvas.move(self.carh2, x, y)
             self.canvas.update()
             
        print ("check1")
        frame.grid_forget()
        self.startframe.grid_forget()

        
     def animationstop(self):
        '''frame=self.frame
        self.stopframe.grid()

        self.canvasstop= Canvas(self.stopframe, width=1280, height=720)
        self.canvasstop.pack() '''
        self.carm2 = self.canvas.create_oval(630, 30, 670, 70, outline='#A9A9A9', fill='red')
        self.carm1 = self.canvas.create_oval(580, 30, 620, 70, outline='#A9A9A9',fill='#A9A9A9')
        self.carm3 = self.canvas.create_oval(680, 30, 720, 70, outline='#A9A9A9', fill='#A9A9A9')
          
        for i in range(0,200):
             time.sleep(0.5)
             self.canvas.update()
        print("check2")

     def animationreverse(self):
        '''frame=self.frame
        self.reverseframe.grid()

        self.canvasreverse= Canvas(self.reverseframe, width=1280, height=720)
        self.canvasreverse.pack()'''
        self.carm3 = self.canvas.create_oval(680, 30, 720, 70, outline='#A9A9A9', fill='yellow')
        self.carm1 = self.canvas.create_oval(580, 30, 620, 70, outline='#A9A9A9',fill='#A9A9A9')
        self.carm2 = self.canvas.create_oval(630, 30, 670, 70, outline='#A9A9A9', fill='#A9A9A9')
        
        for i in range(0,200):
             x =-5
             y =0 
             time.sleep(0.025)
             self.canvas.move(self.carb1, x, y)
             self.canvas.move(self.carb3, x, y)
             self.canvas.move(self.carb5, x, y)
             self.canvas.move(self.carb6, x, y)
             self.canvas.move(self.carb7, x, y)
             self.canvas.move(self.carb8, x, y)
             self.canvas.move(self.carb9, x, y)
             self.canvas.move(self.carb10, x, y)
             self.canvas.move(self.carb11, x, y)
             self.canvas.move(self.carb12, x, y)
             self.canvas.move(self.carw1, x, y)
             self.canvas.move(self.carw2, x, y)
             self.canvas.move(self.carw3, x, y)
             self.canvas.move(self.carw4, x, y)
             self.canvas.move(self.carw5, x, y)
             self.canvas.move(self.carw6, x, y)
             self.canvas.move(self.carw7, x, y)
             self.canvas.move(self.carw8, x, y)
             self.canvas.move(self.carh1, x, y)
             self.canvas.move(self.carh2, x, y)
             self.canvas.update()
        print ("check3")
             
                    

root=Tk()

mainobj=car(root)
mainobj.home()

root.mainloop()
