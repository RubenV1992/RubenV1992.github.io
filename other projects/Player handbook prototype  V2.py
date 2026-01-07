# Array for the races
races = [
    "Dwarf",
    "Elf",
    "Halfling",
    "Human",
    "Dragonborn",
    "Gnome",
    "Half-Elf",
    "Half-Orc",
    "Tiefling"
]

# Array for the races traits including ability score improvements, key racial traits, height, weight, and age range
races_traits = [
    {
        "race": "Dwarf",
        "ability_score_improvement": [0, 0, 2, 0, 0, 0],
        "traits": ["Darkvision", "Dwarven Resilience", "Stonecunning"],
        "height": "4 to 5 feet",
        "weight": "150 to 200 pounds",
        "age_range": "50 to 350 years"
    },
    {
        "race": "Elf",
        "ability_score_improvement": [0, 2, 0, 0, 0, 0],
        "traits": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
        "height": "5 to 6 feet",
        "weight": "100 to 145 pounds",
        "age_range": "100 to 750 years"
    },
    {
        "race": "Halfling",
        "ability_score_improvement": [0, 2, 0, 0, 0, 0],
        "traits": ["Lucky", "Brave", "Halfling Nimbleness"],
        "height": "3 feet",
        "weight": "40 to 45 pounds",
        "age_range": "20 to 150 years"
    },
    {
        "race": "Human",
        "ability_score_improvement": [1, 1, 1, 1, 1, 1],
        "traits": ["Versatility"],
        "height": "5 to 6 feet",
        "weight": "125 to 250 pounds",
        "age_range": "20 to 100 years"
    },
    {
        "race": "Dragonborn",
        "ability_score_improvement": [2, 0, 0, 0, 0, 1],
        "traits": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
        "height": "6 to 7 feet",
        "weight": "250 to 300 pounds",
        "age_range": "15 to 80 years"
    },
    {
        "race": "Gnome",
        "ability_score_improvement": [0, 0, 0, 2, 0, 0],
        "traits": ["Darkvision", "Gnome Cunning"],
        "height": "3 to 4 feet",
        "weight": "40 to 45 pounds",
        "age_range": "40 to 500 years"
    },
    {
        "race": "Half-Elf",
        "ability_score_improvement": [0, 0, 0, 0, 0, 2],
        "traits": ["Darkvision", "Fey Ancestry", "Skill Versatility"],
        "height": "5 to 6 feet",
        "weight": "100 to 180 pounds",
        "age_range": "20 to 180 years"
    },
    {
        "race": "Half-Orc",
        "ability_score_improvement": [2, 0, 1, 0, 0, 0],
        "traits": ["Darkvision", "Menacing", "Relentless Endurance", "Savage Attacks"],
        "height": "5 to 7 feet",
        "weight": "180 to 250 pounds",
        "age_range": "14 to 75 years"
    },
    {
        "race": "Tiefling",
        "ability_score_improvement": [0, 0, 0, 1, 0, 2],
        "traits": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
        "height": "5 to 6 feet",
        "weight": "125 to 250 pounds",
        "age_range": "20 to 100 years"
    }
]

