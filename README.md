# Recipe Recommender System
Inspired by my daughter's love for [cooking and baking](https://paintpencilpastries.com/), I decided to build a recipe recommender system to fulfill my graduation requirement from General Assembly.


**Machine Learning Problems**:
1. Given certain ingredients, such as things I have in the fridge, could I find some recipes or some suggestions about what to cook?

2. Given a person’s preferences of one recipe, could I recommend other recipes they might enjoy?

3. Can I categorize the recipes? Given a certain recipe, can I find other recipes that fall in same categories?

The motivation behind this recommendation system is to help users discover personalized and new recipes, and prepare for grocery runs.


# Data

This dataset consists of 230K+ recipes and 1M+ recipe reviews covering 18 years of user interactions and uploads on Food.com (formerly GeniusKitchen). The is collected by Shuyang Li and stored at [Kaggle](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv).



**Content Data**

- `RAW_recipes.csv`

- 231,637 Recipes

- Data Columns
|Feature|Type|Description|
|---|---|-----|
|name|*object*|Recipe name|
|id|*int*|Recipe id|
|minutes|*int*|Minutes to prepare recipe|
|contributor_id|*int*|User ID who submitted this recipe|
|submitted|*object*|Date recipe was submitted|
|tags|*object*|Food.com tags for recipe|
|nutrition|*object*|Nutrition information (calories (#), total fat (PDV), sugar (PDV) , sodium (PDV) , protein (PDV) , saturated fat|
|n_steps|*int*|Number of steps in recipe|
|steps|*object*|Text for recipe steps, in order|
|description|*object*|User-provided description|


**Content Data**

- `RAW_interactions.csv`
- 1,132,367 users reviews and ratings

- Data Columns
|Feature|Type|Description|
|---|---|-----|
|user_id|*int*|User ID|
|recipe_id|*int*|Recipe id|
|date|*object*|Date of review/rating|
|rating|*int*|Rating given, range 0 to 5|
|review|*object*|Review text|





# EDA
Notebook `02_Exploratory_Data_Analysis.ipynb` <br>

**Top 20 words in ingredients**
![](img/top_20_ing.png)
<br><p>

**Top 20 words in recipe names**
![](img/top_20_name.png)


| Recipe ingredient top words                                       | Recipe name top words Stopwords                               |
| ----------------------------------------------------- | ----------------------------------------------- |
| ![](img/rec_word.png) | ![](img/ing_word.png) |


# Models


1. Classifications - Use Naive Bayes and Gradient Boost Models to predict ratings from review text--- `03_Ratings_Classifier.ipynb`

> If I found one user wrote in the review  "So simple, so delicious! Great",  the model can predict which rating the user would give.

2. Matching - Use Numpy and Pandas to create search functions which would find recipes with the best ingredient matches. --- `04_Ingredient_match.ipynb`

> If I have winter squash, Mexican seasoning, mixed spice and honey in the fridge, the model can give some recipes on what to cook with these ingredients

3. Collaborative Filtering - Suggest recipes that other users similar to you also liked (Cosine Similarity) --- `05_User_Collaborative.ipynb`

> If I liked *Oven fried chicken*, and another user similar to me liked *The Texas bbq rub* and I haven't tried it, the model would recommend that recipe.

4. Content Based Filtering - Suggest recipes that are similar to recipes that you like (LDA model similarities) --- `06_LDA_Content Based.ipynb`

> If I liked *baked winter squash*, the model would recommend *outback croutons*, because the model found some categories that both recipes share.



# References

Special thanks to
