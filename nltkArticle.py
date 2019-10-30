import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from nltk import ne_chunk
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from bs4 import BeautifulSoup
import html5lib
import requests
import re
import random
nlp = en_core_web_sm.load()

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

sent = preprocess(ex)
print(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
pprint([(X.text, X.label_) for X in doc.ents])
pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])

def url_to_string(url):
            res = requests.get(url)
            html = res.text
            soup = BeautifulSoup(html, 'html5lib')
            for script in soup(["script", "style", 'aside']):
                script.extract()
            return " ".join(re.split(r'[\n\t]+', soup.get_text()))
            
ny_bb = url_to_string('https://www.forbes.com/sites/danidiplacido/2019/03/31/what-i-dont-understand-about-pewdiepie/#4b036fab42d5')
article = nlp(ny_bb)
labels = [x.label_ for x in article.ents]
# print(Counter(labels))
# find 3 most common
items = [x.text for x in article.ents]
print(Counter(items).most_common(3))
# # dividing into sentences
# sentences = [x for x in article.sents]
# print(sentences[20])
# # show what code is actually 
# displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')
# displacy.render(nlp(str(sentences[20])), style='dep', jupyter = True, options = {'distance': 120})

# # get parts of sentence
# print([(x.orth_,x.pos_, x.lemma_) for x in [y 
#                                       for y
#                                       in nlp(str(sentences[40])) 
#                                       if not y.is_stop and y.pos_ != 'PUNCT']])

# print(dict([(str(x), x.label_) for x in nlp(str(sentences[40])).ents]))
# print([(x, x.ent_iob_, x.ent_type_) for x in sentences[40]])


# test bot code
articleList = ['https://www.forbes.com/sites/danidiplacido/2019/03/31/what-i-dont-understand-about-pewdiepie/#4b036fab42d5','https://www.nationalreview.com/corner/who-is-the-democratic-frontrunner/', 'https://www.gamesradar.com/rick-and-morty-season-4-release-date-cast-trailer-new-episodes/', 'https://www.theguardian.com/technology/2019/oct/23/google-claims-it-has-achieved-quantum-supremacy-but-ibm-disagrees' ]
propNoun = []
for i in articleList:
    articleURL = url_to_string(i)
    article = nlp(articleURL)
    items = [x.text for x in article.ents]
    propNoun.append(Counter(items).most_common(5))
print(propNoun)

halloweenObject = propNoun[random.randint(0,len(propNoun))][random.randint(0,len(propNoun))][0]

print('You should be a', halloweenObject)