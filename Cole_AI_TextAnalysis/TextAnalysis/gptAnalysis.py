''' 
Author: Cole Barbes
Last edited: 03/27/2024
Analyze abstracts to determine a set of categories
'''
import openai
import random
import os
import json
#mport arxiv
#from nltk.corpus import wordnet

API_KEY = os.getenv('OPENAI_API_KEY')

# Here we define the various prompts we will need within this framework of analysis functions

format = """{ "Top-Level-Category" : { "mid-level-category": "low-level-category", "..."} }"""

format2 = """{
    "Health and Medicine": {
        "Obesity": "Sleep",
        "Sleep": "Sleep Duration, Sleep Quality"
    },
    "Social Sciences": {
        "College Students": "Health Behaviors",
        "Race/Nationality": "Blacks, Whites, South Koreans",
        "Gender": "Men, Women"
    },
    "Statistics": {
        "Multinomial Logistic Regression": "Association between Sleep Duration and Independent Variables",
        "Poisson Regression": "Relationship between Sleep Quality and Independent Variables"
    }
}"""

task = """You are a expert at generating Taxonomies from text. Users will prompt you with blocks of text and you are to do as follows. \
    I should be able to search each category and find college majors and research areas not just words \
    Analyze the text they give you and Generate a category taxonomy from: the text, your analysis and the summary you create. \
    Please find a hierarchy of topics 
    Output the taxonomy in JSON\
    <Parent Category> : <Child Category>, <Child Category> \
    This should be a concise category like Computer Science
    Only give about 5 or 6 categories, they should be categories from this site https://arxiv.org/category_taxonomy\
    The caregories should not be sentences
    Here is an example taxonomy:
    machine learning 1st level
    learning paradigms 2nd level
    cross validation 2nd level -> supervised learning 3rd level, unsupervised learning 3rd level
    To be a successful taxonomy, It should look as follows {format} in JSON \
    """
__initial_prompt__ = f"""
You are an expert constructing a category taxonomy from an abstract to output JSON. \
The output should be as follows: {format}
Given a list of predefined categories and topics \
Please find a hierarchy of topics 
Output the taxonomy in JSON\
<Parent Category> : <Child Category>, <Child Category> \
This should be a concise category like Computer Science
Only give about 5 or 6 categories, they should be categories from this site https://arxiv.org/category_taxonomy\
The caregories should not be sentences
Here is an example taxonomy:
machine learning 1st level
learning paradigms 2nd level
cross validation 2nd level -> supervised learning 3rd level, unsupervised learning 3rd level
heres how it should look
{format2}
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

test_abstract_new = f""" \
Juvenile summer flounder Paralichthys dentatus and southern flounder P. lethostigma inhabit turbid salt marsh estuaries. Predation rates by juveniles (50-90 mm) were examined at 5 daytime light levels (6 x 10(11) to 2 x 10(14) quanta s(-1) cm(-2)) and in darkness and 4 turbidity levels (clear [<= 1], 11, 20, and 40 NTU) at an intermediate light level. Both species fed equally well on benthopelagic mysid shrimp and benthic spionid polychaetes at all daytime light levels tested. However, predation on mysids was significantly reduced in the dark. Consumption of polychaetes was not reduced in the dark by either species, illustrating the effectiveness of non-visual foraging methods on benthic prey. Turbidity levels tested did not affect predation on either prey type by either flounder species. Locomotor behavior was examined at the same turbidity levels. P. lethostigma spent more time swimming in the water column than P. dentatus in lower turbidity (clear-20 NTU), and both species reduced swimming at 40 NTU. It appears that both species primarily use a benthic-oriented ambush foraging strategy under high turbidity conditions. This is a particularly pronounced switch in foraging style for P. lethostigma. Estuarine turbidity is increasing due to the impacts of climate change. When turbidity is elevated enough to eliminate light sufficient for visual feeding on mysids (between darkness and the lowest light level tested), feeding on this motile prey is negatively impacted for both species. Turbidity can thus alter foraging modes and types of prey consumed, affecting nursery habitat quality and the prey base supporting these young fishes.
"""

"""
This function prompts the openai api and returns the output
Parameters: The message in open ai format, the model, the temperature, and the maximum token size
Return: The output content in human readable format
"""
def get_response(messages, model='gpt-3.5-turbo', temperature=0.5, max_tokens=500):
    response = openai.chat.completions.create(
        model=model,
        messages = messages, 
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


"""
This function creates a taxonomy of a random list of abstracts and outputs to json
parameters: The abstract list, the prompt and the number of abstracts
print to json file
"""
def get_taxonomy_abstracts(Abstracts, prompt, num_iter=10):
    file_name = "Taxonomy.json"
    rand_index = random.randint(0, len(Abstracts))
    Abstract_range = Abstracts[rand_index:rand_index+num_iter]
    with open(file_name, 'w') as file:
        json_output = {}
        for abstract in Abstract_range:
            messages = [
                {'role':'system', 'content':prompt},
                {'role':'user', 'content': abstract},
            ]
            output_taxonomy = get_response(messages=messages)
            json_output[abstract] = json.loads(output_taxonomy)
        json.dump(json_output, file, indent=4)
    print("Taxonomy of abstracts Complete")

if __name__ == "__main__":
    with open('abstracts_to_categories.json', 'r') as file:
        data = json.load(file)
    abstract_list = [key for key, __ in data.items()]
    get_taxonomy_abstracts(abstract_list, __initial_prompt__)