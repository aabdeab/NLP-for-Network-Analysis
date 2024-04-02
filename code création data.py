# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:58:43 2024

@author: pc
"""
from neo4j import GraphDatabase
import json

# Function to create nodes and relationships in Neo4j
def import_json_to_neo4j(uri, username, password, database):
    # Connect to Neo4j
    driver = GraphDatabase.driver(uri, auth=(username, password), database=database)
    
    #listing the attributes to match between nodes 
    attrb_dict = ['Owner', 'Key people', 'Headquarters']
    
    # Read JSON data
    with open('C:\\Users\\pc\\Desktop\\cityData.json', "r", encoding="utf-8") as file:
        cityData = json.load(file)
        city_name = []
        city_info = []
        for city in cityData :
            for name, info in city.items() :
                city_name.append(name)
                city_info.append(info)
    with open('C:\\Users\\pc\\Desktop\\personData.json', "r", encoding="utf-8") as file:
        personData = json.load(file)
        person_name = []
        person_info = []
        for person in personData :
            for name, info in person.items() :
                person_name.append(name)
                person_info.append(info)
    with open('C:\\Users\\pc\\Desktop\\companyData.json', "r", encoding="utf-8") as file:
        CompanyData = json.load(file)
        Company_name = []
        Company_info = []
        for Company in CompanyData :
            for Company, info in Company.items() :
                Company_name.append(Company)
                Company_info.append(info)

    # Define Cypher queries
    
    create_person_query = "CREATE (n:Person $attributes)"
    create_city_query = "CREATE (n:City $attributes)"
    create_Company_query = "CREATE (n:Company $attributes)"
    create_relationship_query = "MATCH (a:Auteur {nom_prenom: $source}), (b:Livre {titre: $target}) CREATE (a)-[:EST_AUTEUR]->(b)"
    
    # Iterate through nodes and create them in Neo4j
    with driver.session() as session:
       

        for i in range(len(person_info)) :
            session.run(create_person_query, attributes=person_info[i])
    
        for i in range(len(city_info)) :
            session.run(create_city_query, attributes=city_info[i])
        for i in range(len(Company_info)) :
            session.run(create_Company_query, attributes=Company_info[i])
   
    """
    def find_correspondance(value, liste) :
        
    
    def match_to(company_info, person_name, city_name) :
        for company in company_info :
            attrb_list = list(company.keys())
            for attrb in attrb_list :
                if attrb == attrb_dict[0] or attrb == attrb_dict[1] :
                    find_correspondance(company[attrb], person_name)
                elif attrb == attrb_dict[2] :
                    find_correspondance(company[attrb], city_name)"""
    
    # Close the Neo4j driver
    driver.close()
    
# Set Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "ur__password"
database = "nlp"  # Change this to your database name

# Call the function to import JSON data into Neo4j
import_json_to_neo4j(uri, username, password, database)







