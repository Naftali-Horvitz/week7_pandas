from flask import Flask, jsonify
from utils import *

app = Flask(__name__)

@app.route("/")
def index():
    orders = load_json("orders_simple.json")
    orders = change_amount_Total_to_float(orders)
    orders = str_to_date(orders)
    orders = change_float_to_int(orders, 'shipping_days')
    orders = change_float_to_int(orders, 'customer_age')
    orders = change_int_to_float(orders, 'rating')
    orders = clean_column_html(orders)
    orders = handel_coupon_used_column(orders)
    orders = add_month_order_column(orders)
    orders = add_order_value_high_column(orders)
    orders = sort_by_column(orders)
    orders = add_rating_avg_column(orders)
    orders = filter_by(orders)
    orders = add_column_status_delivery(orders)

    return jsonify({
        "rows": int(len(orders)),
        "columns": list(orders.columns)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
