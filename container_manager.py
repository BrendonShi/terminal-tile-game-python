from container import Container


class ContainerManager:
    def __init__(self):
        self.opened_containers: list[Container] = []
        self.current_index: int = 0

    def get_current_container(self):
        return self.opened_containers[self.current_index]

    def add_container(self, container: Container) -> None:
        if len(self.opened_containers) == 0:
            container.is_focused = True
        self.opened_containers.append(container)

    def get_next_container_index(self):
        new_index = (self.current_index + 1) % len(self.opened_containers)
        return new_index

    def remove_container(self, container: Container) -> None:
        self.opened_containers.remove(container)
        self.current_index = 0

    def change_container(self, index: int) -> None:
        self.get_current_container().is_focused = False
        self.get_current_container().chosen_item = 0
        self.current_index = index
        self.get_current_container().is_focused = True

    def switch_container(self) -> None:
        # self.current_index += 1
        # new_index = (self.current_index + 1) % len(self.opened_containers)
        self.change_container(self.get_next_container_index())

    def display_container(self, container: Container) -> None:
        pass
