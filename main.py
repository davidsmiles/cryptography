from flask import Flask
from flask_restful import Api

from resources.keys import PrivateKey, PublicKey
from resources.signature import Signature
from resources.verification import Verification

app = Flask(__name__)
api = Api(app)


api.add_resource(PrivateKey, '/privatekey')
api.add_resource(PublicKey, '/publickey')
api.add_resource(Signature, '/sign')
api.add_resource(Verification, '/verify')


if __name__ == '__main__':
    app.run(debug=True)



