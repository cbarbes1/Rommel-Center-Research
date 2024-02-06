# APIs related to obtaining documents
## What this is:
A collection of notes from research of various APIs needed for pulling academic papers

## Obtaining DOIs for citations
A DOI is a "Digital Object Identifier", it's a standardized way to identify digital versions of cited sources. To automate obtaining documents from the APIs discussed in this research document we need to get the DOI associated with each papers citation, sometimes the DOI is provided in the citation, other times it's not. 

**Case for when it is:**  
Here are 2 examples of what citations with a DOI looks like:  
><div style="text-indent: -0.5in; margin-left: 0.5in;">Cooper, S. A., Raman, K.K., Yin, J. (2018). Halo Effect or Fallen Angel Effect? Firm Value Consequences of Greenhouse Gas Emissions and Reputation for Corporate Social Responsibility (2018, Journal of Accounting and Public Policy). Journal of Accounting and Public Policy, 37(3), 226-240. <span style="font-weight: bold;">https://doi.org/<span style="color: red">10.1016/j.jaccpubpol.2018.04.003</span></span> [Accepted: March 28, 2018, Published: May 18, 2018, Submitted: February 8, 2017]</div>

&nbsp;
><div style="text-indent: -0.5in; margin-left: 0.5in;">Koval, M. R. (2018). How Shorebilly Brewing Company Won the Trademark Battle, but Lost the War: A Cautionary Tale for Entrepreneurs. Journal of Legal Studies Education, 35(1), 45-82. <span style="font-weight: bold;">http://onlinelibrary.wiley.com/doi/<span style="color: red;">10.1111/jlse.12069</span>/full</span> [Accepted: June 2018, Published: February 8, 2018]</div>
<br>
In the above two examples the bolded text highlighted in red is the DOI value.  

So now that we know whta a DOI looks like how do we actually extract that if our citation has it?  

**Regular Expressions (regex):**  
To extract the DOI string we need from the citation we can use regular expressions. In python the library for this is imported like so:
```python 
import re
```

The process to do this would look something like so:
* First pull all the citations from the document provided into a list in python
* Iterate over the list, each index is a citation, for each citation we extract the DOI
* Construct a **Regular Expression** used to identify the DOI within the citation string
    * Regular Expression: r"10.\d
### SCOPUS/Elsevier (Science Direct)
#### Links:
>[API Portal](https://dev.elsevier.com/)  
>[Documentation](https://dev.elsevier.com/api_docs.html)

#### General Info:
>"Elsevier APIs implement a concept we call a 'VIEW'. Submitted as a parameter, a VIEW is used to deliver specific metadata in an API's payload. Some VIEWs are restricted based on subscription status to an Elsevier product. Some APIs do not utilize the VIEW parameter. VIEWs, where applicable, are documented below. You can see the metadata available for a VIEW by clicking a given API's [Views] link."

### ScienceDirect APIs
