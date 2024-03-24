from bottle import Bottle, request, HTTPError
from app.evaluate import find_matches
from app.deobfuscation.clean import normalize

import json

app = Bottle()

@app.route('/check', method='POST')
def check():
    data = request.json

    header_from_name = data['header_from_name']
    company_users = data['company_users']

    normalized_header_from_name = normalize(header_from_name)

    results = []
    for user in company_users:
        result = find_matches(normalized_header_from_name, user['first_name'], user['last_name'])
        if result:
            results.append(result)
    return json.dump(results, indent=4)