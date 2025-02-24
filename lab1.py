# Solicitarea prenumelui și afișarea unui mesaj de salut
userFirstName = input('Introduce prenumele tau: ')  
print("Bună", userFirstName + "!")

# Definirea variabilelor
userAge = 22
weeklyActivityHours = 70
maritalStatus = "Celibatar"  
dailySchedule = "Luni-Vineri: Studii\nSâmbătă-Duminică: Zile de odihna"

# Afișarea tipurilor de date
print(type(userAge), type(weeklyActivityHours))  
print(len(maritalStatus))  

# Conversia maritalStatus în litere mici
maritalStatusLower = maritalStatus.lower()  
print(maritalStatusLower)  

# Extrage o secțiune din dailySchedule
scheduleSnippet = dailySchedule[0:52]  
print(scheduleSnippet)  

# Mesaj de rămas bun
farewellMessage = "Succes, {}".format(userFirstName)  
print(farewellMessage)  