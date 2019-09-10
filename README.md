# Redes Generativas Antagónicas
Trabajo Fin de Máster.

**Autor:** Antón Makarov Samusev.

**Director:** Francisco Javier Yáñez Gestoso.

Máster en Tratamiento Estadístico Computacional de la Información. Universidad Complutense de Madrid y Universidad Politécnica de Madrid.

## Algunos ejemplos de imágenes generadas
![gen_image](/images/results/generated_data.png?raw=true "generated_images")

## Evolución de la muestra de control a lo largo del entrenamiento
![evolution_gif](/animations/animation_19_7_14_11.gif)

## Contenido
Trabajo fin de máster sobre redes generativas antagónicas. En el repositorio se incluye:
- Memoria
- Presentación
- Código PyTorch en el que se implementa una [DCGAN](https://arxiv.org/abs/1511.06434) para la generación de arte a partir de un conjunto de datos obtenido en [Kaggle](https://www.kaggle.com/c/painter-by-numbers)
- Imágenes y gifs generados
- Otros recursos

## Instrucciones para reproducir los resultados
Se ha tratado de hacer el código y los resultados lo más accesibles posible. Para reproducir los experimentos hay que seguir los pasos siguientes:

1. Clonar el repositorio (necesario instalar [git](https://git-scm.com)) introduciendo en la consola:
```
git clone https://github.com/ant-mak/tfm.git
```

2. Instalar [Anaconda](https://www.anaconda.com)

3. Crear un entorno virtual y activarlo, introduciendo en la consola:
```
conda create -n tfm_anton python=3.6
conda activate tfm_anton
```

4. Instalar los paquetes del archivo `requirements.txt` introduciendo en la consola
```
pip install -r requirements.txt
```
Por defecto se instalará la versión CPU de PyTorch, Si se quiere hacer el entrenamiento desde cero, es recomendable utilizar una GPU y descargar la versión correspondiente siguiendo las instrucciones de la web de [PyTorch](https://pytorch.org).

5. Descargar de [Kaggle](https://www.kaggle.com/c/painter-by-numbers/data) los archivos `train.zip` y `test.zip` (aproximadamente `50 GB` en total), descomprimirlos en la **misma** carpeta dentro de `data/paintings`, quedando la ruta `data/paintings/test/` con las imágenes de ambas carpetas dentro.

6. Ejecutar en la consola `python rm_corrupt.py` para eliminar del conjunto de datos las imágenes corruptas.

7.1. [Entrenamiendo desde cero] Ejecutar en la consola `jupyter notebook` y abrir el archivo `tfm_teci_antonmakarov_gan-paintings.ipynb` ubicado en la carpeta `src`, ejecutando todas las celdas de manera secuencial.
  
7.2. [Uso de modelo entrenado] Ejecutar en la consola `jupyter notebook` y abrir el archivo `tfm_teci_antonmakarov_gan-paintings.ipynb` ubicado en la carpeta `src`, ejecutando todas las celdas de manera secuencial. (TODO)

**Nota:** El resultado puede variar ligeramente a causa de las semillas utilizadas.
