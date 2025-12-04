import pandas as pd
from utils import *
path = "orders_simple.json"

orders = load_json(path)

orders.total_amount = change_column_amount_Total(orders)
orders.order_date = str_to_date(orders)
orders.items_html = clean_column_html(orders)
orders['coupon_used'] = handel_coupon_used_column(orders)
orders['month_order'] = add_month_order_column(orders)
orders['order_value_high'] = add_order_value_high_column(orders)
orders = sort_by_column(orders)
orders['rating_avg_by_column'] = add_rating_avg_column(orders)
orders = filter_by(orders)
func_apply = status_delivery()
orders['status_delivery'] = orders.shipping_days.apply(func_apply)
save_data_to_csv(orders)
