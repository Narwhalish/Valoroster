from enums import Map, Agent


class Game:
    """This class represents a game in Valorant."""

    def __init__(self):
        """Initialize the Game object."""
        self._teams = None
        self._map = Map.DEFAULT
        self._agents = tuple()
        self._winner = None

    @property
    def teams(self):
        """Return the teams in the game.

        Returns:
            tuple(str, str): The teams that played in the game.
        """
        return self._teams

    @teams.setter
    def teams(self, value):
        """Set the teams in the game.

        Args:
            value (tuple(str, str)): The teams that played in the game.

        Raises:
            ValueError: value is not a 2-tuple of strings.
        """
        if len(value) != 2 or not all(isinstance(v, str) for v in value):
            raise ValueError("value must be a 2-tuple of strings")
        else:
            self._teams = value

    @property
    def map(self):
        """Return the map of the game.

        Returns:
            enum: The map of the game.
        """
        return self._map

    @map.setter
    def map(self, value):
        """Set the map of the game.

        Args:
            value (enum): The map of the game.
        """
        self._map = Map[value]

    @property
    def agents(self):
        """Return the agents in the game.

        Returns:
            tuple(
              tuple(enum, enum, enum, enum, enum),
              tuple(enum, enum, enum, enum, enum)
            ): The agents in the game respective to the order of the teams property.
        """
        return self._agents

    @agents.setter
    def agents(self, value):
        """Set the agents in the game.

        Args:
            tuple(
              tuple(enum, enum, enum, enum, enum),
              tuple(enum, enum, enum, enum, enum)
            ): The agents in the game respective to the order of the teams property.

        Raises:
            ValueError: value is not a 2-tuple of 5-tuples of strings.
        """
        if (
            len(value) != 2
            or not all(isinstance(v, tuple) for v in value)
            or not all(all(isinstance(a, str) for a in v) for v in value)
        ):
            raise ValueError("value must be a 2-tuple of 5-tuples of strings")
        else:
            self._agents = tuple(
                tuple(Agent[agent] for agent in agent_select) for agent_select in value
            )

    @property
    def winner(self):
        """Return the winner of the game.

        Returns:
            str: The winner of the game.
        """
        return self._winner

    @winner.setter
    def winner(self, value):
        """Set the winner of the game.

        Args:
            value (str): The winner of the game.
        """
        self._winner = ""

    def __str__(self):
        """Return string representation of the game.

        Returns:
            str: The string representation of the game.
        """
        return str(
            {
                "Game": {
                    "teams": self.teams,
                    "map": self.map.name,
                    "agents": tuple(
                        tuple(agent.name for agent in agents) for agents in self.agents
                    ),
                }
            }
        )
