from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from flask import request
from flask_restful import Resource

from helper import sign


class Signature(Resource):

    @classmethod
    def post(cls):
        private_key = request.files['private_key']
        private_key = serialization.load_pem_private_key(
            private_key.read(),
            password=None,
            backend=default_backend()
        )

        document = request.files['document'].read()
        signature = sign(private_key, document)

        # Save signature to Disk
        with open('signature.txt', 'wb') as s:
            s.write(signature)
            s.close()

        return {'message': 'Document signed successfully'}, 200
