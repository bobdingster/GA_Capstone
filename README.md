# Recipe Recommender System
Inspired by my daughter's love for [cooking and baking](https://paintpencilpastries.com/), I decided to build a recipe recommender system to fulfill my graduation requirement from General Assembly.


**Machine Learning Problems**:
1. Given certain ingredients, can I find the recipes with the best matches and some suggestions about what to cook?


2. Given a person’s preferences in the name of one recipe, could I predict other recipes they might enjoy?

3. Given a certain recipe, can I find other recipes in the same categories?

The motivation behind this recommendation system is to help users discover personalized and new recipes, and prepare for grocery runs.


# Data

This dataset consists of 230K+ recipes and 1M+ recipe reviews covering 18 years of user interactions and uploads on Food.com (formerly GeniusKitchen). 



Content Data

- ```all_recipes.csv```

- 1100+ Recipes from

- 460+ Cuisines & Categories



Content Data

- ```all_users.csv```
- 55K Users
- 73K Ratings



# Tech Stack

1. **Data Wrangling**: pandas, numpy



2. **Web Scraping**: beautifulsoup, requests, regex

- Please refer to ```web_scraper.py``` for more details



2. **Model:** scikit-learn, scipy

- See ```requirements.txt``` for more



3. **Web Framework**: flask

- Run ```app.py``` on [localhost:5000](localhost:5000/) ```



4. **Front End**: html & css



# Models

Please refer to ```model.py```

1. Collaborative Filtering - Suggest recipes that other users similar to you also liked (Cosine Similarity)

> If I liked *Spaghetti Al Tonno*, and another user similar to me liked *Perfect Prime Rib* and I haven't tried it, the model would recommend that recipe.



2. Content Based Filtering - Suggest recipes that are similar to recipes that you like (Cosine Similiarity)

> If I liked Spaghetti Al Tonno, the model would recommend *Italian Meatballs*, because Italian Meatballs are similar to Spaghetti, in terms of the categories both recipes share (Italian, World Cuisine).



3. Matrix Factorization - Suggest recipes that you like, uncover latent factors, in a lower dimensional space (Singular Value Decomposition)

> If I liked *Turkey*, and I liked *Cranberry Sauce*, the model would recommend *Pumpkin Pie* because it picked up a latent factor that you liked Thanksgiving dishes, where the other models would not be able to.



<img src="static/images/hybrid.png">

# Model Evaluation

<img src="static/images/evaluation.png">

My final model was a hybrid recommender that tackled the cold-start problem with a content recommender, augmented with user preferences, and factorization to rank recipes based on a voting classifier rule.



# Screenshots

#### Onboarding

<img src="static/images/onboard_1.png">

<img src="static/images/onboard_2.png">

#### Results (Hybrid, Collaborative Filtering & Content Filtering)

<img src="static/images/results_1.png">

<img src="static/images/results_2.png">

<img src="static/images/results_3.png">



# References

Special thanks to Kim Falk's book and also Maciej's GitHub for reference during this journey.

1. https://www.manning.com/books/practical-recommender-systems

2. https://github.com/lyst/lightfm

3. https://github.com/maciejkula/spotlight
