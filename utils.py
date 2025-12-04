import pandas as pd

path = "orders_simple.json"

def load_json(path):
    return pd.read_json(path)
    
def change_column_amount_Total(data):
    to_float = lambda x: float(x[:-1])
    return data.total_amount.apply(to_float)

def change_int_to_float(data, column_name):
    to_float = lambda x: float(x)
    return data[column_name].apply(to_float)
    
def str_to_date(data):
    return pd.to_datetime(data.order_date)
   
def clean_column_html(data):
    return data.items_html.replace(r'<[^<>]*>', '', regex=True)

def handel_coupon_used_column(data):
    return data.coupon_used.replace('', 'coupon no')

def add_month_order_column(data):
    return data.order_date.dt.month

def add_order_value_high_column(data):
    avg = data.total_amount.mean()
    return(data.total_amount > avg)
    
def sort_by_column(data):
    return data.sort_values(by='total_amount', ascending= False)   
    
def add_rating_avg_column(data: pd.DataFrame):
    return data.groupby('country')['rating'].transform("mean")

def filter_by(data):
    return data[(data['total_amount'] > 1000) & (data['rating'] > 4.5)]

def status_delivery():
    return lambda x: 'delayed' if x > 7 else 'on'

def save_data_to_csv(data):
    data.to_csv('clean_orders_[315605808].csv')
    
