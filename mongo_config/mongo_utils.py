import pymongo
import streamlit as st
from datetime import datetime, timezone, timedelta

def connect_mongo():
    try:
        client = pymongo.MongoClient("mongodb://admin:password@localhost:27017/",
                                    socketTimeoutMS=20000,
                                    connectTimeoutMS=20000)
        return client
    except Exception:
        st.error(f"Não foi possível a conexão com o banco de dados de interações.")

def access_mongo_collections(selected_collection):
    client = connect_mongo()
    db = client['fit_assistant']
    collection = db[selected_collection]

    return collection