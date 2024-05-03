from flask import Flask
from configuration import confgure_all

#Inicialização
app = Flask(__name__)

confgure_all(app)
#Recarrega o servidor o web a cada atualização
app.run(debug=True)
