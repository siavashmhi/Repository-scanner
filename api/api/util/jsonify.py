from flask import current_app

APP_CODES = {
    100: "ok",
    101: "Feature is not implemented.", 
    102: "Database error.",
    103: "Schema validation failed.",
    104: "Schema instance error.",
}


def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
    resource = {}
    resource["output"] = state
    resource["metadata"] = metadata
    resource["status"] = {"code": code}
    if current_app.debug:
        resource["status"]["message"] = APP_CODES[code]
    return resource, status, headers
