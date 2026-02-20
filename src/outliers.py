
def outliers_iqr(df,col):
    
    """
        Función para crear los outliers IQR de una columna de un dataframe.
        
        Params: 
        df: dataframe al que se le llama.
        col: Columna con la cual queremos trabajar.
        
        Print:
        Imprime los resultados del limite inferior y superior.
        
        Return:
        Retorna un display de los outliers mostrando unicamente los datos que superan los limites inferior y superior. 
    
    """
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr

# Crear copia explícita para evitar SettingWithCopyWarning y poder modificar el df resultante
    outliers = df[
        (df[col] < lim_inf) | (df[col] > lim_sup)
        ].copy()
    
    print(f'Los límites de los outliers son: {round(lim_inf,2)} y {round(lim_sup,2)}')
    
    
    return lim_sup,lim_inf,outliers.sort_values(by=col)
    

