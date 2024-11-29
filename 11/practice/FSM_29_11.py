from enum import Enum, auto

class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()

class Trigger(Enum):
    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNECTED = auto()
    PLACE_ON_HOLD = auto()
    TAKE_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()

rules = {
    State.OFF_HOOK: [
        (Trigger.CALL_DIALED, State.CONNECTING),
    ],
    State.CONNECTING: [
        (Trigger.HUNG_UP, State.ON_HOOK),
        (Trigger.CALL_CONNECTED, State.CONNECTED),
    ],
    State.CONNECTED: [
        (Trigger.TAKE_OFF_HOLD, State.ON_HOOK),
        (Trigger.LEFT_MESSAGE, State.ON_HOOK),
        (Trigger.PLACE_ON_HOLD, State.ON_HOLD),
    ],
    State.ON_HOLD: [
        (Trigger.HUNG_UP, State.ON_HOOK),
        (Trigger.TAKE_OFF_HOLD, State.CONNECTED),
    ],
}

state = State.OFF_HOOK
exit_state = State.ON_HOOK

while state != exit_state:
    print(f"The phone is now in the {state.name} state")

    for i in range(len(rules[state])):
        t = rules[state][i][0]
        print(f"{i}: {t}")

    new_state = int(input("Enter a number: "))
    state = rules[state][new_state][1]

