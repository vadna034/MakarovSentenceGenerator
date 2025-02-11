# Markov Chain Sentence Generator

Quick project I made back in college to work on Python. 

Sentency.py loads all of the text from the books.txt file (books.txt includes text from a number of classic books).
It stores data in a dictionary, and serializes the object using the [Pickle modules](https://docs.python.org/3/library/pickle.html). 

TextAnalyzer.py will then generate 10 sentences using the object stored in obj.pck1 through the use of markov chains. 

## To run

Simply either run python Sentence.py / TextAnalyzer.py. 

The object is stored in the repo, so there's no reason it won't run without running Sentence.py first, but both are included for 
the sake of clarity. 
