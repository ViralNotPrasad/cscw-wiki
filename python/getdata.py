import wikipedia
import csv

articles_eng = {"Kashmir Conflict", "Article 370 of the Constitution of India",
                "Insurgency in Jammu and Kashmir", "2019 Pulwama attack",
                "Jammu and Kashmir Reorganisation Act, 2019"}
           
articles_hin = {"कश्मीर_विवाद":"Kashmir_conflict_hindi", "अनुच्छेद_३७०": "Article_370_hindi",
                                        "जम्मू_और_कश्मीर_में": "Insurgency_hindi", "२०१९_पुलवामा_हमला":"Pulwama_hindi",
                                        "जम्मू_और_कश्मीर_पुनर्गठन_अधिनियम,_2019":"Reorganisation_hindi"}

articles_urdu = {"مسئلہ_کشمیر": "Kashmir_conflict_urdu", "آئین_ہند_کی_دفعہ_370": "Article_370_urdu", "پلوامہ_حملہ،_2019ء": "Pulwama_urdu", "جموں_و_کشمیر_تنظیم_نو_ایکٹ،_2019ء": "Reorganisation_urdu"}

# Hindi
wikipedia.set_lang("hi")

for pagename, fname in articles_hin.items():
    page = wikipedia.page(pagename)
    with open("../data/contents/" + fname + "_contents.txt", "w") as myfile:
        myfile.write(page.content)


# English
wikipedia.set_lang("en")

for pagename in articles_eng:
    page = wikipedia.page(pagename)
    with open("../data/contents/" + pagename + "_eng_contents.txt", "w") as myfile:
        myfile.write(page.content)


# Urdu
wikipedia.set_lang("ur")

for pagename, fname in articles_urdu.items():
    page = wikipedia.page(pagename)
    with open("../data/contents/" + fname + "_contents.txt", "w") as myfile:
        myfile.write(page.content)
