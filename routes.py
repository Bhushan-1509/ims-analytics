from app import app
from helpers import *
from flask import jsonify, request, send_file
import pandas as pd
import csv
import json


@app.route('/')
def index():
    return jsonify({"Status": "working"})


@app.route('/orders-pie-chart', methods=['POST'])
def make_orders_pie_chart():
    data = request.get_json(force=True)
    data = json.loads(data)
    orders = data['orders']
    # Normalize the data
    normalized_orders = [{k: v for k, v in order.items()} for order in orders]
    print(normalized_orders)
    # Create DataFrame
    df = pd.DataFrame(normalized_orders)    
    print(df)
    chart_buffer = generate_orders_pie_chart(df)

    # Return the pie chart as an HTTP response
    return send_file(
        chart_buffer,
        mimetype='image/png',
        as_attachment=False,
        download_name='orders_pie_chart.png'
    )


@app.route('/orders-bar-graph', methods=['POST'])
def make_orders_bar_graph():
    data = request.get_json(force=True)
    data = json.loads(data)
    df = pd.DataFrame(data)
    orders = data['orders']

    # Normalize the data
    normalized_orders = [{k: v for k, v in order.items()} for order in orders]

    # Create DataFrame
    df = pd.DataFrame(normalized_orders)
    bar_graph_buffer = generate_monthly_orders_bar_graph(df)

    # Return the pie chart as an HTTP response
    return send_file(
        bar_graph_buffer,
        mimetype='image/png',
        as_attachment=False,
        download_name='orders_bar_chart.png'
    )

@app.route("/material-pie-chart", methods=['POST'])
def make_material_pie_chart():
    data = request.get_json(force=True)
    data = json.loads(data)
    df = pd.DataFrame(data)
    materials = data['raw_materials']
    # Normalize the data
    normalized_materials = [{k: v for k, v in material.items()} for material in materials]

    df = pd.DataFrame(normalized_materials)
    pie_chart_buffer = generate_material_pie_chart(df)

    # Return the chart as HTTP response
    return send_file(pie_chart_buffer, mimetype='image/png',
                      as_attachment=False,
        download_name='raw_materials_chart.png')

@app.route('/supplier-pie-chart', methods=["POST"])
def make_supplier_pie_chart():
    data = request.get_json(force=True)
    data = json.loads(data)
    df = pd.DataFrame(data)
    suppliers = data['suppliers']
    # Normalize the data
    normalized_materials = [{k: v for k, v in supplier.items()} for supplier in suppliers]

    df = pd.DataFrame(normalized_materials)
    pie_chart_buffer = generate_supplier_pie_chart(df)
    # Return the chart as HTTP response
    return send_file(pie_chart_buffer, mimetype='image/png',as_attachment=False,
                     download_name='supplier_pie_chart.png')
