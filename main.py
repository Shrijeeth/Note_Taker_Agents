from textwrap import dedent
from dotenv import load_dotenv

from crews import NoteTakingCrew
from tools.markdown_tools import MarkdownTools


if __name__ == "__main__":
    load_dotenv()
    markdown_tools = MarkdownTools()

    print("## Welcome to Note Taker Agent")
    print('-------------------------------')

    note_topic = dedent(input("Enter Topic for which you want the notes to be prepared: "))
    note_content = dedent(input("Enter notes / Subtitle for your Topic: "))

    note_preparation_crew = NoteTakingCrew(topic=note_topic, base_notes=note_content)
    result = note_preparation_crew.run()
    
    print("########################\n")
    markdown_tools.save_markdown(topic=note_topic, task_output=result.raw)