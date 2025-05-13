class Usuario:
    
    __email = ''
    __password = '123456'
    
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        
    def login(self,email,password):
        if(self.__email == email and self.__password == password):
            print('Login correcto')
        else:
            print('Login incorrecto')
            

usuario1 = Usuario('admin@gmail.com','123456')
usuario2 = Usuario('empleado@gmail.com','qwerty123')

print("LOGIN DE USUARIOS")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')
#print('--------------------- password ---------------------')
#print(usuario1.__password)
usuario1.login(email,password)