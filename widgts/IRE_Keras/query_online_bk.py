import h5py
from .extract_cnn_vgg16_keras import VGGNet
import numpy as np


def query_online(index, query) :
	h5f = h5py.File(index)

	feats = h5f['dataset_1'][:]
	imgNames = h5f['dataset_2'][:]
	h5f.close()

	# init VGGNet16 model
	model = VGGNet()

	# extract query image's feature, compute simlarity score and sort
	queryVec = model.extract_feat(query)
	scores = np.dot(queryVec, feats.T)
	rank_ID = np.argsort(scores)[::-1]
	rank_score = scores[rank_ID]

	# number of top retrieved images to show
	maxres = 3
	imlist = [imgNames[index].decode() for i,index in enumerate(rank_ID[0:maxres])]

	return imlist

	# print("top %d images in order are: " %maxres, imlist)