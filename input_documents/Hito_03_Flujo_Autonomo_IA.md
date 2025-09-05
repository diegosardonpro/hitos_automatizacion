
# Documentación de Hito: Automatización de Becas

**Hito 3: Implementación de Flujo Autónomo con IA**

- **Fecha:** 04 de setiembre de 2025
- **Estado:** Completado

## 1. Objetivos Cumplidos:

- **Integración de IA Generativa:** Se implementó con éxito la llamada directa a la API del modelo Gemini (`gemini-1.5-pro`) para el análisis y la extracción de datos, eliminando la necesidad de intervención humana en el flujo.
- **Lectura de Documentos Locales:** Se implementó la capacidad de leer archivos PDF directamente desde una carpeta de entrada (`input_documents`) usando la librería `pypdf`.
- **Extracción de Datos Expandida:** Se diseñó y ejecutó un prompt avanzado para que la IA extraiga una estructura de datos rica y detallada del documento, optimizando el valor de cada llamada a la API.
- **Flujo de Trabajo End-to-End:** Se validó el ciclo completo y autónomo: el script identifica un archivo, lo lee, lo envía a la IA para su análisis, recibe los datos estructurados, los inserta en Google Sheets y archiva el documento procesado.

## 2. Entregables:

- Módulo `ai_processor.py` funcional, que se conecta a la API de Gemini.
- Script `main.py` final que orquesta el flujo de trabajo 100% autónomo.
- Un registro en Google Sheets creado a partir de datos reales extraídos por la IA desde un documento PDF.

## 3. Valor Aportado:

Este hito marca la transición del proyecto de un prototipo a una verdadera herramienta de inteligencia artificial aplicada. El sistema ahora posee la capacidad de "leer" y "entender" documentos no estructurados para convertirlos en datos accionables, lo que representa el núcleo de la automatización inteligente que buscábamos crear.

## 4. Estimación de Esfuerzo (Horas-Hombre) sin IA:

| Tarea | Descripción | Horas Estimadas |
| :--- | :--- | :--- |
| **1. Desarrollo de Parser de PDF** | Investigar y desarrollar un sistema robusto basado en reglas para extraer texto de PDFs. | 8.0 |
| **2. Motor de Extracción de Entidades** | Crear un sistema (usando Expresiones Regulares complejas, NLP) para identificar y extraer 10+ entidades específicas del texto. | 12.0 |
| **3. Lógica de Limpieza y Formateo** | Desarrollar código para limpiar y convertir los datos extraídos al formato JSON requerido. | 4.0 |
| **4. Integración y Pruebas** | Unir los tres subsistemas y probar con múltiples documentos para ajustar las reglas. | 6.0 |
| **Total** | | **30.0 horas** |
