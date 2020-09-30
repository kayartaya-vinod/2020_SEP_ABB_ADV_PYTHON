from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)


@app.route('/')
def index():
    return render_template('contact-list.html')


contacts = [
    dict(id=1, name='Vinod Kumar', gender='Male', phone='9731424784', email='vinod@vinod.co', city='Bangalore'),
    dict(id=2, name='Shyam Sundar', gender='Male', phone='9731420000', email='shyam@xmpl.com', city='Bangalore')
]


@app.route('/api/contacts', methods=['GET'])
def get_all_contacts():
    return jsonify(contacts)


@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_one_contact(contact_id):
    c = [c for c in contacts if c['id'] == contact_id]
    # c = filter(lambda contact: contact['id'] == contact_id, contacts)

    if len(c) > 0:
        return jsonify(c[0])

    return jsonify(None)


@app.route('/api/contacts', methods=['POST'])
def add_new_contact():
    data = request.json
    data['id'] = max(contacts, key=lambda c: c['id'])['id'] + 1
    contacts.append(data)
    return jsonify(data)


app.run(port=8080)
