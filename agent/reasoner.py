import json
from agent.memory import AgentMemory

class LLMReasoner:
    def __init__(self):
        self.step = 0
        self.memory = AgentMemory()
        self.history = self.memory.load()

    async def decide(self, state, goal):
        self.step += 1

        if self.step == 1:
            return json.dumps({"thought":"Searching food","action":"fill","value":"Pizza Delhi"})
        if self.step == 2:
            return json.dumps({"thought":"Submit","action":"press"})
        if self.step == 3:
            return json.dumps({"thought":"Click first restaurant","action":"click"})
        if self.step == 4:
            return json.dumps({"thought":"Analyze UX","action":"observe"})
        return json.dumps({"thought":"Done","action":"finish"})
