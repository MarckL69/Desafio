import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen =="celsius" and unidad_destino == "fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    else:
        return None
    
def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen =="kilogramos" and unidad_destino == "fahrenheit":
        return masa.kilogramos_a_gramos(valor)
    else:
        return None
    
def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen =="segundo" and unidad_destino == "minutos":
        return masa.segundos_a_minutos(valor)
    else:
        return None
if __name__=="__main__":
        valor = 20
        unidad_origen= "celsius"
        unidad_destino= "fahrenheit"
        print(f"{valor}grados{unidad_origen} equivalen a {unidad_destino}")

