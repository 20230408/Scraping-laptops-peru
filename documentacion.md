# 📝 Documentación técnica del proyecto

## 📌 Nombre del proyecto
**Comparación de precios de laptops en supermercados peruanos**

---

## 1. 🎯 Descripción general

Este proyecto fue desarrollado con el objetivo de automatizar la recolección de precios de **laptops** desde las plataformas en línea de **Plazavea, Metro y Vivanda**, utilizando sus APIs públicas. Posteriormente, los datos son visualizados mediante gráficos para identificar diferencias de precios entre supermercados.

---

## 2. 🗂️ Estructura del repositorio

```
📁 capturas/
 └─ grafico_comparativo.png         ← Imagen con gráfico generado

📁 data/
 └─ laptops_supermercados.csv       ← Datos obtenidos desde las APIs

📄 scraping.py                      ← Script que conecta con las APIs y guarda datos
📄 Visualización.py                 ← Script que genera gráfico comparativo
📄 README.md                        ← Descripción general del proyecto
📄 DOCUMENTACION.md                 ← Documentación técnica (este archivo)
📄 requirements.txt                 ← Librerías necesarias para ejecutar el proyecto
```

---

## 3. 🔁 Flujo de ejecución

1. Ejecutar `scraping.py`  
   → Se conecta a las APIs de Plazavea, Metro y Vivanda y guarda los datos en `data/laptops_supermercados.csv`.

2. Ejecutar `Visualización.py`  
   → Lee los datos del CSV, calcula el precio promedio por tienda y genera un gráfico comparativo (`grafico_comparativo.png`).

---

## 4. ⚙️ Descripción de funciones

### `scraping.py`

- `buscar_en_plazavea(producto, cantidad)`  
  Consulta la API de Plazavea y devuelve productos coincidentes con el nombre buscado.

- `buscar_en_metro(producto, cantidad)`  
  Consulta la API de Metro de forma similar.

- `buscar_en_vivanda(producto, cantidad)`  
  Consulta la API de Vivanda.

- El bloque `if __name__ == "__main__"` ejecuta todo el proceso de scraping y guarda un CSV consolidado.

---

### `Visualización.py`

- Lee el archivo CSV con pandas.
- Calcula el promedio de precios por supermercado.
- Genera un gráfico de barras con `matplotlib`.
- Guarda el gráfico en la carpeta `capturas/`.

---

## 5. 🧱 Requisitos / Dependencias

Incluidas en `requirements.txt`:

```
pandas
requests
matplotlib
```

Instalación rápida:

```bash
pip install -r requirements.txt
```

---

## 6. ✅ Resultado esperado

- Archivo `.csv` con datos reales de laptops desde tres supermercados peruanos.
- Gráfico `.png` mostrando visualmente los precios promedio por tienda.

---

## 👨‍🎓 Autores

- **Victor López Acuña**
- **Freddy Ramos**

---

## 📚 Curso

**Lenguaje de Programación II**   
Facultad de Estadística e Informática – Universidad Nacional Agraria La Molina
