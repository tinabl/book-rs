# importing libraries

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# data & some arragements

##  had 819623 row values of data after merging

books= pd.read_csv('C:/Users/tina/Desktop/data/books.csv', on_bad_lines='skip')
ratings= pd.read_csv('C:/Users/tina/Desktop/data/Ratings.csv')
books.rename(columns = {'Image-URL-L;;;;;;':'Image-URL-L'}, inplace = True)
books_ratings = pd.merge(books, ratings, on='ISBN')


##  decreased top 250 rated books in order that algorithms & web-app work efficiently

n = 250
top_n = books_ratings["Book-Title"].value_counts().index[:n]
books_ratings_= books_ratings[books_ratings['Book-Title'].isin(top_n)]




# streamlit screen

st.title('What to Read Next?')

book= st.sidebar.selectbox('Choose the book you are currently reading', ('1984', '1st to Die: A Novel', '2nd Chance', 'A Bend in the Road',
       'A Case of Need', 'A Heartbreaking Work of Staggering Genius',
       'A Is for Alibi (Kinsey Millhone Mysteries (Paperback))',
       'A Map of the World', 'A Painted House', 'A Prayer for Owen Meany',
       "A Thousand Acres (Ballantine Reader's Circle)", 'A Time to Kill',
       'A Walk to Remember', 'A Widow for One Year', "ANGELA'S ASHES",
       'About a Boy', 'Airframe', 'All I Really Need to Know',
       'Along Came a Spider (Alex Cross Novels)', 'American Gods',
       "Angela's Ashes (MMP) : A Memoir", "Angela's Ashes: A Memoir",
       'Angels &amp; Demons', 'Animal Farm', 'Ashes to Ashes',
       'At Home in Mitford (The Mitford Years)',
       'B Is for Burglar (Kinsey Millhone Mysteries (Paperback))',
       'Back Roads', 'Balzac and the Little Chinese Seamstress : A Novel',
       'Beach Music', 'Bel Canto: A Novel', 'Big Trouble', 'Black Notice',
       'Black and Blue', 'Brave New World', 'Breathing Lessons',
       "Bridget Jones's Diary", 'Bridget Jones: The Edge of Reason',
       'Carolina Moon', 'Cause of Death',
       'Chicken Soup for the Soul (Chicken Soup for the Soul)',
       'Chocolat', 'Circle of Friends', 'Cold Mountain : A Novel',
       'Confessions of a Shopaholic (Summer Display Opportunity)',
       'Confessions of an Ugly Stepsister : A Novel', 'Congo',
       'Cradle and All', "Daddy's Little Girl",
       'Dance upon the Air (Three Sisters Island Trilogy)',
       'Deception Point', 'Digital Fortress : A Thriller', 'Disclosure',
       'Divine Secrets of the Ya-Ya Sisterhood: A Novel',
       'Dolores Claiborne',
       "Don't Sweat the Small Stuff and It's All Small Stuff : Simple Ways to Keep the Little Things from Taking Over Your Life (Don't Sweat the Small Stuff Series)",
       'Dreamcatcher', 'Empire Falls',
       "Ender's Game (Ender Wiggins Saga (Paperback))",
       "Everything's Eventual : 14 Dark Tales",
       'Face the Fire (Three Sisters Island Trilogy)', 'Fahrenheit 451',
       'Fall On Your Knees (Oprah #45)', 'False Memory',
       'Fast Food Nation: The Dark Side of the All-American Meal',
       'Five Quarters of the Orange', 'Flesh and Blood',
       'Four To Score (A Stephanie Plum Novel)',
       'Fried Green Tomatoes at the Whistle Stop Cafe',
       "From Potter's Field", 'From the Corner of His Eye',
       "Full House (Janet Evanovich's Full Series)",
       'Girl in Hyacinth Blue', 'Girl with a Pearl Earring',
       'Good in Bed', 'Hannibal',
       'Hard Eight : A Stephanie Plum Novel (A Stephanie Plum Novel)',
       'Harry Potter and the Chamber of Secrets (Book 2)',
       'Harry Potter and the Goblet of Fire (Book 4)',
       'Harry Potter and the Order of the Phoenix (Book 5)',
       'Harry Potter and the Prisoner of Azkaban (Book 3)',
       "Harry Potter and the Sorcerer's Stone (Book 1)",
       "Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))",
       'Heaven and Earth (Three Sisters Island Trilogy)', 'Here on Earth',
       'High Fidelity', 'High Five (A Stephanie Plum Novel)',
       "Hornet's Nest", 'House of Sand and Fog',
       'How Stella Got Her Groove Back', 'How to Be Good',
       'I Know This Much Is True', 'Icy Sparks', 'Insomnia',
       'Interview with the Vampire',
       'Into Thin Air : A Personal Account of the Mt. Everest Disaster',
       'Into the Wild', 'Isle of Dogs', 'It', 'Jewel', 'Jurassic Park',
       'Kiss the Girls',
       "Left Behind: A Novel of the Earth's Last Days (Left Behind No. 1)",
       'Life of Pi', 'Lightning', 'Little Altars Everywhere: A Novel',
       'Lord of the Flies', 'Lucky : A Memoir', 'Me Talk Pretty One Day',
       'Message in a Bottle',
       'Midnight in the Garden of Good and Evil: A Savannah Story',
       'Midwives: A Novel', 'Misery', 'Mystic River', 'Neverwhere',
       'Nickel and Dimed: On (Not) Getting By in America',
       'One Door Away from Heaven', 'One True Thing',
       'One for the Money (Stephanie Plum Novels (Paperback))',
       'Outlander', 'P Is for Peril', 'Pet Sematary', 'Pigs in Heaven',
       'Point of Origin', 'Pop Goes the Weasel', 'Presumed Innocent',
       "Pretend You Don't See Her", 'Prodigal Summer: A Novel',
       'Q Is for Quarry', 'Red Dragon', 'Rising Sun',
       'Roses Are Red (Alex Cross Novels)', 'SHIPPING NEWS',
       'STONES FROM THE RIVER', 'Saving Faith', 'Scarlet Feather',
       'Seabiscuit: An American Legend',
       'Seven Up (A Stephanie Plum Novel)',
       "She's Come Undone (Oprah's Book Club (Paperback))",
       "She's Come Undone (Oprah's Book Club)",
       'Shopaholic Takes Manhattan (Summer Display Opportunity)',
       'Sick Puppy', 'Silence of the Lambs', 'Skipping Christmas',
       'Slow Waltz in Cedar Bend', 'Snow Falling on Cedars',
       "Songs in Ordinary Time (Oprah's Book Club (Paperback))",
       "Sophie's World: A Novel About the History of Philosophy",
       'Southern Cross', 'Sphere',
       'Stupid White Men ...and Other Sorry Excuses for the State of the Nation!',
       'Summer Sisters', "Suzanne's Diary for Nicholas", 'Tara Road',
       'Tell No One', 'The Alchemist: A Fable About Following Your Dream',
       'The Alienist', 'The Beach House', 'The Bean Trees',
       'The Blind Assassin', 'The Body Farm', "The Bonesetter's Daughter",
       "The Book of Ruth (Oprah's Book Club (Paperback))", 'The Brethren',
       'The Bridges of Madison County', 'The Chamber',
       'The Cider House Rules',
       "The Clan of the Cave Bear (Earth's Children (Paperback))",
       'The Client', 'The Color Purple',
       "The Color of Water: A Black Man's Tribute to His White Mother",
       'The Da Vinci Code', 'The Dark Half',
       'The Divine Secrets of the Ya-Ya Sisterhood: A Novel',
       'The Door to December', 'The English Patient', 'The Firm',
       'The Five People You Meet in Heaven', 'The Gift',
       "The Girls' Guide to Hunting and Fishing",
       'The God of Small Things', 'The Green Mile', "The Handmaid's Tale",
       "The Hitchhiker's Guide to the Galaxy",
       'The Hobbit : The Enchanting Prelude to The Lord of the Rings',
       'The Horse Whisperer', 'The Hot Zone', 'The Hours: A Novel',
       'The Hundred Secret Senses', 'The Hunt for Red October',
       'The Joy Luck Club', 'The King of Torts', "The Kitchen God's Wife",
       'The Last Precinct', 'The Lost World', 'The Murder Book',
       'The Nanny Diaries: A Novel',
       "The No. 1 Ladies' Detective Agency (Today Show Book Club #8)",
       'The Notebook', 'The Partner', 'The Pelican Brief',
       'The Perfect Storm : A True Story of Men Against the Sea',
       'The Pillars of the Earth', "The Pilot's Wife : A Novel",
       'The Poisonwood Bible', 'The Poisonwood Bible: A Novel',
       'The Prince of Tides',
       'The Queen of the Damned (Vampire Chronicles (Paperback))',
       'The Rainmaker', 'The Reader',
       'The Red Tent (Bestselling Backlist)', 'The Rescue',
       'The Runaway Jury', 'The Saving Graces: A Novel',
       'The Secret Life of Bees', 'The Shipping News : A Novel',
       'The Smoke Jumper', 'The Stone Diaries', 'The Street Lawyer',
       'The Summerhouse', 'The Summons',
       "The Sweet Potato Queens' Book of Love", 'The Talisman',
       'The Tao of Pooh', 'The Testament', 'The Thorn Birds',
       'The Tommyknockers', 'The Villa',
       'The Witching Hour (Lives of the Mayfair Witches)', 'Three Junes',
       'Three To Get Deadly : A Stephanie Plum Novel (A Stephanie Plum Novel)',
       'Timeline', 'To Kill a Mockingbird', 'Two for the Dough',
       'Unnatural Exposure',
       "Vinegar Hill (Oprah's Book Club (Paperback))", 'Violets Are Blue',
       'Watership Down', 'We Were the Mulvaneys', "We'll Meet Again",
       'What Looks Like Crazy On An Ordinary Day', 'When the Wind Blows',
       "Where the Heart Is (Oprah's Book Club (Paperback))",
       'While I Was Gone', 'Whispers',
       "White Oleander : A Novel (Oprah's Book Club)",
       'Wicked: The Life and Times of the Wicked Witch of the West',
       'Wild Animus', 'Wish You Well',
       'Zen and the Art of Motorcycle Maintenance: An Inquiry into Values')
        )

