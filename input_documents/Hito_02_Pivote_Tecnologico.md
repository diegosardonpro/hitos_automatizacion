
# Documentación de Hito: Automatización de Becas

**Hito 2: Pivote Tecnológico y Depuración de APIs**

- **Fecha:** 04 de setiembre de 2025
- **Estado:** Completado

## 1. Objetivos Cumplidos:

- **Diagnóstico de Errores de API:** Se investigaron, diagnosticaron y documentaron errores de conexión persistentes (`403 Forbidden`, `404 Not Found`, `401 Unauthorized`, `Incorrect padding`) en múltiples plataformas (Airtable, Notion, Google Sheets).
- **Pivote Tecnológico Ágil:** Se tomó la decisión estratégica de pivotar entre diferentes tecnologías de backend (Airtable -> Notion -> Google Sheets) en respuesta a los bloqueos técnicos, demostrando agilidad en la gestión del proyecto.
- **Implementación de Múltiples Clientes de API:** Se desarrollaron y refactorizaron múltiples clientes de API en Python, adaptando el código a las especificaciones de cada plataforma.
- **Resolución de Problemas Complejos:** Se resolvieron problemas de bajo nivel relacionados con la configuración de entornos, el formato de credenciales (claves PEM), los permisos de API (scopes) y los roles de servicio (IAM), culminando en una conexión exitosa y estable con la API de Google Sheets.

## 2. Entregables:

- Múltiples versiones de clientes de API para distintas plataformas (desechados pero parte del proceso).
- Un cliente de Google Sheets funcional y robusto, capaz de manejar la autenticación de forma segura.
- Una metodología de depuración documentada para errores de API comunes.

## 3. Valor Aportado:

Este hito, aunque arduo, fue crucial para encontrar una base tecnológica estable para el proyecto. El proceso de depuración exhaustivo garantiza que la solución final es resiliente y fiable. El valor reside en la creación de una base sólida y la eliminación de incertidumbre técnica para futuras automatizaciones.

## 4. Estimación de Esfuerzo (Horas-Hombre) sin IA:

| Tarea | Descripción | Horas Estimadas |
| :--- | :--- | :--- |
| **1. Depuración Multi-Plataforma** | Investigar y depurar errores de autenticación y permisos en 3 APIs distintas, leyendo documentación y foros. | 12.0 |
| **2. Refactorización de Código** | Reescribir la lógica de conexión y envío de datos para cada una de las 3 plataformas. | 8.0 |
| **3. Depuración de Credenciales** | Diagnosticar y resolver errores de formato de claves criptográficas y archivos JSON. | 6.0 |
| **Total** | | **26.0 horas** |
