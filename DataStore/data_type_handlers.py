import json

from conf import data_store_file_name


def get_data_handler(data):
    if data['data_format'] == 'json':
        return JSONHandler(data)
    if data['data_format'] == 'xml':
        return XMLHandler


class BaseHandler:
    def __init__(self, data, **kwargs):
        self.request_data = data
        self.user_data = data['data'] if 'data' in data else {}
        self.file_path = data_store_file_name
        self.file_data = self.get_from_file()

    def get_from_file(self):
        with open(self.file_path, 'r') as f: return json.loads(f.read())

    def add_to_file(self):
        with open(self.file_path, 'w') as f: json.dump(self.file_data, f, indent=4)


class JSONHandler(BaseHandler):
    def __init__(self, data, **kwargs):
        super(JSONHandler, self).__init__(data, **kwargs)

    def get(self, id_):
        result, idx = self.__find_record(id_)
        if not result:
            result = 'Record not found'
        return result

    def create(self):
        store_data = self.file_data['store_data']
        current_id = self.file_data['current_id']

        user_data = self.user_data[0]
        user_data['id'] = current_id
        store_data.append(user_data)

        self.file_data['store_data'] = store_data
        self.file_data['current_id'] += 1
        self.add_to_file()
        return user_data

    def bulk_create(self):
        store_data = self.file_data['store_data']
        current_id = self.file_data['current_id']

        for obj in self.user_data:
            obj['id'] = current_id
            store_data.append(obj)

            self.file_data['store_data'] = store_data
            self.file_data['current_id'] += 1
            self.add_to_file()

        return 'Data added'

    def update(self, id_):
        store_data = self.file_data['store_data']
        result, idx = self.__find_record(id_)
        if result:
            result.update(self.user_data)
            store_data[idx] = result
            self.file_data['store_data'] = store_data
            self.file_data['current_id'] += 1
            self.add_to_file()
            return result
        else:
            return 'Record not found'

    def delete(self, id_):
        store_data = self.file_data['store_data']
        result, idx = self.__find_record(id_)
        if result:
            store_data.pop(idx)
            self.file_data['store_data'] = store_data
            self.file_data['current_id'] += 1
            self.add_to_file()
            return 'Record deleted successfully'
        else:
            return 'Record not found'

    def __find_record(self, id_):
        return next(((record, i) for i, record in enumerate(self.file_data['store_data']) if record['id'] == id_), (None, None))


class XMLHandler(BaseHandler):
    def __init__(self, data, **kwargs):
        kwargs['data'] = data
        super(BaseHandler, self).__init__(**kwargs)

    def create(self):
        pass

    def bulk_create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
