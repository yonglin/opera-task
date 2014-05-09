from __future__ import  division
def jaccard_sim(A,B):
	'''computing Jaccard similary between set A and set B'''

	overlap = len(A & B)
	total = len(A | B)

	similary = overlap / total # or smoothing it as (overlap + 1) / total

	return similary