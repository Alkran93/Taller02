from flask import Blueprint, jsonify, render_template
import socket
from .pokeneas_data import pokenea_random

routes = Blueprint("routes", __name__)

@routes.route("/api/pokenea")
def api_pokenea():
    p = pokenea_random()
    data = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "contenedor_id": socket.gethostname()
    }
    return jsonify(data)

@routes.route("/pokenea")
def show_pokenea():
    p = pokenea_random()
    return render_template(
        "pokenea.html",
        pokenea=p,
        contenedor_id=socket.gethostname()
    )
