const express = require('express');
const cors = require('cors');
const { createClient } = require('redis');
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const app = express();
app.use(cors());
app.use(express.json());

// Swagger definition
const swaggerOptions = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'Cart Service API',
            version: '1.0.0',
            description: 'Shopping cart management service',
        },
        servers: [
            {
                url: 'http://localhost:5002',
                description: 'Local server',
            },
        ],
    },
    apis: ['./index.js'],
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);
app.use('/docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));

// In-memory cart store (replace with Redis in production)
const carts = new Map();

/**
 * @swagger
 * /cart/add:
 *   post:
 *     summary: Add item to cart
 *     description: Add a product to user's shopping cart
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - userId
 *               - productId
 *               - quantity
 *             properties:
 *               userId:
 *                 type: integer
 *                 description: ID of the user
 *               productId:
 *                 type: integer
 *                 description: ID of the product to add
 *               quantity:
 *                 type: integer
 *                 description: Quantity of the product
 *     responses:
 *       200:
 *         description: Item added to cart successfully
 *       400:
 *         description: Invalid input
 */
app.post('/cart/add', (req, res) => {
    try {
        const { userId, productId, quantity } = req.body;

        if (!userId || !productId || !quantity) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        const key = String(userId);  // <-- convert to string here

        let cart = carts.get(key) || [];
        
        // Check if product already in cart
        const existingItem = cart.find(item => item.productId === productId);
        if (existingItem) {
            existingItem.quantity += quantity;
        } else {
            cart.push({ productId, quantity });
        }

        carts.set(key, cart);  // <-- use string key
        res.json(cart);
    } catch (error) {
        res.status(500).json({ error: 'Error adding to cart' });
    }
});

/**
 * @swagger
 * /cart/{userId}:
 *   get:
 *     summary: Get user's cart
 *     description: Retrieve the shopping cart for a specific user
 *     parameters:
 *       - in: path
 *         name: userId
 *         required: true
 *         schema:
 *           type: integer
 *         description: ID of the user
 *     responses:
 *       200:
 *         description: User's cart contents
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   productId:
 *                     type: integer
 *                   quantity:
 *                     type: integer
 */
app.get('/cart/:userId', (req, res) => {
    const key = String(req.params.userId);  // <-- convert to string here
    const cart = carts.get(key) || [];
    res.json(cart);
});

const PORT = 5002;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Cart service running on port ${PORT}`);
});
