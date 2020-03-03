class Essex_Shape_Config():
    root_folder = "geog_files"
    OUPUT_GEOJSON = f"{root_folder}/essex_output_area.geojson"
    #Obtained from https://geoportal.statistics.gov.uk/datasets/output-area-to-county-and-unitary-authority-december-2018-lookup-in-england
    MAPPING_TABLE = f"{root_folder}/Output_Area_to_County_and_Unitary_Authority_December_2018_Lookup_in_England.csv" 

    LAU_SHP_FILE = f"{root_folder}/Local_Authority_Districts_April_2019_Boundaries_UK_BFC"


    LAD_boundaries = "https://opendata.arcgis.com/datasets/8edafbe3276d4b56aec60991cbddda50_2.geojson"

    COUNT_MAP_LAD = f"{root_folder}/Local_Authority_District_to_County_December_2015_Lookup_in_England.csv" 

class Web_Scrape_Config():
    root_folder = "web_data"
    OUTPUT_COLS = ['search_area','job_title', 'pay', 'pay_freq', 'company', "job_location", "desc"]
    SCRAPE_OUTPUT_PATH = f"{root_folder}/scrape_dump.csv"
    NUM_PAGES = 2000 #these need to be in units of 10, i think can go up to 2000?
    JOB_DATA_HEADERS = ["search_term", "job_title", "wage", "wage_freq", "company", "location", "desc"]





