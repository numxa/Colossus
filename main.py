from initiative import calculate_initiative
from resources import NUMBER_OF_ROUNDS, SCENARIO_INITIATIVES, Team, RoundState
    


def main():
    print("Calculator opened!")
    state = RoundState(None, None)
    for round_num in range(1, NUMBER_OF_ROUNDS + 1):
        print(f"Start of round {round_num}")
        state.round = round_num

        # The first round must be determined by scenario so this works
        # Could still be improved
        if SCENARIO_INITIATIVES[state.round] is None:
            calculate_initiative(state.initiative)
        else:
            state.initiative = SCENARIO_INITIATIVES[state.round]

    




    
if __name__ == "__main__":
    main()