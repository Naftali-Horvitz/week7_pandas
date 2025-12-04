import pandas as pd

path = "orders_simple.json"

def load_json(path: str):
    return pd.read_json(path)
    
def change_amount_Total_to_float(data : pd.DataFrame):
    to_float = lambda x: float(x[:-1])
    data.total_amount = data.total_amount.apply(to_float)
    return data
def change_float_to_int(data : pd.DataFrame, column_name):    # this is a generic func
    to_int = lambda x: float(x)
    data[column_name] = data[column_name].apply(to_int)
    return data

def change_int_to_float(data : pd.DataFrame, column_name):     # this is a generic func
    to_float = lambda x: int(x)
    data[column_name] = data[column_name].apply(to_float)
    return data

def str_to_date(data):
    data.order_date = pd.to_datetime(data.order_date)
    return data
   
def clean_column_html(data):
    data.items_html = data.items_html.replace(r'<[^<>]*>', '', regex=True)
    return data

def handel_coupon_used_column(data):
    data.coupon_used = data.coupon_used.replace('', 'coupon no')
    return data

def add_month_order_column(data):
    data['month_order'] = data.order_date.dt.month
    return data

def add_order_value_high_column(data):
    avg = data.total_amount.mean()
    data['order_value_high'] = (data.total_amount > avg)
    return data
    
def sort_by_column(data):
    data =  data.sort_values(by='total_amount', ascending= False)   
    return data
    
def add_rating_avg_column(data: pd.DataFrame):
    data['rating_avg_by_column'] =  data.groupby('country')['rating'].transform("mean")
    return data

def filter_by(data):
    data =  data[(data['total_amount'] > 1000) & (data['rating'] > 4.5)]
    return data

def add_column_status_delivery(data):
    status_delivery = lambda x: 'delayed' if x > 7 else 'on'
    data['status_delivery'] = data.shipping_days.apply(status_delivery)
    return data 

def save_data_to_csv(data):
    data.to_csv('clean_orders_[315605808].csv')
    
