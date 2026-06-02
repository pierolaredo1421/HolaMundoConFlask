# ── IMPORTACIONES ──────────────────────────────────────────
from flask import Flask, render_template

# ── CREAR LA APLICACIÓN ────────────────────────────────────
app = Flask(__name__)

# ── DEFINIR LA RUTA PRINCIPAL ──────────────────────────────
@app.route('/')
def index():
    # Cuando alguien visita la raíz (/), Flask devuelve index.html
    return render_template('index.html')

# ── EJECUTAR EL SERVIDOR ───────────────────────────────────
if __name__ == '__main__':
    # debug=True: muestra errores detallados durante desarrollo
    app.run(debug=True)