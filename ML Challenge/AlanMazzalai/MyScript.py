# -*- coding: utf-8 -*-
import unittest
import requests
import json
import csv
import os
import sys

from pathlib import Path

from tableauhyperapi import HyperProcess, Telemetry, \
    Connection, CreateMode, \
    NOT_NULLABLE, NULLABLE, SqlType, TableDefinition, \
    Inserter, \
    escape_name, escape_string_literal, \
    HyperException


product_table = TableDefinition(
    # Since the table name is not prefixed with an explicit schema name, the table will reside in the default "public" namespace.
    table_name="Products",
    columns=[
        TableDefinition.Column("category", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("title", SqlType.text(), NOT_NULLABLE),
        TableDefinition.Column("price", SqlType.double(), NOT_NULLABLE),
        TableDefinition.Column("available_quantity", SqlType.big_int(), NOT_NULLABLE),
        TableDefinition.Column("sold_quantity", SqlType.big_int(), NOT_NULLABLE),
        TableDefinition.Column("permalink", SqlType.text(), NOT_NULLABLE)
    ]
)

def call_mlapi_to_dict(SearchCategory):

    print("Start call_mlapi_to_dict.")

    try:
        query = {'1':SearchCategory, 'limit':'50'}
        response = requests.get('https://api.mercadolibre.com/sites/MLA/search?q='+SearchCategory+'&limit=50#json', timeout=5)
        json_data = json.loads(response.text)
        response.raise_for_status()
        #for i in json_data["results"]:
        #    print(i["title"],i["price"],i["available_quantity"],i["sold_quantity"],i["permalink"])
        print("End call_mlapi_to_dict.")
        return json_data["results"]
        # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

def run_create_hyper_file_from_csv(Myfilename):
    print("Start run_create_hyper_file_from_csv.")
    MyCSVfilename = ""
    MyCSVfilename = Myfilename + ".csv"

    path_to_database = Path(Myfilename+".hyper")

    process_parameters = {
        "log_file_max_count": "2",
        "log_file_size_limit": "100M"
    }

    with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU, parameters=process_parameters) as hyper:

        connection_parameters = {"lc_time": "en_US"}

        with Connection(endpoint=hyper.endpoint,
                        database=path_to_database,
                        create_mode=CreateMode.CREATE_AND_REPLACE,
                        parameters=connection_parameters) as connection:

            connection.catalog.create_table(table_definition=product_table)

            path_to_csv = str(Path(__file__).parent / str(MyCSVfilename) )

            print(path_to_csv)

            count_in_product_table = connection.execute_command(
                command=f"COPY {product_table.table_name} from {escape_string_literal(path_to_csv)} with "
                f"(format csv, NULL 'NULL', delimiter ';', header)")

            print(f"The number of rows in table {product_table.table_name} is {count_in_product_table}.")

        print("The connection to the Hyper file has been closed.")
    print("End run_create_hyper_file_from_csv.")

api_columns = ['title','price','available_quantity','sold_quantity','permalink']
csv_columns = ['category','title','price','available_quantity','sold_quantity','permalink']

def transform_listdict_to_filterlistdict(i,MyNewlistDict,Category):
    MyNewDict = {}
    for j in api_columns:
        if type(i.get(j)) == type("str"):
            MyNewDict[j] = i.get(j).strip()
        else:
            MyNewDict[j] = i.get(j)
        #print(MyNewDict)
    MyNewDict["category"] = Category
    MyNewlistDict.append(MyNewDict)
    return MyNewlistDict

def main():
    """Params"""
    Myfilename = sys.argv[1] #'MyFile'
    category1 = sys.argv[2] #'chromecast'
    category2 = sys.argv[3] #'fire stick'
    category3 = sys.argv[4] #'google home mini'

    """Call ML Api to get inforation to dictionary"""
    MyListDict1 = call_mlapi_to_dict(category1)
    MyListDict2 = call_mlapi_to_dict(category2)
    MyListDict3 = call_mlapi_to_dict(category3)

    MyNewlistDict1 = []
    MyNewlistDict2 = []
    MyNewlistDict3 = []

    """Data transformation (filter)"""
    for i in MyListDict1:
        MyNewlistDict1 = transform_listdict_to_filterlistdict(i,MyNewlistDict1,category1)
    for i in MyListDict2:
        MyNewlistDict2 = transform_listdict_to_filterlistdict(i,MyNewlistDict2,category2)
    for i in MyListDict3:
        MyNewlistDict3 = transform_listdict_to_filterlistdict(i,MyNewlistDict3,category3)

    """Concat dictionaries in the same variable"""
    MylistDict = []
    for i in MyNewlistDict1:
        MylistDict.append(i)
    for i in MyNewlistDict2:
        MylistDict.append(i)
    for i in MyNewlistDict3:
        MylistDict.append(i)

    """Save to csv file previous run Hyper API"""
    try:
        with open(Myfilename+'.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.DictWriter(csvfile, delimiter=';',fieldnames=csv_columns) #i.keys()
            csvwriter.writeheader()
            for row in MylistDict:
                csvwriter.writerow(row)
    except IOError as err:
        print("I/O error({0})".format(err))
        return

    """Execute Hyper API"""
    try:
        run_create_hyper_file_from_csv(Myfilename)
    except HyperException as err:
        print("Hyper({0})".format(err))

if __name__ == '__main__':
    """unittest.main()"""
    main()
