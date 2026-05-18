from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 模拟东北特产数据（真实项目会用数据库）
products = [
    {"id": 1, "name": "五常大米", "price": 68.00, "stock": 100},
    {"id": 2, "name": "哈尔滨红肠", "price": 45.00, "stock": 200},
    {"id": 3, "name": "长白山人参", "price": 298.00, "stock": 50},
    {"id": 4, "name": "榛蘑", "price": 88.00, "stock": 80},
    {"id": 5, "name": "松子", "price": 55.00, "stock": 150},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({"code": 200, "data": products, "message": "success"})

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify({"code": 200, "data": product})
    return jsonify({"code": 404, "message": "商品不存在"}), 404

from flask import render_template_string

# 在 app.py 里加入这个首页路由
@app.route('/')
def index():
    # 这是一个简单的 HTML 页面模板，直接写在代码里
    html = '''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>东北特产商城</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .product { border: 1px solid #ccc; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .product h2 { margin: 0 0 10px 0; }
            .price { color: #e00; font-weight: bold; }
            button { background: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 3px; cursor: pointer; }
            button:hover { background: #45a049; }
            #cart { margin-top: 20px; padding: 15px; background: #f5f5f5; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>🍄 东北特产商城</h1>
        <div id="product-list"></div>
        <div id="cart">
            <h3>🛒 购物车</h3>
            <div id="cart-items">暂无商品，快去挑选吧！</div>
        </div>

        <script>
            // 页面加载时从 API 获取商品列表
            fetch('/api/products')
                .then(res => res.json())
                .then(data => {
                    const list = document.getElementById('product-list');
                    data.data.forEach(p => {
                        const div = document.createElement('div');
                        div.className = 'product';
                        div.innerHTML = `
                            <h2>${p.name}</h2>
                            <p>价格：<span class="price">¥${p.price.toFixed(2)}</span></p>
                            <p>库存：${p.stock} 件</p>
                            <button onclick="addToCart('${p.name}')">加入购物车</button>
                        `;
                        list.appendChild(div);
                    });
                });

            function addToCart(name) {
                const cart = document.getElementById('cart-items');
                if (cart.innerText === '暂无商品，快去挑选吧！') {
                    cart.innerHTML = '';
                }
                const item = document.createElement('div');
                item.innerText = '✅ ' + name;
                cart.appendChild(item);
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)