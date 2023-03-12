import subprocess
import re
import sys
def checking():
    modulos_en_el_sistema = subprocess.check_output("pip3 freeze", shell=True).decode("utf-8") # Comprobar los módulos en el sistema
    modulos_instalados = [module.strip() for module in modulos_en_el_sistema.split('\n')] # Separarlos
    modulos_necesarios = ["fastapi","uvicorn", "PyMySQL", "pandas", "requests", "mariadb"]
    modulos_cumplidos = [ re.sub("==[0-9.]*", "", x) for x in modulos_instalados if any(i in x for i in modulos_necesarios) ] # Comprobar si los necesarios están entres los instalados
    if len(modulos_cumplidos) == len(modulos_necesarios): # Si están todos, no se hace nada
        print("Están instalados todos los módulos necesarios.")
    else:
        print("Faltan módulos.")
        for modulo in modulos_cumplidos:
            if modulo in modulos_necesarios:
                modulos_necesarios.remove(modulo)
        print(f"Se van a instalar los siguientes módulos: {modulos_necesarios}")
        try:
            for modulo in modulos_necesarios: # Se intentan instalar
                subprocess.run([sys.executable, "-m", "pip", "install", modulo], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except: # Y si hay algún error, se mostrará un mensaje
            print("No se han podido instalar los módulos modulos_necesarios.")

'''
Con la función checking() puedes comprobar que los módulos necesarios están instalados. En caso de que no lo estén, se instalarán automáticamente. Si ya están instalados, no se hará nada.
'''