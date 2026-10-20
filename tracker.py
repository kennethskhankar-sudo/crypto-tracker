import requests
url = "https://api.coinbase.com/v2/prices/spot"
response = requests.get(url)
data = response.json()
print("live coinbase bitcoin price:", data["data"]["amount"], "USD")
import sqlite3
import requests

# 1. INGEST THE LIVE DATA FROM COINBASE
url = "https://api.coinbase.com/v2/prices/spot"
response = requests.get(url)
data = response.json()

# Isolate the clean numeric price from the JSON layout
price = data["data"]["amount"]

# 2. INITIALIZE THE DATABASE FILING CABINET
# This automatically creates a file named 'crypto_history.db' in your folder
connection = sqlite3.connect("crypto_history.db")

# Create the invisible pen (cursor) to write inside the database file
cursor = connection.cursor()

# 3. CREATE THE STORAGE DRAWER (SQL Table)
# This sets up 3 columns: exact time, the asset name, and the numeric price
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS btc_vault (
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        asset TEXT,
        price REAL
    )
"""
)

# 4. INSERT THE LIVE PRICE INTO THE STORAGE DRAWER
# The '?' marks are safe placeholders for ("BTC", price)
cursor.execute("INSERT INTO btc_vault (asset, price) VALUES (?, ?)", ("BTC", price))

# 5. COMMIT THE CHANGES AND CLOSE THE PIPELINE
# This locks the data onto your Mac's hard drive and closes the file safely
connection.commit()
connection.close()

print("Successfully pulled price:", price, "and saved it to crypto_history.db!")
