'''APUNTES:
*Función debe recibir como parámetro un diccionario ✔️
*La función debe retornar un diccionario con la siguiente estructura: ✔️
*apto es verdad si está dentro del rango de edad de la tabla
*atraccion y total_boleta -> Si no cumple con el rango de edad se asignarà : 'N/A'

informacion = {
        'idCliente': int, 
        'nombre': str,
        'edad': int,
        'primerIngreso': bool,
        'valorBoleta': float,
        'apto': bool
    }'''

def cliente(informacion: dict)-> dict:
    
    atracciones = dict()

    apto = False
    atraccion = 'N/A'
    valorBoleta = 'N/A'
    dtoExtreme = valorBoleta * 0.05
    dtoCarrosChocones = valorBoleta * 0.07
    dtoSillasVoladoras = valorBoleta * 0.05

    if informacion ['edad'] < 18:
        apto = True
        atraccion = 'X-Treme'
        if informacion ['primerIngreso']:
            valorBoleta -= dtoExtreme
        else:
            valorBoleta = 20000
    
    elif informacion ['edad'] >= 15 and informacion ['edad'] <= 18:
        apto = True
        atraccion = 'Carros chocones'
        if informacion['primerIngreso']:
            valorBoleta = valorBoleta - dtoCarrosChocones
        else:
            valorBoleta = 5000

    elif informacion ['edad'] >= 7 and informacion ['edad'] < 15:
        apto = True
        atraccion = 'Sillas voladoras'
        if informacion['primerIngreso']:
            valorBoleta = valorBoleta - dtoSillasVoladoras
        else:
            valorBoleta = 10000


    respuesta = {}
    respuesta ['nombre'] = informacion['nombre']
    respuesta ['edad'] = informacion['edad']
    respuesta ['atraccion'] = atraccion
    respuesta ['apto'] = apto
    respuesta ['primerIngreso'] = informacion['primerIngreso']
    respuesta ['nombre'] = informacion['nombre']
    return respuesta

dict3 = {
        'id_cliente': 1,
        'nombre': "johana Fermandez",
        'edad': 20,
        'primer_ingreso': True,
}

print (cliente(dict3))
