# Consideraciones de Frame3dd
permite el calculo estático  y  dinámico  de estructuras elásticas.
mediante el  uso de la terminal de comandos
este programa  funciona como parte de la linea de  comandos, se recomienda
vincularlo a la terminal de trabajo, sea powershell, o la terminal 

# Configurando en powershell
*resume epicamente como se pone un comando en  powershell*

# Configurando en terminal linux via bashrc
*explica epicamente como se hace*

# Consideraciones Adicionales de los ejemplos
este repositorio reune algunos ejemplos de uso de este programa,
en caso  use esta  info por favor referencie
los ejemplos han considerado que el comando de uso será *frame3dd*
se usaran algunos scripts en python para automatizar el uso pero
es posible prescindir  de ellos si se usa la terminal unicamente

# Documentacion oficial del proyecto
el proyecto frame3dd es de codigo abierto, por lo que puede ser 
descargado y analizado por cualquier usuario
[Pagina del proyecto](http://frame3dd.sourceforge.net/)
[Documentacion en ingles](http://svn.code.sourceforge.net/p/frame3dd/code/trunk/doc/Frame3DD-manual.html)
[Repositorio](https://sourceforge.net/p/frame3dd/code/HEAD/tree/)

# Resumen de los atributos del comando
para usar el comando *frame3dd* se pueden usar  los siguientes  atributos

| atributos comando    | descripcion                                                              |
|----------------------|--------------------------------------------------------------------------|
| -i <ArchivoEntrada>  |define archivo con datos de entrada                                       |
| -o <ArchivoSalida>   |define archivo para datos de salida                                       |
| -h                   |muestra  ayuda y sale                                                     |
| -v                   |muestra la version e info del programa y sale                             |
| -a                   |muestra la version e info del autor, y sale                               | 
| -c                   |comprueba  si la data ingresada es correcta                               |
| -w                   |escribe matrices de masa  y rigidez                                       |
| -x                   |suprime la escritura de 't' o 'c' para señal de fuerzas axiales           |
| -q                   |suprime la salida de la pantalla excepto los mensajes de advertencia      |
| -s On/Off            |On: incluye la deformación por cortante o Off: ignora                     |
| -g On/Off            |On: incluye la rigidez geométrica o Off: ignora                           |
| -e <valor>           |factor de exageración de la deformación estática para la salida de Gnuplot|
| -z                   |fuerza trazado X-Y-Z                                                      |
| -l On/Off            |On: matriz de masa concentrada o Off: matriz de masa consistente          |
| -f <valor>           |cambio de frecuencia modal para estructuras no restringidas               |
| -m J/S               |método de análisis modal: J=Jacobi-Subspace o S=Stodola                   |
| -t <valor>           |tolerancia de convergencia para análisis modal                            |
| -p <valor>           |tasa de desplazamiento para animación de forma de modo                    |
| -r <valor>           |método de condensación de matriz: 0, 1, 2 o 3                             |

- En caso se escriban matrices estas seran Ks (matriz de rigidez), Kd ,Md(matriz de masa)

# metodo de calculo en frame3dd
el metodo  que utiliza este programa, es el metodo matricial de la rigidez y el analisis
se realiza colocando coordenadas de los nodos y colocando las propiedades simples de estos
[Metodo matricial de la rigidez](https://es.wikipedia.org/wiki/M%C3%A9todo_matricial_de_la_rigidez)




 
