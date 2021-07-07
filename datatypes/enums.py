import enum


class WeeklyStatus(enum.Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class EntryStatus(enum.Enum):
    REGISTERED = 'REGISTERED'
    TIME_SUBMITTED = 'TIME_SUBMITTED'
    DONE = 'DONE'
    DNF = 'DNF'


class Games(enum.Enum):
    ALTTPR = (
        "A Link to the Past Randomizer",
        ["alttp", "alttpr"],
        0x188020,
    )
    OOTR = (
        "Ocarina of Time Randomizer",
        ["oot", "ootr", "ocarina"],
        0x5F1412,
    )
    MMR = (
        "Majora's Mask Randomizer",
        ["mm", "mmr", "majora", "majoras", "majora's"],
        0xae27cf,
    )
    PKMN_CRYSTAL = (
        "Pokemon Crystal Full Item Randomizer",
        ["pkmn", "pokemon", "pkm", "poke", "pokémon"],
        0xFFCB06,
    )
    SMR = (
        "Super Metroid Randomizer",
        ["sm", "smr", "metroid3", "m3", "m3r"],
        0x127C6A,
    )

    def __init__(self, str, keys, color):
        self.str = str
        self.keys = keys
        self.color = color

    def __str__(self):
        return self.str
