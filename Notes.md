# Meeting notes 3/18/24

Look at the proposoals, have AI find the semantic meaning of them, use that to fit them into categories as well as potentially generating themes for said category ?


4 proposals
a -> AI
b -> AI
c -> SWE
d -> SWE

Computer science -> aggregate data from a,b,c,d
AI->aggregate data a,b           SWE -> aggregate data from c,d
    NLP -> a                            theme1->c
    Prmpt Eng -> b                      theme2->d

click on a b c d and see the one you want to specifically 

a b c d
cs -> all
ai -> a b d
swe -> a c d       <- ai decides where to put them, and can put in multiple places: 
bio -> c
econ -> d



bert

Here are my categories-> top lev -> mid -> themes. hey i have some root categories that are very general and i have some more specific categories

not to tie the specific cats directly to the root cats but to rather have more specific information 

top lev
mid lev

give bert categories, give bert abstracts
bert maps abstracts to top levels, and to mid levels. each abstract can be mapped to > 1 for both top and mid
    take the abstracts and compare the abstracts all your categories and get a % score value for all of them
    then based on a threshold you put them in those
    ai paper has a .0001% similarilty to theatre -> i only want ones that make sense so ones with very low % confidence score dont assign to

a bunch of themes that i derived from wherever, themes appear under the mid level cats that make sense, could appear under > 1


1. While categorizing the abstracts discover themes from them. take all themes created from all abstracts and create a total set of themes. 
    since each abstract either discovered a theme or got assigned to a theme you add that theme anywhere the article that abstract is from
        abstract1 -> catA and catB
        abstract1 -> theme1 and theme2
        catA and catB -> theme1 and theme2
    
fac research
-> playing with something -> seek publication -> apply for money

proposals are fewer 
i wrote 5 articles on this i should go get money for expanding research
get money -> publish again -> get money -> publish again -> ...

most of research in crm (business, customer relation managemetn) or marketing analytics or economic theory, where we specialize is important

for searching via prompt from industry member -> send to a chatbot and have it find the categories that prompt matches  

a bunch of words from some random person
-> how do you even know what categories to look for
-> you just type type to a gpt or whatever type thing and it comes back with articles/faculty/cats/theme and either their data directory and/or links to the pages

