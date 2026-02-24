class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> None:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return Distance(self.km + value)

    def __iadd__(self, other: int) -> None:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        self.km += value
        return self

    def __mul__(self, other: int) -> None:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> None:
        result = self.km / other
        return Distance(round(result, 2))

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km == value

    def __ne__(self, other: int) -> bool:
        return (self.km != other.km) or (self.km != other.km)

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km < value

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km > value

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km >= value

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            value = other.km
        else:
            value = other
        return self.km <= value
