# Social Sentiment Profiling on Public Health and Safety using AI/ML
Abstract – In today's rapidly growing landscape of social data, researchers and organizations are increasingly tapping into online conversations for valuable insights. This includes understanding sentiments around crucial topics like the global COVID-19 outbreak, crime, depression, and other societal issues. By analyzing data from platforms like Twitter, Reddit, and Facebook using Python and machine learning models, sentiment analysis helps classify user posts as positive, negative, or neutral. This approach aids organizations in making informed decisions without offending public sentiment. Leveraging Python's versatility, sentiment analysis is performed on Twitter data using libraries like Tweepy and TextBlob. Graphical representations provide insights into sentiment trends around hashtags such as COVID-19, crimes, depression, and others.

Key Words: Crime-related Keywords: Crime, Theft, Assault, Violence, Fraud
COVID-19-related Keywords: COVID-19, Lockdown, Pandemic

PROBLEM STATEMENT: The complexity of human language presents challenges in teaching machines to accurately analyze sentiments in textual data, including grammatical nuances, cultural variations, slang, and misspellings. Sentiment analysis, also known as opinion mining, is a crucial natural language processing technique used to interpret and classify emotions in subjective data, such as emails, survey responses, and social media posts. This process is especially useful in social media monitoring, offering organizations valuable insights into public opinion on various topics.

Steps Involved
1. Scraping Data from Social Platforms:
   - Data from social platforms, particularly Twitter, is scraped using the Scala library "Twitter4j" and the Twitter API. This involves registering a developer account with Twitter and providing necessary parameters such as API Key, Access token key, Consumer Secret key, and Access Secret Token Key.
   - Filters are applied to retrieve tweets related to specific keywords, enabling targeted data collection.

2. Cleaning of Scraped Data:
   - Data processing involves tokenization, where tweets are split into individual words or tokens, typically using whitespace or punctuation characters. This facilitates further analysis using techniques like the bag-of-words model.
   - Data filtering involves removing stop words, numbers, and punctuations, as well as stemming to reduce derived words to their roots. This enhances the quality of the dataset by eliminating irrelevant information.

3. Feature Extraction:
   - Feature extraction techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) are employed to assess the importance of terms in the corpus. This facilitates the identification of trending topics and the creation of word clouds, aiding in data visualization and analysis.

4. Sentiment Analysis:
   - Sentiment analysis is performed using a custom algorithm to determine the polarity of tweets.
   - Polarity is determined by counting positive and negative words in each tweet and comparing them against predefined lists. Positive sentiment leads to higher scores, while negative sentiment decreases scores.

Architecture Diagram: 
  
![sentiarchitecture](https://github.com/Tanishab17/Social-Sentiment-Profiling-on-Public-Health-and-Safety-using-AI-ML/assets/100562690/467bb3db-a29c-457d-ad54-854ffa22f6c8)

Result/Observation in detail is attached in the Report.
