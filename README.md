# 🛍️ Comparación de precios de laptops en supermercados peruanos

Este proyecto permite comparar los precios de **laptops** en tres supermercados en línea del Perú, utilizando sus **APIs públicas**. El objetivo es automatizar la recolección de datos reales para análisis comparativo.

---

## 📌 Objetivo

Automatizar la extracción de precios de laptops desde:

- 🛒 Plazavea
- 🛒 Metro
- 🛒 Vivanda

---

## ⚙️ Estructura del proyecto

```
📁 data/
 └─ laptops_supermercados.csv     ← Datos combinados desde Plazavea, Metro y Vivanda
📄 scraping_supermercados.py      ← Script principal de extracción
📄 README.md                      ← Este archivo
```

---

## 🚀 Cómo ejecutar

### 1. Instalar dependencias

Asegúrate de tener Python 3 instalado, luego ejecuta:

```bash
pip install pandas requests
```

### 2. Ejecutar el script

```bash
python scraping_supermercados.py
```

Se generará automáticamente el archivo `data/laptops_supermercados.csv`.

---

## 📄 Formato del archivo de salida

| supermercado | producto_buscado | nombre                       | precio   |
|--------------|------------------|------------------------------|----------|
| Plazavea     | laptop           | Laptop HP Ryzen 5            | 2099.00  |
| Metro        | laptop           | Laptop Lenovo IdeaPad 3      | 1899.00  |
| Vivanda      | laptop           | Laptop Asus Intel Core i5    | 2499.00  |

---

## 👨‍🏫 Proyecto académico

Este trabajo fue desarrollado como parte del curso:

- **Diseños Experimentales I**
- Docente: Luz Bullón Camarena

---

## 👨‍💻 Autores

| Nombre             | Usuarios                                                  |
|--------------------|------------------------------------------------------|
| Victor López Acuña | Victorlopez281199  |
| Freddy Ramos       | 20230408 |

---

## 📊 Siguientes pasos (opcional)

- Agregar gráficos comparativos por tienda
- Extender el análisis a más productos: leche, arroz, azúcar, etc.
- Comparar con tiendas como Ripley y Falabella (requiere Selenium)
