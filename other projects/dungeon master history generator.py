import random

# Defining dictionaries for various aspects

# Government Types
government_types = {
    (1, 8): "Autocracy",
    (9, 13): "Bureaucracy",
    (14, 19): "Confederacy",
    (20, 22): "Democracy",
    (23, 27): "Dictatorship",
    (28, 42): "Feudalism",
    (43, 44): "Gerontocracy",
    (45, 53): "Hierarchy",
    (54, 56): "Magocracy",
    (57, 58): "Matriarchy",
    (59, 64): "Militocracy",
    (65, 74): "Monarchy",
    (75, 78): "Oligarchy",
    (79, 80): "Patriarchy",
    (81, 83): "Meritocracy",
    (84, 85): "Plutocracy",
    (86, 92): "Republic",
    (93, 94): "Satrapy",
    (95, 95): "Kleptocracy",
    (96, 100): "Theocracy"
    # Add more government types ...
}

# Rank Titles
rank_titles = {
    1: "Emperor/Empress",
    2: "King/Queen",
    # Add more rank titles ...
}

# Faction Ranks
faction_ranks = {
    "Order of the Gauntlet": [
        "Cheval I",
        "Marcheon",
        "Whitehawk",
        "Vindicator",
        "Righteous Hand"
    ],
    "Emerald Enclave": [
        "Springwarden",
        "Summerstrider",
        "Autumnreaver",
        "Winterstalker",
        "Master of the Wild"
    ],
    "Alliance Zhentarim": [
        "Fang",
        "Wolf",
        "Viper",
        "Ardragon",
        "Dread Lord"
    ],
    "Harper Renown": [
        "Watcher",
        "Harpshadow",
        "Brightcandle",
        "Wise Owl",
        "High Harper"
    ]
    # Add more faction ranks ...
}

# World Shaking Events
world_shaking_events = [
    "Rise of a leader or an era",
    "Fall of a leader or an era",
    "Cataclysmic disaster",
    "Assault or invasion",
    "Rebellion, revolution, overthrow",
    "Extinction or depletion",
    "New organization",
    "Discovery, expansion, invention",
    "Prediction, omen, prophecy",
    "Myth and legend"
]

# Leader Types
leader_types = [
    "Political",
    "Religious",
    "Military",
    "Crime/underworld",
    "Agriculture",
    "Philosophy/learning/magic"
]

# Cataclysmic Disasters
cataclysmic_disasters = [
    "Earthquake",
    "Famine/drought",
    "Fire",
    "Flood",
    "Plague/disease",
    "Rain of fire (meteoric impact)",
    "Storm (hurricane, tornado, tsunami)",
    "Volcanic eruption",
    "Magic gone awry or a planar warp",
    "Divine judgment"
]

# Invading Forces
invading_forces = [
    "A criminal enterprise",
    "Monsters or a unique monster",
    "A planar threat",
    "A past adversary reawakened, reborn, or resurgent",
    "A splinter faction",
    "A savage tribe",
    "A secret society",
    "A traitorous ally"
]

# Extinction or Depletion
extinction_or_depletion = [
    "A kind of animal (insect, bird, fish, livestock)",
    "Habitable land",
    "Magic or magic-users (all magic, or specific kinds or schools of magic)",
    "A mineral resource (gems, metals, ores)",
    "A type of monster (unicorn, manticore, dragon)",
    "A people (family line, clan, culture, race)",
    "A kind of plant (crop, tree, herb, forest)",
    "A waterway (river, lake, ocean)"
]

# New Organizations
new_organizations = [
    "Crime syndicate/bandit confederacy",
    "Guild (masons, apothecaries, goldsmiths)",
    "Magical circle/society",
    "Military/knightly order",
    "New family dynasty/tribe/clan",
    "Philosophy/discipline dedicated to a principle or ideal",
    "Realm (village, town, duchy, kingdom)",
    "Religion/sect/denomination",
    "School/university",
    "Secret society/cult/cabal"
]


# Discoveries
discoveries = [
    "Ancient ruin/lost city of a legendary race",
    "Animal/monster/magical mutation",
    "Invention/technology/magic (helpful, destructive)",
    "New (or forgotten) god or planar entity",
    "New (or rediscovered) artifact or religious relic",
    "New land (island, continent, lost world, demiplane)",
    "Otherworldly object (planar portal, alien spacecraft)",
    "People (race, tribe, lost civilization, colony)",
    "Plant (miracle herb, fungal parasite, sentient plant)",
    "Resource or wealth (gold, gems, mithral)"
]

