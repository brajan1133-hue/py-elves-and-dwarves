mkdir -p app/players/elves app/players/dwarves

touch app/__init__.py
touch app/players/__init__.py
touch app/players/elves/__init__.py
touch app/players/dwarves/__init__.py

cat > app/players/player.py <<'EOF'
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
EOF

cat > app/players/elves/elf.py <<'EOF'
from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(
            f"{self.nickname} is playing a song on the "
            f"{self._musical_instrument}"
        )
EOF

cat > app/players/elves/elf_ranger.py <<'EOF'
from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self):
        return 3 * self._bow_level

    def player_info(self):
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )
EOF

cat > app/players/elves/druid.py <<'EOF'
from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self):
        return len(self._favourite_spell)

    def player_info(self):
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: "
            f"{self._favourite_spell}"
        )
EOF

cat > app/players/dwarves/dwarf.py <<'EOF'
from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")
EOF

cat > app/players/dwarves/dwarf_warrior.py <<'EOF'
from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname, favourite_dish, hummer_level):
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self):
        return self._hummer_level + 4

    def player_info(self):
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the "
            f"{self._hummer_level} level"
        )
EOF

cat > app/players/dwarves/dwarf_blacksmith.py <<'EOF'
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish, skill_level):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self):
        return self._skill_level

    def player_info(self):
        return (
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self._skill_level} level"
        )
EOF

cat > app/main.py <<'EOF'
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
EOF
