import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import fcluster, dendrogram, linkage
from sklearn.cluster import DBSCAN


df = pd.read_csv('./weather-check.csv')

df.head()

df = df.drop(labels=df.columns[0], axis=1)
df = df.drop(labels=df.columns[2], axis=1)

df.head()

df_dummy = pd.get_dummies(df)

X = df_dummy.values

scores = []

for k in range(2, 20):
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=1)
    labels = kmeans.fit_predict(X)

    silhouette = silhouette_score(X, labels)
    scores.append(silhouette)

answer1 = round(max(scores), 2)

Z = linkage(X, method='average', metric='cosine')
dend = dendrogram(Z)

# there should be a chart

from collections import Counter

for t in np.arange(0.1, 1 + 0.1, 0.1):
    label = fcluster(Z, t, criterion='distance')

    if np.unique(label).size == 5: break  # must have five clusters

label_count = Counter(label)
second_largest_count = sorted(label_count.values(), reverse=True)[1]
second_largest_claster = [k for k, v in label_count.items() if v == second_largest_count]

df.loc[:, 'label'] = label
group = [group for i, group in df.groupby('label') if i == second_largest_claster[0]]

gender_count = Counter(group[0]['What is your gender?'])
answer2 = round(gender_count['Male'] / gender_count.total(), 2)

blank_rate = {}
for eps in np.arange(0.1, 1 + 0.1, 0.1):
    dbscan = DBSCAN(eps=eps, min_samples=20, metric='cosine')
    dbscan.fit(X)
    labels = dbscan.labels_

    if np.unique(labels).size < 2: continue  # must have at least two clusters

    df.loc[:, 'label'] = labels
    group = [group for i, group in df.groupby('label') if i == -1]

    blank_count, total_labels = 0, 0
    for title in list(df):
        count = Counter(group[0][title])
        blank_count += count['-']
        total_labels += count.total()

    blank_rate[blank_count / total_labels] = eps

answer3 = blank_rate[max(blank_rate.keys())]

print('kmeans {:.2f}\nagg    {:.2f}\ndbscan {:.2f}'.format(answer1, answer2, answer3))