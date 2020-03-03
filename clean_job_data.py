from config import Essex_Shape_Config, Web_Scrape_Config
from job_scrape import crawl_pages
import os
import pandas as pd
import geopandas as gpd

def get_job_data(scrape_path = Web_Scrape_Config.SCRAPE_OUTPUT_PATH):
    """Pulls job data from the job_scrape file, creates a new scrape if needed"""
    if os.path.exists(scrape_path) == False:
        print(f"There is no file {scrape_path}")
    else:
        return(pd.read_csv(scrape_path, names=Web_Scrape_Config.JOB_DATA_HEADERS))

def add_shapes(df):
    """merges geopandas df to add polygons to job search terms"""
    gdf = gpd.read_file(Essex_Shape_Config.LAU_SHP_FILE)
    gdf.replace({'LAD19NM': {"Epping Forest": "Epping"}}, inplace = True) #epping is shortened in scraping
    merge_df = pd.merge(df,gdf, left_on='search_term', right_on='LAD19NM')
    merge_gdf = gpd.GeoDataFrame(merge_df)
    return merge_gdf





def job_data_w_geog():
    job_data = get_job_data()
    merged_gdf = add_shapes(job_data)


    return(merged_gdf)



if __name__ == "__main__":
    print(job_data_w_geog().head())