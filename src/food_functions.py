import pandas as pd
import numpy as np
import re
def matches_df(column, df, user_input):

    matches = []

    # split the entered keywords by comma
    keywords = re.split('; |, |,|\*|\n',user_input.lower())
#     keywords = user_input.lower().split(',')

    # create an empty list to store keywords
    keyword_list = []

    for i in range(len(keywords)):

        # remove white space
        keywords[i] = keywords[i].strip()
#         print(f'User Input: {keywords[i]}\n')
        # append it to keyword_list
        keyword_list.append(keywords[i])

    # separate each row
    for text in column:

        # initiate 0 as match
        match = 0

        # iterate through words in keyword_list
        for keyword in keyword_list:

            # if keyword found in text, assign 1 as match
            # stop comparing once assigned as 1, then append it to the list
            if keyword in text:
                match += 1
                #print(text)
#                 break
        matches.append(match)

    df['match'] = matches
    return  df.sort_values(by=['match'], ascending=False).head(3)

def ingredient_find(user_input):
    df = pd.read_csv('../data/organized_recipes.csv')
    df['ingredients'] = df['ingredients'].map(lambda s: s.strip('[').strip(']').replace("'", "").split(', '))
    ingredient_list=[]
    for row in df['ingredients']:
        ingredient_list.extend(row)
    chosen_recipe = matches_df(df['ingredients'], df, user_input)

    return chosen_recipe
