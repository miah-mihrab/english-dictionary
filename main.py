import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

con = mysql.connector.connect(
    user=os.environ.get('USER'),
    password=os.environ.get('password'),
    host=os.environ.get('HOST'),
    database=os.environ.get('DATABASE')
)

myCursor = con.cursor()


def definition(word):
    word = word.lower()

    myCursor.execute(
        "Select * from Dictionary WHERE SOUNDEX(Expression) = SOUNDEX('%s')" % word)

    data = {}

    for i in myCursor:
        if i[0] in data:
            data[i[0]].append(i[1])
        else:
            data[i[0]] = [i[1]]

    keywords = data.keys()
    keywords = list(keywords)  # dict_keys to list

    if len(keywords) == 0:
        return "No similar word exist in our system."

    if word in data:
        return data[word]
    else:
        confirmation = input(
            f"Did you mean {keywords[0]} instead of {word}. If yes write 'y' else 'n': ")
        if confirmation.lower() == 'y':
            return data[keywords[0]]
        else:
            return "No similar word exist in our system."


word = input('Enter word: ')

print("".join(definition(word)))
