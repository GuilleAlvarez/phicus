# Prueba conocimiento Phicus #

## Table of Contents
1. [Instalacion](#instalacion)
2. [Iniciar la aplicación](#iniciar-la-app)
3. [Metodologia y desarrollo](#metodologia)
4. [Alcance](#alcance)

### Instalacion
Para poder realizar la instalacion del software es recomendable crear un entorno virtual con el comando:

```
$ virtualenv venv
```
```
$ source venv/bin/activate
```
```
$ pip install -r requirements.txt
```
 
### Iniciar la aplicación
Para iniciar la aplicación se ejecuta
```
$ python app.py
```
Cabe destacar que esta puesta para que funcione por terminal. En siguientes secciones se hablara más sobre el alcance de la misma.

### Metodologia y desarrollo
Para la realizacion de las tareas se ha utilizado la arquitectura hexagonal el cual nos permite separar la logica de la aplicaicon con el resto de modulos externos como puede ser una base de datos
o la forma de representar los dtos, etc. Ademas de dicha arquitectura se ha utilizado patrones de diseño de software para la realizacion de codigo limpio en todas sus facetas, se ha utilizado el Paton Singletos para
solo tener una instancia de aquellas clases que solo haga falta una y por ende tener mejor rendimiento. Se ha utilizado el patron de adaptadores cuando se disponia a la representacion de datos
como es el caso de la terminal o de la API REST. 

En las distintas tareas de desarrollo se utilizo git flow para tener una mejor gestion de las tareas, correcciones y refactoring que se estaban llevando a cabo.

### Alcance
Se han desarrollado los requisitos minimos y los siguientes puntos a mayores en distintos grados de consecución:
* Implamantar el juego a travez de un API Rest: Parcial. En este aspecto cabe destacar que lo más costoso fue separar la logica de negocio con el intercambio hacia afuera de informacion.
  En este caso se han llevado a cabo 2 adaptadores para dicho intercambio, el terminal y un servicio http. Esto se refleja en el directorio cliente/infrastructure/ en el cual se encuentran
  los 2 adaptadores. Tan solo para utilizar uno u otro se debe especificar en la clase App del archivo app.py haciendo que la logica de negocio del juego quede aislada e independiente.
* Realizacion de test unitarios: se realizan con la libreria pytest. En esta parte se ha realizado un test de ejemplo Mockeando los distntos intercambios con el resto de modulos. Ademas, se
  ha puesto a disposicion 2 comandos (run_tests.sh y run_test_coverage.sh) para facilitar la tarea de relanzar los test.
 
