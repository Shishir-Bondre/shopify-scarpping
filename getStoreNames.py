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
def getStoreNames(url,fromPageNo,toPageNo):
    toPageNo=int(toPageNo)+1
    fromPageNo=int(fromPageNo)
    for inc in range(fromPageNo,toPageNo):
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
    store_details=pd.DataFrame({'name': store_name,'Link': store_link,'Ranking': store_ranking})
    store_details.to_csv("csv/orginalScrapped.csv",encoding='utf-8')
    print "Got Stores Successfully"
    print "========================="
    print len(store_name)
def getStoreDetails(store_name,noRec,accessToken):
    graph = facebook.GraphAPI(access_token=accessToken, version="2.11")
    for i in range(0,noRec):
        name=store_name[i]
        try :
          store_facebook_details.append(graph.get_object(id=name, fields='id,name,emails,category,link,fan_count,website'))
        except :
          store_notListed.append(name)
    notFacebookStores = pd.DataFrame(store_notListed)
    facebookStores = pd.DataFrame(store_facebook_details)
    notFacebookStores.to_csv("csv/notFacebook.csv",encoding='utf-8')
    facebookStores.to_csv("csv/storeDetails.csv",encoding='utf-8')
    print "Got facebook details Successfully"
    print "========================="
    print "No of Store with full details : "
    print len(store_facebook_details)
    print "========================="
    print "No of Store with no details : "
    print len(store_notListed)

# this is the main fuction calling the above two functions

#link = raw_input("Enter the Link for Scrapping the Details")
fromPageNo=raw_input("Enter page No to be begin scarpping : ")
toPageNo=raw_input("Enter page No to be end scarpping : ")
#accessToken= raw_input("Enter Facebook access Token")

getStoreNames("http://xpareto.com/",fromPageNo,toPageNo)
noRec=len(store_name)
accessToken="EAACEdEose0cBAI9Rs7iL2P38a4ph0TWj1sFresZCA22w9aKM3j8hLJT7vRKE751qbSJmvViGgSZALbIB77ZArpvNkm8RgbOUisIkdZBFgZBsNho9cufB4E5VXiegfuiZCTzmJ5svZCBn9xjDDbxDT9bU5OZBWmwA4SRqZAzI9PMEJ1kG4NFRu565ApMcNH8bPMlLj3CqJwjZCmXQZDZD"
getStoreDetails(store_name,noRec,accessToken)
#storedetailsfrist=pd.read_csv("orginalScrapped.csv")
#storedetailssecond=pd.read_csv("storeDetails.csv")
#finalstore=pd.concat([storedetailsfrist,storedetailssecond], on='name',join='inner')
#finalstore.to_csv("final.csv",encoding='utf-8')
