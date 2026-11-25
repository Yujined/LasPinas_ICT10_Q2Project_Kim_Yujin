from pyscript import document

def candidate_checker(e):
    club_members = [
        "saburo arasaka",
        "michiko arasaka",
        "kei arasaka",
        "hanako arasaka"
    ]

    f_name = document.getElementById("first_name").value
    l_name = document.getElementById("last_name").value

    candidate = f_name.strip() + " " + l_name.strip()

    member_checker = candidate.lower() in club_members

    messages = (
        f"{candidate}, you are not a member of the Arasaka Family, Your presence from this webpage is prohibited..",
        f"Welcome, Beloved {candidate}. Entering your credentials into our database."
    )

    document.getElementById("result").innerHTML = messages[member_checker]