# Astral Color Pools
astral_color_pools = {
    1: ("Ysgard", "Indigo"),
    2: ("Limbo", "Jet black"),
    3: ("Pandemonium", "Magenta"),
    # Add more astral color pools ...
}

# Psychic Wind Effects
psychic_wind_locations = {
    (1, 8): "Diverted; add 1d6 hours to travel time",
    (9, 12): "Blown off course; add 3d10 hours to travel time",
    (13, 16): "Lost; at the end of the travel time, characters arrive at a location other than the intended destination",
    (17, 20): "Sent through color pool to a random plane (roll on the Astral Color Pools table)"
}

psychic_wind_mental_effects = {
    (1, 8): "Stunned for 1 minute; you can repeat the saving throw at the end of each of your turns to end the effect on yourself",
    (9, 10): "Short-term madness",
    (11, 12): "(2d10) psychic damage",
    (13, 16): "(4d10) psychic damage",
    (17, 18): "Long-term madness (see chapter 8)",
    (19, 20): "Unconscious for 5 (1d10) minutes; the effect on you ends if you take damage or if another creature uses an action to shake you awake"
}

# Ethereal Curtains
ethereal_curtains = {
    1: ("Material Plane", "Bright turquoise"),
    2: ("Shadowfell", "Dusky gray"),
    # Add more ethereal curtains ...
}

# Feywild Time Warp
feywild_time_warp = {
    1: "Days become minutes",
    2: "Days become hours",
    3: "No change",
    4: "Days become weeks",
    5: "Days become months",
    6: "Days become years"
}

# Dungeon Goals
dungeon_goals = [
    "Stop the dungeon's monstrous inhabitants from raiding the surface world.",
    "Foil a villain's evil scheme.",
    "Destroy a magical threat inside the dungeon.",
    "Acquire treasure.",
    "Find a particular item for a specific purpose.",
    "Retrieve a stolen item hidden in the dungeon.",
    "Find information needed for a special purpose.",
    "Rescue a captive.",
    "Discover the fate of a previous adventuring party.",
    "Find an NPC who disappeared in the area.",
    "Slay a dragon or some other challenging monster.",
    "Discover the nature and origin of a strange location or phenomenon.",
   "Pursue fleeing foes taking refuge in the dungeon.",
    "Escape from captivity in the dungeon.",
    "Clear a ruin so it can be rebuilt and reoccupied.",
    "Discover why a villain is interested in the dungeon.",
    "Win a bet or complete a rite of passage by surviving in the dungeon for a certain amount of time.",
    "Parley with a villain in the dungeon.",
    "Hide from a threat outside the dungeon.",
    "Roll twice, ignoring results of 20."
]

# Wilderness Goals
wilderness_goals = [
    "Locate a dungeon or other site of interest (roll on the Dungeon Goals table to find out why).",
    "Assess the scope of a natural or unnatural disaster.",
    "Escort an NPC to a destination.",
    "Arrive at a destination without being seen by the villain's forces.",
    "Stop monsters from raiding caravans and farms.",
    "Establish trade with a distant town.",
    "Protect a caravan traveling to a distant town.",
    "Map a new land.",
    "Find a place to establish a colony.",
    "Find a natural resource.",
    "Hunt a specific monster.",
    "Return home from a distant place.",
    "Obtain information from a reclusive hermit.",
    "Find an object that was lost in the wilds.",
    "Discover the fate of a missing group of explorers.",
    "Pursue fleeing foes.",
    "Assess the size of an approaching army.",
    "Escape the reign of a tyrant.",
    "Protect a wilderness site from attackers.",
    "Roll twice, ignoring results of 20."
]

# Other Goals
other_goals = [
    "Seize control of a fortified location such as a fortress, town, or ship.",
    "Defend a location from attackers.",
    "Retrieve an object from inside a secure location in a settlement.",
    "Retrieve an object from a caravan.",
    "Receive information from an NPC in the area.",
    "Rescue a captive.",
    "Discover the fate of a missing NPC.",
    "Slay a specific monster.",
    "Discover the nature and origin of a strange phenomenon in the area.",
    "Secure the aid of a character or creature in the area.",
    "Roll twice, ignoring results of 20."
]

# Adventure Patrons
adventure_patrons = [
    "Retired adventurer",
    "Local ruler",
    "Military officer",
    "Temple official",
    "Sage",
    "Respected elder",
    "Deity or celestial",
    "Mysterious fey",
    "Old friend",
    "Former teacher",
    "Parent or other family member",
    "Desperate commoner",
    "Embattled merchant",
    "Villain posing as a patron"
]

