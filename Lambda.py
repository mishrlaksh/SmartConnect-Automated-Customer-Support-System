

import json

def lambda_handler(event, context):
    # Sample logic to return order status
    order_id = event['Details']['Parameters']['order_id']
    order_status = get_order_status(order_id)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'order_status': order_status
        })
    }

def get_order_status(order_id):
    # Sample logic, replace with actual API call
    return 'Shipped'
