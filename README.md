# <h1 align="center">**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h1>

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="200">

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="200">

<h1 align='center'>Sistema de Recomendación de Restaurantes en NY, California y Florida</h1>

Este proyecto está orientado al análisis de reseñas de usuarios en las plataformas Yelp y Google Maps, centrado en el sector de restaurantes en Nueva York, Florida y California. A través de técnicas avanzadas de análisis de sentimientos y Machine Learning, buscamos generar un entendimiento profundo de las opiniones de los usuarios, lo cual permitirá a nuestro cliente —un conglomerado de empresas de turismo— tomar decisiones basadas en datos para estrategias de expansión, marketing, y servicio al cliente.

### Tabla de contenido

1.  [Objetivos del Proyecto](#objetivos)
2.  [Equipo de Trabajo](#team)
3.  [Instalación y Requisitos](#requirements)
4.  [Estructura del Proyecto](#struct)
5.  [Uso y Ejecución](#use)
6.  [Datos y Fuentes](#data)
7.  [Stack Tecnológico](#stack)
8.  [Resultados y Conclusiones](#result)
9.  [Contribución y Colaboración](#colab)


<h2 align='center' id='objetivos'>Objetivos del Proyecto</h2>


1. **Analizar las opiniones de usuarios** de Yelp y Google Maps para identificar tendencias en la percepción de restaurantes.


2. **Realizar un análisis de sentimientos** para identificar aspectos positivos y negativos en reseñas de los restaurantes.


3. **Desarrollar un sistema de recomendación** para ayudar a los usuarios a descubrir nuevos lugares de acuerdo con sus experiencias previas.


4. **Identificar ubicaciones óptimas para nuevos locales** en función de la demanda, puntajes y popularidad en las reseñas.


5. **Primer entrega:**.

<h2 align='center' id='team'>Equipo de Trabajo</h2>

<p align='center'>
    <b><a href='https://github.com/AballayNicolas' target="blank">Nicolás Aballay:</b></a> Data Engineer
</p>

<p align='center'>
    <b><a href='https://github.com/Santino-Rocchietti' target="blank">Santino Rocchietti:</b></a> Data Engineer
</p>

<p align='center'>
    <b><a href='https://github.com/aestebangnivia23' target="blank">Esteban Nivia:</b></a> Data Analyst
</p>

<p align='center'>
    <b><a href='https://github.com/ArtiomDiakov' target="blank">Artiom Diakov:</b></a> Machine Learning Engineer
</p>

<p align='center'>
    <b><a href='https://github.com/DataSciGina' target="blank">Agostina Fernández:</b></a> Machine Learning Engineer
</p>


<h2 align='center'>Alcance</h2>

Nuestro enfoque se centra en el rubro de restaurantes en Nueva York, California y Florida debido a su alto PBI per cápita y su alcance turístico. Sin embargo, el análisis y modelo podrían aplicarse en un futuro a otros tipos de comercios, otros estados o ampliarse a nivel internacional.

<<<<<<< Updated upstream
Nuestro objetivo es la recopilación, procesamiento y análisis de datos en los cinco estados con mayor PBI total de los Estados Unidos, con el propósito de comprender las opiniones de los usuarios, anticipar tendencias de crecimiento o declive en el sector de restaurantes, seleccionar ubicaciones estratégicas y desarrollar un sistema de recomendación personalizado para los usuarios.
=======
Nuestro objetivo es la recopilación, procesamiento y análisis de datos en los tres de los estados con mayor PBI total de los Estados Unidos, con el propósito de comprender las opiniones de los usuarios, anticipar tendencias de crecimiento o declive en el sector de restaurantes, seleccionar ubicaciones estratégicas y desarrollar un sistema de recomendación personalizado para los usuarios.
>>>>>>> Stashed changes

<h2 align='center' id='requirements'>Instalación y Requisitos</h2>

### Requisitos:

- Python.
- NumPy.
- Pandas.
- Matplotlib.
- Scikit-Learn.
- FastApi.
- Ubicorn.
- Power BI.

### Pasos de Instalación:

1. Clonar el repositorio: `git clone https://github.com/DataSciGina/Google-Yelp.git`
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4. Instalar las dependencias: `pip install -r requirements.txt`

<h2 align='center' id='struct'>Estructura del Repositorio</h2>

<b>📁 Google-Yelp</b>

- 📁 **data/**
    - **raw/:** Datos crudos descargados
    - **processed/:** Datos procesados y listos para análisis
    - **external/:** Fuentes de datos adicionales (externas)
- 📁 **notebooks/:** Jupyter Notebooks para exploración de datos y desarrollo del modelo
- 📁 **src/**
    - **data/:** Scripts de procesamiento y limpieza de datos
    - **features/:** Scripts para generación de características para modelos
    - **models/:** Scripts para entrenamiento y evaluación de modelos
    - **visualization/:** Scripts para generación de gráficos y visualizaciones
    - **utils/:** Funciones y utilidades auxiliares
- 📁 **reports/**
    - **figures/:** Gráficos e imágenes para informes
    - **results/:** Resultados finales del análisis y del modelo
- 📁 **tests/:** Tests para asegurar calidad en los scripts y funciones

- **README.md:** Información general del proyecto
- **requirements.txt:** Dependencias del proyecto
- **.gitignore:** Archivos y carpetas a ignorar en Git


<h2 align='center' id='use'>Uso y Ejecución</h2>

### Analizar Productos Finales:

1. **Visualización de datos:** En el directorio `reports/results` encontrarán los resultados finales de las visualizaciones en el archivo con extensión `.pbix`
2. **API:** Escribir en la terminal ubicada en la carpeta del proyecto: `uvicorn main:app --reload`

### Ejecución Completa del Proyecto

Aquí se ingresarán los pasos de ejecución de cada etapa.

<h2 align='center' id='data'>Datos y Fuentes</h2>

Datos extraídos de la plataforma de reseñas **Yelp** y de **Google Maps**, para Estados Unidos. Tiene información sobre la ubicación de los comercios, su categoría, puntajes promedios, si están abiertos o no, sobre los usuarios, las reseñas que hicieron, cuántas reseñas hicieron, cuántos votos han recibido esas reseñas entre otros.

<h2 align='center' id='stack'>Stack Tecnológico</h2>

- **Visual Studio Code:** Software para trabajar de forma local en el proyecto
- **Git:** Sistema de control de versiones distribuido, para el seguimiento de cambios en el código fuente.
- **Github:** Alojamiento de nuestro repositorio.
- **Python:** Para el procesamiento de datos.
- **Pandas y Numpy:** Manipulación de datos.
- **NLTK y SpaCy:** Análisis de lenguaje natural.
- **Scikit-Learn:** Modelado de Machine Learning.
- **SQL:** Almacenamiento y consulta de datos.
- **Matplotlib y Seaborn:** Visualización de datos.
- **PowerBI:** Visualización interactiva de datos.

<h2 align='center' id='result'>Resultados y Conclusiones</h2>

### KPIs

<<<<<<< Updated upstream
primer KPI : Tendencia de satisfacción en periodos de tiempo:

Este KPI trata de ver la evolución de la satisfacción del cliente durante periodos de tiempo

En caso de usar meses como periodo la formula seria (Satisfacción promedio del mes actual - el mes anterior % el promedio del mes anterior multiplicado x 100)

El objetivo seria identificar si la calidad de mi servicio mejora o empeora con el tiempo y tomar medias necesarias


=======
>>>>>>> Stashed changes
<h2 align='center' id='colab'>Contribución y Colaboración</h2>

<p align='center'>¿Te gustaría aportar algo al proyecto, darnos una opinión, colaborar con nosotros o proponernos algo?<br><b>¡Contáctanos!</b> Nos encantaría conocer tu opinión:</p>

<h3 align='center'><b>Nicolás Aballay</b></h3> 
<p align='center'>📫 thedarkin32@gmail.com</p>

<p align='center'>
    <a href="https://www.linkedin.com/in/nicolas-aballay-6a3543335/" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Nicolás Aballay" height="40" width="40" /></a>
    <a href="https://github.com/AballayNicolas" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000" alt="GitHub Nicolás Aballay" height="40" width="40" /></a>
</p>

<h3 align='center'><b>Santino Rocchietti</b></h3> 
<p align='center'>📫 santirocchietti777@gmail.com</p>

<p align='center'>
    <a href="https://www.linkedin.com/in/santino-mart%C3%ADn-rocchietti-7aa0b7318/" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Santino Rocchietti" height="40" width="40" /></a>
    <a href="https://github.com/Santino-Rocchietti" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000" alt="GitHub Santino Rocchietti" height="40" width="40" /></a>
</p>

<h3 align='center'><b>Esteban Nivia</b></h3>
<p align='center'>📫 aestebangnivia23@gmail.com</p>

<p align='center'>
    <a href="https://www.linkedin.com/in/andr%C3%A9s-esteban-gutierrez-nivia-9035a62b7/" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Esteban Nivia" height="40" width="40" /></a>
    <a href="https://github.com/aestebangnivia23" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000" alt="GitHub Esteban Nivia" height="40" width="40" /></a>
</p>

<h3 align='center'><b>Artiom Diakov</b></h3>
<p align='center'>📫 artiomdiakov@gmail.com</p>

<p align='center'>
    <a href="https://www.linkedin.com/in/artiom-diakov/" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Artiom Diakov" height="40" width="40" /></a>
    <a href="https://github.com/ArtiomDiakov" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000" alt="GitHub Artiom Diakov" height="40" width="40" /></a>
</p>

<h3 align='center'><b>Agostina Fernández</b></h3>
<p align='center'>📫 fernandezagostina.ra@gmail.com</p>

<p align='center'>
    <a href="https://www.linkedin.com/in/agostina-fern%c3%a1ndez-aab4a8323/" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Agostina Fernández" height="40" width="40" /></a>
    <a href="https://github.com/DataSciGina" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000" alt="GitHub Agostina Fernández" height="40" width="40" /></a>
</p>

<h2 align='center' id='autores'>Autores</h2>


<p align='center'><b>Nicolás Aballay</b></p>
<p align='center'><b>Santino Rocchietti</b></p>
<p align='center'><b>Esteban Nivia</b></p>
<p align='center'><b>Artiom Diakov</b></p>
<<<<<<< Updated upstream
<p align='center'><b>Agostina Fernández</b></p>
=======
<p align='center'><b>Agostina Fernández</b></p>
>>>>>>> Stashed changes
