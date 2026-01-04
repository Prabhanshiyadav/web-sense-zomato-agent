import json
import os

class AgentMemory:
    FILE = "logs/memory.json"

    def load(self):
        if os.path.exists(self.FILE):
            return json.load(open(self.FILE))
        return {"failed": [], "success": []}

    def save(self, data):
        json.dump(data, open(self.FILE, "w"), indent=2)
