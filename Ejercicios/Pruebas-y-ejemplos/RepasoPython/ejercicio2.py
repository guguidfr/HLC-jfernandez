def transformar(segundos):
    horas = segundos//3600
    segundos_restantes1 = segundos%3600
    minutos = segundos_restantes1//60
    segundos_finales = segundos_restantes1%60

    print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_finales} segundos.")

transformar(68543)