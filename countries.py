# Tackle your project here!
# from https://python.tecladocode.com/3_continuous_countries/3_continuous_countries_project.html
countries =[]
country_count =''
user_input = input('Enter "a" to add a country you have visited, or"q" to quit: ')

while user_input !="q":
  user_country = input('enter country name: ')
  countries.append(user_country)
  if len(countries) > 1:
    country_count = "countries"
  else:
    country_count = "country"
    
  print(f"you have visited {len(countries)} {country_count}")


user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")
