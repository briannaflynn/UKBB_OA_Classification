import numpy as np
from sklearn.metrics import confusion_matrix as cmatrix
import matplotlib.pyplot as plt
import seaborn as sns

def binary_cm(preds, y):
    argpreds = np.argmax(preds, axis=1)
    input, target = argpreds.cpu().numpy(), y.cpu().numpy()
    y_true = [y for y in target]
    predictions = [x for x in input]
    confusion_matrix = cmatrix(y_true, predictions, labels = [0, 1])
    return(confusion_matrix)

def plot_binary_cm(cm, title="Your Confusion Matrix Plot", cmap="YlGnBu", figheight=10, figwidth=8):
    plt.figure(figsize=(figheight, figwidth))
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax, cmap="YlGnBu", fmt='g');
    
    ax.set_xlabel('Predicted');ax.set_ylabel('Actual');
    ax.set_title(title);
    ax.xaxis.set_ticklabels(['0', '1']); ax.yaxis.set_ticklabels(['0', '1']);
