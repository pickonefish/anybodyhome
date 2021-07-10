from component import Component

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self, result):
        self._component.operation(result)