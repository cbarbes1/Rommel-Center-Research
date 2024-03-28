''' 
Author: Cole Barbes
Last edited: 03/27/2024
Analyze abstracts to determine a set of categories
'''
import openai
import os
import json

API_KEY = os.getenv('OPENAI_API_KEY')

# Here we define the various prompts we will need within this framework of analysis functions

__initial_prompt__ = f"""
You are an expert constructing a taxonomy from an abstract. \
Given a list of predefined categories and topics \
Please find a hierarchy of topics that go as JSON as follows\
<Parent Category> : <Child Category>, <Child Category> \
This should be a consise category like Computer Science
There should only be one root category with all the subcategories under it
Make sure the root category is a high level category
For the subcategories, give a relation score of high, medium or low
"""

test_abstract = f"""\
    Taxonomies represent hierarchical relations between 
entities, frequently applied in various software modeling and
natural language processing (NLP) activities. They are typically
subject to a set of structural constraints restricting their content.
However, manual taxonomy construction can be time-consuming,
incomplete, and costly to maintain. Recent studies of large
language models (LLMs) have demonstrated that appropriate
user inputs (called prompting) can effectively guide LLMs, such
as GPT-3, in diverse NLP tasks without explicit (re-)training.
However, existing approaches for automated taxonomy construc-
tion typically involve fine-tuning a language model by adjusting
model parameters. In this paper, we present a general framework
for taxonomy construction that takes into account structural
constraints. We subsequently conduct a systematic comparison
between the prompting and fine-tuning approaches performed on
a hypernym taxonomy and a novel computer science taxonomy
dataset. Our result reveals the following: (1) Even without explicit
training on the dataset, the prompting approach outperforms
fine-tuning-based approaches. Moreover, the performance gap
between prompting and fine-tuning widens when the training
dataset is small. However, (2) taxonomies generated by the
fine-tuning approach can be easily post-processed to satisfy all
the constraints, whereas handling violations of the taxonomies
produced by the prompting approach can be challenging. These
evaluation findings provide guidance on selecting the appropri-
ate method for taxonomy construction and highlight potential
enhancements for both approaches.
    """

test_abstract_other = f""" \
Two studies examined relations of humor styles with well-being, social support, cognitive reappraisal, and social competence. In Study 1 (N = 108), self-enhancing and affiliative humor were associated fewer health difficulties and less psychological distress, mediated by reappraisal and social support, respectively. Self-defeating humor was associated with greater distress, mediated by both reappraisal and social support. Social competence moderated the relation of aggressive humor with social support: Individuals high on both aggressive humor and communication difficulties reported the least support. Study 2 followed undergraduates (N = 193) over ten weeks. T1 results for psychological distress replicated Study 1. Social support and reappraisal mediated relations of humor styles with T1 distress, and social support indirectly mediated the relation of aggressive humor with increased T2 distress. Aggressive humor was associated with T1 health difficulties, and self-defeating humor predicted greater health difficulties over time. Reappraisal and social support indirectly mediated the relation of self-enhancing and affiliative humor with fewer Ti health difficulties, and social support indirectly mediated the relation of aggressive humor with increased health difficulties over time. Communication difficulties moderated the relation of aggressive humor with fewer T1 positive interactions and greater somatic symptoms over time. Relations largely held controlling for shared variance among humor styles.
"""

def get_response(messages, model='gpt-3.5-turbo', temperature=0, max_tokens=500):
    response = openai.chat.completions.create(
        model=model,
        messages = messages, 
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

"""

def createTaxonomyFromJson():
    ''' 
    Create a Taxonomy with a file of abstracts
    '''
    with open('abstracts_to_categories.json', 'r') as file:
        data = json.load(file)
    abstracts = list(data.keys())
    with open('Taxonomy-Of-Abstracts.json', 'w') as file:
        for abstract in abstracts:
            messages = [{'role':'system', 'content': }]
            get_Response()
            print(, file=file)
    print("The analysis has been completed. ")

def createTaxonomyFromAbstract(abstract, label):
    ''' 
    Create a Taxonomy with an individual abstract
    parameters < The abstract of the paper >, < label for the paper designated by the user >
    '''
    fileName = str(label) + 'Taxonomy.json'
    # set all needed parameters for the api call 
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type":"json_object"},
        messages = [
            {"role": "system", "content":  "You are an expert constructing a taxonomy from a list of concepts. \
             Given a list of concepts, construct a taxonomy by creating a list of their parent-child relationships.\
             Concepts: "},
            {"role": "user", "content": abstract},
        ],
        temperature=0,
        max_tokens=500
    )
    with open(fileName, 'w') as file:
        print(response.choices[0].message.content, file=file)
    print("The analysis has been completed. ")
"""
if __name__ == "__main__":
    
    messages = [
        {'role':'system', 'content':__initial_prompt__},
        {'role':'user', 'content': test_abstract},
    ]
    response = get_response(messages)
    print(response)