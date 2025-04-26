import anthropic
import os
from agents.base_agent import BaseAgent
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class ConAgent(BaseAgent):
    def generate_response(self, message_history):
        prompt = f"""
You are {self.name}, an AI agent participating in a structured, academic debate.
You have been **explicitly assigned** to argue the {self.stance.upper()} position on the topic:

"Should universal basic income be implemented?"

You must present persuasive, clear, and well-reasoned arguments **in support of your assigned stance**,
even if you personally would take a more nuanced view in real life.

Please stay in character as a debate participant and respond as if you're trying to convince an audience.
Do not express neutrality. You are acting as the {self.stance.upper()} side.

Debate so far:
{message_history}

Respond with a logical and convincing continuation:
"""

        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.7,
            system="You are a debate agent on the con side of a topic.",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
