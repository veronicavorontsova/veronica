# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

def print_names_of_stars(targets):
    for star in targets:
        print(star)

print_names_of_stars(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def print_names_and_spectral_types_of_stars(targets):
    for star in targets:
        print(star, targets[star]["Spectral Type"])

print_names_and_spectral_types_of_stars(targets)


# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def stars_with_magnitude_greater_than_point_one(targets):
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(star)

stars_with_magnitude_greater_than_point_one(targets)

# 4) Look up another target, add all the necessary information to the targets list. 

# Canopus

targets["Canopus"] ={
    "RA": "06h 23m 57.1s",
    "Dec": "-52° 41′ 44″",
    "Magnitude": -0.72,
    "Spectral Type": "A9II"
}

print(targets) 

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def declination_closest_to_20(targets):
    star = None
    declinations = []
    for star in targets:
        targets[star]["Dec"] = targets[star]["Dec"].replace("°", "").replace("′", "").replace("″", "").replace("+", "")
        dec_value = float(targets[star]["Dec"].split()[0])
        difference = abs(dec_value - 20)
        declinations += [(star, abs(dec_value - 20))]
    print(declinations)

# im sorry im stuck and i dont know :(

declination_closest_to_20(targets)

# 6) What is your favorite constellation?

# big dipper 