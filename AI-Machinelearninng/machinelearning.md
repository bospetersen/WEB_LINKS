[]() 
# Machine Learning

## Resources
* [tensorflow.org/resources](https://www.tensorflow.org/resources/learn-ml)
* [neuralnetworksanddeeplearning.com](http://neuralnetworksanddeeplearning.com/)
* [machinelearningmastery.com](https://machinelearningmastery.com/)

## Notes
* [chrisalbon.com/](https://chrisalbon.com/)
* [Understanding a Confusion Matrix and How to Plot It](https://www.turing.com/kb/how-to-plot-confusion-matrix)
* [Applied Machine Learning Process](https://machinelearningmastery.com/process-for-working-through-machine-learning-problems/)

# Evaluation
## Machine Learning Model Evaluation
**Classification Model Evaluation Metrics/Techniques**

**Accuracy** - The accuracy of the model in decimal form. Perfect accuracy is equal to 1.0.

[Precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score) - Indicates the proportion of positive identifications (model predicted class 1) which were actually correct. A model which produces no false positives has a precision of 1.0.

[Recall](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score) - Indicates the proportion of actual positives which were correctly classified. A model which produces no false negatives has a recall of 1.0.

[F1 score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score) - A combination of precision and recall. A perfect model achieves an F1 score of 1.0.

[Confusion matrix](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) - Compares the predicted values with the true values in a tabular way, if 100% correct, all values in the matrix will be top left to bottom right (diagonal line).

[Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) - Splits your dataset into multiple parts and train and tests your model on each part then evaluates performance as an average.

[Classification report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html) - Sklearn has a built-in function called ``classification_report()`` which returns some of the main classification metrics such as precision, recall and f1-score.

[ROC Curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_score.html) - Also known as [receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) is a plot of true positive rate versus false-positive rate.

[Area Under Curve (AUC) Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html) - The area underneath the ROC curve. A perfect model achieves an AUC score of 1.0.

## Regression Model Evaluation Metrics/Techniques
[R^2 (pronounced r-squared) or the coefficient of determination](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html) - Compares your model's predictions to the mean of the targets. Values can range from negative infinity (a very poor model) to 1. For example, if all your model does is predict the mean of the targets, its R^2 value would be 0. And if your model perfectly predicts a range of numbers it's R^2 value would be 1.

[Mean absolute error (MAE)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html) - The average of the absolute differences between predictions and actual values. It gives you an idea of how wrong your predictions were.

[Mean squared error (MSE)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html) - The average squared differences between predictions and actual values. Squaring the errors removes negative errors. It also amplifies outliers (samples which have larger errors).

**For more resources on evaluating a machine learning model, be sure to check out the following resources:**
[Scikit-Learn documentation for metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) - Quantifying the quality of predictions

[Beyond Accuracy: Precision and Recall](https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c) - by Will Koehrsen

[Describing MSE (mean squared error) and RSME (root mean squared error)](https://stackoverflow.com/a/37861832) - Stack Overflow answer


# Reading Extension: ROC Curve + AUC
**For more information on these metrics, bookmark the following resources and refer to them when you need:**

* [ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM) by StatQuest
* [ROC documentation in Scikit-Learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html) (contains code examples)
* [How the ROC curve and AUC are calculated](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) by Google's Machine Learning team

### CNN
* [Image Kernels](https://setosa.io/ev/image-kernels/)

### RNN
* [How to Use the TimeseriesGenerator for Time Series Forecasting in Keras](https://machinelearningmastery.com/how-to-use-the-timeseriesgenerator-for-time-series-forecasting-in-keras/)

# Mathematics for Machine Learning
Github: [Mathematics for Machine Learning](https://github.com/dair-ai/Mathematics-for-ML.git) - A collection of resources to learn and review mathematics for machine learning.

### 📖 Books
**Algebra, Topology, Differential Calculus, and Optimization Theory For Computer Science and Machine Learning**

* Book: [Applied Math and Machine Learning Basics](https://www.cis.upenn.edu/~jean/math-deep.pdf)
* Chapter: [Mathematics for Machine Learning](https://www.deeplearningbook.org/contents/part_basics.html)
* Book: [Probabilistic Machine Learning: An Introduction](https://mml-book.github.io)
* Book: [Mathematics for Deep Learning](https://probml.github.io/pml-book/book1.html)

* Book: [Bayes Rules!](https://www.bayesrulesbook.com/index.html)  
  * Chapter: [Bayes Rules! An Introduction to Applied Bayesian Modeling](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/index.html)

### 📄 Papers
**The Matrix Calculus You Need For Deep Learning**

* Paper: [The Mathematics of AI](https://arxiv.org/abs/1802.01528)
* Paper: [https://arxiv.org/pdf/2203.08890.pdf](https://arxiv.org/pdf/2203.08890.pdf)

### 🎥 Video Lectures
**Multivariate Calculus by Imperial College London**

* Video Playlist: [Mathematics for Machine Learning - Linear Algebra](https://www.youtube.com/playlist?list=PLiiljHvN6z193BBzS0Ln8NnqQmzimTW23)
* Video Playlist: [CS229: Machine Learning](https://www.youtube.com/playlist?list=PLiiljHvN6z1_o1ztXTKWPrShrMrBLo5P3)
* Course: [https://www.youtube.com/](https://www.youtube.com/playlist?list=PLoROMvodv4rNH7qL6-efu_q2_bPuy0adh)

### 🧮 Math Basics
**The Elements of Statistical Learning**

* Book: [https://hastie.su.domains/ElemStatLearn/](https://hastie.su.domains/ElemStatLearn/)
* Source: [Information Theory, Inference and Learning Algorithms](https://bayes.wustl.edu/etj/prob/book.pdf)
* Book: [Statistics and probability](https://www.inference.org.uk/itprnn/book.html)
* Course: [Linear Algebra Done Right](https://www.khanacademy.org/math/statistics-probability)
* Lecture and Slides: [Linear Algebra](https://linear.axler.net/LADRvideos.html)
* Course: [Calculus](https://www.khanacademy.org/math/linear-algebra)
* Course: [https://www.khanacademy.org/math/calculus-home](https://www.khanacademy.org/math/calculus-home)

# Feature Scaling
* [Feature Scaling](https://medium.com/@rahul77349/feature-scaling-why-it-is-required-8a93df1af310) - why is it required? by Rahul Saini
* [Feature Scaling with Scikit-Learn](https://benalexkeen.com/feature-scaling-with-scikit-learn/) by Ben Alex Keen
* [Feature Scaling for Machine Learning](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/) Understanding the Difference Between Normalization vs. Standardization by Aniruddha Bhandari 

## Youtube
* [(Non-technical) How Machines Learn by GCP Grey: ](https://www.youtube.com/watch?v=R9OHn5ZF4Uo)
* [(Technical) Deep Learning series by 3Blue1Brown: ](https://www.youtube.com/watch?v=aircAruvnKk)
* [PyTorch at Tesla - Andrej Karpathy, Tesla](https://www.youtube.com/watch?v=oBklltKXtDE&t=173s)


