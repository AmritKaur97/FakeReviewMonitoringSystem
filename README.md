# FakeReviewMonitoringSystem

Online markets and e-commerce platforms are becoming more prevalent and necessary.
Volume of product reviews is likewise detailed and available for users to review before purchasing. Which makes it very important for users and merchants.
The main aim of this project is to ensure that only genuine posts and reviews on products are provided for the user and for removing fake posts and reviews to ensure no one else would be cheated in the future.
This system will find out fake reviews made by posting fake comments about a product by identifying the IP address along with review posting patterns.


# Dataset

One of Amazon's most recognisable offerings is Amazon Customer Reviews, often known as Product Reviews. Since the first review appeared in 1995, nearly 20 years have passed, and over 100 million Amazon consumers have posted reviews to the website to share their thoughts and experiences with various products. As a result, academic scholars working in the fields of Natural Language Processing (NLP), Information Retrieval (IR), and Machine Learning (ML), among others, can find a wealth of information in Amazon Customer Reviews.

This dataset was created specifically to reflect a sample of customer evaluations and opinions, variations in how a product is perceived across different geographic areas, and bias or promotional intent in reviews. Researchers can access more than 130 million customer reviews as part of this release.

Each line in the data files corresponds to an individual review, with fields separated by tabs and no quote or escape characters. The dataset contains the following columns:

marketplace: The 2-letter country code of the marketplace where the review was written.
customer_id: A random identifier that can be used to aggregate reviews written by a single author.
review_id: The unique ID of the review.
product_id: The unique Product ID the review pertains to. In the multilingual dataset, reviews for the same product in different countries can be grouped by the same product_id.
product_parent: A random identifier that can be used to aggregate reviews for the same product.
product_title: The title of the product.
product_category: The broad product category that can be used to group reviews. It is also used to group the dataset into coherent parts.
star_rating: The 1-5 star rating of the review.
helpful_votes: The number of helpful votes received by the review.
total_votes: The total number of votes the review received.
vine: Indicates if the review was written as part of the Vine program.
verified_purchase: Indicates if the review is on a verified purchase.
review_headline: The title of the review.
review_body: The main text of the review.
review_date: The date the review was written.
timestamp: The time for each review posted.
IP Address: IP address of the users posted that review. 

The initial dataset has been aquired from : https://huggingface.co/datasets/amazon_us_reviews/viewer/Mobile_Electronics_v1_00/train

# Features Used

Sentiment analysis, the captivating field of interpreting emotions from text, unveils the rich tapestry of human expression. Through linguistic analysis, it reveals the underlying sentiments and intricacies that paint our words with meaning. By dissecting the nuances of joy, sorrow, love, and excitement, sentiment analysis provides valuable insights into the depth of human experiences. Like a bridge between language and emotion, it connects us, fostering empathy and understanding. With its power to decipher the sentiments that shape our stories, sentiment analysis unravels the vibrant spectrum of emotions, inviting us to appreciate the beauty and complexity of human sentiment within the confines of written and spoken words.

# Targeted Use Cases
1. Reviews which have dual view
2. Reviews in which same user promoting or demoting a particular brand
3. Reviews in which person from same IP Address promoting or demoting a particular brand
4. Reviews which are posted as flood by same user all the reviews are either positive or negative.
5. Reviews which are posted as flood by same person from same IP Address
6. Similar reviews posted in the same time interval
7. Reviews in which Reviewer using arming tone to by the product
8. Reviews in which reviewer is writing his own story
9. Meaningless Texts in reviews


