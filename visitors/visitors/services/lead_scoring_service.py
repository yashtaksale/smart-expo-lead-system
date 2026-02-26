def calculate_lead_score(visitor):
    """
    Business logic for scoring leads
    """

    score = 0

    # Category weight
    if visitor.category == "investor":
        score += 5
    elif visitor.category == "business":
        score += 4
    elif visitor.category == "vendor":
        score += 3
    elif visitor.category == "job":
        score += 2
    else:
        score += 1

    # Company presence
    if visitor.company:
        score += 2

    # Email provided
    if visitor.email:
        score += 1

    # Final classification
    if score >= 7:
        return "hot"
    elif score >= 4:
        return "warm"
    else:
        return "cold"