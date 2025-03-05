"""
**Dictionary Comprehension**:
   - Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.
"""
Kannada_cities = {"Bangalore": 1200000,
                  "Mysore": 80000,
                  "Madikeri": 45000,
                  "Mangalore": 60000,
                  "Belagavi": 1300000
                  }

Cities_population = {cities:population for cities,population in Kannada_cities.items() if population < 100000}
print(Cities_population)
