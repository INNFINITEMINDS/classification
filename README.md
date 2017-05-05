# Classification of a biomedical dataset to predict human diseases

### Dataset Description: 
1. The dataset contains 19 features which are extracted from an image set to predict whether that image contains the signs of a disease or not
2. Each row corresponds to a patient's eye image
3. Each column corresponds to a feature (Total 19 columns for 19 features)

### Number of training and testing samples
1. 920 training samples
2. 231 testing samples 

### Label description 
1. +1 corresponds to having a disease
2. -1 corresponds to not having a disease

## Results: 

| Classification Algorithm | Accuracy  |
|:------------------------:|:---------:|
|    k-nearest neighbors   |   67.82%  |
|  Support Vector Machine  |   69.56%  |
|        Naive Bayes       |   56.04%  |
|       Decision Tree      |   63.47%  |
|       Random Forest      |   72.17%  |
|    Logistic Regression   |   75.21%  |

Logistic regression turns out to provide the highest accuracy for this dataset i. e. 75.21%
