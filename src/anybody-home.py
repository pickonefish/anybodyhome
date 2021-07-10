from component import Component
from concrete import ImHereComponent
from concrete import ImHereAndOutputDateDecorator
from concrete import ImHereAndCheckSmtpAvailableDecorator
from concrete import ImHereAndTelnetAvailableDecorator
from datetime import datetime


def anybodyHome(timestamp, component: Component) -> None:
    result = {
        'timestamp': timestamp
    }
    component.operation(result)

    print(result)

if __name__ == "__main__":
    imhere = ImHereComponent()
    imhere = ImHereAndOutputDateDecorator(imhere)
    imhere = ImHereAndCheckSmtpAvailableDecorator(imhere)
    imhere = ImHereAndTelnetAvailableDecorator(imhere)

    now = datetime.now()

    anybodyHome(now.strftime("%Y-%m-%d %H:%M:%S"), imhere)