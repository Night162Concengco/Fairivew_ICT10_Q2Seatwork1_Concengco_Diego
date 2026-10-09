from js import document
from pyodide.ffi import create_proxy


club_members = [
    "Athena Ari",
    "Brian Bo",
    "Carter Cu",
]

def check_membership(event):
  
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()

   
    full_name_lower = full_name.lower()
    members_lower = list(map(str.lower, club_members))

  
    is_member = full_name_lower in members_lower


    messages = [
        f"Sorry, {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]

   
    document.getElementById("result").innerText = messages[is_member]

def setup():
    button = document.getElementById("btn-submit")
    button.addEventListener("click", create_proxy(check_membership))

setup()