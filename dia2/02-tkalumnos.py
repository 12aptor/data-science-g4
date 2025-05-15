from tkinter import *
from tkinter.ttk import Treeview

class Alumno:
    
    def __init__(self,app):
        
        self.app = app
        self.app.title('Crud de alumnos')
        self.app.geometry('640x480')
        
        frame = LabelFrame(self.app,text='Nuevo Alumno')
        frame.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
        
        ##### NOMBRE ####
        lb_nombre = Label(frame,text='Nombre : ')
        lb_nombre.grid(row=1,column=0)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=1,column=1)

        ##### EMAIL ####
        lb_email = Label(frame,text='Email : ')
        lb_email.grid(row=2,column=0)
        self.txt_email = Entry(frame)
        self.txt_email.grid(row=2,column=1)

        ##### CELULAR ####
        lb_celular = Label(frame,text='Celular : ')
        lb_celular.grid(row=3,column=0)
        self.txt_celular = Entry(frame)
        self.txt_celular.grid(row=3,column=1)
        
         ### BOTON INSERTAR ###
        btn_insertar = Button(frame,text='Insertar Nuevo Alumno',command=self.insertar)
        btn_insertar.grid(row=4,column=1,columnspan=2)
        
        ### LISTA DE ALUMNOS
        self.tree = Treeview(self.app)
        self.tree['columns'] = ('Nombre','Email','Celular')

        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column('Nombre')
        self.tree.column('Email')
        self.tree.column('Celular')

        self.tree.heading('#0',text='id')
        self.tree.heading('Nombre',text='Nombre')
        self.tree.heading('Email',text='Email')
        self.tree.heading('Celular',text='Celular')

        self.tree.grid(row=5,column=0,pady=20,padx=20)
        
    def insertar(self):
        
        nuevo_alumno = (self.txt_nombre.get(),self.txt_email.get(),self.txt_celular.get())
        self.tree.insert('',END,values=nuevo_alumno)
        

app = Tk()

if __name__ == '__main__':
    app_alumno = Alumno(app)
    app.mainloop()