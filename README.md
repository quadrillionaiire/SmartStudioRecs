
# Smart Studio Recommendations
![movie photo](<images/premium_photo-1661675440353-6a6019c95bc7.jpeg>)
# Analysis of Movie Data for Business Insights

## Overview
This report analyzes data from Box Office Mojo and IMDB to identify key factors that influence box office success. The primary goal is to help a new movie studio make data-driven decisions to optimize revenue by examining genre performance, the impact of director loyalty, and the power of franchises. In addition to this, this project analyzes movie data to predict user preferences and suggest movies based on similarities and historical viewing patterns. The goal is to provide actionable insights to movie studios that can help optimize movie selection strategies, improve marketing, and develop successful franchises.

## Business Problem 
A new movie studio is looking to produce films that will generate significant box office revenue. To guide their business decisions, the studio needs insights into how various factors like genre, director-studio loyalty, and franchise involvement affect total gross revenue. The analysis addresses three main questions:

  1. What genres perform best at the box office?
  2. How does director loyalty or studio collaboration affect box office success?
  3. What impact does franchise power have on revenue?

By answering these questions, the studio will have the tools to focus on the right types of films and build lasting director-studio relationships for successful franchises.

## Data Understanding 
The analysis combines data from two main sources:

- Box Office Mojo (BOM): This dataset contains information on 3,387 movies released between 2010 and 2018, including domestic and foreign box office gross.

- IMDB Database: This database includes detailed information on 146,144 movies, such as cast, crew, genres, and ratings. The key variables used in this analysis are domestic gross, foreign gross, studio, director, and whether the movie belongs to a franchise.

These datasets were merged and cleaned to create a comprehensive view of movie performance and underlying factors.

## Data Preparation
Data preparation involved several key steps:

Merging: We merged the BOM and IMDB datasets to ensure we had complete data on each movie’s financial performance, genre, and production team.

Handling Missing Data: In cases where foreign gross or domestic gross data was missing, we either dropped the data points or imputed zero where appropriate.

Creating New Features:

- A franchise column was created to identify franchise movies.
- A calculated column for total revenue was added by summing domestic and foreign gross.
- Director loyalty was assessed by counting the number of collaborations between a director and studio.

### Recommendation System

Our recommendation system uses a hybrid approach combining collaborative filtering and content-based filtering to provide personalized movie suggestions. We also predict whether a movie will be high-grossing based on its attributes.

Collaborative Filtering: This method identifies patterns in user behavior and recommends movies based on the preferences of similar users.
Content-Based Filtering: Recommends movies that are similar to those a user has previously watched, based on movie attributes such as genre and director.

Measure of Success

We aim to establish a measure of success that the new studio can strive to achieve, which will also help shape our recommendations. Since the studio's goal is to maximize revenue, we will define success as the annual gross revenue of the 5th highest-performing competitor studio.

 ![totalgrossperstudio](<images/total gross per studio.png>)   

## Analysis & Results
Top Performing Genres:

![top performing generes.png](<images/top performing generes.png>)

Using 2018 data, we performed an ANOVA test to determine whether there are significant differences in box office performance across genres. The results indicate that genres do not perform equally. The Null Hypothesis that all genres on average perform the same in the box office in 2018 was rejected (p-value < 0.05).

We used Tukey’s HSD Post-Hoc Test to identify specific genre pairs that have significantly different box office performance. The test shows that Adventure movies are the top performers, with an additional $44,750,000 in total gross revenue compared to the baseline genre. Action, Comedy, Sci-Fi, Drama, and Animation also perform well, surpassing the new studio’s target revenue of $2,128,500,000.
  
Factors Influencing Success:
- Director-Genre Alignment: 
   - Directors who specialize in certain genres tend to have consistent success.
   - For example, Joe and Anthony Russo have proven to be top-performing directors in the Action-Adventure genre, contributing to huge successes like the Avengers franchise.
  
- Studio Performance:
   - Studios like BV, Fox, Universal, and Warner Bros consistently produce high-grossing films, particularly when they work with established directors and franchises.

