# Project Task Checklist

## Priority List FrontEnd

### High Priority
- [ ] Get category data from JSON to a simple HTML page with labels.

#### Jude & Will's idea:
- [ ] Fully incorporate data transfer from one page to another
    - [ ] If we click a faculty's name, it should take me to this page
- [ ] Create singular topic page
- [ ] Update style to not be so hectic
- [ ] Combine sites into one (refactor)
- [ ] Get first category page of just HTML page with label with data from the JSON
    - [ ] Do it for all of them
    - [ ] Style that
    - [ ] Incorporate that into the larger site
- [ ] Follow the principles here: [Google Business Site Builder Support](https://support.google.com/businesssitebuilder/answer/1657560?hl=en)

## Variables for measuring research done so far
- [ ] # of faculty publishing articles
    - have the data to figure this out but still need to write the code to do it
- [ ] # of articles publishes
    - have the data to figure this out but still need to write the code to do it
- [ ] # of class A publications
    - have the data to figure this out but still need to write the code to do it
        - Theres a * on this as not all the citations tracked publication class.
- [ ] # Of faculty submitting funding proposals
    - have the data to figure this out but still need to write the code to do it
- [ ] # of faculty awarded funding
    - have the data to figure this out but still need to write the code to do it
- [ ] # of proposals submitted
    - have the data to figure this out but still need to write the code to do it
- [ ] # of proposals awarded
    - have the data to figure this out but still need to write the code to do it
- [ ] $ of funding awarded
    - have the data to figure this out but still need to write the code to do it
**Reminder this data is only needed for last 5 years** 

Some of these may only be able to be done for purdue/henson currently due to what data we currently have.

## Data needed 
- [ ] Get lab space data (low priority do after all other data)
- [ ] Key funded project
    - have the data to figure this out but still need to write the code to do it


## More TODO
- [ ] Go through WoS and instead of getting data for Salisbury University past 5 years do it for every Professor currently working at Salisbury for the past years, once done rerun the WoS data pipeline with this data. 
- [ ] Combine all data together in a single JSON with an intuitive layout  
- [ ] Move data to a CSV in an intuitive way
    - May need to look at intermediaries such as pandas to do this 
- [ ] Figure out how to convert WoS department abbreviations to full department names
- [ ] Determine a category taxonomy strategy (Simplifying WoS categories into many-to-one or maybe combining several databases like CCS, ArXiv, etc)
    - cole is going to try to go through the citation categories and link bert topic output to a citation
- [ ] Refactor code
- [ ] Move code into one directory
- [ ] Clean up code and try to write code that's reusable
- [ ] Help on front end


**First things to do (Cole & Spencer)** 

1) Create the Taxonomy on abstracts from WoS
2) Figure out an algorithm to reduce the bag of words to a coherent category
3) Take the categories and apply them to the Wos Data 
4) output should be json with a citation and the categories found with BERTopic

Spencer
1) get the new WoS data and rerun pipeline (professors at SU over past 5 years rather than SU over past 5 years)
2) Move abbreviated departments to full department names 
3) Get the extra data metrics





