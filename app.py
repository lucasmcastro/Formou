from flask import (
    Flask, render_template, flash,
    url_for, redirect, request
)
app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'Evolux <3 Python',
    'DEBUG': True
})

@app.route('/<nome>')
def hello(nome):
    return "Hello World %s!" % nome

@app.route("/", methods=['GET', 'POST'])
def formou():
    if request.method == 'POST':
        if request.form.get('nome'):
            return redirect(
                url_for(
                    'hello', 
                    nome=request.form.get('nome')
                )
            )
        else:
            flash('Pfv poe o nome.')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
