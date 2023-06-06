#Optimistic Machine
print("Optimistic Machine")
print("We will give you a different phrase each day. You will see how it improves your mood!")
name = input("What's your name? ")
day = input("What day is it?")
color = input("What is your favorite color?")
sign = input("What is your horoscope sign?")
age = input("How old are you?")
age = int(age)
oldage = int(age) + 80

#Stage calc
if age < 15:
  print("Such a baby! Go with momma, she wants to change your diaper")
  stage = "minor"
elif age >= 15 < 25:
  print("You are in the dying flower of human life!")
  stage = "adolescent"
elif age >= 25 >= 50:
  print("Getting old, babe!")
  stage = "adult"
elif age >= 50:
  print("Half foot in the grave!")
  stage = "elderly"
print(stage)

#Phrase for each day
if day == "monday" or day == "Monday":
  print("""
  
  Hey""",stage,"""Here you have a happy phrase for your""",day,"""!:
  
  "In an indirect way, we would also have shown, more than enough, that life in the best State of our time lacks value. Life is, in truth, a "miserable desolate thing": it always was and will be miserable and desolate, and not to be is better than to be."
  Phillip Mäinlander.

  Perfect for a young""",age,"""!
  I hope that you enjoy the rest of your day!
  
  """)
elif day == "tuesday" or day == "Tuesday":
  print("""
  
  “A man is never happy, but spends his whole life in striving after something that he thinks will make him so; he seldom attains his goal, and when he does, it is only to be disappointed; he is mostly shipwrecked in the end, and comes into harbour with mast and rigging gone."
  Arthur Schopenhauer.
  
  Happy""",day,"""!!!
  
  """)
elif day == "wednesday" or day == "Wednesday":
  print("""
  
  Having a bad""",day,name,"""? Read this...
  
  “Being asked for what purpose he thought men were bom, he laughingly replied “ To realise how much better it were not to be born.”
  Giacomo Leopardi.
  
  Hope you feel better now!
  
  """)
elif day == "thursday" or day == "Thursday":
  print("""
  
  Having a bad""",day,"""? This suits perfectly for""",sign,"""people...
  
  “Being asked for what purpose he thought men were bom, he laughingly replied “ To realise how much better it were not to be born.”
  Giacomo Leopardi.
  
  You must feel renewed now!
  
  """)
elif day == "friday" or day == "Friday":
   print("""
  
  Beautiful phrase to enlighten""",sign,"""'s day!
  
  “Man starts over again every day, in spite of all he knows, against all he knows.”
  Emil Cioran.
  
  Keep the good work Sisyphus! Perhaps you will remember it when you have
  
  """)

elif day == "saturday" or day == "Saturday":
   print("""
  
  Happy future! Future is like the color""",color,"""
  
  "Future, n.That period of time in which our affairs prosper, our friends are true and our happiness is assured."
  Ambrose Bierce.
  
  Repeat this every day! Today I'm not happy, tomorrow I will.
  
  """)

elif day == "sunday" or day == "Sunday":
   print("""
  
  Sunday mood""",name,"""! This is a long one:
  
"Consider the capacity of the human body for pleasure. Sometimes, it is pleasant to eat, to drink, to see, to touch, to smell, to hear, to make love. The mouth. The eyes. The fingertips. The nose. The ears. The genitals. Our voluptific faculties (if you will forgive me the coinage) are not exclusively concentrated in these places, but it is undeniable that they are concentrated here. The whole body is susceptible to pleasure, but in places there are wells from which it may be drawn up in greater quantity. But not inexhaustibly. How long is it possible to know pleasure? Rich Romans ate to satiety, and then purged their overburdened bellies and ate again. But they could not eat for ever. A rose is sweet, but the nose becomes habituated to its scent. And what of the most intense pleasures, the personality-annihilating ecstasies of sex? ... Even if I were a woman, and could string orgasm on orgasm like beads upon a necklace, in time I should sicken of it. Yet consider. Consider pain. Give me a cubic centimetre of your flesh and I could give you pain that would swallow you as the ocean swallows a grain of salt. And you would always be ripe for it, from before the time of your birth to the moment of your death. We are always in season for the embrace of pain. To experience pain requires no intelligence, no maturity, no wisdom, no slow working of the hormones in the moist midnight of our innards. We are always ripe for it. All life is ripe for it. Always. ... Consider the ways in which we may gain pleasure. Consider. Consider the ways in which we may be given pain. The one is to the other as the moon is to the sun."

Jesús Ignacio Aldapuerta, The Eyes: Emetic Fables from the Andalusian de Sade, (1996), pp. 52–53
  
  Pain day""",sign,"""! Yey!
  
  """)
else:
  print("That's not a day in gregorian calendar, sorry, not enough time to include others")
  print("We really appreciate your comments. If you feel like you don't like our phrases, we welcome your contributions! Please send them trough your ass. It will arrive quickly. XOXO")