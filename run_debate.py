from agents.pro_agent import ProAgent
from agents.con_agent import ConAgent
from orchestrator import run_debate

if __name__ == "__main__":
    topic = "Should universal basic income be implemented?"
    print(f"\nDebate Topic: {topic}\n")

    agent_pro = ProAgent("Agent A", "Pro")
    agent_con = ConAgent("Agent B", "Con")

    debate = run_debate(agent_pro, agent_con, turns=6)

    for msg in debate:
        print(f"[Turn {msg['turn']}] {msg['agent']} ({msg['role']}):\n{msg['content']}\n")
