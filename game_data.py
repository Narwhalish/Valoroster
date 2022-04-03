from enums import Map, Agent


class Game:
    def __init__(self):
        self._teams = None
        self._map = Map.DEFAULT
        self._agents = tuple()
        self._winner = None

    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, value):
        if len(value) != 2:
            raise Exception("Teams must be a tuple of 2")
        else:
            self._teams = value

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, value):
        self._map = Map[value]

    @property
    def agents(self):
        return self._agents

    @agents.setter
    def agents(self, value):
        if len(value) != 2:
            print(value)
            raise Exception("Agents must be a tuple of 2 agent selections")
        self._agents = tuple(
            tuple(Agent[agent] for agent in agent_select) for agent_select in value
        )

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, value):
        self._winner = ""

    def __str__(self):
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
