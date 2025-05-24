"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

        # Saltar las primeras 4 líneas (encabezado)
    data = []
    for line in lines[4:]:
        if re.match(r'^\s*\d+', line):
                # Nueva fila
            parts = re.split(r'\s{2,}', line.strip())
            if len(parts) >= 4:
                    cluster, cantidad, porcentaje, palabras = parts[:4]
                    palabras_clave = palabras
                    data.append([int(cluster), int(cantidad), float(porcentaje.replace(',', '.').replace('%', '')), palabras_clave])
            else:
                    # Continuación de palabras clave
                    data[-1][3] += ' ' + parts[0]
        else:
                # Continuación de palabras clave
            if data:
                data[-1][3] += ' ' + line.strip()

        # Formatear palabras clave
    for row in data:
        palabras = row[3]
        palabras = re.sub(r'\s+', ' ', palabras)  # Un solo espacio
        palabras = palabras.replace('.', '')      # Sin puntos
        palabras = ', '.join([w.strip() for w in palabras.split(',')])
        row[3] = palabras

    df = pd.DataFrame(data, columns=[
        'cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'
    ])

    return df

print(pregunta_01())