# Adventure Villains
adventure_villains = [
    "Beast or monstrosity with no particular agenda",
    "Aberration bent on corruption or domination",
    "Fiend bent on corruption or destruction",
    "Dragon bent on domination and plunder",
    "Giant bent on plunder",
    "Undead with any agenda",
    "Fey with a mysterious goal",
    "Humanoid cultist",
    "Humanoid conqueror",
    "Humanoid seeking revenge",
    "Humanoid schemer seeking to rule",
    "Humanoid criminal mastermind",
    "Humanoid raider or ravager",
    "Humanoid under a curse",
    "Misguided humanoid zealot"
]

# Adventure Allies
adventure_allies = [
    "Skilled adventurer",
    "Inexperienced adventurer",
    "Enthusiastic commoner",
    "Soldier",
    "Priest",
    "Sage",
    "Revenge seeker",
    "Raving lunatic",
    "Celestial ally",
    "Fey ally",
    "Disguised monster",
    "Villain posing as an ally"
]

# Adventure Introduction
adventure_introduction = [
    "While traveling in the wilderness, the characters fall into a sinkhole that opens beneath their feet, dropping them into the adventure location.",
    "While traveling in the wilderness, the characters notice the entrance to the adventure location.",
    "While traveling on a road, the characters are attacked by monsters that flee into the nearby adventure location.",
    "The adventurers find a map on a dead body. In addition to the map setting up the adventure, the adventure's villain wants the map.",
    "A mysterious magic item or a cruel villain teleports the characters to the adventure location.",
    "A stranger approaches the characters in a tavern and urges them toward the adventure location.",
    "A town or village needs volunteers to go to the adventure location.",
    "An NPC the characters care about needs them to go to the adventure location.",
    "An NPC the characters must obey orders them to go to the adventure location.",
    "An NPC the characters respect asks them to go to the adventure location.",
    "One night, the characters all dream about entering the adventure location.",
    "A ghost appears and terrorizes a village. Research reveals that it can be put to rest only by entering the adventure location."
]

# Adventure Climax
adventure_climax = [
    "The adventurers confront the main villain and a group of minions in a bloody battle to the finish.",
    "The adventurers chase the villain while dodging obstacles designed to thwart them, leading to a final confrontation in or outside the villain's refuge.",
    "The actions of the adventurers or the villain result in a cataclysmic event that the adventurers must escape.",
    "The adventurers race to the site where the villain is bringing a master plan to its conclusion, arriving just as that plan is about to be completed.",
    "The villain and their minions take one last stand against the characters in a location full of traps and obstacles.",
    "The adventurers must traverse a portal or passageway to reach the villain, battling monsters from the other side and overcoming otherworldly hazards.",
    "The characters must assault a fortress or secret lair in which the villain is hiding, facing guards, traps, and other hindrances before confronting the villain.",
    "The villain summons a powerful entity to do battle while they make their escape, and the characters must find a way to banish or defeat it.",
    "The adventurers must navigate a treacherous environment (such as a raging storm, active battlefield, or complex trap) while facing off against the villain and their minions.",
    "The climax takes place in the presence of a powerful third party, such as a monarch, a deity, or a magical being, who plays a key role in determining the outcome.",
    "The villain uses a powerful relic, artifact, or magical device in the final confrontation, forcing the characters to find a way to disable or counter it.",
    "The characters must race against time to prevent a ritual, magical event, or catastrophe from occurring, all while the villain does everything in their power to stop them.",
    "The climax takes place in a surreal or otherworldly environment, where the normal rules of reality may be suspended or altered in unpredictable ways.",
    "The adventurers face off against the villain in a grand arena or battleground, with an audience (willing or unwilling) witnessing the outcome.",
    "The climax takes place within the villain's mind or in a dreamscape, where the characters must navigate a landscape of thoughts, memories, and illusions.",
    "The adventurers must confront the villain in a location infused with powerful magic, where the environment itself aids or hinders them in the battle.",
    "The climax involves a high-stakes chase or pursuit, with the characters racing to catch the villain before they can accomplish their final goal.",
    "The adventurers must make a critical decision that could drastically affect the outcome of the confrontation with the villain.",
    "The climax takes place in a location of great personal significance to one or more of the characters, adding an emotional layer to the final battle.",
    "The adventurers must confront the villain in a place that is intimately connected to their identity, source of power, or origin.",
    "The climax is a battle of wits and strategy, with the characters using their intelligence and cunning to outmaneuver the villain.",
    "The villain attempts to flee, and the characters must pursue them through a series of dangerous obstacles and challenges.",
    "The adventurers must find a way to turn the villain's own tactics or powers against them in the final confrontation.",
    "The climax takes place in a location that is inherently unstable or in the process of undergoing a transformation, adding an element of unpredictability to the battle.",
    "The characters must work together to activate or harness a powerful artifact, ritual, or magical phenomenon to overcome the villain.",
    "The climax involves a showdown with the villain in a location that is both physically and thematically significant, representing the culmination of their journey."
]

