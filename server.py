import os
import json
from uuid import uuid4
from datetime import datetime
from bottle import get, post, run, request, static_file

@post('/api/<endpoint>')
def api(endpoint):
    directory = os.path.join("data", endpoint)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = uuid4().hex + ".json"
    with open(os.path.join(directory, filename), "wt", encoding="utf8") as fout:
        data = {}
        data["json"] = request.json
        data["time"] = str(datetime.now())
        json.dump(data, fout, indent=2)
    return filename

@get('/')
@get('/<filename:path>')
def base(filename='index.html'):
    if ".htm" not in filename:
        filename += ".html"
    return static_file(filename, root='app')

run(host='0.0.0.0', port=8080)
