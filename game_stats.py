import json


class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Get the existing high score.
        self.filename = 'ai_high_score.json'
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """
        Load the existing high score from the json file
        and set it to the game's high score.
        """
        try:
            with open(self.filename) as f:
                high_score = json.load(f)
        except FileNotFoundError:
            # Create the file if it doesn't exist.
            high_score = 0
            with open(self.filename, 'w') as f:
                json.dump(high_score, f)
        return high_score

    def reset_high_score(self):
        """Reset the high score and dump it to the json file."""
        self.high_score = self.score
        with open(self.filename, 'w') as f:
            json.dump(self.high_score, f)