alg = st.sidebar.selectbox('Show results as',('Author & Publisher',
                        'Most similar according to voters',
                        'Least similar according to voters')
                         )




# some data edits and display for the first sidebar.selectbox to select the last read book

dff = books_ratings_[['Book-Title', 'Image-URL-M']]
df1 = dff.drop_duplicates()

df2= books_ratings_[['ISBN', 'Book-Title', 'Book-Author', 'Publisher', 'Year-Of-Publication']]
df3= df2.drop_duplicates()

dd1= df3[df3['Book-Title'] == book ]['Book-Author'].tolist()
dd2= df3[df3['Book-Title'] == book ]['Publisher'].tolist()
dd3= df3[df3['Book-Title'] == book ]['Year-Of-Publication'].tolist()
dd4= df3[df3['Book-Title'] == book ]['ISBN'].tolist()

y= dd1[0]
z= dd2[0]
t= dd3[0]
w= dd4[0]

S= df1[df1['Book-Title'] == book ]['Image-URL-M'].to_string(index=False).lstrip()

aut= books_ratings_[['Book-Title','Book-Author']]
auth = aut.drop_duplicates()
aut_= books_ratings_[['Book-Title','Book-Rating']]
auth_= books_ratings_.groupby(['Book-Title']).mean()
author = pd.merge(auth, auth_, on='Book-Title')
authors = author.drop_duplicates(subset='Book-Title', keep="first")


