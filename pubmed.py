# query the pubmed database 
def search(query):
	Entrez.email = 'shachi.iitd@gmail.com'
	handle = Entrez.esearch(db='pubmed',sort='relevance',retmax='20',retmode = 'xml',term=query)
	results = Entrez.read(handle)
	return results
