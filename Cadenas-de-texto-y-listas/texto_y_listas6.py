# José Daniel Fernández López
# 05/10/2022
# Recortar la fecha introducida por el usuario
date_base=input("Introduce tu fecha de nacimiento (formato: DD/MM/YYYY): ")
date_day=date_base[:date_base.find("/")] # Obtenemos el día recortando la fecha base introducida por el usuario hasta la primera "/"
date_base2=date_base[date_base.find("/")+1:] # Transformamos la fecha quitando el día y la primera "/"
date_month=date_base2[:date_base2.find("/")] # Obtenemos el mes haciendo lo mismo que con el día
date_year=date_base2[date_base2.find("/")+1:] # A partir de la fecha2 recortamos de la "/" hasta el final
print(f"Naciste el día {date_day} del mes {date_month} del año {date_year}")