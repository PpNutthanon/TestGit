import ccxt
import pandas as pd

# Initialize Binance Exchange
binance = ccxt.binance()

# Fetch historical data (OHLCV)
def fetch_data(symbol, timeframe='1d', limit=365):
    ohlcv = binance.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Example for BTC/USDT
df = fetch_data('BTC/USDT')
def calculate_emas(df):
    df['EMA50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['EMA150'] = df['close'].ewm(span=150, adjust=False).mean()
    df['EMA200'] = df['close'].ewm(span=200, adjust=False).mean()
    return df

df = calculate_emas(df)
def check_conditions(df):
    latest = df.iloc[-1]
    conditions = [
        latest['close'] > latest['EMA150'],
        latest['close'] > latest['EMA200'],
        latest['EMA150'] > latest['EMA200'],
        latest['EMA200'] > df['EMA200'].iloc[-2],  # Check if EMA200 is trending up
        latest['EMA50'] > latest['EMA150'],
        latest['EMA50'] > latest['EMA200'],
        latest['close'] > latest['EMA50'],
        latest['close'] > df['close'].min() * 1.30,  # 30% above 52-week low
        latest['close'] >= df['close'].max() * 0.25  # At least 25% of 52-week high
    ]
    return all(conditions)

is_valid = check_conditions(df)
symbols = ['BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'SOL/USDT']  # Add your symbols here

valid_pairs = []
for symbol in symbols:
    try:
        df = fetch_data(symbol)
        df = calculate_emas(df)
        if check_conditions(df):
            valid_pairs.append(symbol)
    except Exception as e:
        print(f"Error processing {symbol}: {e}")

print("Valid Pairs:", valid_pairs)
