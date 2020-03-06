from config import Zoopla_Config
import requests
import json
import pandas as pd




def parse_pages(ret_obj:dict):
    pass


def get_prop_api(use_api = False):
    # TODO fix the itterator
    if use_api == False:
        return pd.read_csv(Zoopla_Config.output_add)
    
    else:
        # TODO may have to use mulitple times because of api key limit
        json_resp = requests.get(Zoopla_Config.base_url, Zoopla_Config.params).json() #uses the config params to get the first page

        # with open('web_data/zoopla_essex.json', 'r') as f:
        #     json_resp = json.load(f)

        prop_store_df = pd.DataFrame.from_dict(json_resp["listing"]) # creates the df with the first page
        prop_store_df.to_csv(Zoopla_Config.output_add)
        num_pages = (json_resp["result_count"]//100)+1 # gets the number of results - finds the number of pages (100 results per page) 
        print(num_pages)
        for page in range(1,num_pages+1): # start at 1 for first page, end at the last page
            params = Zoopla_Config.params 
            params["page_num"] = page #update teh page number to itterate through pages
            print(params)
            page_json_resp = requests.get(Zoopla_Config.base_url, Zoopla_Config.params).json() #get the page
            page_df = pd.DataFrame.from_dict(page_json_resp["listing"]) # append the listings to the original df
            page_df.to_csv(Zoopla_Config.output_add, mode='a')
        
        return pd.read_csv(Zoopla_Config.output_add)



def clean_prop(df: pd.DataFrame):
    pass


if __name__ == "__main__":
    x  = get_prop_api(use_api = True).head()
    print(x)

    clean_prop(pd.read_csv("web_data/zoopla_dump_test.csv")) #just pass the other functiona s an argument 