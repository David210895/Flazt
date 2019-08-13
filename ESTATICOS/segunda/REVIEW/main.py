from flask import Flask,render_template,abort
app =Flask(__name__)
@app.route('/tecsup')
@app.route('/tecsup/<profesion>')
def mensaje(profesion=None):
   return render_template("template1.html",prof=profesion)
@app.route('/calculodolar/<valor>/<cantidad>')
def montosoles(valor,cantidad):
   try:
       monto=float(valor)*float(cantidad)
   except:
       abort(404)
   return render_template("template2.html",val=valor,can=cantidad,
           res=monto)

@app.route('/tabla/<valor>')
def generarmultiplo(valor):
    try:
        numero = int(valor)
    except:
        abort(404)
    return render_template("template3.html",num=numero)

@app.route('/mascotas')
def pagmascotas():
    web = [ {"url":"https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwid36rnqoDkAhXdIbkGHfHIBzAQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.bbc.com%2Fmundo%2Fnoticias-48676663&psig=AOvVaw0Az0OLlnDMgjQYWwndLxYp&ust=1565802446557924","nombre":"DUQUE"}, 
    {"url":"https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwibh_SXq4DkAhXdK7kGHY7rD5EQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.muymascotas.es%2Falimentacion%2Fperro%2Ffotos%2Fcosas-que-no-debes-dar-de-comer-a-tu-perro-y-a-lo-mejor-lo-estas-haciendo&psig=AOvVaw0Az0OLlnDMgjQYWwndLxYp&ust=1565802446557924","nombre":"OSO"},
    {"url":"https://estaticos.muyinteresante.es/media/cache/760x570_thumb/uploads/images/article/5c3871215bafe83b078adbe3/perro.jpg","nombre":"SMITH"}]
    return render_template("template4.html",sitios=web)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("error.html",error="Pagina No encontrada"),404

if __name__ == '__main__':
   app.run(debug=True,port=8000)




