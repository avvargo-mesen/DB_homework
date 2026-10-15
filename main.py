import csv
import os
from dotenv import load_dotenv
load_dotenv()
import psycopg2

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=os.getenv("DB_PASSWORD"))
try:
    with conn:
        with conn.cursor() as cur:
            with open("data/employees_data.csv", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO employees (first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)",
                                row)


finally:
    conn.close()


conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=os.getenv("DB_PASSWORD"))
try:
    with conn:
        with conn.cursor() as cur:
            with open("data/customers_data.csv", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                                row)

finally:
    conn.close()


conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=os.getenv("DB_PASSWORD"))
try:
    with conn:
        with conn.cursor() as cur:
            with open("data/orders_data.csv", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
                                row)

finally:
    conn.close()