## round does not return significant figures always, so i defined 'truncate', it's better

def truncate(m, decimals=0):
        multiplier = 10 ** decimals
        return int(m * multiplier) / multiplier

rate= authors[authors['Book-Title'] == book]['Book-Rating'].to_string(index=False).lstrip()
rate= float(rate)
rate= truncate(rate, 2)


st.write(f'## {book}')
col1, mid, col2, mid, col3 = st.columns([10, 1, 10, 1, 10])
with col1:
        st.image(S, width=139)
with col2:
        st.write(y)
        st.write(z)
        st.text(t)
        st.text(w)
with col3:
        st.write('Rating:')
        st.success(rate)




# algorithms of collaborative recommender system

## used cosine similarity method reversely in the function 'find_nonsimilar_books' and
## presented a new option to the reader. i thought some readers may sometimes like to read irrelevant books

df_books_ = pd.pivot_table(books_ratings_, values=['Book-Rating'],
        index=['Book-Title', 'User-ID'],
        aggfunc=np.mean).unstack()
df_books_ = df_books_.fillna(0)

cosine_sim = cosine_similarity(df_books_)
cosine_sim_df = pd.DataFrame(cosine_sim, index=df_books_.index, columns=df_books_.index)


def find_similar_books(x):
        selected_book = [x]
        books_summed = np.sum(cosine_sim_df[selected_book], axis=1)
        books_summed = books_summed.sort_values(ascending=False)
        ranked_books = books_summed.index
        ranked_books = ranked_books.tolist()
        ranked_books_5 = [ranked_books[1], ranked_books[2], ranked_books[3], ranked_books[4], ranked_books[5]]

        return ranked_books_5

def find_nonsimilar_books(x):
        selected_book = [x]
        books_summed = np.sum(cosine_sim_df[selected_book], axis=1)
        books_summed = books_summed.sort_values(ascending=True)
        ranked_books = books_summed.index
        ranked_books = ranked_books.tolist()
        ranked_books_5 = [ranked_books[0], ranked_books[1], ranked_books[2], ranked_books[3], ranked_books[4]]
        return ranked_books_5




# algorithms of content-based recommender system

## had to edit almost whole data from scratch since some difficulties in data
## combined the columns 'Book-Author' and 'Publisher' to get language-based similarities with the column 'Book-Title'

books_ratings_new= books_ratings.copy()
books_ratings_new['Attributes'] = books_ratings_new['Book-Author'] + ' ' + books_ratings_new['Publisher']

