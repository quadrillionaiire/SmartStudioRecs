
# Phase-2-Project
# Analysis of Movie Data for Business Insights

## Overview
This report analyzes data from Box Office Mojo and IMDB to identify key factors that influence box office success. The primary goal is to help a new movie studio make data-driven decisions to optimize revenue by examining genre performance, the impact of director loyalty, and the power of franchises. The findings from this analysis will provide strategic insights for movie selection, talent retention, and franchise development to maximize box office gross.

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


## Analysis & Results
Top Performing Genres:

- Adventure and Action genres consistently generate the highest revenue, with Adventure pulling in nearly $70 billion and Action producing over $60 billion in 2018 alone.
Genres that combine Adventure and Action with Sci-Fi, Fantasy, or Animation also perform strongly, indicating that studios should focus on these combinations for box office success.
Factors Influencing Success:

Director-Genre Alignment: 
- Directors who specialize in certain genres tend to have consistent success. For example, Joe and Anthony Russo have proven to be top-performing directors in the Action-Adventure genre, contributing to huge successes like the Avengers franchise.
Studio Performance: Studios like BV, Fox, Universal, and Warner Bros consistently produce high-grossing films, particularly when they work with established directors and franchises.
Franchise Power:

Movies that are part of a franchise (e.g., Avengers, Deadpool, Jurassic Park) outperform non-franchise movies by a significant margin.
Franchise movies bring in higher revenue, likely due to brand loyalty and audience anticipation for sequels.
Director vs Studio Loyalty (T-Test):

A t-test was conducted to compare revenue between directors who consistently work with the same studio and those who do not. The results showed a statistically significant difference, with directors like the Russo Brothers bringing in higher revenue when working with loyal studios. The T-statistic of 2.63 and P-value of 0.0086 indicate that loyal director-studio partnerships significantly contribute to box office success.

## Conclusions
The findings highlight several key factors that can drive box office success for the new studio:

- Adventure and Action genres should be the studio’s primary focus, with particular attention to combining them with Sci-Fi and Fantasy.
- Franchise development is essential. Investing in long-term franchises will generate steady revenue over time.
- Director loyalty plays a critical role. Studios should aim to collaborate consistently with successful directors to maintain brand strength and ensure audience retention.

### **Additional Insights & Recommendations**
1. Franchise Development:
The studio should prioritize creating franchises. Building multi-movie series like Avengers or Jurassic Park provides long-term profitability and audience engagement.
2. Director and Talent Loyalty:
Maintaining long-term relationships with proven directors is key to consistent success. Directors with established track records in popular genres are critical assets.
3. Genre Strategy:
Focus on producing Adventure and Action films, particularly those with elements of Sci-Fi, Fantasy, or Animation. These genres have a wide audience base and consistently bring in high revenue.

 ### **Overall Strategic Enhancements**
- Develop a strong brand around franchises. Franchises bring predictable revenue and brand loyalty.

- Build lasting relationships with top directors. Proven directors like the Russo Brothers drive success, especially in Action and Adventure genres.

- Leverage genre performance data to invest in high-revenue genres like Adventure, Action, and Animation.
 

 ### Next Steps
- Franchise Feasibility Study: Conduct a deeper analysis into potential franchises that align with the studio’s brand and audience.
- Director Partnership Program: Build long-term contracts with proven directors who specialize in high-grossing genres.
- Genre-Specific Marketing: Develop targeted marketing strategies for Adventure and Action films, emphasizing Sci-Fi and Fantasy crossovers.
 ## For More Information

 ## Repository Structure 

```
├── data
├── images
├── notebooks
├── presentations
├── src
├── .gitignore
```
