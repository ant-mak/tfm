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
- Código PyTorch en el que se implementa una DCGAN (https://arxiv.org/abs/1511.06434) para la generación de arte a partir de un conjunto de datos obtenido en Kaggle (https://www.kaggle.com/c/painter-by-numbers)

## Instrucciones para reproducir los resultados
Se ha tratado de hacer el código y los resultados lo más accesibles posible. Para reproducir los experimentos hay que seguir los pasos siguientes:

1. Instalar Anaconda (https://www.anaconda.com)
2. Crear un entorno virtual, introduciendo en la consola `conda create tfm_anton python=3.6` y activar el entorno con `conda activate tfm_anton`
3. Instalar los paquetes del archivo `requirements.txt` introduciendo en la consola `pip install`
3.1. Obs. Por defecto se instalará la versión CPU de PyTorch, Si se quiere hacer el entrenamiento desde cero, es recomendable utilizar una gpu y descargar la versión correspondiente
4. Ejecutar en la consola `jupyter notebook` y abrir el archivo `taltal`
5. Ejecutar las celdas de manera secuencial

**Nota 1:** El entrenamiento puede llevar mucho tiempo.
**Nota 2:** El resultado puede variar ligeramente a causa de las semillas utilizadas.

## Bibliografía principal
- Uno
- Dos
- Tres
