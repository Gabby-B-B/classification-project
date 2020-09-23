<p><h1> Predicting Churn at Darden Telco </h1>
<h2>About the project</h2>
<h3>Goals </h3>
<p>My goal for this project is to create a model predicting churn using the data obtained from the Telco database. I would like to identify what conditions and attributes are the biggest drivers of churn. In this project I will deliver acquire.py, prepare.py, telco.csv and final_presentation.ipynb which will hold my report</p>
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

<li>Support: The number of occurrences of each class in where y is true.</li><br><br>
<h2>Hypothesis Testing </h2>
<ul>
<li>First Hypothesis
𝐻0 : Tenure has no effect on churn rate.<br>
𝐻𝑎 : Tenure effects the churn rate.<br>
alpha ( 𝛼 ): 1 - confidence level (95% confidence level ->  𝛼=.05 )<br></li>
<br><br>
 <li>Second Hypothesis<br>
𝐻0 : People who churn are paying more per month than those who arent. <br>
𝐻𝑎 : People who churn are paying the equal to or less than those who dont churn. </li> <br><br><br>


<h2> Data Science Pipeline Used </h2>
<p>
<h4>acquire.py</h4>
<ul>
<li>acquire data from csv gathered from sql.</li>

<h4>prepare.py</h4>
<ul>
<li>address missing data</li>
<li>address outliers</li>
<li>split into train, validate, test</li>
<br><br>

<li>explore</li>
<li>plot correlation matrix of all variables </li>
<li>test each hypothesis</li>


<h4>model</h4>

<li>try different algorithms: decision tree, logistic regression, random forest, knn </li>
<li><which features are most influential?</li>
<li>evaluate on train</li>
<li>select top 3 +/- models to evaluate on validate</li>
<li>select top model</li>
<li>run model on test to verify.</li>

<h4>conclusion</h4>

<li>summarize findings</li>
<li>make recommendations</li>
<li>next steps</li>
<li>how to run with new data.</li>

<h2>Conclusion </h2>

<p>Customers without dependents, on month to month contracts and who have additional features are more likely to churn. Through analyzing the data, we have found that the customers who churn are paying more. This can be explained by the additional features that many customers have. Next steps would be to find out which specific features cost the most and cause the highest churn. My recommendation to retain customers would be to investigate  offering bundle deals and having customers sign contracts to reduce the churn with the company. </p>
<h2> How to reproduce the results </h2>
<p>You may download acquire.py and prepare.py. You will need your own env.py file with your SQL credentials in order to access the SQL server.</p>