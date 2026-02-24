"""
Genera reporte HTML personalizado con Jinja2
"""
from pathlib import Path
from jinja2 import Template
from datetime import datetime
import base64

# Leer imágenes y convertir a base64
def img_to_base64(img_path):
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()


def generar_reporte_final(saldo_seguridad,fecha_reporte,cliente):
    
    if fecha_reporte is None:
        fecha_reporte = datetime.now()
    
# Preparar datos
    figures_dir = Path("../reports/figures")
    imagenes = {
        'mov_categoria': img_to_base64(figures_dir / "cantidad_movimientos_por_categoria.png"),
        'top5_gastos': img_to_base64(figures_dir / "Top5_importes_de_gastos_por_categoria.png"),
        'comparacion_mensual': img_to_base64(figures_dir / "comparacion_gasto_ingreso_por_mes.png"),
        'saldo_final': img_to_base64(figures_dir / "saldo_total_fonalizar_mes.png"),
        'flujo_mensual': img_to_base64(figures_dir / "flujo_mensual_diferencia_ingreso_gasto.png"),
        'top5_influencia': img_to_base64(figures_dir / "Top5_categorias_inlfuyentes_en_ingreso.png"),
        'optimizado': img_to_base64(figures_dir / "Saldo_total_finalizar_mes_optimizado.png"),
        'escenario_25': img_to_base64(figures_dir / "saldo_final_25_gasto_ext.png"),
        'escenario_50': img_to_base64(figures_dir / "saldo_final_50_gasto_ext.png"),
        'escenario_75': img_to_base64(figures_dir / "saldo_final_75_gasto_ext.png"),
    }

    # Template HTML
    template_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Análisis de Gastos Personales 2024</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                background: #f5f5f5;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
            
            header {
                background: linear-gradient(135deg, #003f5c 0%, #1e829b 100%);
                color: white;
                padding: 60px 40px;
                text-align: center;
            }
            
            header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            
            header p {
                font-size: 1.1em;
                opacity: 0.9;
            }
            
            .meta {
                background: #7b26bc;
                color: white;
                padding: 15px 40px;
                display: flex;
                justify-content: space-between;
                font-size: 0.9em;
            }
            
            nav {
                background: #f8f9fa;
                padding: 20px 40px;
                border-bottom: 2px solid #e0e0e0;
                position: sticky;
                top: 0;
                z-index: 100;
            }
            
            nav a {
                color: #003f5c;
                text-decoration: none;
                margin-right: 25px;
                font-weight: 600;
                transition: color 0.3s;
            }
            
            nav a:hover {
                color: #1e829b;
            }
            
            ul{
                list-style: none;
            }
            
            .content {
                padding: 40px;
            }
            
            section {
                margin-bottom: 60px;
            }
            
            h2 {
                color: #003f5c;
                font-size: 2em;
                margin-bottom: 20px;
                padding-bottom: 10px;
                border-bottom: 3px solid #1e829b;
            }
            
            h3 {
                color: #1e829b;
                font-size: 1.5em;
                margin: 30px 0 15px 0;
            }
            
            .insight-box {
                background: #f0f8ff;
                border-left: 4px solid #1e829b;
                padding: 20px;
                margin: 20px 0;
                border-radius: 4px;
            }
            
            .alert-box {
                background: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 20px;
                margin: 20px 0;
                border-radius: 4px;
            }
            
            .success-box {
                background: #d4edda;
                border-left: 4px solid #28a745;
                padding: 20px;
                margin: 20px 0;
                border-radius: 4px;
            }
            
            .chart-container {
                margin: 30px 0;
                text-align: center;
            }
            
            .chart-container img {
                max-width: 100%;
                height: auto;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            
            .recommendations {
                background: #e8f5e9;
                padding: 30px;
                border-radius: 8px;
                margin: 30px 0;
            }
            
            .recommendations h3 {
                color: #2e7d32;
            }
            
            .recommendations ol {
                margin-left: 20px;
            }
            
            .recommendations li {
                margin: 15px 0;
                line-height: 1.8;
            }
            
            footer {
                background: #263238;
                color: white;
                text-align: center;
                padding: 30px;
                margin-top: 60px;
            }
            
            .stat-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            
            .stat-card {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 25px;
                border-radius: 8px;
                text-align: center;
            }
            
            .stat-card h4 {
                font-size: 0.9em;
                opacity: 0.9;
                margin-bottom: 10px;
            }
            
            .stat-card .value {
                font-size: 2.5em;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>📊 Análisis de Gastos Personales</h1>
                <p>Reporte Ejecutivo 2024</p>
            </header>
            
            <div class="meta">
                <span>📅 Generado: {{fecha}}</span>
                <span>👤 Cliente: {{cliente}}</span>
            </div>
            
            <nav>
                <a href="#resumen">Resumen Ejecutivo</a>
                <a href="#analisis">Análisis Detallado</a>
                <a href="#optimizacion">Optimización</a>
                <a href="#recomendaciones">Recomendaciones</a>
            </nav>
            
            <div class="content">
                <!-- RESUMEN EJECUTIVO -->
                <section id="resumen">
                    <h2>📋 Resumen Ejecutivo</h2>
                    
                    <div class="alert-box">
                        <h3>⚠️ Hallazgo Principal</h3>
                        <p>El cliente presenta una <strong>caída notoria del saldo</strong> debido a <strong>gastos extraordinarios</strong> que afectan el ahorro mensual. Los meses críticos son <strong>Enero y Julio</strong>.</p>
                    </div>
                    
                    <div class="stat-grid">
                        <div class="stat-card">
                            <h4>Saldo de Seguridad</h4>
                            <div class="value">{{ saldo_seguridad }}€</div>
                        </div>
                    </div>
                </section>
                
                <!-- ANÁLISIS DETALLADO -->
                <section id="analisis">
                    <h2>🔍 Análisis Detallado</h2>
                    
                    <h3>Movimientos por Categoría</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.mov_categoria }}" alt="Movimientos por categoría">
                    </div>
                    <div class="insight-box">
                        <strong>Insight:</strong> La alimentación presenta la mayor cantidad de movimientos, aunque no necesariamente el mayor impacto monetario.
                    </div>
                    
                    <h3>TOP 5 Categorías de Gasto</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.top5_gastos }}" alt="TOP 5 Gastos">
                    </div>
                    <div class="insight-box">
                        <strong>Insight:</strong> El alquiler es el gasto más importante que tiene, igualmente es un gasto que es predecible.
                    </div>
                    
                    <h3>Comparación Mensual: Ingresos vs Gastos</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.comparacion_mensual }}" alt="Comparación mensual">
                    </div>
                    <div class="alert-box">
                        <strong>Alerta:</strong> Tendencia clara de gastar más de lo que se ingresa. A partir de octubre se observa una mejora.
                    </div>
                    
                    <h3>Evolución del Saldo Final por Mes</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.saldo_final }}" alt="Saldo final mensual">
                    </div>
                    <div class="alert-box">
                        <strong>Alerta:</strong> El saldo al finalizar cada mes, esta siempre por debajo del saldo de seguridad.
                    </div>
                    
                    <h3>Flujo Mensual (Diferencia Ingreso - Gasto)</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.flujo_mensual }}" alt="Flujo mensual">
                    </div>
                    <div class="alert-box">
                        <strong>Alerta:</strong> La diferencia entre el dinero que ingresa a la cuenta y lo que gasta tambien esta por debajo del saldo de seguridad.
                    </div>
                    
                    <h3>TOP 5 Categorías que Influyen en el Ingreso</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.top5_influencia }}" alt="TOP 5 Influencia">
                    </div>
                    <div class="insight-box">
                        <strong>Conclusión:</strong> Los gastos extraordinarios generan los picos más críticos. El alquiler es consistente pero previsible.
                    </div>
                </section>
                
                <!-- OPTIMIZACIÓN -->
                <section id="optimizacion">
                    <h2>⚙️ Escenarios de Optimización</h2>
                    
                    <h3>Escenario Base Optimizado</h3>
                    <p>Eliminación de préstamo personal, gastos extraordinarios y reducción del 15% en alimentación:</p>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.optimizado }}" alt="Escenario optimizado">
                    </div>
                    <div class="alert-box">
                        <strong>Resultado:</strong> Sin los gastos extraordinarios el saldo del cliente esta muy por encima de su saldo de seguridad.
                    </div>
                    
                    <h3>Escenario: 25% de Gastos Extraordinarios</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.escenario_25 }}" alt="Escenario 25%">
                    </div>
                    <div class="success-box">
                        <strong>✅ Plan Ideal:</strong> Con solo el 25% de los gastos extraordinarios, se supera el saldo de seguridad todos los meses.
                    </div>
                    
                    <h3>Escenario: 50% de Gastos Extraordinarios</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.escenario_50 }}" alt="Escenario 50%">
                    </div>
                    <div class="success-box">
                        <strong>✅ Plan Recomendado:</strong> Mejora sustancial en 9 de 12 meses. Julio sigue siendo crítico.
                    </div>
                    
                    <h3>Escenario: 75% de Gastos Extraordinarios</h3>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{{ imagenes.escenario_75 }}" alt="Escenario 75%">
                    </div>
                    <div class="insight-box">
                        <strong>Observación:</strong> Con el 75% no se alcanzan diferencias sustanciales.
                    </div>
                </section>
                
                <!-- RECOMENDACIONES -->
                <section id="recomendaciones">
                    <h2>💡 Recomendaciones</h2>
                    
                    <div class="recommendations">
                        <h3>Acciones Concretas</h3>
                        <ol>
                            <li><strong>Controlar gastos extraordinarios:</strong> Si no dispone del dinero, evitar realizar el gasto. Estos eventos son los que generan mayor impacto negativo.</li>
                            
                            <li><strong>Reducir gastos extraordinarios entre 50% y 75%:</strong> Recomendamos el <strong>50%</strong> para no reducir sustancialmente la calidad de vida y alcanzar el saldo de seguridad en la mayoría de los meses.</li>
                            
                            <li><strong>Reducir 15% en Alimentación:</strong> Especialmente los <strong>martes y sábados</strong>, días que presentan consumo entre 15% y 18% superior a la media.</li>
                            
                            <li><strong>Terminar de pagar préstamos personales:</strong> Estos préstamos existen por los gastos extraordinarios. Al reducir estos últimos, se reduce la necesidad de financiación.</li>
                        </ol>
                    </div>
                    
                    <div class="success-box">
                        <h3>📈 Impacto Esperado</h3>
                        <p>Implementando estas medidas, el cliente puede:</p>
                        <ul>
                            <li>✅ Superar el saldo de seguridad en 9 de 12 meses</li>
                            <li>✅ Reducir situaciones de saldo negativo</li>
                            <li>✅ Aumentar el ahorro mensual sin comprometer la calidad de vida</li>
                        </ul>
                    </div>
                </section>
            </div>
            
            <footer>
                <p>Análisis generado el {{ fecha }}</p>
                <p>Análisis de Gastos Personales - Maximiliano Cóceres</p>
            </footer>
        </div>
    </body>
    </html>
    """

    # Renderizar template
    template = Template(template_html)
    html_output = template.render(
        fecha=fecha_reporte,
        saldo_seguridad=saldo_seguridad,
        imagenes=imagenes,
        cliente=cliente
    )

    # Guardar
    output_path = Path("../reports/reporte_personalizado.html")
    output_path.write_text(html_output, encoding='utf-8')

    print(f"✅ Reporte generado: {output_path.absolute()}")
    
    
   

if __name__ == "__main__":
    generar_reporte_final(saldo_seguridad=900, fecha_reporte=datetime.now(),cliente="Análisis")