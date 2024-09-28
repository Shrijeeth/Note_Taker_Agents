# Note_Taker_Agents

Basic Note Taking Agents using Local LLM's and CrewAI

## Requirements
- Python 3.10+
- Virtualenv (Optional)

## Build Instructions
1. First clone this repository.
2. After cloning run the following command from project directory in the terminal:
    ```
    pip install -r requirements.txt
    ```

## Usage Instructions
1. Run the following command from the project directory in the terminal to run the application:
    ```
    python main.py
    ```
2. The command interface asks for Topic and Base Content. Provide the necessary details accordingly.
3. Once the processing is over by the agents, the output is stored in `outputs` directory in following file format `{topic}-{timestamp}.md`.