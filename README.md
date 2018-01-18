# Ecommerce-Stores
### This is a web scrapper which will collect the information about the Ecommerce stores from the web.

**Information collected will be**
- Name
- Category
- Ranking
- Email id
- Facebook Page Id
- Facebook Page Name
- About
- Instagram URL
- Facebook Page Link
- Subscribers
- Alexa Ranking

### Contains :
- How To Use
- Input
- Output
- CopyRights
## 1) How Use

getStoreDetails.py is file which contains programe for extracting the shopify store and their information.
>**Installation**
- >> python version 2.6.7
- >> panadas
- >> urllib
- >> BeautifulSoup
- >> facebook-sdk (refer: https://facebook-sdk.readthedocs.io/en/latest/install.html)

run the python script ie (python getStoreDetails.py)

## 2) Input
- Website Url
- Beginning Page No :
- Ending Page No :
- Access Token : (This token you need to generate from Facebook graph Api)

## 3) Output

- StoreDetails.csv will be created in the same folder which will contain the store information having the required information
- OrginalScrapped.csv will have the details of store which are crawaled from the url sepcified
- StoresNotListed.csv contains the store which are not having the information on facebook