from flask import jsonify


def success_response(data=None, status_code=200, **extra):
    body = {"success": True, "data": data}
    body.update(extra)
    return jsonify(body), status_code


def error_response(message, status_code=400):
    return jsonify({"success": False, "error": message}), status_code
