import sys
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
import pymssql
from configparser import ConfigParser, ConfigParser
from datetime import datetime
from shapely import wkt
import time
import datetime
import timeit
import json
import logging
from bs4 import BeautifulSoup as Soup
import unittest

#tests

# does kml file exist

# does connection succeed

# does  destination table exist

###########################################################################################
# Main
# Purpose : main wrapper for al other fucntions
###########################################################################################
def main():
    start_time = datetime.datetime.now()
    print("Start Time %s " % (start_time))
    
    if len(sys.argv) == 3:
        
        kml_file=sys.argv[1];
        dhp_file=sys.argv[2]

    with open(kml_file) as data:
        kml_soup = Soup(data, 'lxml-xml') # Parse as XML

    folders=kml_soup.find_all('Folder')

    try :
        for folder in folders:

            name_tag=folder.select('name')
            name=name_tag[0].string
            Placemarks=folder.select('Placemark')            

            for Placemark in Placemarks:
               
               Point=Placemark.Point.contents
               for coordinates in Point:
                    Coords=coordinates.contents

               table=Placemark.select('table')
               for items in table:
                   cameraLoc = items.h1.contents
                   Cameras = items.select('td')

                   i=0
                   for Camera in Cameras:
                       Imgs=Camera.select('h1')
                       Srcs=Camera.select('img')

                       for Img in Imgs:                                                 
                            cameraDesc = Img.contents
                            cameraRef = Srcs[i].get('src')
                            print(name, Coords, cameraDesc, cameraRef)
                            i=i+1 
                       i=i+1
           
      
    except Exception as err:
        print('FunctionName: %s',  err)
       


    else :
        print("Wrong number of arguements")  
    return 0;
############################################
#
#  Main
# https://curl.trillworks.com/#
############################################
if __name__ == '__main__':
    
    main()
    
