
from pyscript import display, document

kaiju = {
    #Few of the many iterations of Godzilla across the years. I only included the more recent, iconic versions
    #Trust me, There is a LOT more than this amount and if you don't believe me search it up.
    "Godzilla": ("Godzilla", 1954, "Himself"),
    "Shin Godzilla": ("Shin Godzilla", 2016, "Himself"),
    "Godzilla Minus One": ("Godzilla Minus One", 2023, "Himself"),
    "Minus One Godzilla": ("Godzilla Minus One", 2023, "Himself"),
    "Godzilla Minus Zero": ("Godzilla Minus Zero", 2026, "Himself"),
    "Godzilla Minus One": ("Godzilla Minus One", 2023, "Himself"),
    "Legendary Godzilla": ("Godzilla", 2014, "Himself"),
    "Zilla": ("no", 0, "no"),
    "Chibi Godzilla": ("Chibi Godzilla, Raids again!", 2023, "Himself"),

    #These are the children of Godzilla, Though not all biological, for some reason?
    "Minilla": ("Son of Godzilla", 1967, "Son"),
    "Godzilla Junior": ("Godzilla vs. Mechagodzilla II", 1993, "Son"),
    "Godzilla Jr": ("Godzilla vs. Mechagodzilla II", 1993, "Son"),
    "Godzooky": ("The Godzilla Power Hour", 1978, "Son"),

    #These are the jokes/gag section, they are not meant in foul, These are jokes between friends.
    #Ethan allows these jokes!
    "Ethan Deleon": ("Ethan, The Giant-Lasagna Monster", 1975, "Homeboy"),
    "Po": ("Kung Fu Panda", 2008, "Biggest Enemy"),
    "Lightning Mcqueen": ("War of the Worlds", -1500, "Great Grandfather"),

    #The are the side-characters of Godzilla, whether friend or foe.
    "Mothra": ("Mothra", 1961, "Ally"),
    "Rodan": ("Rodan", 1956, "Rival / Ally"),
    "Jet Jaguar": ("Godzilla vs. Megalon", 1973, "Ally"),
    "King Ghidorah": ("Ghidorah, the Three-Headed Monster", 1964, "Enemy"),
    "Ghidorah": ("Ghidorah, the Three-Headed Monster", 1964, "Enemy"),
    "Anguirus": ("Godzilla Raids Again", 1955, "Ally"),
    "Mechagodzilla": ("Godzilla vs. Mechagodzilla", 1974, "Enemy"),
    "Gigan": ("Godzilla vs. Gigan", 1972, "Enemy"),
    "Hedorah": ("Godzilla vs. Hedorah", 1971, "Enemy"),
    "Biollante": ("Godzilla vs. Biollante", 1989, "Enemy"),
    "Destoroyah": ("Godzilla vs. Destoroyah", 1995, "Enemy"),
    "Spacegodzilla": ("Godzilla vs. SpaceGodzilla", 1994, "Enemy"),
    "Megalon": ("Godzilla vs. Megalon", 1973, "Enemy"),
    "Kumonga": ("Son of Godzilla", 1967, "Enemy"),
    "Baragon": ("Frankenstein Conquers the World", 1965, "Ally"),
    "King Caesar": ("Godzilla vs. Mechagodzilla", 1974, "Ally"),
    "Battra": ("Godzilla vs. Mothra", 1992, "Rival"),
}

# USING .get() TO FIND THE KAIJU
def check_element(e):
    document.getElementById('result').innerHTML = ""

    kaiju1 = document.getElementById('element').value.strip().title()

    info = kaiju.get(
        kaiju1,
        ("Kaiju not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Movie of Origin:</b> {info[0]} <br>
    <b>Year of Creation / Debut:</b> {info[1]} <br>
    <b>Status with Godzilla:</b> {info[2]}
    """
