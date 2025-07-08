
import sys
from binance.client import Client
from src.logger import logger
from src.utils import validate_order
import os

def limit_order(symbol, side, quantity, price):
    try:
        validate_order(symbol, side, float(quantity))
        client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_API_SECRET"))
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=str(price)
        )
        logger.info(f"Limit Order Placed: {order}")
        print("Order executed:", order)
    except Exception as e:
        logger.error(f"Limit order failed: {str(e)}")
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python src/limit_orders.py SYMBOL SIDE QUANTITY PRICE")
    else:
        limit_order(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
