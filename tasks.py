from crewai import Task
from textwrap import dedent


class NoteTakingTasks:
    def _tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    
    def prepare_raw_data(self, agent, topic, base_notes):
        return Task(
            description=dedent(
                f"""
                **Task**: Fetch and Prepare raw data
                **Description**: Given a topic and basic notes on it, you need to prepare raw data on topics which can be further used for note taking purposes. This raw data must cover all aspects of the base notes and improve it. No extra content must be there apart from base notes on the topic.
                **Parameters**:
                    - Topic: ```{topic}```
                    - Base Notes: ```{base_notes}```
                **Note**: {self._tip_section()}
                """
            ),
            expected_output="Prepare raw data which can be used for taking notes based on topic and basic notes.",
            agent=agent,
        )
    
    def prepare_detailed_notes(self, agent, topic, base_notes):
        return Task(
            description=dedent(
                f"""
                **Task**: Prepare detailed notes from given data
                **Description**: Given a topic, base notes and data related to the topic, you need to create a detailed notes in markdown format. Notes must be split into logical Headings, Sub Headings and relevant source codes accordingly. Your final answer must be a clean and detailed notes in a markdown format strictly.
                **Parameters**:
                    - Topic: {topic}
                    - Base Notes: {base_notes}
                **Note**: {self._tip_section()}
                """
            ),
            expected_output="Create a error free detailed notes with proper content and sections",
            agent=agent,
        )