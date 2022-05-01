import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import boto3

def handler(event, context):
	s3 = boto3.client("s3")	
	key = "headlines/raw/periodico=bbc/year=2022/month=05/day=01/page_text_str.txt" 

	now = datetime.now()
	year = now.strftime("%Y")
	month = now.strftime("%m")
	day = now.strftime("%d")
	periodicos = ["bbc", "nejm"]
	for i in periodicos:
		s3.download_file('parcial22dobigdata', "headlines/raw/periodico="+i+"/year="+year+"/month="+month+"/day="+day+"/page_text_str.txt", "/tmp/page_text_str.txt")
		#s3.upload_file('/tmp/page_text_str.txt', 'bigdata-alexxx-2022-01', 'hello-remote.txt')
	
		f = open("/tmp/page_text_str.txt")
		soup = f.read()
		bs = BeautifulSoup(soup,"html.parser")
		if (i=="bbc"):
			extractor_titulo = bs.find_all('h3', class_='media__title')
			titulos_noticias = scrapText(extractor_titulo)

			extractor_categoria = bs.find_all('a', class_='media__tag')
			tags = scrapText(extractor_categoria)

			extractor_enlace = bs.find_all('a', class_='media__link', href=True)
			enlaces = scrapLinks(extractor_enlace)
		else:
			extractor_titulo = bs.find_all('b', class_='m-article__title')
			titulos_noticias = scrapText(extractor_titulo)

			extractor_categoria = bs.find_all('a', class_='m-article__type')
			tags = scrapText(extractor_categoria)

			extractor_enlace = bs.find_all('a', class_='m-article__link', href=True)
			enlaces = scrapLinks(extractor_enlace)

		df = pd.DataFrame({"Titular":titulos_noticias, "Categoria":tags, "Enlace":enlaces}, index=[*range(0, len(titulos_noticias))])
		df.to_csv("/tmp/"+i+"_news_records.csv", index=None)
		s3.upload_file('/tmp/'+i+'_news_records.csv', 'parcial22dobigdata', 'news/final/periodico='+i+'/year='+year+'/month='+month+'/day='+day+'/'+i+'_news_records.csv')
	return{}


def scrapText(listaScraping):
	items = list()
	for i in listaScraping:
		if i != "":
			items.append(i.text.strip())
		else:
			items.append(" ")
	return items

def scrapLinks(listaScraping):
	items = list()
	for i in listaScraping:
		items.append(i['href'])
	return items
