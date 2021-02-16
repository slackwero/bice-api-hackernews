import requests
import logging
import sys
import os
import json
import pytz
from datetime import datetime
from datetime import datetime, date

logging.basicConfig(
    # format="%(asctime)s level=%(levelname)-7s %(message)s",
    format="%(message)s level=%(levelname)-7s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


class PayloadParser:

    payload = []   

    def getHackernews(self):

        URL = "http://hn.algolia.com/api/v1/search?tags=front_page"       

        try:
            r = requests.get(url=URL)

            data = r.json()

            for value in data["hits"]:
                #print(value)
                #print("---------------------------------")  
                template = {}
                date_time = datetime.fromtimestamp(value["created_at_i"])
                d = date_time.strftime("%d/%m/%Y %H:%M:%S")

                
                template["title"]   = value["title"]
                template["author"]  = value["author"]
                template["url"]  = value["url"]
                template["date"]  = d
                template["num_comments"] = value["num_comments"]

                self.payload.append(template)
 
            print(self.payload)               

        except Exception as error:
            print(error)
            template = {"error":"Error en el api de Indecom Online"}
            self.payload.append(template)
            sys.exit(1)
            
        return self.payload