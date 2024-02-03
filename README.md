# Rommel Center Research | Salisbury University Software Engineering Project

Salisbury University  
https://www.salisbury.edu/ 

## Description
> The home of The Rommel Center Research Concentrations Study. This project harnesses various AI tools to analyze textual data and create an application that will visualize each category of research at Salisbury University. Each individual category will have in depth details related to funding, Influential Faculty, etc...

## Table of Contents

## Basic Structure of the project
- AI analysis of different documents to find keywords, topics, and recurring themes which is fed into a database
- Textual Database of Various Data points regarding research proposals and such.
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

## Roadmap

### Module 1
### In this module, We will be completing a spreadsheet that allows us to first gather the needed data and organize it for businesses at minimum.

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
