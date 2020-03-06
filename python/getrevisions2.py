# getrevision.py actually works - saving this just in case 

import urllib.request
import re

def GetRevisions(pageTitle):
    url = "https://en.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&titles=" + pageTitle
    revisions = []                                        #list of all accumulated revisions
    next = ''                                             #information for the next request
    while True:
        response = urllib.request.urlopen(url + next).read()     #web request
        print(response)
        revisions += re.findall(b'<rev [^>]*>', response)  #adds all revisions from the current request to the list
        #print(revisions)
        with open("rev_kash_en.txt", "w+") as file:
            file.write(str(revisions))
        #cont = re.search(b'<continue rvcontinue="([^"]+)"', response)
        #print("cont " + cont)
        #if not cont:                                      #break the loop if 'continue' element missing
        #    break

        #next = "&rvcontinue=" + cont.group(1)  
                   #gets the revision Id from which to start the next request

    #response = urllib.request.urlopen(url + next).read()
    print(response)
    return revisions

testrev = GetRevisions("Kashmir conflict")
print(testrev)




#response
#b'<?xml version="1.0"?><api batchcomplete=""><query><normalized><n from="Kashmir_conflict" to="Kashmir conflict" /></normalized><pages><page _idx="3030955" pageid="3030955" ns="0" title="Kashmir conflict"><revisions><rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" /></revisions></page></pages></query></api>'


#Revisions
#ifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />', b'<rev revid="921247748" parentid="920038026" user="InternetArchiveBot" timestamp="2019-10-14T19:14:01Z" comment="Bluelinking 1 books for [[WP:V|verifiability]].) #IABot (v2.1alpha3" />']


