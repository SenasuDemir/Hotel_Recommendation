import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from ast import literal_eval
from nltk.stem import SnowballStemmer
import warnings
import streamlit as st

warnings.filterwarnings('ignore')

# Load your dataset
df = pd.read_csv('edited_hotel_list.csv')

# Function for hotel recommendation
def recommend_hotel(location, description):
    description = description.lower()
    location = location.lower()

    word_tokenize(description)
    stop_words = stopwords.words('english')
    lemma = WordNetLemmatizer()
    
    # Clean up description text
    filtered_description = {word for word in description.split() if word not in stop_words}
    filtered_description_set = {lemma.lemmatize(word) for word in filtered_description}

    # Filter the data by location
    country = df[df['country'] == location]
    country = country.set_index(np.arange(country.shape[0]))

    # Calculate similarity scores
    cos = []
    for i in range(country.shape[0]):
        temp_tokens = set(word_tokenize(country['Tags'][i]))
        vector = temp_tokens.intersection(filtered_description_set)
        cos.append(len(vector))
    
    country['similarity'] = cos
    country.sort_values(by=['similarity', 'Average_Score'], ascending=False, inplace=True)
    country.drop_duplicates(subset='Hotel_Name', keep='first', inplace=True)
    country.reset_index(inplace=True)
    
    return country[['Hotel_Name', 'Average_Score', 'Hotel_Address']].head(20)


# Streamlit UI: Make the interface fancier and more visually appealing
def main():
    # Title and description with icons
    st.title('Hotel Recommendation System 🏨✨')
    st.markdown("""
    <style>
        .title {
            font-size: 36px;
            color: #1E90FF;
            font-weight: bold;
        }
        .description {
            font-size: 18px;
            color: #333;
            margin-bottom: 30px;
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #aaa;
        }
        .recommend-button {
            background-color: #1E90FF;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="title">Find Your Perfect Hotel</p>', unsafe_allow_html=True)
    st.markdown('<p class="description">Enter your desired hotel qualifications, and let us recommend the best hotels for you!</p>', unsafe_allow_html=True)

    # Sidebar for selecting country and entering description
    st.sidebar.header('Your Preferences 🏡')
    location = st.sidebar.selectbox('Select Country 🌍', df['country'].unique())
    description = st.sidebar.text_input('Describe your desired hotel features 🏨')

    # Button to trigger recommendation
    if st.sidebar.button('Recommend Hotels 🔍', key="recommend_button"):
        if description:
            hotels = recommend_hotel(location, description)
            st.markdown(f"### Top 20 Recommended Hotels in {location.capitalize()} 🌟")
            
            # Fancy dataframe with color-coding and custom styling
            st.dataframe(
                hotels.style.applymap(lambda v: 'background-color: lightblue', subset=['Hotel_Name'])
                .set_properties(**{'text-align': 'center'})
                .set_table_styles([
                    {'selector': 'thead th', 'props': [('background-color', '#1E90FF'), ('color', 'white'), ('font-size', '14px')]},
                    {'selector': 'tbody td', 'props': [('font-size', '14px')]},
                ])
            )
            
        else:
            st.warning('Please enter a description of your desired hotel features!')

    # Footer section with custom styling
    st.markdown("""
    <div class="footer">
        Made with ❤️ by Senasu
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
