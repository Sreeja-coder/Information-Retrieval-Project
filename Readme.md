 FAQ Maker for Products 


:small_blue_diamond: Project Scope:

▪ Help create a question bank for a particular product description using the amazon Q/A and description dataset.

Motivation:

▪ Understand the perspective of the Manufacturers/Sellers
▪ Manufactures need to have insight to the user’s perception of the product and other similar products in market.
▪ Reduce redundancy when there are many similar questions from users.
▪ Generate a set of questions so that users can find relevant information.

DataSet:

Amazon Product Dataset[2] – It consists of product meta-data.
Amazon Review/Rating Dataset[2] – It consists of product ratings, review and q/a for each product.
We used the following features from the Datasets:
▪ ASIN (Product id)
▪ Question
▪ Description
▪ Category
▪ Title
▪ Brand
We used Electronics dataset to build our model.

Methodolgy:
The developed IR model includes the following components:
▪ Data Fetch and Pre-processing
▪ Descriptions (Description, category, title, brand)
▪ Question
▪ Query
▪ TF – IDF
▪ Cosine Similarity and Ranking
▪ BM25
▪ Evaluation of this IR model will be discussed in the later sections.

