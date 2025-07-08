
def validate_order(symbol: str, side: str, quantity: float):
    valid_sides = ["BUY", "SELL"]
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are allowed.")
    if side not in valid_sides:
        raise ValueError("Order side must be BUY or SELL.")
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
