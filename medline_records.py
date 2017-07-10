from Bio import Medline 
	handle = Entrez.efetch(db="pubmed" id = idList, rettype= "medline",retmode= "text")
	records= Medline.parse(handle)
	records= list(records)
	for record in records:
		print("title:", record.get("TI","?"))
		print("authors:", record.get("AU","?"))
		print("source:",record.get("SO","?"))
		print("")

