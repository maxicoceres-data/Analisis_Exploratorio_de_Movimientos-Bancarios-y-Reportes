## FEEDBACK PROGRAMACIÓN (Código)

- [ x] **CRÍTICA:** Reemplazar sys.path hack por solución robusta (pip install -e . o imports relativos en pyproject.toml)
- [x ] Agregar try-except en carga de datos (CSV path validation)

- [ x] Mejorar validación de datos: duplicados

- [ ] Refactorizar código repetido en src/funciones.py (groupby normalizados, cálculo de % gastos, etc.)
- [ x] Agregar docstrings a celdas complejas (outliers, pivot, etc.)

---

## FEEDBACK ANÁLISIS DE NEGOCIO

### Preguntas de Negocio (Obligatorio)

- [ ] Profundizar: Descomponer saldo mes a mes — tabla de cascada (por qué enero bajó -X, julio bajó -Y, etc.)
- [ ] Investigar repunte septiembre-diciembre (¿gastos menores? ¿ingresos mayores? ¿fin de préstamo?)
- [ ] Implementar PREDICCIÓN: Gasto/ahorro esperado próximo mes (promedio o regresión) + intervalo de confianza
- [ ] Implementar SENSIBILIDAD: Simular escenarios (reducir alquiler -5%, alimentación -10%, etc.) + tabla de impacto en ahorro final
- [ ] Implementar con el cliente SALDO MINIMO: ¿Qué saldo mínimo de seguridad implementar?
- [ ] Ratio sostenibilidad: ¿Promedio ahorro mensual es positivo? ¿Tendencia? ¿Cumple mínimo de seguridad de saldo?

### Mejoras de Análisis Exploratorio

- [ ] Heatmap: categorías vs meses (intensidad = gasto absoluto)

- [ ] Volatilidad/Estacionalidad: desv. std por mes/categoría

- [ ] Benchmark: comparar % gastos del cliente vs estándares (ej: alquiler ≤30%, alimentación ≤20%)

- [ ] Verificar supuestos de datos: ¿Saldo negativo = deuda? ¿Transferencias externas?

---

## CONCLUSIONES Y RECOMENDACIONES FINALES

- [ ] Completar acciones concretas (incompleto: "(1)Reducir ...")

- [ ] Redactar recomendaciones ESPECÍFICAS: — Qué categoría cortar — Cuánto ahorraría (%) — Impacto en calidad de vida
- [ ] Exportar reportes: - resumen_ejecutivo.csv - reporte_categorias.csv - predicciones.csv (si aplica)

- [ ] README actualizado con resumen de hallazgos principales
