from flask import jsonify


class messages(object):
    def __init__(self, __code):
        self.code = __code
    def resp(self, data):
        if self.code == 200:
            json_message = 'Request Valid'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 201:
            json_message = 'Request Created'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 202:
            json_message = 'Request Accepted'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 204:
            json_message = 'Success but Data not found'
            return  jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 400:
            json_message = 'Client Not Valid Request'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 401:
            json_message = 'Client Not Unauthorized Request'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})
        elif self.code == 500:
            json_message = 'Server Error Response Request'
            return jsonify({'Code': self.code, 'Message': json_message, 'Data': data})