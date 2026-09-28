"""API mínima de pedidos."""

from flask import Flask, jsonify, request

app = Flask(__name__)
_pedidos = {}
_siguiente_id = 1


@app.post("/pedidos")
def crear_pedido():
    global _siguiente_id
    datos = request.get_json(force=True)
    pedido = {"id": _siguiente_id, "producto": datos["producto"], "cantidad": datos["cantidad"]}
    _pedidos[_siguiente_id] = pedido
    _siguiente_id += 1
    return jsonify(pedido), 201


@app.get("/pedidos/<int:pedido_id>")
def obtener_pedido(pedido_id):
    pedido = _pedidos.get(pedido_id)
    if pedido is None:
        return jsonify({"error": "no encontrado"}), 404
    return jsonify(pedido)
