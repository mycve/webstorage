import json
import os
from flask import Flask, jsonify, request, render_template
import uuid
import shutil
from werkzeug.utils import secure_filename

app = Flask(__name__)
if not os.path.exists("./static/files"):
    os.mkdir("./static/files")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api", methods=["GET", "POST"])
def api():
    if request.args.get("action") == "upload":
        f = request.files["file"]
        path_name = uuid.uuid4().hex
        os.mkdir(os.path.join(r".\static\files", r"{}".format(path_name)))
        filepath = os.path.join(r".\static\files", r"{}\{}".format(path_name, secure_filename(f.filename)))
        f.save(filepath)
        return jsonify({"code": 0, "path": filepath})
    elif request.args.get("action") == "file_list":
        _data = []
        for file_path in os.listdir("static/files"):
            file_name = os.listdir("static/files/{}".format(file_path))[0]
            full_path = "static/files/{}/{}".format(file_path, file_name)
            ctime = os.path.getctime(full_path)*1000
            file_size = os.path.getsize(full_path)
            _data.append({"uid": file_path, "filename": file_name, "down_path": full_path, "uptime": ctime, "filesize": file_size})
        return jsonify({"code": 0, "data": _data})
    elif request.args.get("action") == "del":
        path = json.loads(request.data.decode())["path"]
        shutil.rmtree(os.path.join("./static/files", secure_filename(path)))
        return jsonify({"code": 0})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8899, debug=False, threaded=True)
