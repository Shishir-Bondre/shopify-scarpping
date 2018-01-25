import pandas as pd
from bs4 import BeautifulSoup
import urllib
import facebook
store_name=[]
store_link=[]
store_ranking=[]
#this is the app list
#you can modify the same





#store_facebook_details=[]
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

import pandas as pd
from bs4 import BeautifulSoup
import urllib
import facebook
store_name=[]
store_link=[]
store_ranking=[]
#this is the app list
#you can modify the same





#store_facebook_details=[]
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
    tempList=pd.read_csv("csv/storeDetails/orginalScrapped.csv")
    app=
    store=[]
    about=[]
    category=[]
    email=[]
    website=[]
    ranking=[]
    fb_id=[]
    link=[]
    fan_count=[]
    insta=[]
    graph = facebook.GraphAPI(access_token=accessToken, version="2.11")
    count=1
    print "============================="
    for i in range(0,noRec):
        name=store_name[i]
        instagram="https://www.instagram.com/"+name
        try :
          facebook_data=graph.get_object(id=name, fields='name,category,emails,link,fan_count,about,website')
          email.append(facebook_data.get('emails'))
          link.append(facebook_data.get('link'))
          fan_count.append(facebook_data.get('fan_count'))
          about.append(facebook_data.get('about'))
          website.append(facebook_data.get('website'))
          fb_id.append(facebook_data.get('id'))
          category.append(facebook_data.get('category'))
          store.append(facebook_data.get('name'))
          ranking.append(store_ranking[i])
          insta.append(instagram)
          count+=1
        except :
          store_notListed.append(name)
   # print "===================="
   # print len(insta)
   # print len(ranking)
   # print len(store)
   # print len(email)
   # print len(link)
   # print len(fan_count)
   # print len(about)
   # print len(website)
   # print len(ranking)
   # print len(fb_id)
   # print len(category)
   # print "========================================"
    facebookStores = pd.DataFrame({'name': store, 'about': about, 'category':category, 'email':email,'Link': website,'Ranking': ranking,'facebook page': link,'facebook subscribers': fan_count,'instagram Url':insta})
    #print facebookStores
    notFacebookStores = pd.DataFrame(store_notListed)

    notFacebookStores.to_csv("csv/notFacebook.csv",encoding='utf-8')
    facebookStores.to_csv("csv/storeDetails.csv",encoding='utf-8')
    print "Got facebook details Successfully Total records fetched"
    print "========================="
    print count
    print "========================="
# this is the main fuction calling the above two functions

#link = raw_input("Enter the Link for Scrapping the Details")
fromPageNo=raw_input("Enter page No to begin scarpping : ")
toPageNo=raw_input("Enter page No to end scarpping : ")
#accessToken= raw_input("Enter Facebook access Token")

getStoreNames("http://xpareto.com/",fromPageNo,toPageNo)
noRec=len(store_name)
accessToken="EAACEdEose0cBAKNnKJqk7EcGIDjqqrrvX3pdDKm0cM7ODptM6PeEkYd0xA5GV4joB3VuKl5wXFvWIUFDLhvtu0AOs5LvSbzKvdRCqhmxZAdpD3NjJ3quw5arC7KC0gO3bwSrmofZCYrOZCeWJZBN13pB6LP8zO27xOaVjwKRJxr2F4EG5gfLx34m5HzjZCZANksQHF5nzF2gZDZD"
getStoreDetails(store_name,noRec,accessToken)
#storedetailsfrist=pd.read_csv("orginalScrapped.csv")
#storedetailssecond=pd.read_csv("storeDetails.csv")
#finalstore=pd.concat([storedetailsfrist,storedetailssecond], on='name',join='inner')
#finalstore.to_csv("final.csv",encoding='utf-8')




def getStoreDetails(store_name,noRec,accessToken):
    tempList=pd.read_csv("csv/storeDetails/orginalScrapped.csv")
    app=
    store=[]
    about=[]
    category=[]
    email=[]
    website=[]
    ranking=[]
    fb_id=[]
    link=[]
    fan_count=[]
    insta=[]
    graph = facebook.GraphAPI(access_token=accessToken, version="2.11")
    count=1
    print "============================="
    for i in range(0,noRec):
        name=store_name[i]
        instagram="https://www.instagram.com/"+name
        try :
          facebook_data=graph.get_object(id=name, fields='name,category,emails,link,fan_count,about,website')
          email.append(facebook_data.get('emails'))
          link.append(facebook_data.get('link'))
          fan_count.append(facebook_data.get('fan_count'))
          about.append(facebook_data.get('about'))
          website.append(facebook_data.get('website'))
          fb_id.append(facebook_data.get('id'))
          category.append(facebook_data.get('category'))
          store.append(facebook_data.get('name'))
          ranking.append(store_ranking[i])
          insta.append(instagram)
          count+=1
        except :
          store_notListed.append(name)
   # print "===================="
   # print len(insta)
   # print len(ranking)
   # print len(store)
   # print len(email)
   # print len(link)
   # print len(fan_count)
   # print len(about)
   # print len(website)
   # print len(ranking)
   # print len(fb_id)
   # print len(category)
   # print "========================================"
    facebookStores = pd.DataFrame({'name': store, 'about': about, 'category':category, 'email':email,'Link': website,'Ranking': ranking,'facebook page': link,'facebook subscribers': fan_count,'instagram Url':insta})
    #print facebookStores
    notFacebookStores = pd.DataFrame(store_notListed)

    notFacebookStores.to_csv("csv/notFacebook.csv",encoding='utf-8')
    facebookStores.to_csv("csv/storeDetails.csv",encoding='utf-8')
    print "Got facebook details Successfully Total records fetched"
    print "========================="
    print count
    print "========================="
# this is the main fuction calling the above two functions

#link = raw_input("Enter the Link for Scrapping the Details")
fromPageNo=raw_input("Enter page No to begin scarpping : ")
toPageNo=raw_input("Enter page No to end scarpping : ")
#accessToken= raw_input("Enter Facebook access Token")

getStoreNames("http://xpareto.com/",fromPageNo,toPageNo)
noRec=len(store_name)
accessToken="EAACEdEose0cBAKNnKJqk7EcGIDjqqrrvX3pdDKm0cM7ODptM6PeEkYd0xA5GV4joB3VuKl5wXFvWIUFDLhvtu0AOs5LvSbzKvdRCqhmxZAdpD3NjJ3quw5arC7KC0gO3bwSrmofZCYrOZCeWJZBN13pB6LP8zO27xOaVjwKRJxr2F4EG5gfLx34m5HzjZCZANksQHF5nzF2gZDZD"
getStoreDetails(store_name,noRec,accessToken)
#storedetailsfrist=pd.read_csv("orginalScrapped.csv")
#storedetailssecond=pd.read_csv("storeDetails.csv")
#finalstore=pd.concat([storedetailsfrist,storedetailssecond], on='name',join='inner')
#finalstore.to_csv("final.csv",encoding='utf-8')
