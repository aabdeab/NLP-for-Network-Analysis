# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:26:21 2024

@author: pc
"""

import json
import os

def generate_cypher_queries(json_data):
    cypher_queries = []

    company_name = None
    properties = {}

    for item in json_data:
        if "Company" in item:
            if company_name:
                cypher_query = generate_cypher_query(company_name, properties)
                cypher_queries.append(cypher_query)
                company_name = None
                properties = {}
            company_name = item["Company"]
        elif "data" in item:
            data = item["data"]
            title = data.get("title", "").replace(' ', '_')
            content = data.get("content", "")
            properties[title] = content

    if company_name:
        cypher_query = generate_cypher_query(company_name, properties)
        cypher_queries.append(cypher_query)

    return cypher_queries

def generate_cypher_query(company_name, properties):
    properties_str = ", ".join([f"{key}: '{value}'" for key, value in properties.items()])
    cypher_query = f"CREATE (:Company {{name: '{company_name}', {properties_str}}})"
    return cypher_query

def write_cypher_queries_to_file(cypher_queries, output_directory):
    for i, query in enumerate(cypher_queries):
        output_file_path = os.path.join(output_directory, f"cypher_commands_{i}.txt")
        with open(output_file_path, "w") as f:
            f.write(query + "\n")
        print(f"Cypher commands have been written to {output_file_path}")

def main():
    input_json_file = input("Enter the path to the JSON file: ")
    output_directory = r"C:\Users\pc\Desktop\cypher"

    with open(input_json_file, "r") as f:
        json_data = json.load(f)

    cypher_queries = generate_cypher_queries(json_data)

    write_cypher_queries_to_file(cypher_queries, output_directory)

if __name__ == "__main__":
    main()




