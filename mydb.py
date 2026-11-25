import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dataBase = mysql.connector.connect(
	host = os.environ.get('DB_HOST'),
	user = os.environ.get('DB_USER'),
	password = os.environ.get('DB_PASSWORD')
	)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE dcrm")