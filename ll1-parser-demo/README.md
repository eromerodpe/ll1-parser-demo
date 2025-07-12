# LL(1) Parser Demo

Este proyecto construye una tabla LL(1), deriva una cadena paso a paso y genera un árbol de derivación.

## Archivos
- `grammar.txt`: gramática LL(1)
- `table_generator.py`: construcción de la tabla LL(1)
- `parser.py`: parser paso a paso y árbol
- `tree_visualizer.py`: genera imagen del árbol con Graphviz
- `demo.ipynb`: demo compatible con Google Colab

## Cómo usar

```bash
pip install -r requirements.txt
python parser.py
```

O abre `demo.ipynb` en Google Colab.
