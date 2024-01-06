# book-rs
a book recommendation system with Streamlit

An application of ML Recommender Systems algorithms, implementing Collaborative and Content-Based Filtering methods separately. I created a neat web-app page 
using Streamlit for the presentation.

The two datasets I've merged have columns containing information of some books with user Ids as well as their ratings and have image URLs of most of them.
And the program offers the user five books in three categories from this database for the book selected from the list. The categories are about; the closest 
through the author and publisher, closest according to similar user ratings and furthest according to similar user ratings. The first one is an example of 
Content-Based Filtering Method, a comparison is made by establishing similarity on the words that make up the selected columns. Second and third ones are the 
same algorithm and are Collaborative Filtering Method application. Unlike the first one, the series of algorithms I've chosen here provides the output based
on the proximity of other users' behavior. I calculated the measure of similarity in both cases with the cosine-similarity function from Sklearn.


In the preparation of the study, I was inspired and benefited a lot from the notebook 'https://github.com/Zekeriyabesiroglu/DSMay22/blob/main/project04/tavsiye-sistemleri/Tavsiye_Sistemleri.ipynb' along with lots of web research.



https://github.com/tinabl/book-rs/assets/93467399/ad4a44ce-9216-41ab-afbf-357f610f9504

