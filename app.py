from flask import Flask, render_template, jsonify

app = Flask(__name__)

#usuarios = ['Lusciana', 'Ana', 'Paulo', 'Jorge', 'Helena', 'Diego', 'Júlia']
usuarios = {
    'Lusciana': { 
        'senha':'101'
    },
    'Ana': { 
        'senha':'102'
    },
    'Paulo': { 
        'senha':'103'
    },
    'Jorge': { 
        'senha':'104'
    },
    'Helena': { 
        'senha':'105'
    },
    'Diego': { 
        'senha':'106'
    },
    'Júlia': { 
        'senha':'107'
    },
}

#print(usuarios.keys())

# Rota principal
@app.route('/')
def home():
    return 'Hello World!'

@app.route('/usuarios')
def listar_usuarios():
     # Converte as chaves para uma lista
    chaves_lista = list(usuarios.keys())
    
    return chaves_lista

if __name__ == '__main__':
    app.run(debug=True)