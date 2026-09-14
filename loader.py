from dataclasses import dataclass


@dataclass
class Loader:
    azvnk: int = 974
    pmspixm: int = 137

    def total(self):
        return self.azvnk + self.pmspixm


if __name__ == "__main__":
    x = Loader()
    print(x.total())
