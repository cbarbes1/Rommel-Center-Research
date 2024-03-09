# Using Set Operations to solve Duplicate and Incorrect formatting of names issue

## Removing near-near-duplicates

I've handled removing the bulk of near-duplicates but am still faced with 2 issues:

1. Some near-duplicates were not similar enough to trigger the threshold. The example I noticed was the following 2 names which represent the same person.:
    - Berry, Jim
    - Berry, James
2. Name formatting is not consistent across sets. This is because the only names which had duplicates that got a standardized format (i.e. the name that appeared the most across the entire set). There were cases where not all versions of the name were present in a set. This had lead to the below:
    - Gang, KwangWook <- this is the majority of the format
    - Gang, Kwangwook <- but there's also this version in a set, because there was no duplicate, so it never got compared to see the version that appeared the most because there was only one version.

## Proposed Solution

While there are multiple ways to approach this such as FuzzyString matching, FuzzyString matching can be hard to have a repeatable process as one may need to use very specific Fuzzy functionality for one format of documents but will need another very specific Fuzzy suite for another format of documents.

Idea:
Preliminary:

- Pull in professor names from Isaac's CSV. The format I store these in should be set of strings, each item in the set should be a the professors last name in this format: "Lastname, Firstname M."
- This will act as an "Offical Faculty Name" set.

Steps:

Terminology:

- The offical set of faculty names will be referred to as the **offical set**.
- The set of faculty names we have constructed and want to modify will be called the **constructed set**.

1. Run the script as normal to remove the bulk of duplicates.
    - Now we are left with almost no duplicates, just a few left and some name formatting issues, such as it not being KwangWook in every set and some sets having Kwangwook instead.
2. For each **constructed set** we will take the intersection of it and the **official set**
    - Taking the intersection will show us the names that both the i'th constructed set and the official set have in common. The names the i'th contructed set had in common with the offical set are names we want to keep as those are correct.
3. Subtract the i'th **intersection set** from the i'th **constructed set**. Now we are left with a **leftover set**, this leftover set will contain names that are either duplicates or names which are not formatted to match their offical formatting.
4. Apply either the same process as before (MinHash and threshold simlarity) or a Fuzzy string (Levensthein) technique to find the best match in the official set for k'th element in the leftover set.
5. Once the best match is found we change the k'th element in the leftover set to the one it matched best with from the official set. This will now make the k'th name in the leftover set THE SAME STRING THAT IT MATCHED WITH IN THE OFFICIAL SET.
6. Try to reinsert the k'th name back into the construted set. 
    - If it is already in the constructed set then this k'th name was a near-duplicate and does not need to be in the set, due to sets not allwoing duplicates it will not be added.
    - If it is not alrleady in the constructed set then this k'th name was not a near-duplicate but had incorrect formatting (Kwangwook vs KwangWook) and it should still be in the set, it will then be inserted into the set.
7. This should theoretically solve the issue.
