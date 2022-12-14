"""
Script para convertir los archivos CSV generados por abstract_scrapper.py a
un documento BibTeX. Sólo para usar con los resultados de Springer Link.

Puede acceder a abstract_scrapper.py aquí:
https://gist.github.com/arielmachini/f6f299c69230e258f4e49ab9814b3087

Por Ariel Machini (arielmachini (at) protonmail (dot) com).
"""

import csv
import os
import sys
import textwrap

# Defino como "constantes" a los índices correspondientes a las columnas del documento CSV:
ITEM_TITLE, ITEM_DOI, AUTHORS, PUBLICATION_YEAR, CONTENT_TYPE, URL, ABSTRACT = 0, 1, 2, 3, 4, 5, 6

print("\n*** CONVERSOR DE RESULTADOS DE SPRINGER (.csv -> .bib)")
print("Este script tiene como finalidad convertir los archivos CSV generados por abstract_scrapper.py a un documento BibTeX.\nEscrito por Ariel Machini.")

try:
    os.remove("./BibTeXGenerado.bib") # Se elimina el documento .bib si ya existe.
except OSError as e:
    pass # No hace falta hacer nada.

for i in range(1, len(sys.argv)):
    rutaDocumentoCsv = sys.argv[i]
    contenidoBibtex = ""
    
    with open(rutaDocumentoCsv) as documentoCsv:
        lectorDocumentoCsv = csv.reader(documentoCsv, delimiter = ",")
        lineasProcesadas = 0
        
        for fila in lectorDocumentoCsv:
            if fila[CONTENT_TYPE] == "Article":
                contenidoBibtex = contenidoBibtex + "@article {Art%s%s,\n" \
                    "\ttitle = {%s},\n" \
                    "\tauthor = {%s},\n" \
                    "\tyear = {%s},\n" \
                    "\tdoi = {%s},\n" \
                    "\tabstract = {%s},\n" \
                    "\turl = {%s},\n}\n\n" % (lineasProcesadas, fila[PUBLICATION_YEAR], fila[ITEM_TITLE], fila[AUTHORS], fila[PUBLICATION_YEAR], fila[ITEM_DOI], fila[ABSTRACT], fila[URL])
            elif fila[CONTENT_TYPE] == "Chapter":
                contenidoBibtex = contenidoBibtex + "@incollection {Cap%s%s,\n" \
                    "\ttitle = {%s},\n" \
                    "\tauthor = {%s},\n" \
                    "\tyear = {%s},\n" \
                    "\tdoi = {%s},\n" \
                    "\tabstract = {%s},\n" \
                    "\turl = {%s},\n}\n\n" % (lineasProcesadas, fila[PUBLICATION_YEAR], fila[ITEM_TITLE], fila[AUTHORS], fila[PUBLICATION_YEAR], fila[ITEM_DOI], fila[ABSTRACT], fila[URL])
            else:
                if (lineasProcesadas > 0):
                    print(f"ERROR: Tipo de contenido no reconocido en la fila {lineasProcesadas} del documento \"{os.path.basename(rutaDocumentoCsv).split('/')[-1]}\".")
                    
                    lineasProcesadas -= 1
            
            lineasProcesadas += 1
        
        documentoBibtex = open("./BibTeXGenerado.bib", "a")
        documentoBibtex.write(textwrap.dedent(contenidoBibtex))
        documentoBibtex.close()

        print(f"\n* {lineasProcesadas} líneas del documento \"{os.path.basename(rutaDocumentoCsv).split('/')[-1]}\" fueron procesadas exitosamente.")

print(f"\n*** ¡El documento BibTeX fue generado exitosamente! :)")
