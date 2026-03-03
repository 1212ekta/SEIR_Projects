import sys #for reading command line argument
import requests #it sends requests to the server
from bs4 import BeautifulSoup   #used in scraping the web page taught in dhp class

class Information_Retreive:
    def __init__(self,webLink):
        #if the provided link not starts with http or https we will add it for fetching the data
        self.link = webLink if webLink.startswith("http")else "https://"+webLink
        
        self.parsed_page = None

    def extrct_web_data(self):
        try:
            server_respnse = requests.get(self.link, headers={"User-Agent": "Mozilla/5.0"}) #request as a browser so that it cannot deny your request as a client
            server_respnse.raise_for_status()
        except requests.exceptions.RequestException as err: #server error may be too many requests or robots.txt file is not allowing to crawl
            print("some error from server side",err)
            sys.exit()

        parsed_doc = server_respnse.text #fetch the page of html content as server accepted client request
        self.parsed_page = BeautifulSoup(parsed_doc, "html.parser") #parsed the html content and extract useful information
        main_page_head = (self.parsed_page.title.string.strip()if self.parsed_page.title and self.parsed_page.title.string else "") #extract the title of the page 
        print(main_page_head)
        Actual_body_cont = (self.parsed_page.body.get_text("\n", strip=True)if self.parsed_page.body else "") #extrat the content of body in descriptive way
        print(Actual_body_cont)
        for link_tag in self.parsed_page.find_all("a"):#find all the anchor tags
            conn_link_val = link_tag.get("href")    #in href there will be the libks connected extraxt it
            if conn_link_val:
                print(conn_link_val) #printing all the outlinks connected in the page ..outlinks are very imp in crawling

if len(sys.argv)<2: # two arguments required filename url
    print("syntax is filename.py and url") #python filename.py link
    sys.exit()  #argument is invalid exit
url_argument = sys.argv[1]  #url will be in 1 index as in the 0th index file name
execute_url_prog = Information_Retreive(url_argument)
execute_url_prog.extrct_web_data()












