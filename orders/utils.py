import datetime
def generate_order_number(pk):
    current_dateime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    order_number=current_dateime+str(pk)
    return order_number