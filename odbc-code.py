import pyodbc
from dotenv import load_dotenv
import os

load_dotenv('.env.local')

price_data = [
    ["2023-01-01", "AAPL", 150.00],
    ["2023-01-02", "AAPL", 152.00],
    ["2023-01-03", "AAPL", 151.50],
    ["2023-01-01", "GOOGL", 2800.00],
    ["2023-01-02", "GOOGL", 2825.00],
    ["2023-01-03", "GOOGL", 2810.00],   
    ["2023-01-01", "MSFT", 300.00],
    ["2023-01-02", "MSFT", 305.00],
    ["2023-01-03", "MSFT", 302.50]
]

# loop through all the drivers and try to connect
# for driver in pyodbc.drivers():

server = 'localhost,1433'
database = 'stock_database'

driver = 'ODBC Driver 18 for SQL Server'
password = os.getenv('SQL_SERVER_PWD')
# define the connection string
connection = pyodbc.connect(f'DRIVER={driver}; \
                                    SERVER={server}; \
                                    DATABASE={database}; \
                                    UID=sa; \
                                    PWD={password}; \
                                    TrustServerCertificate=yes;')

cursor = connection.cursor()

insert_query = ''' INSERT INTO td_price_data (close_price, high, low, open, \
                volume, date, symbol) VALUES (?, ?, ?, ?, ?, ?, ?) '''

for row in price_data: 
    values = (row[2], row[2], row[2], row[2], 1000, row[0], row[1])

cursor.execute(insert_query, values)