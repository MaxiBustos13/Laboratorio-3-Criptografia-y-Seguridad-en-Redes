# Función para procesar una contraseña
def process_password(password):
    # Elimina espacios
    password = password.strip()
    # Verifica si la contraseña no comienza con un número
    if password and not password[0].isdigit():
        # Capitaliza la primera letra y agrega "0" al final
        Npass = password[0].upper() + password[1:] + "0" 
        return Npass
    
# Archivo de entrada y salida
input_file = "rockyou.txt"
output_file = "rockyou_mod.dic"

# Abre el archivo de entrada en modo lectura
with open(input_file, "r", encoding="latin-1") as file:
    lines = file.readlines()

# Procesa las contraseñas
modified_passwords = [process_password(line) for line in lines]

# Abre el archivo de salida en modo escritura con formato UTF-8
count = 0
with open(output_file, "w") as output:
    # Escribe las contraseñas modificadas en el nuevo archivo
    for password in modified_passwords:
        if password is not None:
            output.write(password + "\n")
            count = count +1
    output.truncate(output.tell() - 1)
print("cantidad contraseñas validas: ", count)