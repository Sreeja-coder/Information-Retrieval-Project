 FAQ Maker for Products 


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

:blue_medium_small_square: Pre-processing:<br/>
▪ Pre-processing means to bring the text into a form that is analyzable for our task<br/>
▪ Pre-processing also helps removes noise from the data.<br/>
▪ The steps in Pre-processing are:<br/>
▪ Tokenization: Split a text into individual tokens<br/>
▪ Stemming: Reducing inflected word to their base or root form.<br/>
▪ Stop-words: Removing frequent unusual words, called stopwords.<br/>
▪ Special characters and URL removal: Using Regex<br/>
▪ POS tagging<br/>
