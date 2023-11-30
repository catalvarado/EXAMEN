from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/calculocompras', methods=['GET', 'POST'])
def calculocompras():
    if request.method == 'POST':
        resultado1 = str(request.form['nombre'])
        edad = int(request.form['edad'])
        pintura = int(request.form['pintura'])
        resultado2 = pintura * 9000
        if edad < 18:
            resultado3 = 0
            resultado4 = resultado2
        elif 18 <= edad <= 30:
            resultado3 = resultado2 * 0.15
            resultado4 = resultado2 - resultado3
        else:
            resultado3 = resultado2 * 0.30
            resultado4 = resultado2 - resultado3
        return render_template('calculocompras.html', resultado1=resultado1, resultado2=resultado2, resultado3=resultado3, resultado4=resultado4)
    return render_template('calculocompras.html')


@app.route('/iniciosesion', methods=['GET', 'POST'])
def iniciosesion():
    if request.method == 'POST':
        nombre = str(request.form['tunombre'])
        contraseña = str(request.form['contraseña'])

        if nombre.lower() == "juan" and contraseña == "admin":
            resultado1 = str("Bienvenido administrador juan")
        elif nombre.lower() == "pepe" and contraseña == "user":
            resultado1 = str("Bienvenido usuario pepe")
        else:
            resultado1 = str("Usuario o contraseña incorrectos")

        return render_template('iniciosesion.html', resultado1=resultado1)
    return render_template('iniciosesion.html')


if __name__ == '__main__':
    app.run(debug=True)
