import json
import os
from agent.memory import AgentMemory

class LLMReasoner:
    def __init__(self, scenario="default"):
        self.step = 0
        self.memory = AgentMemory()
        self.history = self.memory.load()
        self.scenario_name = scenario
        self.scenarios = self.load_scenarios()
        self.steps = self.scenarios.get(self.scenario_name, [])

    def load_scenarios(self):
        if os.path.exists("scenarios.json"):
            with open("scenarios.json", "r") as f:
                return json.load(f)
        return {"default": []}

    async def decide(self, state, goal):
        # step is 1-based index in the logic, so subtract 1 for list access
        if self.step < len(self.steps):
            action = self.steps[self.step]
            self.step += 1
            return json.dumps(action)

        return json.dumps({"thought":"Done","action":"finish"})
