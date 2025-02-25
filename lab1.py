# Solicitarea prenumelui și afișarea unui mesaj de salut
userFirstName = input('Introduce prenumele tau: ')  
print("Bună", userFirstName + "!")

# Definirea variabilelor
userAge = 22
weeklyActivityHours = 70
activityStatus = "Student"  
dailySchedule = "USM Facultatea Matematica si Informatica\n Game Design"

# Afișarea tipurilor de date
print(type(userAge), type(weeklyActivityHours))  
print(len(activityStatus))  

# Conversia activityStatus în litere mici
activityStatusLower = activityStatus.lower()  
print(activityStatusLower)  

# Extrage o secțiune din dailySchedule
scheduleSnippet = dailySchedule[2:5]  
print(scheduleSnippet)  

# Mesaj de rămas bun
farewellMessage = "Succes, {}".format(userFirstName)  
print(farewellMessage) 
