
# Binance Futures CLI Trading Bot

## Setup

1. Install dependencies:
```bash
pip install python-binance
```

2. Set your API credentials as environment variables:
```bash
export BINANCE_API_KEY=your_api_key
export BINANCE_API_SECRET=your_api_secret
```

## Usage

### Market Order
```bash
python src/market_orders.py BTCUSDT BUY 0.01
```

### Limit Order
```bash
python src/limit_orders.py BTCUSDT SELL 0.01 30000
```

## Logging

All actions and errors are logged in `bot.log`.
