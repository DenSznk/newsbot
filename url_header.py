from dotenv import load_dotenv
import os

load_dotenv()


header = os.getenv('header')

url = 'https://forklog.com/news/'

TOKEN = os.getenv('TOKEN')
