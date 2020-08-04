#!/usr/bin/env python
# coding: utf-8

# In[3]:
from nltk.tokenize.casual import TweetTokenizer
from itertools import chain #to unnest lists
from nltk import ngrams, word_tokenize, pos_tag
import nltk
import pickle
t = TweetTokenizer()
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.feature_extraction.text import (
    CountVectorizer, 
    TfidfTransformer, 
    TfidfVectorizer,)
from sklearn.feature_extraction import text
from wordcloud import WordCloud, ImageColorGenerator,STOPWORDS

from nltk import *
import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords, wordnet

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

from scipy import stats
import seaborn as sns

import gensim
from gensim import matutils, models, corpora
import scipy.sparse

class socialAnalysis:
    
    def __init__(self, frame):
        self.__frame = frame
        self.__tokens = []
        self.__alph = []

    def lexical_diversity(self, text):
        '''returns percentage representing lexical diversity of the text'''
        return(len(set(text))/len(text))

    def prep(self):
        '''input: column of dataframe
        output: returns nested list of tokenized, lemmatized words with stop words removed'''

        stop_words = set(stopwords.words('english'))
        lem = nltk.WordNetLemmatizer()

        #lemmatize words
        #lowercase words
        #remove stop words
#         tokens = []
        for i in self.__frame:
            sentence = []

            #lemmatize based on the pos
            # Get the single character pos constant from pos_tag like this:
            tik = t.tokenize(i)
            for tok in tik:
                pos_label = (pos_tag(tok)[0][1][0]).lower()

                # pos_refs = {'n': ['NN', 'NNS', 'NNP', 'NNPS'],
                #            'v': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
                #            'r': ['RB', 'RBR', 'RBS'],
                #            'a': ['JJ', 'JJR', 'JJS']}

                if pos_label == 'j': pos_label = 'a'    # 'j' <--> 'a' reassignment

                if pos_label in ['r']:  # For adverbs it's a bit different
                    try:
                        s = wordnet.synset(tok+'.r.1').lemmas()[0].pertainyms()[0].name()
                    except:
                        s = tok
                        continue

                elif pos_label in ['a', 's', 'v']: # For adjectives and verbs
                    try:
                        s = lem.lemmatize(tok, pos=pos_label)
                    except:
                        s = tok
                        continue

                else:   # For nouns and everything else as it is the default kwarg
                    try:
                        s = lem.lemmatize(tok)
                    except:
                        s = tok
                        continue

                if s not in stop_words:
                    #tokenize
                    sentence.append(s)
                else:
                    del s

            self.__tokens.append(sentence)

        return self.__tokens
    
    def alph(self, tokens):      
        '''input: takes a nested list of tokenized words
        output: returns unnested list of tokens with letters, emojis, and punctuation removed.
        Only alphabetical characters greater than length 4 are returned'''
        #unnest list
        unlist = list(chain(*tokens))

        #remove anything non alphabetical and append to une_alph
        regex = re.compile('[^a-zA-Z]')

#         alph = []

        #only keep words greater than 4 letters long
        for i in unlist:
            if (len(i) > 4 and i != ", "):
                self.__alph.append(regex.sub('', i))

        return self.__alph
    
    def freqChart(self, alph):
        '''Input: word list, not nested, of only alphabetical words
        Output: returns word frequency list(l) and graph of top 20 words (f)
        returns least common words (u)
        '''

        #create frequency distribution of words
        fdist1 = FreqDist(alph)

        #ten most common words
        l = fdist1.most_common(10)

        #frequency distribution chart of top 20 words
        f = fdist1.plot(20, cumulative=True)

        #10 most infrequent words
        u = fdist1.hapaxes()

        return l, u[:10], f
    
    def plot_word_cloud(self, alph):
        '''input: word list, not nested, of only alphabetical words
        output: plots word cloud'''
        str_Cloud = " ".join(alph)

        wc = WordCloud(# font_path='simsun.ttf',  
                   background_color="white",  
                   width=600,height=300,
                   min_font_size=10,
                   stopwords=STOPWORDS,
                   max_words=2000,  
                   # mask=back_coloring, 
                   max_font_size=120, 
                   random_state=42,
                   collocations=False,
                   colormap = 'cool').generate(str_Cloud)
        # image_colors = ImageColorGenerator(back_coloring)
        plt.figure(figsize=(60,30))
        plt.imshow(wc)
        plt.axis("off")
        # plt.savefig("word_cloud.jpeg")
        plt.show()
        
    def polplot(self, df, threshold):
        '''Input: polarization column and thresholds list [positive threshold, negative threshold]
        Output: Pie chart of polarization'''

        # Data to plot
        #parameter is threshold of subjectivity
        positive_threshold = threshold[0]
        negative_threshold = threshold[1]

        negative = 0
        neutral = 0
        positive = 0

        #adding count to subjective or objective depending on threshold
        for i in df:
            if (i >= positive_threshold):
                positive += 1
            elif (i <= negative_threshold):
                negative += 1
            else:
                neutral += 1

        counts=[negative, neutral, positive]

        labels = 'Negative', 'Neutral', 'Positive'
        colors = ['lightcoral', 'gray', 'lightskyblue']
        explode = (0.1, 0.07, 0.1)  # explode 1st and 3rd slice

        # Plot
        plt.pie(counts, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()
        
    def subpie(self, df, threshold):
        '''Input: subjectivity column and threshold
        Output: Pie chart of subjectivity'''

        # Data to plot
        #parameter is threshold of subjectivity
        threshold = threshold

        subjective = 0
        objective = 0
        #adding count to subjective or objective depending on threshold
        for i in df:
            if (i >= threshold):
                subjective += 1
            elif (i < threshold):
                objective += 1

        counts=[subjective, objective]

        labels = 'Opinion', 'Fact'
        colors = ['lightcoral', 'lightskyblue']
        explode = (0.1, 0)  # explode 1st slice

        # Plot
        plt.pie(counts, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()
        
    def __str__(self):
        return ','.join(self.__tokens)

        

