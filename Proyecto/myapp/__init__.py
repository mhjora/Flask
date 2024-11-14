from flask import Flask
from myapp.config import DevConfig
from myapp.task.controllers import taskRoute  # Asegúrate de que tienes un Blueprint llamado `taskRoute`

# Crear la aplicación Flask
app = Flask(__name__)

# Registrar el Blueprint `taskRoute` desde el módulo de tareas
app.register_blueprint(taskRoute)

# Configurar la aplicación con el objeto de configuración `DevConfig`
app.config.from_object(DevConfig)

# Ruta de prueba
@app.route('/')
def hello_word() -> str:
    return '¡Hola Mundo!'

