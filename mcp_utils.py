def create_mcp_message(agent_name, role, content, turn):
    return {
        "agent": agent_name,
        "role": role,
        "content": content,
        "turn": turn
    }

def format_history_for_prompt(history):
    return "\n".join([f"{m['agent']} ({m['role']}): {m['content']}" for m in history])
