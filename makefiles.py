import os

# Define the directory structure
structure = {
    "dnd_pvp_game": [
        "main.py",
        "settings.py",
        "game.py",
        "turn_manager.py",
        "entity.py",
        "spells.py",
        {"assets": [
            {"images": ["player.png", "enemy.png", "spell_effect.png"]},
            {"sounds": ["attack.wav", "spell_cast.wav"]},
            {"fonts": ["game_font.ttf"]}
        ]},
        {"scenes": ["menu.py", "battle.py", "game_over.py"]},
        {"entities": ["player.py", "enemy.py", "npc.py"]},
        {"spells": ["fireball.py", "heal.py", "lightning.py"]},
        {"utils": ["helpers.py", "constants.py"]}
    ]
}

def create_structure(base_path, structure):
    for key, value in structure.items():
        if isinstance(value, list):
            dir_path = os.path.join(base_path, key)
            os.makedirs(dir_path, exist_ok=True)
            for item in value:
                if isinstance(item, dict):
                    create_structure(dir_path, item)
                else:
                    open(os.path.join(dir_path, item), 'a').close()
        else:
            open(os.path.join(base_path, key), 'a').close()

# Create the project structure
base_path = "."
create_structure(base_path, {"dnd_pvp_game": structure["dnd_pvp_game"]})

print("Project structure created successfully!")
