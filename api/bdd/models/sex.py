from enum import Enum, auto


class Sex(Enum):
    MAN = auto()
    WOMAN = auto()

if __name__ == "__main__":
    print(Sex.MAN.value)
