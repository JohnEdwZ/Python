#ganancia:
#tiempo > 2 meses
# valorInteres = cantidad * porcentajeInteres * tiempo / 12
#porcentajeDeInteres = 0.03 %
# valorTotal = valorInteres + cantidad
# Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}”

#perdidas
# inferior o igual <= 2 meses  
# valorAPerder = cantidad * porcentajeAPerder= 0.02
#valorTotal = cantidad - valorAPerder
#“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}

def CDT(usuario: str, capital: int, tiempo: int):
    mensaje = ''
    if tiempo <= 2:
        valorAPerder = capital * 0.02
        valorTotalDinero = capital - valorAPerder
        mensaje = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotalDinero}'
    else:
        valorInteres = (capital * 0.03 * tiempo) / 12
        valorTotalDinero = valorInteres + capital
        mensaje = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotalDinero}'
    return mensaje

print(CDT("AB1012",1000000,3))    
print(CDT("DGF",12455,2))