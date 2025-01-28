import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector

files = [f for f in os.listdir('D:\PROJETO_WEBSCRAP_FMS\\archive/')]
print(type(files[0]))