# Password-Strength-Detector

The project aimed at predicting the **strength of a password** using **NLP(TFIDF)** & **ML Algorithms**.

## Step followed in development of this project :-

- Downloaded a dataset of size 669639*2 .
- Performed data preprocessing & data cleaning on the dataset.
- Performed Feature Engineering on the dataset to obtain Independent and Dependent features
- Used data visualization to get insight on the processed data.
- Perform Text Preprocessing (Tokenization).
- Applied TF-IDF model for creating vectors.
- Trained Linear Regression Model with the dataset & achieved accuracy of 81.23%.
- Trained Xgboost Model with the dataset & achieved accuracy of **98.63%**.
- Trained MultinimialNB Model with the dataset & achieved accuracy of 74.38%.
- Xgboost model offers maximum accuracy, hence made a pickle file of xgboost model.
- Made a pickle file for vectorizing the input.
- Build front end graphical user interface for the web app.
- Build the web app using Flask web framework.
- Deploy the app on web using Heroku platform.

**Strength of password is classified in 3 categories as weak ,medium ,strong.**


