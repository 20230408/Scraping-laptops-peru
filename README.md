# 💻 Análisis de Precios de Laptops en Perú

Proyecto colaborativo que recopila y analiza datos de laptops en Perú mediante Web Scraping desde MercadoLibre, Linio y Ripley. Se estructura la información en un archivo .csv y se generan visualizaciones para facilitar comparaciones de precios y características técnicas.

---

## 🎯 Objetivos

- Obtener automáticamente datos de laptops desde:
  - [MercadoLibre Perú](https://listado.mercadolibre.com.pe/laptop)
  - [Linio Perú](https://www.linio.com.pe/laptops)
  - [Ripley Perú](https://simple.ripley.com.pe/electronica/computo/laptops)
- Extraer características como marca, modelo, precio, RAM, almacenamiento y disponibilidad.
- Estructurar y guardar los datos en un archivo `.csv`.
- Generar análisis y gráficos comparativos.

---

## 📦 Producto final

- `data/laptops_peru.csv`: conjunto de datos unificado con los registros recolectados.
- `notebooks/scraping_laptops.ipynb`: cuaderno Jupyter con el código de scraping, limpieza y visualización.
- Visualizaciones: gráficos de precios promedio por marca y distribución de RAM.
- Repositorio colaborativo con documentación y planeamiento del proyecto.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clona este repositorio
```bash
git clone https://github.com/usuario/laptops-scraping.git
cd laptops-scraping
```

### 2. Instala las dependencias
Asegúrate de tener Python 3.9+ instalado y luego ejecuta:
```bash
pip install -r requirements.txt
```

### 3. Ejecuta el cuaderno
Abre el Jupyter Notebook con:
```bash
jupyter notebook notebooks/scraping_laptops.ipynb
```

---

## 📁 Estructura del repositorio

```
laptops-scraping/
├── data/
│   └── laptops_peru.csv              # Datos estructurados
├── notebooks/
│   └── scraping_laptops.ipynb        # Cuaderno con código principal
├── images/
│   └── grafico_marcas.png            # Visualizaciones generadas (opcional)
├── README.md                         # Este archivo
├── requirements.txt                  # Librerías necesarias
└── .gitignore                        # Exclusiones de Git
```

---

## 👥 Integrantes

- **Ramos Freddy** – Código de extracción y visualización  
- **López Victor** – Documentación y estructuración de datos  
(GitHub: [VictorLopez281199](https://github.com/VictorLopez281199))

---

## 🛠 Herramientas utilizadas

- Python 3
- Jupyter Notebook
- Librerías: `requests`, `BeautifulSoup`, `pandas`, `matplotlib`, `seaborn`
- Git y GitHub para trabajo colaborativo

---

## 🔒 Licencia

Este proyecto es parte del curso *Lenguaje de Programación 2 - 2025-1* y no posee fines comerciales.
