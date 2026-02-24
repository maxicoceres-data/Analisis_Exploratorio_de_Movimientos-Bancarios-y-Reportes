# Análisis de Gastos Personales (EDA + Reportes)

Proyecto de análisis exploratorio de movimientos bancarios personales para entender patrones de gasto, detectar eventos extraordinarios y presentar recomendaciones accionables. Incluye reportes HTML listos para mostrar resultados.

## Qué incluye

- Limpieza y transformación de datos de movimientos bancarios.
- Análisis de gastos por categoría y evolución mensual.
- Detección de outliers/eventos extraordinarios.
- Escenarios de optimización (25%, 50%, 75% de gastos extraordinarios).
- Reportes HTML ejecutivos con visualizaciones y recomendaciones.

## Reportes y resultados

- `reports/reporte_personalizado.html`: reporte ejecutivo completo con gráficos embebidos.
- `reports/tabla_comparativa.html`: tabla comparativa entre escenario actual y optimizado.
- `reports/figures/`: gráficos generados (PNG) usados en los reportes.

> Los reportes pueden abrirse directamente en el navegador.

## Estructura del proyecto

- `data/raw/` : datos crudos (CSV / Excel).
- `notebooks/` : notebook principal de análisis (`analisis.ipynb`).
- `src/` : lógica reutilizable (ETL, análisis, reportes).
- `reports/` : reportes HTML y figuras generadas.
- `docs/` : documentación adicional.

## Requisitos

- Python 3.10+
- `numpy`, `pandas`, `matplotlib`, `seaborn`
- `jinja2` (para los reportes HTML)

## Cómo reproducir

1. Activar entorno virtual (Windows PowerShell):

```powershell
C:\Users\maxim\Proyectos\analisis_gastos_personales\entorno_analisis\Scripts\Activate.ps1
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar el notebook principal:

```bash
jupyter lab notebooks/analisis.ipynb
```

## Generar reportes HTML

- Reporte ejecutivo completo:

```bash
python src/reporte_final.py
```

- Tabla comparativa (se genera desde el notebook usando `src/report_html.py`).

## Notas sobre datos

Los datos fueron generados por IA para poder realizar la práctica del proyecto. El repositorio se estructura para trabajar con datos locales en `data/raw/` y generar reportes en `reports/`.

## Autor

Maximiliano Cóceres
