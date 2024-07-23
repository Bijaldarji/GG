import streamlit as st

# Load word lists
def load_word_lists():
    with open('gender_lists/male_words.txt') as f:
        male_words = set(f.read().splitlines())
    with open('gender_lists/female_words.txt') as f:
        female_words = set(f.read().splitlines())
    return male_words, female_words

def predict_gender(text):
    male_words, female_words = load_word_lists()
    text_words = set(text.lower().split())
    
    # Calculate scores for each gender
    male_score = len(text_words & male_words)
    female_score = len(text_words & female_words)
    
    # Determine gender based on scores
    return 'Male' if male_score > female_score else 'Female'

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
