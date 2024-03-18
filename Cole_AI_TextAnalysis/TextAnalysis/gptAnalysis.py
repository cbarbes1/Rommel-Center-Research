import openai
import os
import json

API_KEY = os.getenv('OPENAI_API_KEY')

def createTaxonomy():
    
    with open('abstracts_to_categories.json', 'r') as file:
        data = json.load(file)
    abstracts = list(data.keys())
    with open('Taxonomy-Of-Abstracts.json', 'w') as file:
        for abstract in abstracts:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                response_format={"type":"json_object"},
                messages = [
                    {"role": "system", "content": "You are a helpful topic model. Every prompt will be an abstract, your job is to analyze the abstract and extract a list of possible topics for it. The topics start at a high level and get more detailed as you go. The topics for example should be like Computer Science or Business etc..., output should be JSON with the root being the abstract"},
                    {"role": "user", "content": abstract},
                ]
            )
            print(response.choices[0].message.content, file=file)
    print("The analysis has been completed. ")

if __name__ == "__main__":
    createTaxonomy()