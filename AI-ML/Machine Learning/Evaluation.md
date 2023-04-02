
# Evaluation
## Machine Learning Model Evaluation
**Classification Model Evaluation Metrics/Techniques**

**Accuracy** - The accuracy of the model in decimal form. Perfect accuracy is equal to 1.0.

[Precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score) 
Indicates the proportion of positive identifications (model predicted class 1) which were actually correct. A model which produces no false positives has a precision of 1.0.

[Recall](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score) 
Indicates the proportion of actual positives which were correctly classified. A model which produces no false negatives has a recall of 1.0.

[F1 score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score) 
A combination of precision and recall. A perfect model achieves an F1 score of 1.0.

[Confusion matrix](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) 
Compares the predicted values with the true values in a tabular way, if 100% correct, all values in the matrix will be top left to bottom right (diagonal line).

[Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) 
Splits your dataset into multiple parts and train and tests your model on each part then evaluates performance as an average.

[Classification report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html) 
Sklearn has a built-in function called ``classification_report()`` which returns some of the main classification metrics such as precision, recall and f1-score.

[ROC Curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_score.html)
Also known as [receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
is a plot of true positive rate versus false-positive rate.

[Area Under Curve (AUC) Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)
The area underneath the ROC curve. A perfect model achieves an AUC score of 1.0.

### Regression Model Evaluation Metrics/Techniques
[R^2 (pronounced r-squared) or the coefficient of determination](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)
Compares your model's predictions to the mean of the targets. Values can range from negative infinity (a very poor model) to 1. For example, if all your model does is predict the mean of the targets, its R^2 value would be 0. And if your model perfectly predicts a range of numbers it's R^2 value would be 1.

[Mean absolute error (MAE)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)
The average of the absolute differences between predictions and actual values. It gives you an idea of how wrong your predictions were.

[Mean squared error (MSE)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)
The average squared differences between predictions and actual values. Squaring the errors removes negative errors. It also amplifies outliers (samples which have larger errors).

**For more resources on evaluating a machine learning model, be sure to check out the following resources:**
[Scikit-Learn documentation for metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)
Quantifying the quality of predictions

[Beyond Accuracy: Precision and Recall](https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c) 
by Will Koehrsen

[Describing MSE (mean squared error) and RSME (root mean squared error)](https://stackoverflow.com/a/37861832)
Stack Overflow answer

