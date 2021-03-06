# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import DBSCAN as DensityBasedSpatialClustering
from sklearn.metrics import silhouette_score
import gensim
# from principal import saida_dir
import sys

def kmeans(conjunto_de_dados, k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(conjunto_de_dados)

    try:
        silhouette_avg = silhouette_score(conjunto_de_dados, kmeans.labels_, sample_size=1024)
        # print 'kmeans:' + str(silhouette_avg) + ';'
        # print str(silhouette_avg) + ';'
        sys.stdout.write(str(silhouette_avg) + ';')
    except ValueError:
        # print 'kmeans:null;'
        sys.stdout.write('null;')

    return kmeans.cluster_centers_


def LDA_gensim(dic, n_topicos):
    ldamodel = gensim.models.ldamodel.LdaModel(dic, num_topics=n_topicos)

    topicos = []
    for i in range(n_topicos):
        distribuicao = []

        for k in ldamodel.show_topic(i, topn=len(dic[0])):
            distribuicao.append(k[1])

        topicos.append(distribuicao)

    # print topicos
    return topicos


def LDA(conjunto_de_dados, n_topicos):
    lda = LatentDirichletAllocation(n_topics=n_topicos, learning_method='online') #  DeprecationWarning: The default value for 'learning_method' will be changed from 'online' to 'batch' in the release 0.20. This warning was introduced in 0.18.
    lda.fit(conjunto_de_dados)

    # silhouette_avg = silhouette_score(conjunto_de_dados, lda.components_)
    # print silhouette_avg
    # print lda.components_
    return lda.components_


def DBSCAN(conjunto_de_dados, eps, minPts):
    dbscan = DensityBasedSpatialClustering(eps=eps, min_samples=minPts)
    dbscan.fit(conjunto_de_dados)

    try:
        silhouette_avg = silhouette_score(conjunto_de_dados, dbscan.labels_, sample_size=1024)
        # print 'dbscan:' + str(silhouette_avg) + ';'
        # print str(silhouette_avg) + ';'
        sys.stdout.write(str(silhouette_avg) + ';')
    except ValueError:
        sys.stdout.write('null;')
    # sys.stdout.write('\n')

    n_clusters_ = set(dbscan.labels_)
    n_clusters_.discard(-1)

    return dbscan.labels_, n_clusters_