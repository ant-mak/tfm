# Redes Generativas Antagónicas
Trabajo Fin de Máster.

**Autor:** Antón Makarov Samusev.

**Director:** Francisco Javier Yáñez Gestoso.

Máster en Tratamiento Estadístico Computacional de la Información. Universidad Complutense de Madrid y Universidad Politécnica de Madrid.

## Imágenes de ejemplo
Imagen

## Contenido
Trabajo fin de máster sobre redes generativas antagónicas. En el repositorio se incluye:
- Memoria
- Presentación
- Código PyTorch en el que se implementa una [DCGAN](https://arxiv.org/abs/1511.06434) para la generación de arte a partir de un conjunto de datos obtenido en [Kaggle](https://www.kaggle.com/c/painter-by-numbers)
- Imágenes y gifs generados
- Otros recursos

## Instrucciones para reproducir los resultados
Se ha tratado de hacer el código y los resultados lo más accesibles posible. Para reproducir los experimentos hay que seguir los pasos siguientes:

1. Descargar el repositorio o clonarlo (necesario instalar [git](https://git-scm.com)) haciendo `git clone https://github.com/ant-mak/tfm.git`.
2. Instalar [Anaconda](https://www.anaconda.com)
3. Crear un entorno virtual, introduciendo en la consola `conda create -n tfm_anton python=3.6` y activar el entorno con `conda activate tfm_anton`.
4. Instalar los paquetes del archivo `requirements.txt` introduciendo en la consola `pip install -r requirements.txt`. Por defecto se instalará la versión CPU de PyTorch, Si se quiere hacer el entrenamiento desde cero, es recomendable utilizar una gpu y descargar la versión correspondiente.
5. Ejecutar en la consola `setup.py` para crear todos los directorios necesarios y la estructura del proyecto. Es posible que necesite permisos de administrador.
6. Descargar de [Kaggle](https://www.kaggle.com/c/painter-by-numbers/data) los archivos `train.zip` y `test.zip` (aproximadamente `50 GB` en total), descomprimirlos en la **misma** carpeta dentro de `data/paintings`
7. Ejecutar en la consola `python rm_corrupt.py` para eliminar del conjunto de datos las imágenes corruptas.
8. Ejecutar en la consola `jupyter notebook` y abrir el archivo `taltal`.
9. Ejecutar las celdas de manera secuencial (Se incluyen modelos ya entrenados en la carpeta `models` que se pueden cargar y evitar tener que entrenar desde cero).

**Nota:** El resultado puede variar ligeramente a causa de las semillas utilizadas.

## Bibliografía principal
- Uno
- Dos
- Tres
