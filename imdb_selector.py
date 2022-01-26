"""
# My first app
DESC: app for IMDB movie recommendation
user inputs: min_year, max_year, genre
output: top ten IMDB_score movie (with title/year/genre/score)
"""
import streamlit as st
import pandas as pd


NA_FILL_VALUE = -1

@st.cache
def get_df():
    df = pd.read_csv('movie_metadata.csv')
    df= df.dropna(subset=['title_year'])
    df['title_year'] = df.title_year.astype(int)
    return df


def get_unique_genres(df):
    all_unique_genres = df.genres.unique()
    unique_genres = set()
    for multi_genres in all_unique_genres:
        unique_genres.update(multi_genres.split('|'))
    return sorted(unique_genres)

st.title('IMDB old movie selector')

#use cache dataframe
movie_table = get_df()
#get min and max year from table 
table_min_year = int(movie_table.title_year.min())
table_max_year = int(movie_table.title_year.max())

#get data from streamlit
user_max_year = st.slider('year of movie not more than ...', min_value=table_min_year, max_value=table_max_year, value=2000)
user_min_year = st.slider('year movie not less than ...', min_value=table_min_year, max_value=table_max_year, value=1990)

# switch two boundary if user misunderstanding
if user_max_year < user_min_year:
   user_max_year, user_min_year = user_min_year, user_max_year

# get unique genres form table
unique_genres = get_unique_genres(movie_table)

# let user select genre
selected_genres = st.selectbox('select the genre you like', unique_genres)

# print out current result
st.write(f'your selection: max year: {user_max_year}, min year: {user_min_year}, selected genres: {selected_genres}')


# set two masks for filter out data user want
year_lower_mask = movie_table.title_year >= user_min_year
year_upper_mask = movie_table.title_year < user_max_year

# select data stand within the period user interested
year_constrain = movie_table[year_lower_mask & year_upper_mask].copy()

# make sure movie contain genre user selected
year_constrain['genres_sellected'] = year_constrain.genres.str.contains(selected_genres)
year_constrain_genre_selected = year_constrain[year_constrain.genres_sellected]

# sorted the result by its imdb score
scored_result = year_constrain_genre_selected.sort_values(by=['imdb_score'], ascending=False)

# print only top ten result by using head(10)
st.write(scored_result[['movie_title', 'imdb_score', 'genres', 'title_year']].head(10).reset_index(drop=True))


st.write("check out how did this app make [link](https://www.notion.so/evenpan/streamlit-8bbc98a6b55546b9b976ac0e01238bb4)")