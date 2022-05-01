import urllib.request
import boto3
from bs4 import BeautifulSoup
import requests
from datetime import datetime

#urls = [("https://www.bbc.com/", "bbc"), ("https://www.nejm.org/","nejm")]

def uploader(url):
  for i,j in url:
    pag3 = requests.get(i).text
    soup3 = BeautifulSoup(pag3, 'html.parser')
    page_text_str = soup3.prettify() #devuelve un string de la page html
    s3 = boto3.resource('s3')
    s3Object = s3.Object.put('parcial22dobigdata', 'headlines/raw/periodico='+j+'/year='+year+'/month='+month+'/day='+day/'page_text_str.txt')
	
def handler (event, context):
	urls = [("https://www.bbc.com/", "bbc"), ("https://www.nejm.org", "nejm")]
	s3 = boto3.client('s3')
	now = datetime.now()
	year = now.strftime("%Y")
	month = now.strftime("%m")
	day = now.strftime("%d")   
	for i,j in urls:
		pag3 = requests.get(i).text
		soup3 = BeautifulSoup(pag3, 'html.parser')
		page_text_str = soup3.prettify() #devuelve un string de la page html
		s3Object = s3.put_object(Body= page_text_str,Bucket = 'parcial22dobigdata', Key='headlines/raw/periodico='+j+'/year='+year+'/month='+month+'/day='+day+'/page_text_str.txt')
	return {}
