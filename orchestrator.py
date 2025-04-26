from mcp_utils import create_mcp_message, format_history_for_prompt

def run_debate(agent_a, agent_b, turns=6):
    history = []
    current_agent = agent_a

    for turn in range(1, turns + 1):
        prompt_history = format_history_for_prompt(history)
        response = current_agent.generate_response(prompt_history)

        message = create_mcp_message(
            agent_name=current_agent.name,
            role=current_agent.stance,
            content=response,
            turn=turn
        )
        history.append(message)
        current_agent = agent_b if current_agent == agent_a else agent_a

    return history
