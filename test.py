import sentiment_mod as s
import keywords_mod as k

phrase = "Northgate is necessary to our line of business. Heather solved the problem quickly and effectively, she was a pleasure to work with"
print(phrase)
print(s.sentiment(phrase))
print(k.keyWords(phrase))

phrase = "Heather didn't solve the problem, due to no knowlege of how the system worked."

print(phrase)
print(s.sentiment(phrase))
print(k.keyWords(phrase))

phrase = "James needs to ensure the customer is happy, and not just himself."
print(phrase)
print(s.sentiment(phrase))
print(k.keyWords(phrase))
