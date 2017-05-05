# Classification of a biomedical dataset to predict human diseases

### Objective: To predict whether the patient has a particular disease or not based on the features extracted from the patient's eye image

### Dataset Description: 
1. The dataset contains 19 features which are extracted from an image set to predict whether that image contains the signs of a disease or not
2. Each row corresponds to a patient's eye image
3. Each column corresponds to a feature (Total 19 columns for 19 features)

### Feature Description (19 features)

| Attribute |                  Description                  |
|:---------:|:---------------------------------------------:|
|     0     |             The quality assessment            |
|     1     |          The result of pre-screening.         |
|   2 - 7   |        The results of Macula detection.       |
|   8 - 15  | The results of Macula detection for exudates. |
|     16    |            The Euclidean distance.            |
|     17    |        The diameter of the optic disc.        |
|     18    |         The AM/FM-based classification        |

### Number of training and testing samples
1. 920 training samples
2. 231 testing samples 

### Label description 
1. 1 corresponds to having a disease
2. 0 corresponds to not having a disease

## Results: 

| Classification Algorithm | Accuracy  |
|:------------------------:|:---------:|
|    k-nearest neighbors   |   67.82%  |
|  Support Vector Machine  |   69.56%  |
|        Naive Bayes       |   56.04%  |
|       Decision Tree      |   63.47%  |
|       Random Forest      |   72.17%  |
|    Logistic Regression   |   75.21%  |

Logistic regression turns out to provide the highest accuracy to predict whether the patient has the disease or not i. e. 75.21%
