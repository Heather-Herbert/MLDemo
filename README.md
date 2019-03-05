# MLDemo
Code for the AppSol team meeting 6-March-2019

## Build
This application requires python 3 and the following modules (and related dependances)

nltk
sklearn

Both can be installed via pip

## To run
0. Remove all the files under the pickled_algos folder
1. To train the models add positive and negative statments to the relivent files under the short_reviews folder
2. Run train.py - I had difficultys running this under IDLE in windows, but runs fine from the command line (under Linux)
3. Once the models are built run test.py

### Importing the modules for you own applications
the sentiment analysis module can be imported with
```python
import sentiment_mod as s
```

And called with
```python
s.sentiment("This is a string")
```
this will return an array, element 0 indicates if the statment is positive and negative (pos or neg) and the second element the confidence level.

the keyword analysis module can be imported with
```python
import keywords_mod as k
```

And called with
```python
k.keyWords("This is a string")
```

This will return an array of the five most common keywords. Each element within the array will consist of the and array containing the keyword and the frequency it occures withing the phrase.
