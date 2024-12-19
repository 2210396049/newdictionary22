import os
from flask import Flask, send_file, render_template, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Load the XML data and create the 'catalog' list
tree = ET.parse('katalog.xml')  # Replace 'renkler.xml' with your XML file path
root = tree.getroot()
catalog = []  # Initialize the catalog list
for cd in root.findall('CD'):
    cd_dict = {}
    for child in cd:
        cd_dict[child.tag] = child.text
    catalog.append(cd_dict)


@app.route("/")
def index():
    return send_file('src/index.html')


@app.route("/arama")
def arama():
    anahtarKelime = request.args.get('anahtarKelime', '')
    return render_template('arama.html', data=anahtarKelime)


@app.route("/katalog", methods=['GET'])
def katalog():
    search_term = request.args.get('anahtarKelime')
    data = []

    for item in catalog:
        if search_term.lower() == item['ingilizce'].lower() or \
           search_term.lower() == item['turkce'].lower():
            data.append(item)
            break  # Exit loop if found

    return render_template('katalog.html', data=data)

# ... (rest of your code) ...