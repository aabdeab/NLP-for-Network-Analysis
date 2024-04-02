# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:38:35 2024

@author: pc
"""

from neo4j import GraphDatabase

# Fonction pour établir la connexion à la base de données Neo4j
def connect_to_database(uri, username, password, database):
    return GraphDatabase.driver(uri, auth=(username, password), database=database)

# Fonction pour créer les relations entre Company et City
def create_relationships(driver):
    with driver.session() as session:
        result = session.run("""
            MATCH (c:Company), (ct:City)
            WHERE ct.City CONTAINS c.Headquarters  
            CREATE (c)-[:LOCATED_IN]->(ct)
            RETURN count(*)
        """)
        return result.single()[0]

# Paramètres de connexion à la base de données Neo4j
uri = "bolt://localhost:7687"
username = "neo4j"
password = "ur_password"
database = "nlp"

# Établir la connexion à la base de données
driver = connect_to_database(uri, username, password, database)

# Créer les relations entre Company et City
count = create_relationships(driver)

# Afficher le nombre de relations créées
print("Nombre de relations créées :", count)

