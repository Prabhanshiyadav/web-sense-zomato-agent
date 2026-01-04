import json

class DecisionEngine:
    def parse(self, llm_output):
        try:
            data = json.loads(llm_output)
            return data
        except json.JSONDecodeError:
            # fallback
            return {"thought":"parse_error","action":"finish","selector":"","value":""}