# Define racial traits
racial_traits = {
    "Human": {"Ability Score Increase": "All ability scores +1"},
    "Variant Human": {"Ability Score Increase": "Two different ability scores +1, gain one skill proficiency, gain one feat"},
    "High Elf": {"Ability Score Increase": "Dexterity +2, Intelligence +1", "Elf Weapon Training": "Proficiency with longsword, shortsword, shortbow, longbow"},
    "Wood Elf": {"Ability Score Increase": "Dexterity +2, Wisdom +1", "Elf Weapon Training": "Proficiency with longsword, shortsword, shortbow, longbow"},
    "Dark Elf (Drow)": {"Ability Score Increase": "Dexterity +2, Charisma +1", "Drow Magic": "Can cast dancing lights, faerie fire, darkness"},
    "Hill Dwarf": {"Ability Score Increase": "Constitution +2, Wisdom +1", "Dwarven Toughness": "Hit point maximum increases by 1, and it increases by 1 every time you gain a level"},
    "Mountain Dwarf": {"Ability Score Increase": "Constitution +2, Strength +2", "Dwarven Armor Training": "Proficiency with light and medium armor"},
    "Lightfoot": {"Ability Score Increase": "Dexterity +2, Charisma +1", "Naturally Stealthy": "Can attempt to hide even when you are obscured only by a creature that is at least one size larger than you"},
    "Stout": {"Ability Score Increase": "Dexterity +2, Constitution +1", "Stout Resilience": "Advantage on saving throws against poison, resistance to poison damage"},
    "Dragonborn": {"Ability Score Increase": "Strength +2, Charisma +1", "Draconic Ancestry": "Choose a dragon type and gain its breath weapon and damage resistance"},
    "Forest Gnome": {"Ability Score Increase": "Intelligence +2, Dexterity +1", "Natural Illusionist": "Can cast minor illusion cantrip"},
    "Rock Gnome": {"Ability Score Increase": "Intelligence +2, Constitution +1", "Artificer's Lore": "Add twice proficiency bonus to History checks related to magic items, alchemical objects, or technological devices"},
    "Half-Elf": {"Ability Score Increase": "Charisma +2, two other ability scores of your choice +1", "Skill Versatility": "Proficiency in two skills of your choice"},
    "Half-Orc": {"Ability Score Increase": "Strength +2, Constitution +1", "Relentless Endurance": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest"},
    "Tiefling": {"Ability Score Increase": "Charisma +2, Intelligence +1", "Infernal Legacy": "You know the thaumaturgy cantrip. When you reach 3rd level, you can cast hellish rebuke as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast darkness once with this trait and regain the ability to do so when you finish a long rest"}
}

# Define background types and options
backgrounds = {
    "Acolyte": ["Shelter of the Faithful", "Skill Proficiencies: Insight, Religion", "Languages: Two of your choice"],
    "Charlatan": ["False Identity", "Skill Proficiencies: Deception, Sleight of Hand", "Tool Proficiencies: Disguise kit, Forgery kit"],
    "Criminal": ["Criminal Contact", "Skill Proficiencies: Deception, Stealth", "Tool Proficiencies: One type of gaming set, Thieves' tools"],
    "Entertainer": ["By Popular Demand", "Skill Proficiencies: Acrobatics, Performance", "Tool Proficiencies: Disguise kit, one type of musical instrument"],
    "Guild Artisan": ["Guild Membership", "Skill Proficiencies: Insight, Persuasion", "Tool Proficiencies: One type of artisan's tools"],
    "Hermit": ["Discovery", "Skill Proficiencies: Medicine, Religion", "Tool Proficiencies: Herbalism kit"],
    "Noble": ["Position of Privilege", "Skill Proficiencies: History, Persuasion", "Languages: One of your choice"],
    "Outlander": ["Wanderer", "Skill Proficiencies: Athletics, Survival", "Tool Proficiencies: One type of musical instrument"],
    "Researcher": ["Library Access", "Skill Proficiencies: Arcana, History", "Languages: Two of your choice"],
    "Sailor": ["Ship's Passage", "Skill Proficiencies: Athletics, Perception", "Tool Proficiencies: Navigator's tools, Vehicles (water)"],
    "Soldier": ["Military Rank", "Skill Proficiencies: Athletics, Intimidation", "Tool Proficiencies: One type of gaming set, Vehicles (land)"],
    "Urchin": ["City Secrets", "Skill Proficiencies: Sleight of Hand, Stealth", "Tool Proficiencies: Disguise kit, Thieves' tools"]
}

# Define class abilities and options
class_options = {
    "Barbarian": {"Hit Dice": "1d12 per Barbarian level", "Primary Ability": "Strength", "Saves": ["Strength", "Constitution"]},
    "Bard": {"Hit Dice": "1d8 per Bard level", "Primary Ability": "Charisma", "Saves": ["Dexterity", "Charisma"]},
    "Cleric": {"Hit Dice": "1d8 per Cleric level", "Primary Ability": "Wisdom", "Saves": ["Wisdom", "Charisma"]},
    "Druid": {"Hit Dice": "1d8 per Druid level", "Primary Ability": "Wisdom", "Saves": ["Intelligence", "Wisdom"]},
    "Fighter": {"Hit Dice": "1d10 per Fighter level", "Primary Ability": "Strength or Dexterity", "Saves": ["Strength", "Constitution"]},
    "Monk": {"Hit Dice": "1d8 per Monk level", "Primary Ability": "Dexterity and Wisdom", "Saves": ["Strength", "Dexterity"]},
    "Paladin": {"Hit Dice": "1d10 per Paladin level", "Primary Ability": "Strength and Charisma", "Saves": ["Wisdom", "Charisma"]},
    "Ranger": {"Hit Dice": "1d10 per Ranger level", "Primary Ability": "Dexterity and Wisdom", "Saves": ["Strength", "Dexterity"]},
    "Rogue": {"Hit Dice": "1d8 per Rogue level", "Primary Ability": "Dexterity", "Saves": ["Dexterity", "Intelligence"]},
    "Sorcerer": {"Hit Dice": "1d6 per Sorcerer level", "Primary Ability": "Charisma", "Saves": ["Constitution", "Charisma"]},
    "Warlock": {"Hit Dice": "1d8 per Warlock level", "Primary Ability": "Charisma", "Saves": ["Wisdom", "Charisma"]},
    "Wizard": {"Hit Dice": "1d6 per Wizard level", "Primary Ability": "Intelligence", "Saves": ["Intelligence", "Wisdom"]}
}


# Define spells for each class
class_spells = {
    "Bard": ["Vicious Mockery", "Cure Wounds", "Charm Person"],
    "Cleric": ["Sacred Flame", "Healing Word", "Bless"],
    "Druid": ["Thorn Whip", "Goodberry", "Entangle"],
    "Paladin": ["Divine Favor", "Cure Wounds", "Shield of Faith"],
    "Ranger": ["Hunter's Mark", "Cure Wounds", "Hail of Thorns"],
    "Sorcerer": ["Fire Bolt", "Magic Missile", "Shield"],
    "Warlock": ["Eldritch Blast", "Hex", "Armor of Agathys"],
    "Wizard": ["Mage Hand", "Magic Missile", "Shield"]
}

# Define starting equipment for each class
class_equipment = {
    "Barbarian": ["Greataxe", "Two Handaxes", "Explorer's Pack", "Javelins (4)"],
    "Bard": ["Rapier", "Diplomat's Pack", "Lute", "Leather Armor", "Dagger"],
    "Cleric": ["Mace", "Scale Mail", "Light Crossbow and 20 bolts", "Priest's Pack", "Shield", "Holy Symbol"],
    "Druid": ["Wooden Shield", "Scimitar", "Leather Armor", "Explorer's Pack", "Druidic Focus"],
    "Fighter": ["Chain Mail", "Longsword and Shield", "Light Crossbow and 20 bolts", "Dungeoneer's Pack"],
    "Monk": ["Shortsword", "Dungeoneer's Pack", "10 darts"],
    "Paladin": ["Chain Mail", "Longsword and Shield", "Priest's Pack", "Javelins (5)", "Holy Symbol"],
    "Ranger": ["Scale Mail", "Two Shortswords", "Dungeoneer's Pack", "Longbow and 20 arrows"],
    "Rogue": ["Rapier", "Shortbow and 20 arrows", "Burglar's Pack", "Leather Armor", "Two Daggers", "Thieves' Tools"],
    "Sorcerer": ["Light Crossbow and 20 bolts", "Component Pouch", "Dungeoneer's Pack", "Two Daggers"],
    "Warlock": ["Light Crossbow and 20 bolts", "Component Pouch", "Scholar's Pack", "Leather Armor", "Simple Weapon", "Two Daggers"],
    "Wizard": ["Quarterstaff", "Component Pouch", "Scholar's Pack", "Spellbook"]
}

# Define feats
feats = {
    "Alert": "Always on the lookout for danger, gain +5 to initiative, can't be surprised while conscious, other creatures don’t gain advantage on attack rolls against you as a result of being hidden",
    "Athlete": "You have undergone extensive physical training, gain +1 to Strength or Dexterity, when prone you can stand up using only 5 feet of movement",
    "Actor": "Skilled at mimicry and dramatics, gain +1 to Charisma, advantage on Charisma (Deception) and Charisma (Performance) checks to impersonate someone else",
    "Charger": "When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to shove a creature",
    "Crossbow Expert": "Ignore the loading quality of crossbows, being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls",
    "Defensive Duelist": "When you are wielding a finesse weapon, you can use your reaction to add your proficiency bonus to your AC against one melee attack that would hit you",
    "Dual Wielder": "You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand, can use two-weapon fighting even when the one-handed melee weapons you are wielding aren’t light",
    "Dungeon Delver": "Alert to the hidden traps and secret doors found in many dungeons, gain advantage on Wisdom (Perception) and Intelligence (Investigation) checks to detect the presence of secret doors",
    "Durable": "Hardy and resilient, gain +1 to Constitution, when you roll a Hit Die to regain hit points, the minimum number of hit points you regain equals twice your Constitution modifier",
    "Elemental Adept": "When you gain this feat, choose one of the following damage types: acid, cold, fire, lightning, or thunder. Spells you cast ignore resistance to damage of the chosen type, treat any 1 on a damage die as a 2",
    "Grappler": "You’ve developed the skills necessary to hold your own in close-quarters grappling, gain advantage on attack rolls against a creature you are grappling, you can use your action to try to pin a creature grappled by you",
    "Great Weapon Master": "On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points, you can make one melee weapon attack as a bonus action",
    "Healer": "You are an able physician, allowing you to mend wounds quickly and get your allies back in the fight, when you use a healer’s kit to stabilize a dying creature, that creature also regains 1 hit point",
    "Heavily Armored": "Gain proficiency with heavy armor, gain +1 to Strength",
    "Heavy Armor Master": "You can use your armor to deflect strikes that would kill others, gain +1 to Strength, while you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical weapons is reduced by 3",
    "Inspiring Leader": "You can spend 10 minutes inspiring your companions, choose up to six friendly creatures who can see or hear you and who can understand you, each creature gains temporary hit points equal to your level + your Charisma modifier",
    "Keen Mind": "You have a mind that can track time, direction, and detail with uncanny precision, gain +1 to Intelligence, always know which way is north, always know the number of hours left before the next sunrise or sunset",
    "Lightly Armored": "Gain proficiency with light armor, gain +1 to Strength or Dexterity",
    "Linguist": "You have studied languages and codes, gaining the following benefits, gain +1 to Intelligence, learn three languages of your choice",
    "Lucky": "You have inexplicable luck that seems to kick in at just the right moment, you have 3 luck points, whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20",
    "Mage Slayer": "When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature",
    "Magic Initiate": "Choose a class: bard, cleric, druid, sorcerer, warlock, or wizard, you learn two cantrips of your choice from that class’s spell list",
    "Martial Adept": "You have martial training that allows you to perform special combat maneuvers, gain 1 superiority die (d6), choose two maneuvers from among those available to the Battle Master archetype in the fighter class",
    "Medium Armor Master": "You have practiced moving in medium armor to gain the following benefits, wearing medium armor doesn’t impose disadvantage on your Dexterity (Stealth) checks",
    "Mobile": "You are exceptionally speedy and agile, gain +10 feet to your speed, when you use the Dash action, difficult terrain doesn’t cost you extra movement on that turn",
    "Moderately Armored": "Gain proficiency with medium armor and shields, gain +1 to Strength or Dexterity",
    "Mounted Combatant": "You are a dangerous foe to face while mounted, while you are mounted and aren’t incapacitated, you have advantage on melee attack rolls against unmounted creatures that are smaller than your mount",
    "Observant": "Quick to notice details of your environment, gain +1 to Intelligence or Wisdom, if you can see a creature’s mouth while it is speaking a language you understand, you can interpret what it’s saying by reading its lips",
    "Polearm Master": "When you take the Attack action and attack with only a glaive, halberd, or quarterstaff, you can use a bonus action to make a melee attack with the opposite end of the weapon",
    "Resilient": "Choose one ability score, gain +1 to that score, you gain proficiency in saving throws using the chosen ability",
    "Ritual Caster": "If you have an Intelligence or Wisdom of 13 or higher, you have learned a number of spells that you can cast as rituals",
    "Savage Attacker": "Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon’s damage dice and use either total",
    "Sentinel": "You have mastered techniques to take advantage of every drop in any enemy’s guard, when you hit a creature with an opportunity attack, the creature’s speed becomes 0 for the rest of the turn",
    "Sharpshooter": "Attacking at long range doesn’t impose disadvantage on your ranged weapon attack rolls, your ranged weapon attacks ignore half cover and three-quarters cover",
    "Shield Master": "You use shields not just for protection but also for offense, if you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield",
    "Skilled": "You gain proficiency in any combination of three skills or tools of your choice",
    "Skulker": "You are expert at slinking through shadows, gain the following benefits, you can try to hide when you are lightly obscured from the creature from which you are hiding",
    "Spell Sniper": "When you cast a spell that requires you to make an attack roll, the spell’s range is doubled, your ranged spell attacks ignore half cover and three-quarters cover",
    "Tavern Brawler": "Accustomed to rough-and-tumble fighting using whatever weapons happen to be at hand, gain the following benefits, gain +1 to Strength or Constitution, you are proficient with improvised weapons",
    "Tough": "Your hit point maximum increases by an amount equal to twice your level when you gain this feat",
    "War Caster": "You have practiced casting spells in the midst of combat, gaining the following benefits, you have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage",
    "Weapon Master": "You have practiced extensively with a variety of weapons, gaining the following benefits, gain +1 to Strength or Dexterity, you gain proficiency with four weapons of your choice"
}



# Array to store class level, proficiency bonus, ability checks, and features
XP_table_classes = {
    "Barbarian": [
        {"class_level": 1,  "proficiency_bonus": 2, "features": ["Rage", "Unarmored Defense"], "rages": 2, "rage_damage": 2},
        {"class_level": 2,  "proficiency_bonus": 2, "features": ["Reckless Attack", "Danger Sense"], "rages": 2, "rage_damage": 2},
        {"class_level": 3,  "proficiency_bonus": 2, "features": ["Primal Path"], "rages": 1, "rage_damage": 2},
        {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"], "rages": 1, "rage_damage": 2},
        {"class_level": 5,  "proficiency_bonus": 3, "features": ["Extra Attack", "Fast Movement"], "rages": 1, "rage_damage": 2},
        {"class_level": 6,  "proficiency_bonus": 3, "features": ["Path Feature"], "rages": 1, "rage_damage": 2},
        {"class_level": 7,  "proficiency_bonus": 3, "features": ["Feral Instinct"], "rages": 1, "rage_damage": 2},
        {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"], "rages": 1, "rage_damage": 2},
        {"class_level": 9,  "proficiency_bonus": 4, "features": ["Brutal Critical (1 Die)"], "rages": 1, "rage_damage": 3},
        {"class_level": 10, "proficiency_bonus": 4, "features": ["Path Feature"], "rages": 1, "rage_damage": 3},
        {"class_level": 11, "proficiency_bonus": 4, "features": ["Relentless Rage"], "rages": 1, "rage_damage": 3},
        {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "rages": 1, "rage_damage": 3},
        {"class_level": 13, "proficiency_bonus": 5, "features": ["Brutal Critical (2 Dice)"], "rages": 1, "rage_damage": 3},
        {"class_level": 14, "proficiency_bonus": 5, "features": ["Path Feature"], "rages": 1, "rage_damage": 3},
        {"class_level": 15, "proficiency_bonus": 5, "features": ["Persistent Rage"], "rages": 1, "rage_damage": 3},
        {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "rages": 1, "rage_damage": 4},
        {"class_level": 17, "proficiency_bonus": 6, "features": ["Brutal Critical (3 Dice)"], "rages": 1, "rage_damage": 4},
        {"class_level": 18, "proficiency_bonus": 6, "features": ["Indomitable Might"], "rages": 1, "rage_damage": 4},
        {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "rages": 1, "rage_damage": 4},
        {"class_level": 20, "proficiency_bonus": 6, "features": ["Primal Champion"], "rages": 1, "rage_damage": 4}
    ],
    "Bard": [
        {"class_level": 1,  "proficiency_bonus": 2, "features": ["Spellcasting", "Bardic Inspiration (d6)"]},
        {"class_level": 2,  "proficiency_bonus": 2, "features": ["Jack of All Trades", "Song of Rest (d6)"]},
        {"class_level": 3,  "proficiency_bonus": 2, "features": ["Bard College", "Expertise"]},
        {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"]},
        {"class_level": 5,  "proficiency_bonus": 3, "features": ["Font of Inspiration"]},
        {"class_level": 6,  "proficiency_bonus": 3, "features": ["Countercharm", "Bard College Feature"]},
        {"class_level": 7,  "proficiency_bonus": 3, "features": ["Expertise"]},
        {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"]},
        {"class_level": 9,  "proficiency_bonus": 4, "features": ["Song of Rest (d8)"]},
        {"class_level": 10, "proficiency_bonus": 4, "features": ["Bardic Inspiration (d10)", "Magical Secrets"]},
        {"class_level": 11, "proficiency_bonus": 4, "features": ["Spellcasting"]},
        {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"]},
        {"class_level": 13, "proficiency_bonus": 5, "features": ["Song of Rest (d10)"]},
        {"class_level": 14, "proficiency_bonus": 5, "features": ["Magical Secrets", "Bard College Feature"]},
        {"class_level": 15, "proficiency_bonus": 5, "features": ["Bardic Inspiration (d12)"]},
        {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"]},
        {"class_level": 17, "proficiency_bonus": 6, "features": ["Song of Rest (d12)"]},
        {"class_level": 18, "proficiency_bonus": 6, "features": ["Magical Secrets"]},
        {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"]},
        {"class_level": 20, "proficiency_bonus": 6, "features": ["Superior Inspiration"]}
    ],
    "Cleric": [
    {"class_level": 1,  "proficiency_bonus": 2,  "features": ["Spellcasting", "Divine Domain"],                       "cantrips_known": 3, "spell_slots": {1: 2}},
    {"class_level": 2,  "proficiency_bonus": 2,  "features": ["Channel Divinity (1/rest)", "Divine Domain Feature"],  "cantrips_known": 3, "spell_slots": {1: 3}},
    {"class_level": 3,  "proficiency_bonus": 2,  "features": ["—"],                                                   "cantrips_known": 3, "spell_slots": {1: 4, 2: 2}},
    {"class_level": 4,  "proficiency_bonus": 2,  "features": ["Ability Score Improvement"],                           "cantrips_known": 4, "spell_slots": {1: 4, 2: 3}},
    {"class_level": 5,  "proficiency_bonus": 3,  "features": ["Destroy Undead (CR 1/2)"],                             "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 6,  "proficiency_bonus": 3,  "features": ["Channel Divinity (2/rest)", "Divine Domain Feature"],  "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3}},
    {"class_level": 7,  "proficiency_bonus": 3,  "features": ["—"],                                                   "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 8,  "proficiency_bonus": 3,  "features": ["Ability Score Improvement", "Destroy Undead (CR 1)"],  "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 9,  "proficiency_bonus": 4,  "features": ["—"],                                                   "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 1}},
    {"class_level": 10, "proficiency_bonus": 4,  "features": ["Divine Intervention"],                                 "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2}},
    {"class_level": 11, "proficiency_bonus": 4,  "features": ["Destroy Undead (CR 2)"],                               "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}},
    {"class_level": 12, "proficiency_bonus": 4,  "features": ["Ability Score Improvement"],                           "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}},
    {"class_level": 13, "proficiency_bonus": 5,  "features": ["—"],                                                   "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}},
    {"class_level": 14, "proficiency_bonus": 5,  "features": ["Destroy Undead (CR 3)"],                               "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}},
    {"class_level": 15, "proficiency_bonus": 5,  "features": ["—"],                                                   "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1}},
    {"class_level": 16, "proficiency_bonus": 5,  "features": ["Ability Score Improvement"],                           "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1}},
    {"class_level": 17, "proficiency_bonus": 6,  "features": ["Destroy Undead (CR 4)", "Divine Domain Feature"],      "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 18, "proficiency_bonus": 6,  "features": ["Channel Divinity (3/rest)"],                           "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 19, "proficiency_bonus": 6,  "features": ["Ability Score Improvement"],                           "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1}},
    {"class_level": 20, "proficiency_bonus": 6,  "features": ["Divine Intervention Improvement"],                     "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1}}
    ],
    "Fighter": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Fighting Style", "Second Wind"]},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Action Surge (one use)"]},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["Martial Archetype"]},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"]},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["Extra Attack"]},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"]},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["Martial Archetype Feature"]},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"]},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["Indomitable (one use)"]},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Martial Archetype Feature"]},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["Extra Attack (2)"]},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"]},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["Indomitable (two uses)"]},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Ability Score Improvement"]},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["Martial Archetype Feature"]},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"]},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Action Surge (two uses)", "Indomitable (three uses)"]},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["Martial Archetype Feature"]},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"]},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Extra Attack (3)"]}
    ],
    "Monk": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Unarmored Defense", "Martial Arts"], "ki_points": 0,  "martial_arts_die": "1d4", "unarmored_movement_bonus": 0},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Ki", "Unarmored Movement"], "ki_points": 2,  "martial_arts_die": "1d4", "unarmored_movement_bonus": 10},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["Monastic Tradition", "Deflect Missiles"], "ki_points": 3,  "martial_arts_die": "1d4", "unarmored_movement_bonus": 10},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement", "Slow Fall"], "ki_points": 4,  "martial_arts_die": "1d4", "unarmored_movement_bonus": 10},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["Extra Attack", "Stunning Strike"], "ki_points": 5,  "martial_arts_die": "1d6", "unarmored_movement_bonus": 10},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Ki-Empowered Strikes", "Monastic Tradition Feature"], "ki_points": 6,  "martial_arts_die": "1d6", "unarmored_movement_bonus": 15},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["Evasion", "Stillness of Mind"], "ki_points": 7,  "martial_arts_die": "1d6", "unarmored_movement_bonus": 15},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"], "ki_points": 8,  "martial_arts_die": "1d6", "unarmored_movement_bonus": 15},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["Unarmored Movement Improvement"], "ki_points": 9,  "martial_arts_die": "1d6", "unarmored_movement_bonus": 15},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Purity of Body"], "ki_points": 10, "martial_arts_die": "1d6", "unarmored_movement_bonus": 20},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["Monastic Tradition Feature"], "ki_points": 11, "martial_arts_die": "1d8", "unarmored_movement_bonus": 20},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "ki_points": 12, "martial_arts_die": "1d8", "unarmored_movement_bonus": 20},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["Tongue of the Sun and Moon"], "ki_points": 13, "martial_arts_die": "1d8", "unarmored_movement_bonus": 20},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Diamond Soul"], "ki_points": 14, "martial_arts_die": "1d8", "unarmored_movement_bonus": 25},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["Timeless Body"], "ki_points": 15, "martial_arts_die": "1d8", "unarmored_movement_bonus": 25},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "ki_points": 16, "martial_arts_die": "1d8", "unarmored_movement_bonus": 25},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Monastic Tradition Feature"], "ki_points": 17, "martial_arts_die": "1d10", "unarmored_movement_bonus": 25},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["Empty Body"], "ki_points": 18, "martial_arts_die": "1d10", "unarmored_movement_bonus": 30},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "ki_points": 19, "martial_arts_die": "1d10", "unarmored_movement_bonus": 30},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Perfect Self"], "ki_points": 20, "martial_arts_die": "1d10", "unarmored_movement_bonus": 30}
    ],
    "Paladin": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Divine Sense", "Lay on Hands"], "spell_slots": {}},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Fighting Style", "Spellcasting", "Divine Smite"], "spell_slots": {1: 2}},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["Divine Health", "Sacred Oath"], "spell_slots": {1: 3}},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"], "spell_slots": {1: 3}},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["Extra Attack"], "spell_slots": {1: 4, 2: 2}},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Aura of Protection"], "spell_slots": {1: 4, 2: 2}},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["Sacred Oath Feature"], "spell_slots": {1: 4, 2: 3}},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3}},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["Aura of Vitality"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Aura of Courage"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["Improved Divine Smite"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["—"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Cleansing Touch"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["Sacred Oath Feature"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Aura improvements (30 ft)"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["—"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Sacred Oath Feature"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}}
    ],
    "Ranger": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Favored Enemy", "Natural Explorer"], "spell_slots": {}},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Fighting Style", "Spellcasting"], "spell_slots": {1: 2}},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["Ranger Archetype", "Primeval Awareness"], "spell_slots": {1: 3}},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"], "spell_slots": {1: 3}},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["Extra Attack"], "spell_slots": {1: 4, 2: 2}},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Favored Enemy Improvement", "Natural Explorer Improvement"], "spell_slots": {1: 4, 2: 2}},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["Ranger Archetype Feature"], "spell_slots": {1: 4, 2: 3}},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement", "Land’s Stride"], "spell_slots": {1: 4, 2: 3}},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["Natural Explorer Improvement"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Hide in Plain Sight"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["Ranger Archetype Feature"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["Favored Enemy Improvement"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Vanish"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["Ranger Archetype Feature"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Natural Explorer Improvement"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["Feral Senses"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Foe Slayer"], "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3}}
    ],
    "Sorcerer": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Spellcasting", "Sorcerous Origin"], "cantrips_known": 4, "sorcery_points": 0,  "spell_slots": {1: 2}},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Font of Magic"], "cantrips_known": 4, "sorcery_points": 2,  "spell_slots": {1: 3}},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["Metamagic"], "cantrips_known": 4, "sorcery_points": 3,  "spell_slots": {1: 4, 2: 2}},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"], "cantrips_known": 5, "sorcery_points": 4,  "spell_slots": {1: 4, 2: 3}},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["—"], "cantrips_known": 5, "sorcery_points": 5,  "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Sorcerous Origin Feature"], "cantrips_known": 5, "sorcery_points": 6,  "spell_slots": {1: 4, 2: 3, 3: 3}},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["—"], "cantrips_known": 5, "sorcery_points": 7,  "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"], "cantrips_known": 5, "sorcery_points": 8,  "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["—"], "cantrips_known": 5, "sorcery_points": 9,  "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 1}},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Metamagic"], "cantrips_known": 6, "sorcery_points": 10, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2}},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["—"], "cantrips_known": 6, "sorcery_points": 11, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "cantrips_known": 6, "sorcery_points": 12, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["—"], "cantrips_known": 6, "sorcery_points": 13, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Sorcerous Origin Feature"], "cantrips_known": 6, "sorcery_points": 14, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["—"], "cantrips_known": 6, "sorcery_points": 15, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1}},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "cantrips_known": 6, "sorcery_points": 16, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1}},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Metamagic"], "cantrips_known": 6, "sorcery_points": 17, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["Sorcerous Origin Feature"], "cantrips_known": 6, "sorcery_points": 18, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "cantrips_known": 6, "sorcery_points": 19, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1}},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Sorcerous Restoration"], "cantrips_known": 6, "sorcery_points": 20, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1}}
    ],
    "Warlock": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Otherworldly Patron", "Pact Magic"], "cantrips_known": 2, "invocations_known": 0, "pact_slots": 1, "slot_level": 1, "mystic_arcanum": {}},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Eldritch Invocations"], "cantrips_known": 2, "invocations_known": 2, "pact_slots": 2, "slot_level": 1, "mystic_arcanum": {}},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["Pact Boon"], "cantrips_known": 2, "invocations_known": 2, "pact_slots": 2, "slot_level": 2, "mystic_arcanum": {}},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"], "cantrips_known": 3, "invocations_known": 2, "pact_slots": 2, "slot_level": 2, "mystic_arcanum": {}},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["—"], "cantrips_known": 3, "invocations_known": 3, "pact_slots": 2, "slot_level": 3, "mystic_arcanum": {}},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Otherworldly Patron Feature"], "cantrips_known": 3, "invocations_known": 3, "pact_slots": 2, "slot_level": 3, "mystic_arcanum": {6: 1}},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["—"], "cantrips_known": 3, "invocations_known": 4, "pact_slots": 2, "slot_level": 4, "mystic_arcanum": {6: 1}},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"], "cantrips_known": 3, "invocations_known": 4, "pact_slots": 2, "slot_level": 4, "mystic_arcanum": {6: 1}},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["—"], "cantrips_known": 3, "invocations_known": 5, "pact_slots": 2, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1}},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Otherworldly Patron Feature"], "cantrips_known": 4, "invocations_known": 5, "pact_slots": 2, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1}},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["Mystic Arcanum (6th Level)"], "cantrips_known": 4, "invocations_known": 5, "pact_slots": 3, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1}},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "cantrips_known": 4, "invocations_known": 6, "pact_slots": 3, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1}},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["Mystic Arcanum (7th Level)"], "cantrips_known": 4, "invocations_known": 6, "pact_slots": 3, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Otherworldly Patron Feature"], "cantrips_known": 4, "invocations_known": 6, "pact_slots": 3, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["Mystic Arcanum (8th Level)"], "cantrips_known": 4, "invocations_known": 7, "pact_slots": 3, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "cantrips_known": 4, "invocations_known": 7, "pact_slots": 3, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Mystic Arcanum (9th Level)"], "cantrips_known": 4, "invocations_known": 7, "pact_slots": 4, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["—"], "cantrips_known": 4, "invocations_known": 8, "pact_slots": 4, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "cantrips_known": 4, "invocations_known": 8, "pact_slots": 4, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Eldritch Master"], "cantrips_known": 4, "invocations_known": 8, "pact_slots": 4, "slot_level": 5, "mystic_arcanum": {6: 1, 7: 1, 8: 1, 9: 1}}
    ],
    "Wizard": [
    {"class_level": 1,  "proficiency_bonus": 2, "features": ["Spellcasting", "Arcane Recovery"], "cantrips_known": 3, "spell_slots": {1: 2}},
    {"class_level": 2,  "proficiency_bonus": 2, "features": ["Arcane Tradition"], "cantrips_known": 3, "spell_slots": {1: 3}},
    {"class_level": 3,  "proficiency_bonus": 2, "features": ["—"], "cantrips_known": 3, "spell_slots": {1: 4, 2: 2}},
    {"class_level": 4,  "proficiency_bonus": 2, "features": ["Ability Score Improvement"], "cantrips_known": 4, "spell_slots": {1: 4, 2: 3}},
    {"class_level": 5,  "proficiency_bonus": 3, "features": ["—"], "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 2}},
    {"class_level": 6,  "proficiency_bonus": 3, "features": ["Arcane Tradition Feature"], "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3}},
    {"class_level": 7,  "proficiency_bonus": 3, "features": ["—"], "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 1}},
    {"class_level": 8,  "proficiency_bonus": 3, "features": ["Ability Score Improvement"], "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 2}},
    {"class_level": 9,  "proficiency_bonus": 4, "features": ["—"], "cantrips_known": 4, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 1}},
    {"class_level": 10, "proficiency_bonus": 4, "features": ["Arcane Tradition Feature"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2}},
    {"class_level": 11, "proficiency_bonus": 4, "features": ["—"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}},
    {"class_level": 12, "proficiency_bonus": 4, "features": ["Ability Score Improvement"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1}},
    {"class_level": 13, "proficiency_bonus": 5, "features": ["—"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}},
    {"class_level": 14, "proficiency_bonus": 5, "features": ["Arcane Tradition Feature"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1}},
    {"class_level": 15, "proficiency_bonus": 5, "features": ["—"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1}},
    {"class_level": 16, "proficiency_bonus": 5, "features": ["Ability Score Improvement"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1}},
    {"class_level": 17, "proficiency_bonus": 6, "features": ["Spell Mastery"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 18, "proficiency_bonus": 6, "features": ["—"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1}},
    {"class_level": 19, "proficiency_bonus": 6, "features": ["Ability Score Improvement"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1}},
    {"class_level": 20, "proficiency_bonus": 6, "features": ["Signature Spells"], "cantrips_known": 5, "spell_slots": {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1}}
    ]



    # Add templates for other classes like Cleric, Druid, Fighter, etc.
}

Class_Proficiencies = {
    "Barbarian": {
        "armor": ["Light Armor", "Medium Armor", "Shields"],
        "weapons": ["Simple Weapons", "Martial Weapons"],
        "tools": [],
        "saving_throws": ["Strength", "Constitution"],
        "skills": {
            "choose": 2,
            "options": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
        }
    },
    "Bard": {
        "armor": ["Light Armor"],
        "weapons": ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"],
        "tools": ["Three Musical Instruments of your choice"],
        "saving_throws": ["Dexterity", "Charisma"],
        "skills": {
            "choose": 3,
            "options": "Any"
        }
    },
    "Cleric": {
        "armor": ["Light Armor", "Medium Armor", "Shields"],
        "weapons": ["Simple Weapons"],
        "tools": [],
        "saving_throws": ["Wisdom", "Charisma"],
        "skills": {
            "choose": 2,
            "options": ["History", "Insight", "Medicine", "Persuasion", "Religion"]
        }
    },
    "Druid": {
        "armor": ["Light Armor", "Medium Armor", "Shields (non-metal)"],
        "weapons": ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
        "tools": ["Herbalism Kit"],
        "saving_throws": ["Intelligence", "Wisdom"],
        "skills": {
            "choose": 2,
            "options": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
        }
    },
    "Fighter": {
        "armor": ["All Armor", "Shields"],
        "weapons": ["Simple Weapons", "Martial Weapons"],
        "tools": [],
        "saving_throws": ["Strength", "Constitution"],
        "skills": {
            "choose": 2,
            "options": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
        }
    },
    "Monk": {
        "armor": [],
        "weapons": ["Simple Weapons", "Shortswords"],
        "tools": ["Choose one type of artisan’s tools or one musical instrument"],
        "saving_throws": ["Strength", "Dexterity"],
        "skills": {
            "choose": 2,
            "options": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
        }
    },
    "Paladin": {
        "armor": ["All Armor", "Shields"],
        "weapons": ["Simple Weapons", "Martial Weapons"],
        "tools": [],
        "saving_throws": ["Wisdom", "Charisma"],
        "skills": {
            "choose": 2,
            "options": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]
        }
    },
    "Ranger": {
        "armor": ["Light Armor", "Medium Armor", "Shields"],
        "weapons": ["Simple Weapons", "Martial Weapons"],
        "tools": [],
        "saving_throws": ["Strength", "Dexterity"],
        "skills": {
            "choose": 3,
            "options": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
        }
    },
    "Rogue": {
        "armor": ["Light Armor"],
        "weapons": ["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"],
        "tools": ["Thieves’ Tools"],
        "saving_throws": ["Dexterity", "Intelligence"],
        "skills": {
            "choose": 4,
            "options": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
        }
    },
    "Sorcerer": {
        "armor": [],
        "weapons": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"],
        "tools": [],
        "saving_throws": ["Constitution", "Charisma"],
        "skills": {
            "choose": 2,
            "options": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
        }
    },
    "Warlock": {
        "armor": ["Light Armor"],
        "weapons": ["Simple Weapons"],
        "tools": [],
        "saving_throws": ["Wisdom", "Charisma"],
        "skills": {
            "choose": 2,
            "options": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
        }
    },
    "Wizard": {
        "armor": [],
        "weapons": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"],
        "tools": [],
        "saving_throws": ["Intelligence", "Wisdom"],
        "skills": {
            "choose": 2,
            "options": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
        }
    }
}














# Define character creation function
def create_character():
    # Basic character information
    print("Create your character")
    name = input("Name: ")
    race = input("Choose a race (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling): ")
    char_class = input("Choose a class (Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard): ")
    background = input("Choose a background (Acolyte, Charlatan, Criminal, Entertainer, Folk Hero, Guild Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin): ")

    # Display race and class options
    print(f"\nRace Abilities for {race}:")
    for ability in race_abilities[race]:
        print(f"- {ability}")
    
    print(f"\nClass Abilities for {char_class}:")
    for key, value in class_options[char_class].items():
        print(f"{key}: {value}")

    # Choose spells if applicable
    if char_class in class_spells:
        print(f"\nSpells for {char_class}:")
        for spell in class_spells[char_class]:
            print(f"- {spell}")

    # Choose equipment
    print(f"\nStarting Equipment for {char_class}:")
    for item in class_equipment[char_class]:
        print(f"- {item}")

    # Choose feats
    print("\nAvailable Feats:")
    for feat, description in feats.items():
        print(f"{feat}: {description}")

    chosen_feats = input("\nChoose your feats (comma separated): ").split(", ")

    # Display chosen feats
    print("\nChosen Feats:")
    for feat in chosen_feats:
        if feat in feats:
            print(f"{feat}: {feats[feat]}")

    # Final character summary
    print("\nCharacter Summary:")
    print(f"Name: {name}")
    print(f"Race: {race}")
    print(f"Class: {char_class}")
    print(f"Background: {background}")
    print("Feats:")
    for feat in chosen_feats:
        if feat in feats:
            print(f"- {feat}")



# Complete the character creation process
def create_character():
    # Basic character information
    print("Create your character")
    name = input("Name: ")
    race = input("Choose a race (Dwarf, Elf, Halfling, Human, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling): ")
    char_class = input("Choose a class (Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard): ")
    background = input("Choose a background (Acolyte, Charlatan, Criminal, Entertainer, Folk Hero, Guild Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin): ")

    # Roll and assign ability scores
    print("\nRolling ability scores...")
    rolled_scores = roll_ability_scores()
    print(f"Rolled Scores: {rolled_scores}")
    assigned_scores = assign_ability_scores(ability_scores, rolled_scores)
    
    # Display race and class options
    print(f"\nRace Abilities for {race}:")
    for ability in race_abilities[race]:
        print(f"- {ability}")
    
    print(f"\nClass Abilities for {char_class}:")
    for key, value in class_options[char_class].items():
        print(f"{key}: {value}")

    # Choose spells if applicable
    if char_class in class_spells:
        print(f"\nChoose spells for {char_class}:")
        spells = class_spells[char_class]
        chosen_spells = []
        for i in range(3):  # Assuming the character can choose 3 spells
            spell = input(f"Choose spell {i + 1} from {spells}: ")
            while spell not in spells:
                print("Invalid choice. Please choose a valid spell.")
                spell = input(f"Choose spell {i + 1} from {spells}: ")
            chosen_spells.append(spell)

    # Display character summary
    print("\nCharacter Summary:")
    print(f"Name: {name}")
    print(f"Race: {race}")
    print(f"Class: {char_class}")
    print(f"Background: {background}")
    print("\nAbility Scores:")
    for ability, score in assigned_scores.items():
        print(f"{ability}: {score}")
    
    print("\nSkills:")
    for ability, score in assigned_scores.items():
        if skills[ability]:
            print(f"{ability} skills:")
            for skill in skills[ability]:
                print(f"- {skill}")

    if char_class in class_spells:
        print("\nSpells:")
        for spell in chosen_spells:
            print(f"- {spell}")

# Create a character
create_character()