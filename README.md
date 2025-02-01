# Hotel Recommendation System 🏨✨

Welcome to the **Hotel Recommendation System** project! This repository contains a machine learning-based recommendation engine that suggests hotels based on user preferences derived from customer reviews, ratings, and tags.

---

## 🚀 Introduction

In today's fast-paced world, selecting the perfect hotel can be overwhelming with numerous options available online. This project simplifies the process by analyzing customer feedback—including textual reviews and ratings—to recommend hotels tailored to various travel needs such as business trips, honeymoons, and leisure stays. The system leverages machine learning techniques to rank hotels according to their relevance and quality.

---

## 🎯 Aim

The goal of this project is to develop a recommendation system that predicts which hotel a user is most likely to choose based on:
- **Location:** The country in which the hotel is located.
- **Description:** The user’s detailed preferences and requirements.

By analyzing hotel reviews and associated tags, the system provides recommendations that match the user's desired travel experience while considering the hotel's average rating and overall user feedback.

---

## 🗂️ Dataset Explanation

The dataset for this project includes a comprehensive set of hotel reviews with the following columns:

- **Hotel_Address:** The physical address of the hotel.
- **Additional_Number_of_Scoring:** An additional numerical score possibly linked to hotel features.
- **Review_Date:** The date when the review was posted.
- **Average_Score:** The overall average score assigned to the hotel.
- **Hotel_Name:** The name of the hotel.
- **Reviewer_Nationality:** The nationality of the reviewer.
- **Negative_Review:** A description of the negative aspects reported by the reviewer.
- **Review_Total_Negative_Word_Counts:** The count of words in the negative review.
- **Total_Number_of_Reviews:** The total reviews the hotel has received.
- **Positive_Review:** A description of the positive aspects reported by the reviewer.
- **Review_Total_Positive_Word_Counts:** The count of words in the positive review.
- **Total_Number_of_Reviews_Reviewer_Has_Given:** The total number of reviews given by the reviewer.
- **Reviewer_Score:** The score provided by the reviewer.
- **Tags:** A list of tags related to the review (e.g., type of trip or room preferences).
- **Days_Since_Review:** The number of days since the review was posted.
- **Lat:** The latitude of the hotel's location.
- **Lng:** The longitude of the hotel's location.

You can find the dataset [here](https://thecleverprogrammer.com/2021/02/13/hotel-recommendation-system-with-machine-learning/) 📊.

---

## ⚙️ How It Works

1. **Preprocessing:**  
   - Convert user description and hotel tags to lower case.
   - Remove stopwords and perform lemmatization.
   - Tokenize text using NLTK for analysis.

2. **Filtering:**  
   - Filter the dataset by the selected location.
   - Calculate similarity scores between the user’s description and hotel tags.

3. **Ranking:**  
   - Rank hotels based on similarity scores and average ratings.
   - Present the top recommendations to the user.

---

## 🌐 Live Demo

Try out the live demo of the Hotel Recommendation System on [Hugging Face Spaces](https://huggingface.co/spaces/Senasu/Hotel_Recommendation_System) 🚀.

---