# Adventure Reward
adventure_rewards = [
    "A significant amount of treasure or wealth.",
    "A powerful magic item or artifact.",
    "Land, property, or a title of nobility.",
    "Fame, renown, or a heroic reputation.",
    "Secret knowledge or a valuable piece of information.",
    "A powerful ally or a group of followers.",
    "The gratitude and support of a community or organization.",
    "The opportunity to learn a new skill, technique, or magical ability.",
    "A boon or blessing from a powerful being or deity.",
    "A favor or owed debt from a powerful figure or organization.",
    "A rare or exotic mount or creature companion.",
    "Access to a hidden or forbidden location.",
    "The removal of a curse or affliction affecting the characters.",
    "A unique, personalized item or piece of equipment.",
    "The chance to establish a legacy or dynasty.",
    "The fulfillment of a personal goal or ambition of one of the characters."
]

# Plot Hooks
plot_hooks = [
    "The characters receive a mysterious letter or message that sets them on the path to adventure.",
    "A powerful NPC seeks the characters' assistance in a matter of great import.",
    "The characters stumble upon a strange artifact or relic that holds a clue to a larger mystery.",
    "A natural disaster or cataclysmic event threatens the characters' homeland, and they must seek a solution.",
    "The characters witness an unusual celestial event that portends a significant event in the near future.",
    "A powerful magical entity or being appears before the characters and delivers a cryptic message.",
    "The characters come into possession of an ancient map or manuscript that leads to a hidden treasure or lost city.",
    "A group of scholars or researchers approaches the characters seeking their expertise or aid on a matter of great importance.",
    "The characters are drawn into a conflict between rival factions or organizations vying for power or control.",
    "A long-lost relative or friend of one of the characters reappears, bringing news of a dire threat that only they can face.",
    "The characters are hired to retrieve a stolen or lost item, but discover that its significance goes far beyond its material value.",
    "A series of seemingly unrelated events or occurrences lead the characters to uncover a larger, interconnected conspiracy.",
    "The characters are cursed or afflicted in some way, and must undertake a quest to find a cure or remedy.",
    "A prophecy or ancient legend foretells of a group of heroes who will rise to face a great evil, and the characters believe they are the ones mentioned.",
    "A powerful magical or supernatural force reaches out to the characters, seeking their aid or intervention in a matter of cosmic significance."
]

#-----------------------------------VARIABLES ARRAY---------------------------------------------------------------------------
variable_names = [
    "government_types",
    "rank_titles",
    "faction_ranks",
    "world_shaking_events",
    "leader_types",
    "cataclysmic_disasters",
    "invading_forces",
    "extinction_or_depletion",
    "new_organizations",
    "discoveries",
    "astral_color_pools",
    "psychic_wind_locations",
    "psychic_wind_mental_effects",
    "ethereal_curtains",
    "feywild_time_warp",
    "dungeon_goals",
    "wilderness_goals",
    "other_goals",
    "adventure_patrons",
    "adventure_villains",
    "adventure_allies",
    "adventure_introduction",
    "adventure_climax",
    "adventure_rewards",
    "plot_hooks"
]