books_ratings_new.dropna(subset='Book-Author', inplace=True)
books_ratings_new.dropna(subset='Publisher', inplace=True)
books_ratings_new.reset_index(drop=True, inplace=True)

n = 250
top_n = books_ratings_new["Book-Title"].value_counts().index[:n]
books_ratings_new_= books_ratings_new[books_ratings['Book-Title'].isin(top_n)]

_books_ratings_ = books_ratings_new_.drop_duplicates(subset='Book-Title', keep="first")

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(_books_ratings_['Attributes'])

from sklearn.metrics.pairwise import cosine_similarity
cosine_simm = cosine_similarity(tfidf_matrix)

_books_ratings_.reset_index(drop=True, inplace=True)
indices = pd.Series(_books_ratings_.index, index=_books_ratings_['Book-Title'])


def get_recommendations(_book, cosine_simm=cosine_simm):
        idx = indices[_book]
        sim_scores = list(enumerate(cosine_simm[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        book_indices = [i[0] for i in sim_scores]

        return (_books_ratings_['Book-Title'].iloc[book_indices]).tolist()





# functions to call alg (algorithm) parameter or options of second sidebar.selectbox item

## you can use st.success, st.info, st.warning & st.error functions for your texts with colorful ribbons (:

if alg == 'Author & Publisher':
        st.title('Take a Look:')
        list2 = find_similar_books(book)

        for b in list2:
                P = df1[df1['Book-Title'] == b]['Image-URL-M'].to_string(index=False).lstrip()
                rate = authors[authors['Book-Title'] == b]['Book-Rating'].to_string(index=False).lstrip()
                rate = float(rate)
                rate = truncate(rate, 2)

                dd1 = df3[df3['Book-Title'] == b]['Book-Author'].tolist()
                dd2 = df3[df3['Book-Title'] == b]['Publisher'].tolist()
                dd3 = df3[df3['Book-Title'] == b]['Year-Of-Publication'].tolist()
                dd4 = df3[df3['Book-Title'] == b]['ISBN'].tolist()

                y = dd1[0]
                z = dd2[0]
                t = dd3[0]
                w = dd4[0]

                st.write(f'## {b}')
                col1, mid, col2, mid, col3 = st.columns([10, 1, 10, 1, 10])
                with col1:
                        st.image(P)
                with col2:
                        st.write(y)
                        st.write(z)
                        st.text(t)
                        st.text(w)
                with col3:
                        st.write('Rating:')
                        st.error(rate)


elif alg == 'Most similar according to voters':
        st.title('Take a Look:')
        list2= find_similar_books(book)

        for b in list2:
                P = df1[df1['Book-Title'] == b]['Image-URL-M'].to_string(index=False).lstrip()
                rate = authors[authors['Book-Title'] == b]['Book-Rating'].to_string(index=False).lstrip()
                rate = float(rate)
                rate = truncate(rate, 2)

                dd1 = df3[df3['Book-Title'] == b]['Book-Author'].tolist()
                dd2 = df3[df3['Book-Title'] == b]['Publisher'].tolist()
                dd3 = df3[df3['Book-Title'] == b]['Year-Of-Publication'].tolist()
                dd4 = df3[df3['Book-Title'] == b]['ISBN'].tolist()

                y = dd1[0]
                z = dd2[0]
                t = dd3[0]
                w = dd4[0]

                st.write(f'## {b}')
                col1, mid, col2, mid, col3 = st.columns([10, 1, 10, 1, 10])
                with col1:
                        st.image(P)
                with col2:
                        st.write(y)
                        st.write(z)
                        st.text(t)
                        st.text(w)
                with col3:
                        st.write('Rating:')
                        st.warning(rate)


else:
        st.title('Take a Look:')
        list2 = find_nonsimilar_books(book)

        for b in list2:
                P = df1[df1['Book-Title'] == b]['Image-URL-M'].to_string(index=False).lstrip()
                rate = authors[authors['Book-Title'] == b]['Book-Rating'].to_string(index=False).lstrip()
                rate = float(rate)
                rate = truncate(rate, 2)

                dd1 = df3[df3['Book-Title'] == b]['Book-Author'].tolist()
                dd2 = df3[df3['Book-Title'] == b]['Publisher'].tolist()
                dd3 = df3[df3['Book-Title'] == b]['Year-Of-Publication'].tolist()
                dd4 = df3[df3['Book-Title'] == b]['ISBN'].tolist()

                y = dd1[0]
                z = dd2[0]
                t = dd3[0]
                w = dd4[0]

                st.write(f'## {b}')
                col1, mid, col2, mid, col3 = st.columns([10, 1, 10, 1, 10])
                with col1:
                        st.image(P)
                with col2:
                        st.write(y)
                        st.write(z)
                        st.text(t)
                        st.text(w)
                with col3:
                        st.write('Rating:')
                        st.info(rate)

