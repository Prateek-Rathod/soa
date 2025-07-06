from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields

app = Flask(__name__)
CORS(app)

# Swagger configuration
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Product Service API"
    }
)
app.register_blueprint(swaggerui_blueprint)

# API Documentation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()

# In-memory product database
products = []

@app.route('/static/swagger.json')
def swagger_spec():
    spec = APISpec(
        title='Product Service API',
        version='1.0.0',
        openapi_version='3.0.2',
        plugins=[MarshmallowPlugin()],
    )

    # Add schemas to spec
    spec.components.schema('Product', schema=ProductSchema)

    # Document endpoints
    spec.path(
        path='/products',
        operations={
            'get': {
                'summary': 'Get all products',
                'description': 'Returns a list of all products',
                'responses': {
                    '200': {
                        'description': 'List of products',
                        'content': {
                            'application/json': {
                                'schema': {
                                    'type': 'array',
                                    'items': {'$ref': '#/components/schemas/Product'}
                                }
                            }
                        }
                    }
                }
            },
            'post': {
                'summary': 'Create a new product',
                'description': 'Add a new product to the catalog',
                'requestBody': {
                    'required': True,
                    'content': {
                        'application/json': {
                            'schema': {'$ref': '#/components/schemas/Product'}
                        }
                    }
                },
                'responses': {
                    '201': {
                        'description': 'Product created successfully',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': '#/components/schemas/Product'}
                            }
                        }
                    },
                    '400': {
                        'description': 'Invalid product data'
                    }
                }
            }
        }
    )

    return jsonify(spec.to_dict())

@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product"""
    product = request.json
    if not product or 'name' not in product or 'price' not in product:
        return jsonify({"error": "Invalid product data"}), 400
    
    product['id'] = len(products) + 1
    products.append(product)
    return jsonify(product), 201

if __name__ == '__main__':
    # Add some sample products
    products.extend([
        {"id": 1, "name": "Laptop", "price": 999.99, "description": "High-performance laptop"},
        {"id": 2, "name": "Smartphone", "price": 499.99, "description": "Latest smartphone"},
        {"id": 3, "name": "Headphones", "price": 99.99, "description": "Wireless headphones"}
    ])
    app.run(host='0.0.0.0', port=5000) 