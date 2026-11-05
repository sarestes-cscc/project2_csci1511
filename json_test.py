import json
from mood import Mood
from needs import Needs

needs = Mood(Needs())

needs.json_dump({
            "Hunger Level": 50,
            "Happiness Level": 50,
            "Energy Level": 50
        })