
# coding: utf-8

# In[31]:


import ipaddress
import sys
import pandas as pd

def check_4(Ip):
    try:
        ip = ipaddress.ip_address(Ip)
#         print('%s is a correct IP%s address.' % (ip, ip.version))
        return True
    except ValueError:
#         print('address/netmask is invalid: %s' % sys.argv[1])
        return False

def files_p(file):
    filet = file+".txt"
    filec = "../data/editors/"+file+".csv"

    df = pd.read_csv(filec, names=['UID'])
    f= open(filet,"w+")
    
    for ind in df.index: 
        if(check_4(df['UID'][ind])):
            f.write(df['UID'][ind] + "\n")
    f.close()

def main():
    
    files = ["authors_article_en_27-10-2019 21-52-24", "authors_article_hi_27-10-2019 21-52-25","authors_article_ur_27-10-2019 21-52-30","authors_insurg_en_27-10-2019 21-52-24","authors_insurg_hi_28-10-2019 11-28-21","authors_kash_en_27-10-2019 21-52-24","authors_kash_hi_27-10-2019 21-52-25","authors_kash_ur_27-10-2019 21-52-30"]
    
    for ff in files:
        files_p(ff)
#         print("hi")

if __name__ == '__main__':
    main()

