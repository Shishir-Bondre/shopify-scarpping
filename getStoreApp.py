# author : Shishir Bondre
#import pandas as pd
#from bs4 import BeautifulSoup
#import urllib
#import facebook

# getStoreApp this function will return a list of store using the given input app name



# appName: name of the app
# appStoreUrl: link of the appstore so you can fetch up the details
def getStoreApp(appName,appStoreUrl,beginPage,endPage):
  pageurl=appStoreUrl+"/"+appName+"?page="+beginPage+"#reviews"
  print pageurl


appName=raw_input("Enter App Name: ")
appStoreUrl=raw_input("Enter store url: ")
beginPage=raw_input("Enter beginning page no: ")
endPage=raw_input("Enter ending page no: ")

getStoreApp(appName,appStoreUrl,beginPage,endPage)