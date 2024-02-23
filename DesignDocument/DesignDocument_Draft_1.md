# Data Needed (1st Semester)
- Number of faculty pubished aricles
- Number of total articles published 
- Number of class A, B, C, etc publications
    - Need publication class for each citation/article
- Average number of citation sper publication*
- Number of faculty submitting funding proposals
- Number of awared funding
    - as in how many proposals have actually been awared $
- Number of proposals submitted & awarded
- Total monetary value of funding awarded  

>This can be done at first on a category by cateogry basis and then we can get total numbers of the school rather easily.  

Citation
    title
    professor

I go to the paper with the associated professor name

how do i get to a specific paper with just a name?


Lastname, Kwangwook
Kwang Wook
KwangWook


Cole's citation way idea:
Give me the title of a paper and the author who wrote it
I go to the file that corresponds with that paper grab the WoS category add that paper into that category and +1 that author you gave me if they have not already been counted

this will get rid of the issue of trying to match WoS author format, as I will be looking up by title, and then just counting it with the one version of the name you gave me
that came from salisbury website

ex:
title "We talk about AI", author "Tu"

Spencer: goes to "We talk about AI" get the WoS category, adds the paper under it as an article, adds Tu as a faculty member for that category if he isn't already
adds Tu's department to that category if it isn't already
- Author, Department are using SU's website one's rather than the inconsistent WoS ones.




Spencer's WOS way idea:
Issue with near duplicate names so same person gets counted under a category more than once. 

>Lastname, Kwangwook<br>
>Kwang Wook<br>
>KwangWook  

and

>Lastname, Firstname M.I.  
>Lastname, Firstname  
>Lastname, Firstname Middlename  

Process:

See a name save it
"Smush" the name
- remove middle initial if it exists
- make everything lower case
- remove white space

the above names turn into
>lastname,firstname  
>lastname,firstname  
>lastname,firstnamemiddlename  

Since the set won't accept duplicates we'll have these two versions  
>lastname,firstname  
>lastname,firstnamemiddlename  

In order to handle the ones that slip through we use a nearest neighbor to identify "near-duplicates"  
Once the near duplicaets have be identified i.e.,  
>lastname,firstname  
>lastname,firstnamemiddlename  

We look across the entire category taxonomy and see which version of the name occurs most. We keep that version and throw the other out. So we'd be left with:  
>lastname,firstname  

From here we convert this name back to the original name we saved so  
>lastname,firstname  

Turns back to  
>Lastname, Firstname  

or  
>Lastname, Firstname M.I.  

If the name that occured the most was
>lastname,firstnamemiddlename  

then we keep that one and throw out  
>lastname,firstname  

then  
>lastname,firstnamemiddlename  

is converted back to  
>Lastname, Firstname Middlename  

Tu, Junyi
Tu, Junyi MI.
Tu, Junyi Middlename

tu,junyi
tu,junyimiddlename

tu,junyi

Tu, Junyi

