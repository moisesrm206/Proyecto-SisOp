# Simulador de Gestión de Memoria RAM
## Descripción
Este proyecto es un simulador académico que implementa los principales algoritmos y conceptos de gestión de memoria RAM en sistemas operativos. El simulador permite visualizar y comprender cómo un sistema operativo asigna, gestiona y libera memoria cuando múltiples procesos se ejecutan simultáneamente.
El proyecto fue desarrollado como parte de la materia Sistemas Operativos, con el objetivo de proporcionar una herramienta interactiva para el aprendizaje de estos conceptos fundamentales.

## Características Principales

Gestión de Procesos: 
1. Crear 
2. Ejecutar
3. Y Eliminar procesos con requisitos de memoria variables
4. Visualización de Memoria: Representación gráfica del estado actual de la RAM
6. Seguimiento de Procesos: Historial de asignaciones y liberaciones
7. Estadísticas: Reportes sobre utilización de memoria

---

## ¿Cómo Contribuir al Proyecto?

Este es un proyecto de equipo desarrollado en conjunto. Si eres parte del equipo, aquí te indicamos cómo contribuir:

### Estructura actual del Proyecto

```
src/
  main.py          - Punto de entrada principal
  Proceso.py       - Clase para gestión de procesos
gui/
  interfaz.py      - Interfaz gráfica del simulador
```

### Antes de Comenzar

1. **Clona o actualiza el repositorio**
   ```bash
   git clone https://github.com/moisesrm206/Proyecto-SisOp.git
   git pull origin main
   ```

2. **Instala las dependencias (opcional)**
   ```bash
   pip install -r requirements.txt
   ```

3. **Activa el entorno virtual (opcional)**
   ```bash
   .venv\Scripts\Activate.ps1   # En Windows PowerShell
   ```
    Nota: Si no instalas las dependencias con requirements, tendras que instalarlas manualmente en tu isntalacion global o en tu entorno vitual

### Pasos para Contribuir

1. **Crea una rama para tu trabajo**
   ```bash
   git checkout -b <nombre de rama>
   ó
   git branch <nombre de rama>
   ```
   Ejemplo: `git checkout -b mejorar-visualizacion`

2. **Realiza los cambios**
   - Modifica los archivos necesarios
   - Sigue el estilo de código existente
   - Agrega comentarios claros en funciones nuevas

3. **Prueba tu código**
   - Ejecuta `python src/main.py` para verificar que funciona
   - Prueba la interfaz gráfica

4. **Commit y Push**
   ```bash
   git add . ó git add <file>
   git commit -m "Descripción clara de qué cambiaste"
   git push origin <rama en la que trabajaste/rama actual>
   ```

5. **Comunícalo al equipo**
   - Avisa que has realizado cambios
   - Describe brevemente qué modificaste
   - Resuelve cualquier conflicto si es necesario

### Convenciones del Proyecto

- Definir una convencion para nombres de variables y funciones y metodos (español o en ingles)
- Funciones con docstrings explicativos
- No elimines código sin consultar con el equipo
- Mantén actualizado el README si cambias la estructura

### Si Encuentras un Bug

- Comunícalo al equipo inmediatamente
- Descubre en qué archivo y función ocurre
- Proporciona pasos para reproducirlo
- Si ya lo arreglaste, sigue los pasos normales de contribución

