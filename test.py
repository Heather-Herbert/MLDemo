import sentiment_mod as s
import keywords_mod as k

phrase = "Northgate is necessary to our line of business. Heather solved the problem quickly and effectively, she was a pleasure to work with"
print(phrase)
input("Press enter.")
print(s.sentiment(phrase)[0])
#print(k.keyWords(phrase))

phrase = "Heather didn't solve the problem, due to no knowlege of how the system worked."

print(phrase)
input("Press enter.")
print(s.sentiment(phrase)[0])
#print(k.keyWords(phrase))

phrase = "James needs to ensure the customer is happy, and not just himself."
print(phrase)
input("Press enter.")
print(s.sentiment(phrase)[0])
#print(k.keyWords(phrase))

input("We can also use language tricks to infer the subject of phrases")

phrase = "Northgate is necessary to our line of business. Heather solved the problem quickly and effectively, she was a pleasure to work with"
print(phrase)
print(k.keyWords(phrase))
phrase = "Heather didn't solve the problem, due to no knowlege of how the system worked."
print(phrase)
print(k.keyWords(phrase))
phrase = "James needs to ensure the customer is happy, and not just himself."
print(phrase)
print(k.keyWords(phrase))

input("Now lets try this with real user feedback")

phrase = "Problem with being unable to log on meant I could not get no for ICT and of course no access to phone  luckily have mobile."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "I can understand the need to log calls generally but when there are outside people in to give a talk and the room is full of pupils waiting because the sound on the laptop does not want to talk to the projector I feel we should be able to ask the IT for help without logging a call for a quick resolution to the matter. Surely the call could be made later."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "I always find our ICT Team helpful and to-day was no exception - very nice polite person XXXX XXXX that I managed to talk to, to-day as trouble with my VPN and now working."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "user profile reset. Speedily done, thanks."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "I had to call twice the operating centre and send in three different tickets for this issue. I also had to ask other people to intervene so that this gets fixed. It involved a serious network access issue that made it impossible for me to use you tube videos that I use for teaching. I had access to these videos and I was using them in my planning and then for two days I was completely locked out by firewalls. It ruined my lessons in two classes and I had to re-arrange my lessons and involved a significant increase in my workload. This issue should be fixed pro-actively by the technicians involved, without effect to our lessons and our planning."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "this query was solved by XXXXX very quickly.  These two documents were required for Committee reports and these were the only versions.  XXXXX has saved me a huge amount of work having to start again if these documents couldn't be retrieved.  I am very, very impressed with the excellent service I have received from her today."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "XXXXX had helped me out with this issue before and had kept full notes of the remedy she worked out on that occasion.  The spreadsheet affected is not kept elsewhere and 1 years worth of training data would have been lost had she not kept a record of how to retrieve it.  Excellent service."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "XXXXX did an excellent job of helping to sort out XXXXX with his new login - he was very concerned and had tried to resolve the matter himself a couple of times without success. But with XXXXX's assistance the issues were resolved with great skill and good humour throughout.    Great Job XXXXX!"
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "XXXXX XXXXXX helped me overcome a potential challenge with sending large files outside the organisation - I was very grateful for his help. "
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "I was given an updated surface pro, Files were transferred from my old computer, nothing else was done etc no bit locker password, no printer installed, Monitor resolution was not correct and my screen was flickering, I was told that the screen was too big to cope with this and I had to change my screen, I asked for another power pack, he said I would have to order one. I have since learnt that they come standard with 2 power packs anyway. I wasn't told how to switch on the machine."
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

phrase = "another issue with missing pc In Marr room, facilties had installed another one, but no instruction on password, spent 40 minutes on phone/im trying to resolve with ICT - was told to log in myself/get someone else to log in/ use the training password that the original pc in Marr room would have used - tried that didn't work, eventually had to source another laptop so course could take place, "
print(phrase)
print(s.sentiment(phrase)[0])
print(" ")
input(" ")

