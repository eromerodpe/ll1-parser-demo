# 📘 LL(1) Parser Demo

Este es un proyecto educativo de análisis sintáctico descendente LL(1) en Python. Se muestra cómo analizar una cadena de entrada basada en una gramática predefinida y visualizar el árbol de derivación.

## 🚀 Abrir en Google Colab

Puedes ejecutar el proyecto directamente desde Google Colab con el siguiente botón:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eromerodpe/ll1-parser-demo/blob/main/demo.ipynb)

---

## 🧱 Estructura del proyecto

- `demo.ipynb`: Notebook principal para ejecutar el análisis sintáctico.
- `parser.py`: Lógica del parser LL(1), incluyendo la pila de análisis.
- `table_generator.py`: Generador de la tabla predictiva LL(1).
- `tree_visualizer.py`: Visualización del árbol sintáctico con `graphviz`.
- `grammar.txt`: Archivo de texto con la gramática usada por el parser.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

---

## 📥 Requisitos

En Colab, los requerimientos se instalan automáticamente. Si lo ejecutas localmente, instala las dependencias:

```bash
pip install -r requirements.txt
id + id * id

---

### ✅ ¿Qué hacer ahora?

1. Sube este contenido como `README.md` a tu repositorio (ya sea editando online o reemplazando el archivo desde tu máquina).
2. Verifica que el botón de Colab abra el notebook correctamente.
3. Asegúrate de que `demo.ipynb` clone el repo y acceda al directorio con:

```python
!git clone https://github.com/eromerodpe/ll1-parser-demo.git
%cd ll1-parser-demo
!pip install graphviz

