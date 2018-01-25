import pandas as pd
from bs4 import BeautifulSoup
import urllib
import facebook
store_name=[]
store_link=[]
store_ranking=[]
store_apps=[]

store_notListed_name=[]
store_notListed_link=[]
store_notListed_ranking=[]
store_notListed_apps=[]

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
    store_details.to_csv("csv/storeDetails/orginalScrapped.csv",encoding='utf-8')
    print "Got Stores Successfully"
    print "========================="
    print len(store_name)




def storeAppDetails():
  noStores=len(store_name)
  print noStores
  temp=pd.read_csv("csv/appDetails/app.csv")
  AppNames=temp['apps']
  #print AppNames
  for i in range(0,noStores):
    slink=store_link[i]
    print("Shop No : "+str(i)+"\nStore Link : "+slink)
    appList=[]
    try:
      r = urllib.urlopen(slink).read()
      soup = BeautifulSoup(r,"lxml")
      scriptTags=soup.find_all("script")
      script=str(scriptTags)
      for app in AppNames:
        if (app in script):
          appList.append(app)
      store_apps.append(appList)
      print "added to list"
    except:
      store_apps.append('None')
      print "added to None to app list"
  store_details=pd.DataFrame({'name': store_name,'link': store_link,'ranking': store_ranking,'apps':store_apps})
  store_details.to_csv("csv/storeDetails/orginalScrapped.csv",encoding='utf-8')
  print "Added the store to CSV file store as orginalScrapped.csv \n Now getting Facebook Details :"



def getStoreDetails(store_name,noRec,accessToken):
    tempList=pd.read_csv("csv/storeDetails/orginalScrapped.csv")
    apps=[]
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
          apps.append(store_apps[i])
          count+=1
        except :
          store_notListed_name.append(name)
          store_notListed_link.append(store_link[i])
          store_notListed_ranking.append(store_ranking[i])
          store_notListed_apps.append(store_apps[i])
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
    facebookStores = pd.DataFrame({'name': store, 'about': about, 'category':category, 'email':email,'Link': website,'Ranking': ranking,'facebook page': link,'facebook subscribers': fan_count,'instagram Url':insta,'Apps Installed':store_apps})
    #print facebookStores
    notFacebookStores = pd.DataFrame({'name':store_notListed_name,'link':store_notListed_link,'ranking':store_notListed_ranking,'apps':store_notListed_apps})

    notFacebookStores.to_csv("csv/storeDetails/notFacebook.csv",encoding='utf-8')
    facebookStores.to_csv("csv/storeDetails/storeDetails.csv",encoding='utf-8')
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
#noRec=int(10)
noRec=len(store_name)
accessToken="EAACEdEose0cBAOXtC7A7t9GOPY6qSgfZB3N1hvkAfqdDPm3Hq6T8ShnBwtGnsKGfJNediW7ZA6psTYz2AZC983F1yawjgPLcZC1rmEWo3IXj0iarEfKyw2r1sgj0up6Tcq4jAqeZCqt1qzlvVVFKjWYqhqhZC0I4JsaslZANVxU3lvZAnrPv1QRQ7zIdKbQtSaZA3wmMinZCgzgQZDZD"
storeAppDetails()
getStoreDetails(store_name,noRec,accessToken)
