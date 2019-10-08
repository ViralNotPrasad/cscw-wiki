import wikipedia
import csv

wikipedia.set_lang("hi")

articles_eng = {"Kashmir Conflict", "Article 370 of the Constitution of India", "Insurgency in Jammu and Kashmir"}
           
articles_hin = {"कश्मीर_विवाद":"Kashmir_conflict_hindi", "अनुच्छेद_३७०": "Article_370_hindi", "जम्मू_और_कश्मीर_में": "Insurgency_hindi"}


for pagename, fname in articles_hin.items():
    print('ehy')
    page = wikipedia.page(pagename)
    with open(fname + "_contents.txt", "w") as myfile:
        myfile.write(page.content)
