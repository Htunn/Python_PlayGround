from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os
import libs.request as r

load_dotenv()

u = os.getenv('cloudbees_username')
p = os.getenv('cloudbees_password')

def getAuth(username=u, password=p):
    return HTTPBasicAuth(username, password)

