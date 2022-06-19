import flask
import json
from flask import request

from data_type_handlers import get_data_handler
from helpers import get_data_from_request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/store/add', methods=['POST'])
def insert_record():
    data = get_data_from_request(request.data)
    handler = get_data_handler(data)
    result = handler.create()
    return result


@app.route('/store/add-many', methods=['POST'])
def insert_bulk_records():
    data = get_data_from_request(request.data)
    handler = get_data_handler(data)
    result = handler.bulk_create()
    return result


@app.route('/store/get', methods=['GET'])
def get_records():
    id_ = int(request.args.to_dict().get('id'))
    data = get_data_from_request(request.data)
    handler = get_data_handler(data)
    result = handler.get(id_)
    return result


@app.route('/store/update', methods=['PATCH'])
def update_record():
    id_ = int(request.args.to_dict().get('id'))
    data = get_data_from_request(request.data)
    handler = get_data_handler(data)
    result = handler.update(id_)
    return json.dumps(result)


@app.route('/store/delete', methods=['DELETE'])
def delete_record():
    id_ = int(request.args.to_dict().get('id'))
    data = get_data_from_request(request.data)
    handler = get_data_handler(data)
    msg = handler.update(id_)
    return msg
