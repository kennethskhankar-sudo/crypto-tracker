# Live Cryptocurrency Data Pipeline

An automated Python data ingestion script that queries the live Coinbase API for cryptocurrency data and streams it directly into a local SQLite database storage engine.

## Tech Stack
* **Language:** Python 3
* **Database:** SQLite3
* **Libraries:** requests

## Features
* Automated loop tracking continuous live price movements in USD.
* Graceful runtime exception logging and console print statements.
* Persistent localized file storage.
