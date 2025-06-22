import psycopg2

conn = psycopg2.connect(
    dbname="cmdb",
    user="postgres",
    password="postgres",
    host="localhost"
)

print("✅ Conexión exitosa a PostgreSQL")
conn.close()
