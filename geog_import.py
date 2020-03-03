
import pandas as pd
import geopandas as gpd
import os.path
import matplotlib
import descartes
from config import Essex_Shape_Config


def get_essex_output_area(create_new = False):

    if os.path.exists('geog_files/essex_output_area.geojson') == False or create_new == True:
        print("Need to download shape ffile again")
        df = pd.read_csv(Essex_Shape_Config.COUNT_MAP_LAD) # Read the mapping table
        df_essex = df.loc[df['CTY15NM'] == "Essex"] 
        gdf = gpd.read_file(Essex_Shape_Config.COUNT_MAP_LAD) # read the geometry shp file
        print("SHP file read succesfully")
        gdf_essex_shapes = gdf.merge(df_essex, on='LAD15CD') # merge the files to only hold the essex files
        gdf_essex_shapes.to_file(Essex_Shape_Config.OUPUT_GEOJSON, driver='GeoJSON') # output to a geojson
        return(gdf_essex_shapes)
    else:
        gdf = gpd.read_file(Essex_Shape_Config.OUPUT_GEOJSON)
        print('Found existing geography file')
        return(gdf)


if __name__ == "__main__":
    essex_gdf = get_essex_output_area()
    print(essex_gdf.LAD15NM_x.unique())



