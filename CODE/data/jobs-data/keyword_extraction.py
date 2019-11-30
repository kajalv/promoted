import pandas
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from scipy.sparse import coo_matrix

# NOTE: Change the dataset name here and output file name.
dataset1 = pandas.read_csv('dice_US_jobs-clean.csv', delimiter = ',')
dataset2 = pandas.read_csv('monster_com_jobs-clean.csv', delimiter = ',')
dataset = pandas.concat([dataset1, dataset2], sort=False)

stop_words = set(stopwords.words("english"))
new_words = ["familiar", "experienced", "experience", "employment", "skill", "job", "responsibility",
"duty", "skilled", "team", "hiring", "looking", "hire", "dollar", "salary", "years", "customer", "store",
"company", "work", "service", "position", "manager", "training", "required", "ability", "impression", "principal"
,"mathworks", "null", "href", "attr", "healthcare", "xcybercx", "move", "comfortable", "must", "resume", "apply",
"please", "right", "forward", "chef", "deere", "john", "receiving", "cisco", "click", "right", "palo", "princeton",
"subvendor", "ntt", "cognizant", "later", "beacon", "hill", "caption", "title", "redwood", "city", "sunnyvale", "alto",
"applicant", "eligibility", "inc", "law", "protected", "src", "medium", "newjobs", "jpg", "cybercoders", "nonjob", "judge",
"typically", "nasdaq","vmware", "building", "strong", "bachelor", "degree", "science", "related"]
stop_words = stop_words.union(new_words)

data_map = {}

for index, row in dataset.iterrows():
    title = row['job_title']
    if title in data_map:
        data_map[title] += str(row['job_description'])
    else:
        data_map[title] = str(row['job_description'])


corpus = []
for key, value in data_map.items(): #number of rows (excluding header)
    # Remove punctuations
    text = re.sub('[^a-zA-Z]', ' ', value)

    # Convert to lowercase
    text = text.lower()

    # remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)

    # remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)

    # Convert to list from string
    text = text.split()

    # Stemming
    ps=PorterStemmer()
    # Lemmatisation
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text if not word in
            stop_words]
    text = " ".join(text)
    corpus.append(text)


cv=CountVectorizer(max_df=0.9,stop_words=stop_words, max_features=10000, ngram_range=(1,2))
X=cv.fit_transform(corpus)
# print(list(cv.vocabulary_.keys())[:10])

#Most frequently occuring words
def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in
                   vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1],
                       reverse=True)
    return words_freq[:n]

# print(get_top_n_words(corpus, 10))

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(X)
# get feature names
feature_names=cv.get_feature_names()

#Function for sorting tf_idf in descending order
def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=30):
    """get the feature names and tf-idf score of top n items"""

    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    # word index and corresponding tf-idf score
    for idx, score in sorted_items:

        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]

    return results

keywords_lists = []

for i in range(0,len(corpus)): # len(corpus)
	# fetch document for which keywords needs to be extracted
	doc=corpus[i]

	#generate tf-idf for the given document
	tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))

	sorted_items=sort_coo(tf_idf_vector.tocoo())

	#extract only the top n; n here is 10
	keywords=extract_topn_from_vector(feature_names,sorted_items,10)

	keywords_lists.append(list(keywords.keys()))

result = pandas.DataFrame()
result.insert(0, "job_title", list(data_map.keys()))
result.insert(1, "keywords", keywords_lists, allow_duplicates = False)

result.to_csv("job_skills_keywords.csv", sep=',')
