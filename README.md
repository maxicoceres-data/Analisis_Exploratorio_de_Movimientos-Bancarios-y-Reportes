# Análisis de Gastos Personales

Descripción
------------
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre movimientos bancarios personales con el objetivo de entender la estructura de gastos, identificar picos o eventos extraordinarios que afectan el ahorro y proponer acciones concretas para mejorar la salud financiera.

Objetivos principales
- Calcular gasto por categoría y su evolución mensual.
- Detectar outliers y eventos extraordinarios que impactan el saldo.
- Identificar gastos fijos vs variables y priorizar áreas de mejora.
- Proveer un resumen ejecutivo (fijos, variables, extraordinarios, ingresos y ahorro estimado).
- Preparar base para análisis predictivo y simulaciones de sensibilidad.

Datos
-----
Los datos originales se encuentran en `data/raw/` (CSV). Cada registro debe contener al menos: fecha, importe (positivo = ingreso, negativo = gasto), categoría, descripción y saldo después del movimiento.

Estructura del proyecto
-----------------------
- `data/raw/`  : datos crudos (CSV / Excel).
- `notebooks/` : notebooks de análisis (`analisis.ipynb`).
- `src/`       : funciones reutilizables (`iniciar_dataframe.py`, `funciones.py`).
- `reports/`   : salidas y tablas finales exportadas (CSV, imágenes).
- `docs/`      : documentación adicional.

Cómo reproducir
---------------
1. Activar entorno virtual (ejemplo Windows PowerShell):
```powershell
C:\Users\maxim\Proyectos\analisis_gastos_personales\entorno_analisis\Scripts\Activate.ps1
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Abrir y ejecutar el notebook principal:
```bash
jupyter lab notebooks/analisis.ipynb
```

Notas sobre cambios realizados
-----------------------------
- El notebook fue actualizado para leer los datos desde `data/raw/` y para importar utilidades desde `src/`.
- Se añadió una celda que genera un `resumen_ejecutivo` con montos mensuales para fijos, variables y extraordinarios.

Próximos pasos recomendados
---------------------------
- Añadir análisis predictivo (media móvil, ARIMA o Prophet) para estimar gasto/ahorro futuro.
- Implementar análisis de sensibilidad (simular reducción X% por categoría).
- Revisar manualmente la clasificación automática de categorías fijas/variables/extraordinarias y ajustarla.

Contacto
-------
Para cambios o preguntas, editar los scripts en `src/` o el notebook en `notebooks/`.



