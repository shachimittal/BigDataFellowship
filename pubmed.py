# query the pubmed database
from Bio import Entrez 
def search(query):
	Entrez.email = 'shachi.iitd@gmail.com'
	handle = Entrez.esearch(db='pubmed',sort='relevance',retmax='20',retmode = 'xml',term=query)
	results = Entrez.read(handle)
	return results

park = search('parkinson disease')
Park_ID = park['IdList']


