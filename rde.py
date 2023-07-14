#RUN THESE IN CMD BEFORE
#pip install spacy
#pip install json
#python -m spacy download en_core_web_sm

import json
data = {}

INPUT = "One of the pokemon in the group is the leader. The leader's commands are supreme"
TOP_ENTRIES_SHOWN = 30


# Opening JSON file
with open('Desktop/rde/data.json') as json_file:
    data = json.load(json_file)
 
data2 = {}
for mon in data:
    a = list(filter(lambda x: x["language"]["name"] == "en", data[mon]))
    data2[mon] = a

data2 = {k:v for k,v in data2.items() if v != []}

for mon in data2:
    data2[mon] = list(set(map(lambda x: x['flavor_text'].replace("\n", " ").replace("\x0c", " ").replace("\xad ", ""), data2[mon])))

import spacy
#nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("en_core_web_md")

key = nlp(' '.join([str(t) for t in nlp(INPUT) if t.pos_ in ['NOUN', 'PROPN', 'ADJ', 'VERB']]))
result = []
for mon in data2:
    for entry in data2[mon]:
        result.append((key.similarity(nlp(' '.join([str(t) for t in nlp(entry) if t.pos_ in ['NOUN', 'PROPN', 'ADJ','VERB']]))), entry))

d = sorted(result, reverse=True)

for i in d[:TOP_ENTRIES_SHOWN]:
    print(i[1])