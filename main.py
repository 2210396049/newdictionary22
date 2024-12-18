import os

from flask import Flask, send_file, render_template, request
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route("/")
def index():
    return send_file('src/index.html')


@app.route("/arama")
def arama():
    anahtarKelime = request.args.get('anahtarKelime', '')

    tree = ET.parse('katalog.xml')
    root = tree.getroot()

    colors = []
    for color in root.findall('renk'):  # Now 'root' is defined
        color_data = {}
        color_data['ingilizce'] = color.find('ingilizce').text
        color_data['turkce'] = color.find('turkce').text

        # Filter data by search keyword
        if anahtarKelime.lower() in color_data['ingilizce'].lower() or anahtarKelime.lower() in color_data['turkce'].lower():
            colors.append(color_data)

    return render_template('arama.html', data=colors)


@app.route("/katalog")
def katalog():
    tree = ET.parse('katalog.xml')
    root = tree.getroot()

    colors = []
    for color in root.findall('renk'):  # Now 'root' is defined
        color_data = {}
        color_data['ingilizce'] = color.find('ingilizce').text
        color_data['turkce'] = color.find('turkce').text
        colors.append(color_data)
    return render_template('katalog.html', data=colors)