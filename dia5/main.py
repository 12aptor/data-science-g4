from randomuser import RandomUser

if __name__ == "__main__":
    random_user = RandomUser()
    number_of_users = int(input("¿Cuántos usuarios quieres generar? "))
    users = random_user.get_users(number_of_users)
    
    for user in users:
        print("="*50)
        print(f"Nombre: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Ubicación: {user['location']['city']}, {user['location']['country']}")
        print(f"Fecha de nacimiento: {user['dob']['date']}")
        print(f"Imagen: {user['picture']['large']}")