#verificar por consola si python esta instalado (python --version)
#verificar si pip esta instalado(pip --version)
#instalcion de flaxk o django ( ejmo flask : pip install flask)

from flask import Flask, render_template # import a libreria flask ya instalda previamente y render_tempalte 
                                         # para los retornos de plantilla

#import pyodbc

app =Flask(__name__) #archivo principal del archivo
@app.route('/')# creacion de ruta o url ruta de pagina incial
def home(): #creacion de la funcion
    return  render_template('home.html')#retorno de la plantilla home creada en la carpeta template

@app.route('/about') #creacion de otra ruta
def about():
   # una forma de reotrar la ruta  
   # return 'About page'
   # Otra forma de retornar la plantilla (la plantilla está previamente creada en la carpeta template)
   return render_template('about.html')

@app.route('/Productos')
def Productos():
    return  render_template('Productos.html')


@app.route('/Compras')
def Compras():
     return render_template('Compras.html')
    
@app.route('/Registro')
def Registro():
    return render_template('Registro.html')

STATIC_URL= '/static'  
if __name__ == '__main__': # paso para que la pagina se quede escuchando
    app.run(debug=True)# para no reiciar el servidor mientras se hacen cambios
    