- Franchise Power:
   - Franchise movies were analyzed using a binary feature that identified whether a movie belonged to a franchise. The data showed that franchise films significantly outperformed non-franchise films in 2018. Major franchises like Avengers, Jurassic Park, and Deadpool generated higher revenues due to brand loyalty and anticipation for sequels.

   - Avengers: Infinity War, an action-adventure franchise movie, generated over $16 billion in 2018, far surpassing non-franchise films.
   - Ralph Breaks the Internet, another franchise film, brought in half the revenue of Avengers but still performed significantly better than non-franchise films in its genre.

  ![franchisepower.png](<images/franchisepower.png>)
   
Director vs Studio Loyalty (T-Test):

A t-test was conducted to compare the total revenue between directors who consistently work with the same studio and those who do not. The results were statistically significant (T-statistic: 2.63, P-value: 0.0086), indicating that directors with established studio partnerships tend to produce higher-grossing films. For instance, movies directed by the Russo Brothers consistently generate billions in revenue, particularly when working with studios like BV or Fox.

   - Top-grossing studios in 2018 included BV, Fox, Universal, and Warner Bros, with films like Avengers: Infinity War directed by the Russo Brothers pulling in over $45 billion.

  ![directorvsstudio.png](<images/directorvsstudio.png>)   
### How the Recommendation System Adds Value

The recommendation system helps movie studios in the following ways:

- Predicting High-Grossing Movies: By analyzing past performance, the system helps the studio identify potential box office hits.
- Personalized Recommendations: By analyzing user preferences and movie features, we provide tailored movie suggestions, which can guide marketing campaigns and streaming platform decisions.
- Data-Driven Decisions: The system allows studios to make more informed decisions about genre focus, director collaborations, and franchise development.

## Conclusions
The findings highlight several key factors that can drive box office success for the new studio:

- Adventure and Action genres should be the studio’s focus, as they consistently generate the highest box office revenue, exceeding the target annual revenue of $2,128,500,000.
- Franchise development is key to long-term financial success. Studios should prioritize creating or investing in franchises that attract loyal audiences and provide opportunities for sequels.
- Director-studio loyalty leads to better financial outcomes. New studios should focus on building strong, long-term relationships with successful directors who specialize in high-grossing genres and franchises.
- The movie recommendation system not only predicts high-grossing films but also personalizes recommendations for users, helping studios optimize their movie selection and marketing strategies based on consumer preferences and historical trends.


### **Additional Insights & Recommendations**
1. Invest in High-Revenue Genres: Genres like Adventure, Action, and Sci-Fi outperform others and should be the core focus for new releases.
2. Develop Franchise Films: Building a long-term franchise strategy will ensure consistent revenue, as franchise films outperform standalone movies.
3. Foster Talent Relationships: Collaborating with proven directors will not only improve movie performance but also contribute to the studio’s brand and audience retention.

 ### **Overall Strategic Enhancements**
- Develop a strong brand around franchises. Franchises bring predictable revenue and brand loyalty.

- Build lasting relationships with top directors. Proven directors like the Russo Brothers drive success, especially in Action and Adventure genres.

- Leverage genre performance data to invest in high-revenue genres like Adventure, Action, and Animation.
 
 ### Next Steps
- Franchise Feasibility Study: Conduct a deeper analysis into potential franchises that align with the studio’s brand and audience.
- Director Partnership Program: Build long-term contracts with proven directors who specialize in high-grossing genres.
- Genre-Specific Marketing: Develop targeted marketing strategies for Adventure and Action films, emphasizing Sci-Fi and Fantasy crossovers.
 ## For More Information
 
 See the full analysis in the [Jupyter Notebook](https://github.com/quadrillionaiire/Phase-2-Project/blob/main/notebooks/phase_2_project.ipynb) or review this [presentation](https://www.canva.com/design/DAGUdTq9QgM/nAR4IIAtVCl-3wPvQOg2Yw/view?utm_content=DAGUdTq9QgM&utm_campaign=designshare&utm_medium=link&utm_source=editor)

[Original data source from IMDb](https://www.imdb.com/)
[Original data source from Box Office Mojo]([https://www.imdb.com/](https://www.boxofficemojo.com/))

 ## Repository Structure 

```
├── data
├── images
├── notebooks
├── presentations
├── src
├── .gitignore
```
