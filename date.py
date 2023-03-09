import datetime

# pour récupérer la date et l'heure actuelle détaillée
now = datetime.datetime.now()
print("Date et heure actuelles :", now)

# initialiser à une date exacte comme ma date de naissance
date = datetime.datetime(2023, 3, 4)
print("Ma date de naissance :", date)

# le jour de la semaine exacte
jour_semaine = date.strftime("%A")
print("Jour de la semaine :", jour_semaine)

# Ajouter 3 jours à une date
nouvelle_date = date + datetime.timedelta(days=3)
print("Nouvelle date :", nouvelle_date)
