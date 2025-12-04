import pandas as pd
from utils import *
path = "orders_simple.json"

orders = load_json(path)

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
save_data_to_csv(orders)