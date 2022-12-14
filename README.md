# Springer2BibTeX
![Captura de pantalla de Springer2BibTeX en funcionamiento](https://i.imgur.com/pWs4HP0.png "Springer2BibTeX en funcionamiento")\
Script para convertir los archivos CSV generados por `abstract_scrapper.py` a un documento BibTeX. Sólo para usar con los resultados de [Springer Link](https://link.springer.com).

**Puede acceder a** `abstract_scrapper.py` **aquí:**\
https://gist.github.com/arielmachini/f6f299c69230e258f4e49ab9814b3087

## Modo de uso
`python springerABibtex.py [ruta a los archivos CSV de entrada]`<br/>\
**Ejemplo:**\
`python springerABibtex.py ./archivo1.csv ./archivo2.csv`<br/>\
**Todos** los elementos contenidos en los archivos CSV que el script recibe como entrada se exportan a un mismo archivo `.bib`.

## Idea de uso
Tal como está escrito, este script debe ser utilizado en conjunto con `abstract_scrapper.py`. En el siguiente diagrama se describe cómo:<br/>\
![Diagrama](https://i.imgur.com/7TVoFB7.png "Diagrama")
