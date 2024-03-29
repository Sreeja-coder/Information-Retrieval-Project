 ### FAQ Maker for Products 

:small_blue_diamond: Introduction: <br/>
In the era of e-commerce , the manufactures needs to have insights into the user's perception of the product & other similar products in the market. <br>
This requires a resourceful product description and a Q & A. This can be done by collecting all the past historical information from Amazon's Q & A dataset for smilar products and retrieving frequently asked questions; thus covering ground while describing the sellers new product or encompassing most of the questions that users look for.

:small_blue_diamond: Project Scope: <br/>

▪ Help create a question bank for a particular product description using the amazon Q/A and description dataset.<br/>

:small_blue_diamond: Motivation:<br/>

▪ Understand the perspective of the Manufacturers/Sellers<br/>
▪ Manufactures need to have insight to the user’s perception of the product and other similar products in market.<br/>
▪ Reduce redundancy when there are many similar questions from users.<br/>
▪ Generate a set of questions so that users can find relevant information.<br/>

:small_blue_diamond: DataSet:<br/>

Amazon Product Dataset[2] – It consists of product meta-data. <br/>
Amazon Review/Rating Dataset[2] – It consists of product ratings, review and q/a for each product.<br/>
We used the following features from the Datasets:<br/>
▪ ASIN (Product id)<br/>
▪ Question<br/>
▪ Description<br/>
▪ Category<br/>
▪ Title<br/>
▪ Brand<br/>
We used Electronics dataset to build our model.<br/>

:small_blue_diamond: Methodolgy:<br/>
The developed IR model includes the following components:<br/>
▪ Data Fetch and Pre-processing<br/>
▪ Descriptions (Description, category, title, brand)<br/>
▪ Question<br/>
▪ Query<br/>
▪ TF – IDF<br/>
▪ Cosine Similarity and Ranking<br/>
▪ BM25<br/>
▪ Evaluation of this IR model will be discussed in the later sections.<br/>


![model](https://github.com/Sreeja-coder/Information-Retrieval-Project/blob/main/model.PNG)

:small_blue_diamond: Evaluation :<br/>
We trained the model with 28795 questions and 2610 unique descriptions. <br>
We tested the model for 20 unseen Queries from the dataset.  <br>
We ran evaualtion by calculating semantic scores. <br>
▪ We calculated semantic similarity between: <br>
▪ Query and Cosine Generated Questions <br>
▪ Query and BM25 Generated Questions <br>
▪ Query and Original Questions <br>

The Scores for these evaluations are as follows: <br>
▪ Query Cosine = 0.865760 <br>
▪ Query BM25 = 0.861166 <br>
▪ Query Original = 0.141647 <br>

Similarity score between Generated and Original Questions: <br>
▪ Cosine: 0.251 <br>
▪ BM25: 0.252 <br>



