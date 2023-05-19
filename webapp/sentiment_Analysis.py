
def analyze_feedback(feedback):
    # Import necessary libraries
    import pandas as pd

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    # Load data
    data = pd.read_csv('webapp/reviews.csv')

    # Preprocess data
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    def preprocess_text(text):
        # Tokenize text
        tokens = word_tokenize(text.lower())
        # Remove stopwords and punctuation
        tokens = [t for t in tokens if t not in stop_words and t.isalnum()]
        # Lemmatize words
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        # Join tokens back into a string
        return ' '.join(tokens)

    data['reviews'] = data['reviews'].apply(preprocess_text)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['reviews'], data['labels'], test_size=0.2, random_state=42)

    # Vectorize text
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train classifier
    clf = LogisticRegression()
    clf.fit(X_train_vec, y_train)

    # Test classifier
    y_pred = clf.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)

    # Predict sentiment of new reviews
    new_review = feedback
    new_review_vec = vectorizer.transform([preprocess_text(new_review)])
    new_sentiment = clf.predict(new_review_vec)[0]
    return new_sentiment

# print(analyze_feedback("very good doctor"))
