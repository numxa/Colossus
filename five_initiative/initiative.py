"""
Case 1:
If neither side had initiative last round, the team that got more VPs
last round gets the initiative. Tie causes another contested round.

Case 2:
If one side had initiative on previous round, the team has to get more
than scenario determined amount of VPs. If neither or both get required
amount, the round is played as contested.
"""

from resources import InitiativeStatus, REQUIRED_VP_FOR_INITIATIVE

def calculate_initiative(prev_initiative, vp_blue, vp_red):
    if prev_initiative is None:
        raise ValueError("Previous round initiative was None!")

    # Case 1:
    if prev_initiative == InitiativeStatus.CONTESTED:
        if vp_blue > vp_red:
            return InitiativeStatus.BLUE
        elif vp_red > vp_blue:
            return InitiativeStatus.RED
        else:
            return InitiativeStatus.CONTESTED

    # Case 2:
    blue_met = vp_blue >= REQUIRED_VP_FOR_INITIATIVE
    red_met = vp_red >= REQUIRED_VP_FOR_INITIATIVE

    if blue_met and red_met:
        return InitiativeStatus.CONTESTED
    if not blue_met and not red_met:
        return InitiativeStatus.CONTESTED
    if blue_met:
        return InitiativeStatus.BLUE
    return InitiativeStatus.RED

