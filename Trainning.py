import ccxt
import requests
import time

def send_telegram_message(message, bot_token, chat_ids):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    for chat_id in chat_ids:
        data = {
            "chat_id": chat_id,
            "text": message
        }
        
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"Message sent to chat_id {chat_id}")
        else:
            print(f"Failed to send message to chat_id {chat_id}: {response.json()}")

# Your bot token and chat IDs
bot_token = "7406337171:AAH-rYxfK6TQdlZ8vCG0M_Ef-W8FtONiXeg"
chat_ids = ["5512154356", "97032333"]  # Replace with your actual chat IDs

# Initialize the MEXC exchange
exchange = ccxt.mexc()

# List of cryptocurrency pairs to monitor
crypto_pairs = [
    'BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'DYDX/USDT', 'AVAX/USDT',
    'NEAR/USDT', 'ID/USDT', 'SOL/USDT', 'APE/USDT', 'SHIB/USDT',
    'OP/USDT', 'ICP/USDT', 'AAVE/USDT', 'BCH/USDT', 'FTM/USDT',
    'INJ/USDT', 'SOL/USDT','LINK/USDT'
]

while True:
    for pair in crypto_pairs:
        try:
            # Fetch ticker data for the pair
            ticker = exchange.fetch_ticker(pair)
            
            lowest_price = ticker['low']
            current_price = ticker['last']
            
            if current_price <= lowest_price:
                message = f"The current price of {pair} has hit the lowest price in 24 hours: ${current_price}"
                send_telegram_message(message, bot_token, chat_ids)
        
        except Exception as e:
            print(f"Error fetching data for {pair}: {e}")
    
    # Wait for 2 minutes before checking again
    time.sleep(120)  # 120 seconds = 2 minutes
