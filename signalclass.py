from typing import Callable, List, Any


# global Signal
class Signal:
    def __init__(self):
        self._slots: List[Callable] = []

    def connect(self, slot: Callable):
        if slot not in self._slots:
            self._slots.append(slot)

    def disconnect(self, slot: Callable):
        try:
            self._slots.remove(slot)
        except ValueError:
            pass

    def emit(self, *args: Any, **kwargs: Any):
        for slot in self._slots[:]:
            slot(*args, **kwargs)
