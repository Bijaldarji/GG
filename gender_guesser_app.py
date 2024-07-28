import streamlit as st
import re

# Load word lists
def load_word_lists():
    with open('gender_lists/male_words.txt') as f:
        male_words = set(f.read().splitlines())
    with open('gender_lists/female_words.txt') as f:
        female_words = set(f.read().splitlines())
    return male_words, female_words

def preprocess_text(text):
    # Normalize and preprocess text
    text = text.lower()  # Convert to lower case
    text = re.sub(r'\W+', ' ', text)  # Remove non-word characters
    return set(text.split())

def predict_gender(text):
    male_words, female_words = load_word_lists()
    text_words = preprocess_text(text)
    
    male_score = sum(1 for word in text_words if word in male_words)
    female_score = sum(1 for word in text_words if word in female_words)
    
    if male_score > female_score:
        return 'Male'
    elif female_score > male_score:
        return 'Female'
    else:
        return 'Undetermined'

# Streamlit app
def main():
    st.title('Gender Guesser')
    
    st.write("This app predicts the gender based on the text you input. Try to use descriptive text that might hint at gender-specific terms.")

    user_input = st.text_area('Enter text:', height=150)
    
    if st.button('Guess Gender'):
        if user_input:
            gender = predict_gender(user_input)
            st.write(f'**Predicted Gender:** {gender}')
        else:
            st.write('Please enter some text.')

if __name__ == '__main__':
    main()
