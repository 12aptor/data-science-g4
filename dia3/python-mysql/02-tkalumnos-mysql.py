from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector

class Alumno:
    
    def __init__(self,app):
        
        self.app = app
        self.app.title('Crud de alumnos')
        self.app.geometry('640x480')
        
        self.alumno_id = 0
        
        try:
            #creamos una conexión a la bd
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='db_g4'
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error al conectar o ejecutar la consulta: {e}")
        
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
        btn_insertar.grid(row=4,column=0,columnspan=2)
        
         ### BOTON ELIMINAR ###
        btn_eliminar = Button(frame,text='Eliminar Alumno',command=self.eliminar)
        btn_eliminar.grid(row=5,column=0,columnspan=2)
        
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
        
    def limpiar_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
    def cargar_alumnos(self):
        self.limpiar_tree()
        self.cursor.execute("select id,nombre,email,celular from alumno order by id asc")
        for row in self.cursor.fetchall():
            alumno_row = (
                row[1],row[2],row[3]
            )
            self.tree.insert('',0,text=row[0],values=alumno_row)
        
    def insertar(self):
        nuevo_alumno = (self.txt_nombre.get(),self.txt_email.get(),self.txt_celular.get())
        query = f"insert into alumno(nombre,email,celular) values (%s,%s,%s)"
        self.cursor.execute(query,nuevo_alumno)
        self.connection.commit()
        self.cargar_alumnos()
        
    def eliminar(self):
        seleccion = self.tree.selection()
        if seleccion:
            self.alumno_id = self.tree.item(seleccion[0])["text"]
            respuesta = messagebox.askyesno("confiramción","¿Esta seguro que desea eliminar el registro?")
            if respuesta:
                alumno_eliminar = (self.alumno_id,)
                query = "delete from alumno where id=%s"
                self.cursor.execute(query,alumno_eliminar)
                self.connection.commit()
                self.cargar_alumnos()
        else:
            messagebox.showerror('Alerta','Por favor seleccione un registro')
        

app = Tk()

if __name__ == '__main__':
    app_alumno = Alumno(app)
    app_alumno.cargar_alumnos()
    app.mainloop()