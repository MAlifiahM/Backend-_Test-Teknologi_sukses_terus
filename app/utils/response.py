from flask import jsonify

def template_response(message, data=None, error=False, response_code=200):
    response = {
        'message': message,
    }

    if not error:
        response['data'] = data
    response = jsonify(response)
    response.status_code = response_code
    return response