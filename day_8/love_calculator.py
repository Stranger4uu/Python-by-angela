logo = """
====================================
        💖 LOVE CALCULATOR 💖
====================================

        ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥
      ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥
     ♥ ♥   TRUE LOVE   ♥ ♥
      ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥
        ♥ ♥ ♥ ♥ ♥ ♥ ♥

------------------------------------
      Let the Love Score Decide 💕
------------------------------------
"""


def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_count = (
        combined_names.count("t") +
        combined_names.count("r") +
        combined_names.count("u") +
        combined_names.count("e")
    )
    
    love_count = (
        combined_names.count("l") +
        combined_names.count("o") +
        combined_names.count("v") +
        combined_names.count("e")
    )
    
    print(f"{true_count}{love_count}")

print(logo)

calculate_love_score("Yash", "No one for now")
