class Circle:
    # Круг
    DEF_RADIUS = 42

    def __init__(self, x, y, radius=DEF_RADIUS):
        self._x = x
        self._y = y
        self._radius = radius
        self._selected = False

    def is_selected(self):
        return self._selected

    def set_selected(self, value):
        self._selected = value

    def geometry(self):
        return self._x, self._y, self._radius

    def __repr__(self):
        return "Круг - x="+str(self._x)+", y="+str(self._y)+", r="+str(self._radius)+", sel="+str(self._selected)

    def contains_point(self, px, py):
        dx = px - self._x
        dy = py - self._y
        return dx * dx + dy * dy <= self._radius * self._radius

class Container:
    # Контейнер
    def __init__(self):
        self._items = []

    def add(self, circle):
        self._items.append(circle)

    def remove(self, circle):
        if circle in self._items:
            self._items.remove(circle)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def topmost_at(self, px, py):
        # Идём с конца списка: последний добавленный — верхний.
        # Возвращаем 1 круг - верхний.
        for circle in reversed(self._items):
            if circle.contains_point(px, py):
                return circle
        return None

    def all_at(self, px, py):
        # Все круги, накрывающие точку. Порядок — снизу вверх.
        result = []
        for circle in self._items:
            if circle.contains_point(px, py):
                result.append(circle)
        return result

    def selected(self):
        result = []
        for circle in self._items:
            if circle.is_selected():
                result.append(circle)
        return result