Villain_Objectives = {
    "Power": {
        "description": "The villain seeks to gain ultimate power, whether magical, political, or divine.",
        "methods": [
            "Collecting ancient artifacts",
            "Making pacts with dark forces",
            "Usurping a throne",
            "Performing forbidden rituals"
        ]
    },
    "Domination": {
        "description": "They aim to conquer and rule over a kingdom, continent, or the world.",
        "methods": [
            "Building an army",
            "Manipulating royal bloodlines",
            "Summoning extraplanar forces",
            "Controlling a mind flayer hive"
        ]
    },
    "Destruction": {
        "description": "They want to destroy a city, a race, the gods, or the fabric of reality itself.",
        "methods": [
            "Activating an apocalyptic artifact",
            "Unleashing an ancient dragon",
            "Opening a rift to the Far Realm",
            "Corrupting a divine relic"
        ]
    },
    "Revenge": {
        "description": "Motivated by a personal slight, betrayal, or injustice—real or imagined.",
        "methods": [
            "Assassinating leaders",
            "Spreading a deadly plague",
            "Turning allies against one another",
            "Sabotaging peace negotiations"
        ]
    },
    "Immortality": {
        "description": "The villain is obsessed with escaping death through undeath, divinity, or arcane means.",
        "methods": [
            "Becoming a lich",
            "Harvesting souls",
            "Bathing in dragon blood",
            "Creating a phylactery"
        ]
    },
    "Wealth": {
        "description": "They pursue treasure hoards, control of trade routes, or monopolies over rare resources.",
        "methods": [
            "Seizing mines or ports",
            "Robbing royal treasuries",
            "Creating counterfeit currency",
            "Running a black market"
        ]
    },
    "Chaos": {
        "description": "They want to plunge the world into madness or disorder.",
        "methods": [
            "Spreading demonic influence",
            "Inciting rebellion or cult uprisings",
            "Breaking magical laws",
            "Summoning an Elder Evil"
        ]
    },
    "Purification": {
        "description": "The villain believes in cleansing the world of impurity, sin, magic, or certain races.",
        "methods": [
            "Leading genocidal crusades",
            "Creating inquisitions",
            "Burning libraries of arcane knowledge",
            "Mind-wiping the population"
        ]
    },
    "Restoration": {
        "description": "They seek to return the world to a lost age or undo a historic tragedy—no matter the cost.",
        "methods": [
            "Time-traveling rituals",
            "Destroying modern civilizations",
            "Reawakening ancient powers",
            "Rebuilding empires from ruins"
        ]
    },
    "Obedience": {
        "description": "They want to force the world to kneel to their ideology, god, or people.",
        "methods": [
            "Casting charm or geas spells en masse",
            "Creating propaganda machines",
            "Using relics of fear or dominance",
            "Creating brainwashing devices"
        ]
    },
    "Experimentation": {
        "description": "Driven by curiosity, they test boundaries—mortal, magical, or moral.",
        "methods": [
            "Mutating prisoners in secret labs",
            "Merging planes",
            "Transplanting souls",
            "Turning towns into test grounds"
        ]
    },
    "Prophecy": {
        "description": "They believe they are fulfilling a dark prophecy or divine plan.",
        "methods": [
            "Sacrificing chosen ones",
            "Decoding ancient runes",
            "Triggering omens",
            "Forcing celestial alignments"
        ]
    },
    "Protection": {
        "description": "A tragic villain who commits atrocities to 'protect' something—a people, a secret, or the world itself.",
        "methods": [
            "Sealing realms with forbidden magic",
            "Creating deadly defenses",
            "Eliminating potential threats preemptively",
            "Kidnapping powerful children"
        ]
    },
    "Addiction": {
        "description": "The villain is consumed by a need—for souls, blood, attention, worship, or arcane power.",
        "methods": [
            "Devouring life force",
            "Siphoning magic from ley lines",
            "Running cults of personality",
            "Performing ritual killings"
        ]
    },
    "Love": {
        "description": "Their actions are to win back, revive, or avenge a loved one—by war, ritual, or madness.",
        "methods": [
            "Raising the dead through necromancy",
            "Destroying all who resemble their lost lover’s killer",
            "Creating simulacra of the beloved",
            "Freezing time to preserve a memory"
        ]
    }
}












#-----------------------------------VARIABLES ARRAY---------------------------------------------------------------------------

#----------------------read variables array----------------------------------------------


def read_list(variable_names):
    for var_name in variable_names:
        var_data = globals().get(var_name, None)
        if var_data is not None:
            print(f"Variable: {var_name}"+":     ")

            random_selection(var_data)
        else:
            print(f"Variable {var_name} not found"+"\n\n")

#----------------------read variables array----------------------------------------------

#----------------------select random values from within the variables arrays and dictionaries----------------

def random_selection(Array_data):
    try:
        if isinstance(Array_data, list):
            random_i = random.randint(0, len(Array_data) - 1)
            random_selector = Array_data[random_i]
            print(random_selector)
        elif isinstance(Array_data, dict):
            data = list(Array_data.items())
            random_i = random.randint(0, len(data) - 1)
            return(data[random_i])
        else:
            print("Unsupported data type"+"\n\n")
    except Exception as e:
        print(f"Error: {e}"+"\n\n")

#---------------------select random values from within the variables arrays and dictionaries----------------

#--------------Just call the function to start all the listing

read_list(variable_names)


