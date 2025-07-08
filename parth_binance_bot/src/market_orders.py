
import sys
from binance.client import Client
from src.logger import logger
from src.utils import validate_order
import os

def market_order(symbol, side, quantity):
    try:
        validate_order(symbol, side, float(quantity))
        client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_API_SECRET"))
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market Order Placed: {order}")
        print("Order executed:", order)
    except Exception as e:
        logger.error(f"Market order failed: {str(e)}")
        print("Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/market_orders.py SYMBOL SIDE QUANTITY")
    else:
        market_order(sys.argv[1], sys.argv[2], float(sys.argv[3]))
