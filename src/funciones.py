
def tipo_gasto(tipo):
    
    """Función para generar una descripción mas global del tipo de gasto, separando por cada descripcion del gasto. Se realiza de esta manera ya que hay pocas descripciones de gastos y se puede dividir de manera más puntual
    
    Params: 
        tipo: descripción del gasto en la columna de "descripción"

    Returns:
        fijo: Descripción global de gasto fijo
        gasto recuerrente: Descripción global de gasto recurrente
        gasto extraordinario: Descripción global de gasto extraordinario
        ingreso dinero: Descripción global de ingreso dinero
        sin definir: descripcion de gasto sin definir (pueden ser entradas o salidas de bizum, etc) Al no ser gastos o ingresos que pueden marcar una diferencia se dejan así.
    """
    
    fijo = ["Internet","Electricidad","Telefonía","Seguro","Alquiler","Gas","Educación","Streaming","Préstamo personal"]
    variable_recurrente = ["Transporte","Alimentación","Salud"]
    variables_extraordinarios = ["Ropa","Ocio","Gasto extraordinario","Restaurantes","Otros"]
    ingresos = ["Salario","Ingreso extra"]
    
    if tipo in fijo:
        return "fijo"
    elif tipo in variable_recurrente:
        return "gasto recurrente"
    elif tipo in variables_extraordinarios:
        return "gasto extraordinario"
    elif tipo in ingresos:
        return "ingreso de dinero"
    else:
        return "sin definir"




def calcular_porcentaje(gasto,porcentaje):
    diferencia = gasto * porcentaje
    return diferencia