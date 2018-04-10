from flask import jsonify


class messages(object):
    def __init__(self, code):
        self.code = code
    def resp(self, data):
        if self.code == 200:
            json_message = 'Request Valid'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 400:
            json_message = 'Client Not Valid Request'
            return jsonify({'Code': self.code, 'Message': json_message})
        elif self.code == 500:
            json_message = 'Server Error Response Request'
            return jsonify({'Code': self.code, 'Message': json_message})