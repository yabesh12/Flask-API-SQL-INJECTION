from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_sanitized(input_string):
    """
    Check if the input string contains SQL injection characters.

    Args:
        input_string (str): The input string to be checked.

    Returns:
        bool: True if the input is sanitized, False if it contains SQL injection characters.
    """
    # Check for SQL injection characters
    sql_injection_pattern = re.compile(r'(\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bDROP\b|\bCREATE\b|\bALTER\b)', re.IGNORECASE)
    
    # Check for any non-alphanumeric characters
    if sql_injection_pattern.search(input_string) or re.search(r'[^a-zA-Z0-9]', input_string):
        return False
    return True

@app.route('/v1/sanitized/input/', methods=['POST'])
def sanitize_input():
    """
    Receive a JSON payload via a POST request and check if the input is sanitized.

    Returns:
        JSON: A JSON response indicating whether the input is sanitized or not.
    """
    data = request.get_json()

    if 'input' not in data:
        return jsonify({"error": "Missing 'input' in the payload"}), 400

    input_string = data['input']

    if is_sanitized(input_string):
        return jsonify({"result": "sanitized"})
    else:
        return jsonify({"result": "unsanitized"})
    

if __name__ == '__main__':
    app.run(debug=True)
