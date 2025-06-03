import requests     #do "pip install requests" in terminal

response = requests.get("https://raw.githubusercontent.com/WhalenSITHS/Pokedex-Python-Starter/main/moves.json")

try:
    data = response.json()
    for moving in data:
        if moving['id'] <= 10:
            print(moving['ename'])

except Exception as e:
    print("Failed to fetch dataings", e)


#this code for pokedex.json, it bit more commplex
""" response = requests.get("https://raw.githubusercontent.com/WhalenSITHS/Pokedex-Python-Starter/main/pokedex.json")

try:
    data = response.json()
    print(data[3]['name']['english'])   # number = id, name is name of id number, english is eng name of id number

#or for all pokemon:

    #for data in data:
        #print(data['name']['english'])


except KeyError:
    print("Failed to fetch data.") """