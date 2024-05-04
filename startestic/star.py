

from typing import Any


class Star:
    database = None

    def __init__(self, id: int, x: int, y: int) -> None:
        assert x >= 0 and x <= 50000
        assert y >= 0 and y <= 50000

        self.id = id
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return self.id

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y
        }
    
    def distance(self, other: Any) -> float:
        assert isinstance(other, Star)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def update(self, x: int, y: int) -> None:
        self.update_x(x)
        self.update_y(y)

    def update_x(self, x: int) -> None:
        assert x >= 0 and x <= 50000
        self.x = x
        self.database.update_star(self)
    
    def update_y(self, y: int) -> None:
        assert y >= 0 and y <= 50000
        self.y = y
        self.database.update_star(self)
