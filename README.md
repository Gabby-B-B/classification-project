<h1> Predicting Churn at Darden Telco </h1>
<h2>About the project</h2>
<h3>Goals </h3>
<p>My goal for this project is to create a model predicting churn using the data obtained from the Telco database. I would like to identify what conditions and attributes are the biggest drivers of churn. In this project I will deliver acquire.py, prepare.py, telco.csv and model.ipynb which will hold my report</p>
<h2> Data Dictionary </h2>
<ul> 
<li> Churn: the measure of the numnber of individuals moving out of a collection group over a specific period. </li>
<li> Logistic Regression: A regression algorithm used to predict discrete outcomes.</li>
<li> Decision Tree: A sequence of rules that can be used to classify 2 or more classes using supervised machine learning processes.</li>
<li>Random Forest:  A learning method that constructs a multitude of decision trees at training time and outputting the classification.</li>
<li> K-Nearest Neighbor (KNN): A lazy algorithm in that it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the k nearest neighbours of each point. Makes predictions based on how close a new data point is to known data points.</li>
<li>Precision: the higher this number is, the more you were able to pinpoint all positives correctly. If this is a low score, you predicted a lot of positives where there were none. tp / (tp + fp)</li>

<li>Recall: If this score is high, you didn’t miss a lot of positives. But as it gets lower, you are not predicting the positives that are actually there. tp / (tp + fn) </li>

<li>f1-score: The balanced harmonic mean of Recall and Precision, giving both metrics equal weight. The higher the F-Measure is, the better.</li>

<li>Support: The number of occurrences of each class in where y is true.</li>