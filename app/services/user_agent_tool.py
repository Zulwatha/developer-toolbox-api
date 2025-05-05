from user_agents import parse

def parse_user_agent(user_agent_str: str) -> dict:
    # Parses the user agent string and extracts information
    ua = parse(user_agent_str)

    return {
        "browser": {
            "family": ua.browser.family,
            "version": ua.browser.version_string
        },
        "os": {
            "family": ua.os.family,
            "version": ua.os.version_string
        },
        "device": {
            "family": ua.device.family,
            "type": "Mobile" if ua.is_mobile else "Tablet" if ua.is_tablet else "PC" if ua.is_pc else "Other"
        },
        "is_bot": ua.is_bot
    }
