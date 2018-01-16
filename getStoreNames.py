import pandas as pd
from bs4 import BeautifulSoup
import urllib
def getStoreNames(url,pageNo):
    store_name=[]
    store_link=[]
    store_ranking=[]
    pageNo=int(pageNo)+1
    for inc in range(1,pageNo):
        no=str(inc)
        page_url=url+'?orderby=rating%20asc&page='+no
        res = urllib.urlopen(page_url).read()
        page= BeautifulSoup(res,"html")
        firstColumn=page.find_all("div",class_="col-xs-3 tborder")
        secondColumn=page.find_all("div",class_="col-xs-1 tborder")
        for i in range(1,200):
            if(i%2!=0):
                store_name.append(firstColumn[i].get_text())
                store_link.append(firstColumn[i].a["href"])
            else :
                store_ranking.append(secondColumn[i].get_text())
            if(i==199):
                store_ranking.append(secondColumn[199].get_text())
    store_details=pd.DataFrame({'Name': store_name,'Link': store_link,'Ranking': store_ranking})
    print store_details