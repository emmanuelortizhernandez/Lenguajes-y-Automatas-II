from flask import Flask, jsonify
import mymodule
import xlrd

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify('Hello, World!')

@app.route('/excel/columna1')
def columna():
    return jsonify('columna 1 data')

@app.route('/excel/num_hojas')
def num_hojas():
    book = xlrd.open_workbook('pagina.xls')
    num_sheets = book.nsheets
    return jsonify({'num_hojas': num_sheets}) 

@app.route('/excel/hoja/<int:hoja_num>')
def hoja(hoja_num):
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(hoja_num)
    data = []
    for row_idx in range(sheet.nrows):
        row_data = []
        for col_idx in range(sheet.ncols):
            cell_value = sheet.cell_value(row_idx, col_idx)
            row_data.append(cell_value)
        data.append(row_data)
    return jsonify(data)

@app.route('/excel/columna/<int:col_num>/<int:hoja_num>')
def columna_hoja(col_num, hoja_num):
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(hoja_num)
    data = []
    for row_idx in range(sheet.nrows):
        cell_value = sheet.cell_value(row_idx, col_num)
        data.append(cell_value)
    return jsonify(data) 

@app.route('/excel/dimensiones/<int:hoja_num>')
def dimensiones(hoja_num):
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(hoja_num)
    num_filas = sheet.nrows
    num_columnas = sheet.ncols
    return jsonify({'hoja': hoja_num, 'num_filas': num_filas, 'num_columnas': num_columnas}) 

@app.route('/modulo')
def modulo():
    return jsonify (mymodule.saludo())

@app.route('/excel/validar_columna/<int:hoja_num>/<int:col_num>/<string:nombre_columna>')
def validar_columna(hoja_num, col_num, nombre_columna):
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(hoja_num)
    
    # Obtener el valor de la celda de la cabecera de la columna
    cabecera_celda = sheet.cell_value(0, col_num)
    
    # Verificacion si el nombre es el deseado
    if cabecera_celda == nombre_columna:
        mensaje = 'La columna es valida.'
    else:
        mensaje = 'La columna no es valida.'
    
    return jsonify({'mensaje': mensaje})

@app.route('/excel/columnas/<int:hoja_num>/<int:col_num>')
def columnas(hoja_num, col_num):
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(hoja_num)
    data = []
    for row_idx in range(sheet.nrows):
        row_data = []
        for col_idx in range(col_num):
            cell_value = sheet.cell_value(row_idx, col_idx)
            row_data.append(cell_value)
        data.append(row_data)
    
    return jsonify(data)

@app.route('/excel/hoja_completa/<int:hoja_num>')
def hoja_completa(hoja_num):
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(hoja_num)
    data = []
    for row_idx in range(sheet.nrows):
        row_data = []
        for col_idx in range(sheet.ncols):
            cell_value = sheet.cell_value(row_idx, col_idx)
            row_data.append(cell_value)
        data.append(row_data)
    return jsonify(data)

if __name__ == '_main_':
    print("Main saludo")
    app.run(host="0.0.0.0")
    