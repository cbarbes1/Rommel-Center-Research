# Rommel Center Research Design Document - First Semester
## Overview

## Workflow
1. Collect data
    - Faculty article metadata accessed via Web of Science database
    - All current Salisbury professors articles from the last 5 years are collected
        - this means they're collected on an author by author basis NOT by affiliation only
    - Faculty contact info and standardized names via:
        - scraping of the salisbury website. Names are linked to current names in the database to get a standardized name.
    - Collect funding related data from proposals provided
    - Collect data off citations provided to get publication class (A, B, C,...)
        - If data not available can look for other avenues to obtain publication class, but some may just not have the data necessary for every feature.
2. Cleaning of data
    - Comb though the raw data extracted and:
        - filter faculty, author, and department by category, not counting duplicates in any one category.
            - involves process of removing near-duplicate names, incorrect departments (such as the university address being identified as a department)
        - Pull out citation data:
            - number of citations
            - grade of the publication
            - associate the above with the citations themselves in a python dataclass, and later a database.

3. 'Web of Science' mode
    - Web of science provides categories for all their paper metadata.
    - Since we already have this information via an easy export on the WoS website we can associate faculty count, dept count, article count, etc as discussed previously.
    - This will give us a full 'Web of Science' mode
    - This is essentially just using the existing web of science taxonomy, which is regarded as one of the most robust, if not the most robust taxonomy currently available, and aggregating and presenting that data in an easy to access way for Salisbury university specifically.  

4. **AI Mode**

### AI Mode Approaches
> Since we already have the WoS category taxonomy and all the metadata our clients want 
> there needs to be a purpose for this AI mode. The purpose of that AI begins to make to make since when you look at WoS categories there's over 100, nearly 150. While this may not seem like a lot in the greater context of academic research when you hone into a particular school it is. This is because each school has their own areas where they're quite strong, and areas whey they aren't as strong. So having all WoS categories may not give useful insights but for the most researched areas, this is due to the vast amount of varying fields and subfields on WoS.  

> Where AI comes in is it will allow us to generate a category taxonomy that is more easy to understand at a glance, which is addressing the needs of the client. Then we need to go about assessing faculty, articles, and department and sorting them into to the heirarchal category taxonomy we created. This can be accomplished in several ways.

## Mix of existing AI resources/ models 
### ChatGPT 

### BERTopic 
> BERTopic allows us to get a collection of topics for each article. This aids in creating a heirarchal structure like CS -> AI -> ML -> DL. It also allows us to find adjacent categories such as 'AI in Economics'.  
- Create an array of topics
    - Combining separate taxonomies which are more focused on specific fields.
        - arXiv: science and technology
        - CCS: Computer Science Specific
        - PubMed: Medical sciences
        - etc
- **BERTopic combs through our abstracts** and via it's bidirectional transformer architecture it attempts to understand what the abstract meaning is.
- **How BERTopic pipeline works for us:**
    - Uses BoW (Bag of Words) to find keywords in each abstract, from here it generates it's own category
    - It then fits that category to the best fitting category you provided it
```python
#TODO: Cole adds more info
```

### Looking ahead - Our own Neural Network 
```python
#TODO: Spencer adds info
```  

# Tools  
- Python Data Classes to avoid nested dictionary structures
- OpenAI API
- Hugging face bert models
- Tensorflow or Pytorch to construct bert model
- 






