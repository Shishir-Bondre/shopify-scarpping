import pandas as pd
from bs4 import BeautifulSoup
import urllib
import facebook
store_name=[]
store_link=[]
store_ranking=[]
store_facebook_details=[]
store_notListed=[]
noRec=0
def getStoreNames(url,pageNo):
    pageNo=int(pageNo)+1
    for inc in range(1,pageNo):
        no=str(inc)
        page_url=url+'?orderby=rating%20asc&page='+no
        res = urllib.urlopen(page_url).read()
        page= BeautifulSoup(res,"lxml")
        firstColumn=page.find_all("div",class_="col-xs-3 tborder")
        secondColumn=page.find_all("div",class_="col-xs-1 tborder")
        for i in range(1,200):
            if(i%2!=0):
                store_name.append(firstColumn[i].get_text().split('.')[0])
                store_link.append(firstColumn[i].a["href"])
            else :
                store_ranking.append(secondColumn[i].get_text())
            if(i==199):
                store_ranking.append(secondColumn[199].get_text())
    store_details=pd.DataFrame({'Name': store_name,'Link': store_link,'Ranking': store_ranking})
    print store_details
    noRec=len(store_name)
    print noRec
def getStoreDetails(store_name,noRec):
    graph = facebook.GraphAPI(access_token="EAACEdEose0cBAObf8y5euJl89ZAr6I139gZAgQqvRWigWqZC5Hiu7QOVEkrkQiVfodGn0JwEzZANdyC94XJhsORIIRTmF6CwnKUZCecbvyRfuktZCg6eHQnuegewu9CpEdCDOI3Bd3BCjYeM7bKEZBsB6WlHy7DptGTMz8EdJ2qQdFnpzAq6Ums3ji2tT7WMHfRnR0GhYo5QQZDZD", version="2.11")
    for i in range(0,noRec):
        name=store_name[i]
        try :
          store_facebook_details.append(graph.get_object(id=name, fields='id,name,emails,category'))
        except :
          store_notListed.append(name)
    notFacebookStores = pd.DataFrame(store_notListed)
    facebookStores = pd.DataFrame(store_facebook_details)
    print ("This are the stores with full details ")
    print ("======================================")
    print facebookStores
    print("==========================================")
    print ("This are the stores which do not have details ")
    print ("======================================")
    print notFacebookStores
    print("=========================================")
    print noRec

getStoreNames("http://xpareto.com/",1)
getStoreDetails(store_name,99)
