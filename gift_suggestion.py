import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')  # WordNet for lemmatization

# Sample conversation
conversation = """
Hey, have you read the latest book by J.K. Rowling? I loved the book!
I like to read. I want to read all her books. I will read when I have time. You should also read them.
I have a cat. I like cats. I want another cat. Do you like to have a cat? I saw a cat.
I'm currently reading a science fiction novel too.
"""

# Gift ideas mapped to interests or keywords
gift_ideas = {
    'book': 'Latest bestselling book',
    'science fiction': 'A sci-fi novel or movie'
}

# Tokenize and clean the conversation
words = word_tokenize(conversation.lower())
filtered_words = [word for word in words if word.isalpha() and word not in stopwords.words('english')]

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize words
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Count word occurrences
word_counts = Counter(lemmatized_words)

# Identify interests based on word frequency
interests = [word for word, count in word_counts.items() if count >= 3]  # Words mentioned three or more times

# Gift suggestions based on keywords
gift_suggestions = []

# Check for interests without gift suggestions and prompt user to add them
for interest in interests:
    if interest not in gift_ideas:
        print(f"No gift ideas available for '{interest}'. Please enter a gift suggestion:")
        user_input = input()  # Get gift suggestion from user
        gift_ideas[interest] = user_input  # Add the new gift suggestion to the map

# Determine gifts based on interests
for interest in interests:
    if interest in gift_ideas and gift_ideas[interest] not in gift_suggestions:
        gift_suggestions.append(gift_ideas[interest])

# Display the gift suggestions
if gift_suggestions:
    print("Gift Suggestions based on interests:", gift_suggestions)
else:
    print("No gift suggestions available based on the conversation.")
