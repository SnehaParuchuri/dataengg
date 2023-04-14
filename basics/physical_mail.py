house_num = 123
street_name = "main street"
city = "anytown"
state = "ny"
zip_code = 12345

street_name = street_name.capitalize()
city = city.capitalize()
state = state.upper()    

full_addr = f"{house_num} {street_name}, {city}, {state}, {zip_code}"

print(full_addr)