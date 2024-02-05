# Rommel Center Research | Salisbury University Software Engineering Project

Salisbury University  
https://www.salisbury.edu/ 

## Description
> The home of The Rommel Center Research Concentrations Study. This project harnesses various AI tools to analyze textual data and create an application that will visualize each category of research at Salisbury University. Each individual category will have in depth details related to funding, Influential Faculty, etc...

## Table of Contents

## Basic Structure of the project
- AI analysis of different documents to find keywords, topics, and recurring themes which is fed into a database
- Database of Various Data points regarding research proposals and such.
- User Interface with categorical data visualization and the ability to drill down each category into detailed chunks of data.

## Front End 
- Comprehensive Map of all research being done at Salisbury University with a user friendly interface and ease of use.
- There should also be a search feature to find exact results
- At the very least, pages associated with each concentration should have enough data to conclude if a topic is a strong or weak area of research at SU

## Back End 
- Open AI api program to process full text (possibly various document types)
- Generic script that pulls data from the SU Digital Measures and store them in a MongoDB database or a SQL database (generally harder to work with)
- Javascript back end of website that pulls data from csv files or possibly from the database

## AI usage
### Text analysis
### find the keywords and topics in research papers and research proposals | Proposed Method
> The main issue with interpreting various sets of text is the context window. Open AI's GPT 3.5 Turbo allows for about 4,096 Tokens in it's context window which translates to about 1,000 to 1,500 words.
> Solution: Automate the process of parsing blocks of text that fit into the Context Window of GPT. Then ask for the keywords and topics throughout the text and build a program around this that will keep all the information together. 

## Tools used in this project
- Tailwindcss for styling.
- React to make modularity possible and more simple to use with javascript.
- JavaScript
- Python

## Options
Neural Network:
	How it works (basically):
Train on labeled dataset
It will learn to recognize patterns based on the dataset
Labels = what you want it to predict
If we want it to predict categories of papers then we provide it papers with the categories already labeled to train on
What is cleaning data in terms of text classification?
Remove “stop words”
Is
Was
As
That
Reducing words to their root word
Running -> Run
Runs -> Run
Ran -> Run
What’s the point of cleaning the data?
Take a paper that studies something about exercise, and has to do with cardiovascular health. It talks a lot about running on a treadmill and the benefits of it.
Go through the paper and turn all the instances of running, ran, runs, run into “run”, then it looks at the frequency of “run” and based on that draws a conclusion based on the patterns it’s already been trained to recognize
So if it’s been trained to recognize that the word “run” is associated with exercise and exercise is associated with health then it can determine the paper is about exercise and health, and even going further could recognize “run” is associated with cardiovascular activity and could also classify it as so.
TRADITIONAL MACHINE LEARNING ALGORITHM WILL LOOK AT WORD FREQUENCY
	Pros:
Full control over design of the model
Can customize it for exactly your use case
Less complex
While BERT doesn’t often give hallucinations this NN never will as it is DETERMINISTIC
Deterministic in the sense means that for the same input it will give the same output every single time you run it
Doesn’t require us to use HPCL but will likely want to anyway so this is sort of a nonfactor
	Cons:
Doesn’t actually understand what a word means
Why’s this matter? To accurately determine what an academic research paper is about you need to understand what the words they’re using means in the context of the research.
“Run” could be associated with the act of running which could be associated with exercise but it could also be associated with running from danger, running because you’re late, etc.
Must ensure careful regularization to mitigate overfitting:
What is this?
If a model becomes overfitted to its training data, then it will hurt its performance on unseen data. 
If the model design is too complex as in it takes too many parameters that are too specific then when it sees new data it will have a hard time actually accurately categorizing it as it’s not used to the kind of language being used
Because it doesn’t understand context or word meaning and only really goes word frequency and matching that to patterns it will perform less than ideal in complex scenarios.
What’s complex:
Classifying a singular category is not complex
But classifying a paper into a category and then classifying it into a subcategories of that category and then an additional “theme” (category) of each of those subcategories is quite complex

BERT:
	What is it?
		A language model
	How it works (basically):
From Default:
Is built on a bidirectional transformer architecture
When looking at word it looks at the words to the left and right of that word to understand the context of the current word in an effort to understand what that word means in the context
Several pretrained “base” models
Trained already on a large set of text, or a chunk of the internet. So things like wikipedia, different forums, etc.
This means it already has a general understanding of language, as in understands what words “mean”
Why is it useful:
If it already understands language meaning then we’re just additionally training it on that language in an academic context
In layman's terms BERT tries to understand what something is actually saying vs a traditional text classification algorithm via a neural network is just looking for frequency patterns.
In the context of academic papers, understanding what something is actually saying is key to knowing how to categorize it. For example, you could have a business research paper that looks at the applicable uses for AI such as ChatGPT in industry. A neural net may want to classify this as an AI paper due to the frequency that AI is talked about in it, but in reality the paper is about using AI in industry so it should really be classified as business. BERT will actually try to understand the meaning of the paper and classify it based on the actual meaning rather than word frequency.
	Pros:
Discriminative model
Designed to make specific predictions from input data.
When fine-tuned on specific data learns to make predictions based on the data, and also uses the categories it was trained on for classification. 
Mitigates overfitting via how it trains:
Masked Language Model (MLM)
Some of your training data is automatically “masked” aka redacted out of the set.
Next Sentence Prediction (NSP)
Train on the unmasked things and try to use that to predict what the masked content is
	Cons:
Computational requirements.
Have to use the HPCL to do the initial training, and could take several hours to a day depending on which version of BERT we choose and how big our fine-tuning training set is.


### Module 1
### In this module, We will be completing a spreadsheet that allows us to first gather the needed data and organize it for businesses at minimum.
- Scripts to take data out of the mongodb database to add data to the spreadsheet

### Module 2

### Module 3

## Team Members

## FAQ

## Sponsors

## Sources



## Meeting 1 Notes

### Questions 
#### What is being researched?
#### Who is researching?
#### What is the research specialization?
#### Is any given specialization a strength or weekness for the university?
- What is considered strong?
- What is considered weak?
#### 
