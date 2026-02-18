
def tipo_gasto(tipo):
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
