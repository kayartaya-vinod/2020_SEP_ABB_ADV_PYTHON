from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True


# mapping URL http://localhost:5000/ to the function home()
# @app.route('/')
def home():
    return """
    <html>
        <head><title>My first flask web app</title></head>
        <body>
            <h1>Welcome to Flask App</h1>
            <hr>
            <p>Powered by Python</p>
        </body>
    </html>
    """


products = [
    dict(id=1, name='Logitech Optical Mouse', price=899.0),
    dict(id=2, name='Logitech wireless keyboard', price=1299.0),
    dict(id=3, name='Samsung Monitor', price=7000),
    dict(id=4, name='Water bottle', price=149.0)
]
title = 'Product Catalog V1.0'


@app.route('/')
def index():
    d = dict(pageTitle='List of products: ')
    d['title'] = title
    d['products'] = products

    for p in products:
        print(p)

    return render_template('product-list.html', data=d)


@app.route('/new-product', methods=['GET', 'POST'])
def new_product():
    d = dict(pageTitle='Add new product')
    d['title'] = title

    if request.method == 'POST':
        pr = dict(request.form)
        products.append(pr)
        d['feedback'] = 'New product added successfully!'

    return render_template('product-form.html', data=d)


app.run()
