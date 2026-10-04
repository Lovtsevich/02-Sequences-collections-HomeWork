countries = {
    "BY": "Belarus",
    "PL": "Poland",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain"
}
countries_keys = countries.keys()
countries_values = countries.values()

new_countries = dict(zip(countries_values,countries_keys)) 
print(new_countries)