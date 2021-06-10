import numpy as np


def cm2senspec(cm):

	negatives = np.array(cm.T)[0]
	positives = np.array(cm.T)[1]

	tn = negatives[0]
	fn = negatives[1]

	tp = positives[1]
	fp = positives[0]
	
	sensitivity = (tp / float(tp+fn))
	sensitivity = round(sensitivity, 2)
	specificity = (tn / float(tn+fp))
	specificity = round(specificity, 2)

	return {'Sensitivity': sensitivity, 'Specificity': specificity}

