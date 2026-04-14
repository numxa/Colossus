from five_initiative.initiative import calculate_initiative
from resources import NUMBER_OF_ROUNDS, SCENARIO_INITIATIVES, InitiativeStatus, RoundState


def round_end(state: RoundState):
    state.prev_vp_blue = state.vp_blue
    state.prev_vp_red = state.vp_red
    state.vp_blue = 0
    state.vp_red = 0
    state.prev_initiative = state.initiative


def main():
    print("Calculator opened!")
    state = RoundState(None, None, None, 0, 0, 0, 0)
    for round_num in range(1, NUMBER_OF_ROUNDS + 1):
        print(f"Start of round {round_num}")
        state.round = round_num

        ########################################################################
        # Initiative
        ########################################################################
        if state.round == 1 and SCENARIO_INITIATIVES.get(1) is None:
            raise ValueError("The initiative must be preset for the first round!")
        if SCENARIO_INITIATIVES[state.round] is None:
            state.initiative = calculate_initiative(state.prev_initiative, state.prev_vp_blue, state.prev_vp_red)
        else:
            state.initiative = SCENARIO_INITIATIVES.get(state.round)

        print(f"Initiative side is: {state.initiative}")


        ########################################################################
        # 
        ########################################################################

        # Last thing of the round, update previous round values with current ones
        # and reset the current round counters

        round_end(state)

    




    
if __name__ == "__main__":
    main()