import streamlit as st
import sqlite3
import pandas as pd

# 👉 Make the app full-width
st.set_page_config(layout="wide")

# Title
st.title("🛒 Olist E-Commerce Database Explorer")

# SQLite DB
DB_FILE = "olist.db"

# Thread-safe connection
@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_FILE, check_same_thread=False)

conn = get_connection()

# SQL query input
st.subheader("Enter your SQL query below:")
query = st.text_area("SQL Query", height=150, placeholder="e.g., SELECT * FROM customers LIMIT 10")

# Run query button
if st.button("Run Query"):
    if not query.strip():
        st.warning("⚠️ Please enter a valid SQL query.")
    else:
        try:
            df = pd.read_sql_query(query, conn)
            st.success(f"✅ Query executed successfully! Returned {len(df)} row(s).")

            # Display results — wide layout + full-width table
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error("❌ Error executing query:")
            st.code(str(e), language="text")
