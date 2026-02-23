import pandas as pd
from pathlib import Path


project_root = Path(__file__).parent.parent if '__file__' in dir() else Path.cwd().parent

def generar_html(df_original, df_optimizado, saldo_seguridad):
    # Obtener datos del escenario original
    gasto_total_original = df_original["gastos"].sum()
    ingreso_total_original = df_original["ingresos"].sum()
    ahorro_total_original = ingreso_total_original + gasto_total_original  # gasto es negativo
    saldo_final_original = df_original["saldo_final"].iloc[-1]
    meses_bajo_seguridad_original = (df_original["saldo_final"] < saldo_seguridad).sum()

    # Obtener datos del escenario optimizado
    gasto_total_optimizado = df_optimizado[0.50]["gastos"].sum()
    ingreso_total_optimizado = df_optimizado[0.50]["ingresos"].sum()
    ahorro_total_optimizado = ingreso_total_optimizado + gasto_total_optimizado  # gasto es negativo
    saldo_final_optimizado = df_optimizado[0.50]["saldo_final"].iloc[-1]
    meses_bajo_seguridad_optimizado = (df_optimizado[0.50]["saldo_final"] < saldo_seguridad).sum()

    # Calcular diferencias y mejoras
    diferencia_ahorro = ahorro_total_optimizado - ahorro_total_original
    diferencia_saldo = saldo_final_optimizado - saldo_final_original
    porcentaje_mejora_ahorro = round((diferencia_ahorro / abs(ahorro_total_original)) * 100, 2) if ahorro_total_original != 0 else 0
    porcentaje_mejora_saldo = round((diferencia_saldo / abs(saldo_final_original)) * 100, 2) if saldo_final_original != 0 else 0
    diferencia_meses = meses_bajo_seguridad_original - meses_bajo_seguridad_optimizado
    
    
    # Crear dataframe comparativo
    comparacion = pd.DataFrame({
    "Métrica": [
        "Ingresos Totales (€)",
        "Gastos Totales (€)",
        "Ahorro Anual (€)",
        "Saldo Final Año (€)",
        "Meses bajo saldo seguridad",
        "Saldo de Seguridad Requerido (€)"
    ],
    "Escenario Actual": [
        round(ingreso_total_original, 2),
        round(gasto_total_original, 2),
        round(ahorro_total_original, 2),
        round(saldo_final_original, 2),
        meses_bajo_seguridad_original,
        saldo_seguridad
    ],
    "Escenario Optimizado": [
        round(ingreso_total_optimizado, 2),
        round(gasto_total_optimizado, 2),
        round(ahorro_total_optimizado, 2),
        round(saldo_final_optimizado, 2),
        meses_bajo_seguridad_optimizado,
        saldo_seguridad
    ],
    "Diferencia": [
        round(ingreso_total_optimizado - ingreso_total_original, 2),
        round(gasto_total_optimizado - gasto_total_original, 2),
        round(diferencia_ahorro, 2),
        round(diferencia_saldo, 2),
        diferencia_meses,
        0
    ],
    "% Mejora": [
        "N/A",
        f"{round((gasto_total_optimizado - gasto_total_original) / abs(gasto_total_original) * 100, 2)}%",
        f"{porcentaje_mejora_ahorro}%",
        f"{porcentaje_mejora_saldo}%",
        f"{diferencia_meses} meses",
        "N/A"
    ]
    })
    
    # Lógica para la recomendación final
    if saldo_final_optimizado >= saldo_seguridad:
        clase_alerta = "alert-success"  # Verde
        titulo_rec = "✅ ESTRATEGIA RECOMENDADA"
        mensaje_rec = f"El cliente alcanza el saldo de seguridad (€{saldo_seguridad}). Saldo final esperado: €{round(saldo_final_optimizado, 2)} (Superado en €{round(saldo_final_optimizado - saldo_seguridad, 2)})."
    else:
        clase_alerta = "alert-warning"  # Amarillo/Naranja
        titulo_rec = "⚠️ ACCIÓN REQUERIDA"
        mensaje_rec = f"El cliente NO alcanza el saldo de seguridad. Falta €{round(saldo_seguridad - saldo_final_optimizado, 2)} para el objetivo. Se recomienda aplicar medidas adicionales."
        
        
    reporte_estilizado = (comparacion.style
    .set_table_attributes('class= table table-striped table-hover table-bordered w-100')
    .format({
        "Escenario Actual": "{:,.2f} €",
        "Escenario Optimizado": "{:,.2f} €",
        "Diferencia": "{:,.2f} €"
    })
    .hide(axis="index")
)

    #Convertimos a HTML
    html_tabla = reporte_estilizado.to_html()


    html_final = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ padding: 40px; background-color: #f8f9fa; font-family: 'Segoe UI', sans-serif; }}
            .container {{ background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
            th {{ background-color: #2c3e50 !important; color: white !important; text-align: center; }}
            td {{ text-align: center; vertical-align: middle; }}
            .table {{ margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2 class="text-center mb-4">📊 Reporte Comparativo de Optimización al 50% de Gastos extraordinarios</h2>
            {html_tabla}
            <p class="text-muted mt-3"><small>Reporte generado automáticamente el 2026.</small></p>
            <h2 class="text-center mt-5">Resumen Ejecutivo</h2>
        <p>✓ Ahorro Anual: {round(ahorro_total_optimizado, 2)}€ (vs {round(ahorro_total_original, 2)}€ actualmente)</p>
        <p>✓ Mejora en Ahorro: +{round(diferencia_ahorro, 2)}€ ({porcentaje_mejora_ahorro}%)"</p>
        <p>✓ Saldo Final Año: {round(saldo_final_optimizado, 2)}€ (vs {round(saldo_final_original, 2)}€ actualmente)</p>
        <p>✓ Mejora en Saldo: +{round(diferencia_saldo, 2)}€ ({porcentaje_mejora_saldo}%)</p>
        <p>✓ Meses bajo seguridad: {meses_bajo_seguridad_optimizado} meses (vs {meses_bajo_seguridad_original} meses actualmente)</p>
        <p>✓ Reducción de meses críticos: {diferencia_meses} meses</p>
        
        <h3>Recomendación Final</h3>
        <div class="alert {clase_alerta} mt-4">
                <h4>{titulo_rec}</h4>
                <p class="mb-0">{mensaje_rec}</p>
            </div>
        
        </div>
        
    </body>
    </html>
    """

    # 4. Guardar el archivo
    filename_html = "tabla_comparativa.html"
    output_path_reports = project_root / "reports" / filename_html
    with open(output_path_reports, "w", encoding="utf-8") as f:
        f.write(html_final)

    print(f"✅ Reporte guardado con éxito en: {output_path_reports}")