stocks = [
    {
        "name": "Company A",
        "symbol": "CMPA",
        "sector": "Technology",
        "current_price": 100.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 98.0,
                    "close": 100.0,
                    "high": 101.0,
                    "low": 97.0
                },
                "volume": 12000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 97.0,
                    "close": 98.0,
                    "high": 99.0,
                    "low": 96.0
                },
                "volume": 15000
            }
        ],
        "locations": ["New York", "London"]
    },
    {
        "name": "Company B",
        "symbol": "CMPB",
        "sector": "Finance",
        "current_price": 200.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 198.0,
                    "close": 200.0,
                    "high": 202.0,
                    "low": 196.0
                },
                "volume": 18000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 196.0,
                    "close": 198.0,
                    "high": 199.0,
                    "low": 195.0
                },
                "volume": 17000
            }
        ],
        "locations": ["Tokyo", "Singapore"]
    },
    {
        "name": "Company C",
        "symbol": "CMPC",
        "sector": "Healthcare",
        "current_price": 300.0,
        "historical_data": [
            {
                "date": "2024-01-10",
                "prices": {
                    "open": 295.0,
                    "close": 300.0,
                    "high": 302.0,
                    "low": 294.0
                },
                "volume": 22000
            },
            {
                "date": "2024-01-09",
                "prices": {
                    "open": 294.0,
                    "close": 295.0,
                    "high": 296.0,
                    "low": 293.0
                },
                "volume": 21000
            }
        ],
        "locations": ["Berlin", "Paris"]
    }
]

# # # ---------------------------------------------------------------------------------------------------
# # # This is how, we will be getting the data from the Broker API, we should be able to get the desired data from the DS
# # # Q 0: Read Data Task: Read and display the close price of "Company B" on 10th january.
# print(stocks)
# print(len(stocks))
# print(type(stocks))
# print(stocks[1].get("historical_data")[1].get("prices").get("close"))
# print(type(stocks[1].get("historical_data")[1].get("prices").get("close")))

# # # ---------------------------------------------------------------------------------------------------
# # # Q 1: Read Data Task: Read and display the current price of "Company B"
# print(stocks[1].get("current_price"))
# # # ---------------------------------------------------------------------------------------------------
# # # Q2: Write Data Task: Add a new company "Company D" with some initial data to the stocks list.
# n ={
#      "name": "Company D",
#         "symbol": "HDFC",
#         "sector": "Bank",
#         "current_price": 1600.0,
#         "locations": ["Bombay", "Chennai"]
# }
# stocks.append(n)
# print(stocks)
# print(stocks[3].get("current_price"))

# # # ---------------------------------------------------------------------------------------------------
# # # Q 3: Update Data Task: Update the current price of "Company C" to 310.0.
# print(stocks[2].update({"current_price": 310.0}))
# print(stocks[2].get("current_price"))

# # # ---------------------------------------------------------------------------------------------------
# # Q 4: Delete Data Task: Remove the historical data for "Company A" on "2024-01-09".
# # print(stocks[0].get("historical_data").pop(1))
