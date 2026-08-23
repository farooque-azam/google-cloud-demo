def find_restaurant(location: str, food_type: str) -> str:
    """Finds a restaurant based on location and food type.

    Args:
        location: The city or neighborhood to search in.
        food_type: The type of cuisine.

    Returns:
        A string containing the name of a mock restaurant.
    """
    mock_db = {
        ("downtown", "pizza"): "Luigi's Downtown Pizzeria",
        ("uptown", "sushi"): "Uptown Sushi Bar",
        ("midtown", "tacos"): "Midtown Taco Stand"
    }
    key = (location.lower(), food_type.lower())
    return mock_db.get(key, f"Generic {food_type.capitalize()} Place in {location}")

def get_transit_directions(start_location: str, destination_restaurant: str) -> str:
    """Gets transportation directions to the restaurant.

    Args:
        start_location: The user's starting location.
        destination_restaurant: The name of the destination restaurant.

    Returns:
        A string containing the transit directions.
    """
    return f"Take the Express Line train from {start_location} directly to the station near {destination_restaurant}. Estimated travel time: 20 minutes."
