# APIs/Research related to obtaining documents
## What this is:
A collection of notes from research of various APIs needed for pulling academic papers

## Obtaining DOIs for citations
A DOI is a "Digital Object Identifier", it's a standardized way to identify digital versions of cited sources. To automate obtaining documents from the APIs discussed in this research document we need to get the DOI associated with each papers citation, sometimes the DOI is provided in the citation, other times it's not. 

Here are 2 examples of what citations with a DOI looks like:  
><div style="text-indent: -0.5in; margin-left: 0.5in;">Cooper, S. A., Raman, K.K., Yin, J. (2018). Halo Effect or Fallen Angel Effect? Firm Value Consequences of Greenhouse Gas Emissions and Reputation for Corporate Social Responsibility (2018, Journal of Accounting and Public Policy). Journal of Accounting and Public Policy, 37(3), 226-240. <span style="font-weight: bold;">https://doi.org/<span style="color: red">10.1016/j.jaccpubpol.2018.04.003</span></span> [Accepted: March 28, 2018, Published: May 18, 2018, Submitted: February 8, 2017]</div>

&nbsp;
><div style="text-indent: -0.5in; margin-left: 0.5in;">Koval, M. R. (2018). How Shorebilly Brewing Company Won the Trademark Battle, but Lost the War: A Cautionary Tale for Entrepreneurs. Journal of Legal Studies Education, 35(1), 45-82. <span style="font-weight: bold;">http://onlinelibrary.wiley.com/doi/<span style="color: red;">10.1111/jlse.12069</span>/full</span> [Accepted: June 2018, Published: February 8, 2018]</div>
<br>  

In the above two examples the bolded text highlighted in red is the DOI value. Note how both start with `10.`, every DOI starts that way. Also notice following `10.` there's always 4 digits, there could be anywhere from 4 to 9 digits in that location. Next you'll notice there's a `/`, the `/` seperates the prefix and suffix of the DOI. The suffix, the thing to the right of the `/` separator can contain 1 or more ASCII characters.

So now that we know what a DOI looks like how do we actually extract that if our citation has it?  

**Regular Expressions (regex):**  
To extract the DOI string we need from the citation we can use regular expressions. In python, the library for this is imported like so:
```python 
import re
```

The process to do this would look something like so:
* First pull all the citations from the document provided into a list in python
* Construct a **Regular Expression** used to identify the DOI within the citation string
    * Regular Expression: `r"10.\d{4,9}/[-._;()/:A-Za-z0-9]+"`
    * What the above means:
        * `r` specifies the thing in quotes is a string literal, this is so python treats the `\` as an actual character and not an espace character
        * `10.` matches the "10." all DOIs start with
        * `\d{4-9}`, `\d` means digit, `{4-9}` means between 4-9 digits. So this part of the expressions matches the sequence of 4-9 digits that can follow the "10."
        * `/` matches the "/" that separates the DOIs prefix and suffix
        * Breaking down `[-._;()/:A-Za-z0-9]+`
            * the `+` means it's a sequence of one or more of the specified character in the character class which is defined by `[-._;()/:A-Za-z0-9]`. 
            * Breaking down `[-._;()/:A-Za-z0-9]` 
                * `[]` defines a character class
                * `-`, `.`, `_`, `(`, `)`, `/`, `:` include all those respective characters into the character class
                * `A-Z` and `a-z` includes any lowercase or uppercase letters into the character class
                * `0-9` includes any digit into the character class
* Iterate over the list, each index is a citation, for each citation we extract the DOI  

A function to accomplish the above could look something like:  
```python
import re

def extract_doi(citations):
    """
        Takes in a list of citations, attempts to get their dois
        If the doi exists it adds the doi to the dois list.
        If the doi doesn't exist adds the citation to the doi_not_found list
        Function returns a tuple of the two lists
    """
    doi_regex = r"10.\d{4,9}/[-._;()/:A-Za-z0-9]+"

    dois = []
    doi_not_found = []

    for citation in citations:
        match = re.search(doi_regex, citation, re.IGNORECASE)
        if match != None:
            # match.group() returns the entire string re.search matched
            dois.append(match.group())
        else:
            doi_not_found.append(citation)
    return dois, doi_not_found
```

## Now What?
### Remember how we got two lists back from the extraction?
Our `dois` list contains the actual dois that we extracted out the citation  
The doi_not_found list contains the citations for which a doi wasn't found.  

So we have 2 cases, we either have a doi or we don't. If we have a doi we progress to using it to obtain the paper via one of the APIs discussed further down. If we don't have the doi for the citation then we need to obtain it, guess what? There's an API for that too. So let's talk about it.

## Case 1: Succesfully extrated a citations DOI
### SCOPUS/Elsevier (Science Direct)
#### Links:
>[API Portal](https://dev.elsevier.com/)  
>[Documentation](https://dev.elsevier.com/api_docs.html)  
><a href="ScopusAPI.pdf" target="_blank">Scopus API PDF</a>

#### General Info:
>"Elsevier APIs implement a concept we call a 'VIEW'. Submitted as a parameter, a VIEW is used to deliver specific metadata in an API's payload. Some VIEWs are restricted based on subscription status to an Elsevier product. Some APIs do not utilize the VIEW parameter. VIEWs, where applicable, are documented below. You can see the metadata available for a VIEW by clicking a given API's [Views] link."

### ScienceDirect APIs

API: **Abstract Retrieval**  
- Description and Root-endpoint:
    >**Returns the Scopus abstracts of a specified document,
including rich metadata like links to author and affiliation
profiles.**  

- Method:
    >**GET**  

- Response formats:
    >**XML**  
  
  <br>
**How to use:**
Follow the steps here:  
>https://github.com/ElsevierDev/elsapy?tab=readme-ov-file