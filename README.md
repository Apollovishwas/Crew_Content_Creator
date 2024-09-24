# Social Media Content Generation System

This project is a sophisticated social media content generation system that leverages AI agents to create trending, engaging content for various platforms.

## Overview

The system uses a crew of AI agents to perform the following tasks:
1. Research top fashion trends
2. Generate relevant hashtags
3. Create platform-specific captions
4. Produce email newsletter content

## Components

- `main.py`: Flask application that serves as the entry point and handles webhooks
- `crew.py`: Defines the AI crew and their process
- `agents.py`: Specifies the AI agents and their roles
- `task.py`: Outlines the tasks for each agent
- `tools.py`: Contains tools used by the agents (not provided in the code snippets)

  ## Setup

1. Install the required dependencies
2. Set up the necessary environment variables
- OPENAI_API_KEY
- SERPER_API_KEY
- LANGCHAIN_API_KEY

3. Run the Flask application

## Note

This project uses various AI and language processing libraries. Ensure you have the necessary API keys and permissions to use these services. Use LocalTunnel or tmole for tunneling
