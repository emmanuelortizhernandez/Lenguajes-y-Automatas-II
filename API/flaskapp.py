# importanción del modulo de flask la clase flask
import funciones as excel

from flask import Flask, jsonify

"""
Jsonify le da formato de json a lo que retorna
"""

app = Flask(__name__)


"""
Regresa numero de hojas
"""
@app.route("/numero_de_hoja/<file>")
def pages(file):
    return jsonify({"Hojas en el libro: ": excel.num_hojas(file)})

"""
Regresa numero de filas
"""
@app.route("/filas_columnas/<file>/<int:page>")
def cols_rows(file, page):
    rows, cols = excel.filas_column(file, page)
    return jsonify({"Filas: ": rows, "Columnas": cols})

"""
Regresa una celda
"""
@app.route("/celda/<file>/<int:page>/<int:row>/<int:col>")
def cell_info(file, page, row, col):
    return jsonify({"Celda: ": excel.cell_info(file, page, row, col)})

"""
Regresa cuantas columnas tiene una pagina
"""
@app.route("/columna/<file>/<int:page>/<int:col>")
def col_info(file, page, col):
    return jsonify({"Columna: ": excel.col_info(file, page, col)})

"""
Busca ID dentro de una pagina
"""
@app.route("/findId/<file>/<int:page>/<int:id>")
def id_find(file, page, id):
    return jsonify({"Fund: ": excel.id_find_xls(file, page, id)})

"""
Regresa todos los valores de las columnas
"""
@app.route("/valuesCols/<file>/<int:page>/<cols>")
def values_cols(file, page, cols):
    # print(cols)
    return jsonify({"Cols: ": excel.show_cols(file, page, cols)})

"""
Regresa una matriz de toda una hoja
"""
@app.route("/matrizSheet/<file>/<int:page>")
def matrix(file, page):
    return jsonify({"Matrix: ": excel.matriz_sheet(file, page)})


if __name__ == "__main__":
    app.run()

    