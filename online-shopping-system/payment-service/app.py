from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields
import random
import time

app = Flask(__name__)
CORS(app)

# Swagger configuration
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Payment Service API"
    }
)
app.register_blueprint(swaggerui_blueprint)

class PaymentSchema(Schema):
    amount = fields.Float(required=True)

class PaymentResponseSchema(Schema):
    status = fields.Str()
    message = fields.Str()
    transaction_id = fields.Str()

@app.route('/static/swagger.json')
def swagger_spec():
    spec = APISpec(
        title='Payment Service API',
        version='1.0.0',
        openapi_version='3.0.2',
        plugins=[MarshmallowPlugin()],
    )

    # Add schemas to spec
    spec.components.schema('Payment', schema=PaymentSchema)
    spec.components.schema('PaymentResponse', schema=PaymentResponseSchema)

    # Document endpoints
    spec.path(
        path='/pay',
        operations={
            'post': {
                'summary': 'Process payment',
                'description': 'Process a payment transaction',
                'requestBody': {
                    'required': True,
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/Payment'}
                        }
                    }
                },
                'responses': {
                    '200': {
                        'description': 'Payment processed successfully',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/PaymentResponse'}
                            }
                        }
                    },
                    '400': {
                        'description': 'Invalid payment data or payment failed'
                    }
                }
            }
        }
    )

    return jsonify(spec.to_dict())

@app.route('/pay', methods=['POST'])
def process_payment():
    payment_data = request.json
    
    if not payment_data or 'amount' not in payment_data:
        return jsonify({'error': 'Invalid payment data'}), 400

    # Simulate payment processing
    time.sleep(1)
    success = random.choice([True, True, True, False])  # 75% success rate

    if success:
        return jsonify({
            'status': 'success',
            'message': 'Payment processed successfully',
            'transaction_id': f'txn_{random.randint(1000, 9999)}'
        })
    else:
        return jsonify({
            'status': 'failed',
            'message': 'Payment processing failed'
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004) 