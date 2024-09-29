# pylint: disable=line-too-long

from textwrap import dedent
from crewai import Task


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
                **Task**: Prepare detailed notes from given data and context.
                **Description**: Given a topic, base notes, and context related to the topic, you need to create detailed notes in markdown format.

                Notes must be split into logical Headings, Sub Headings, and relevant source codes accordingly.

                Consider base notes as a starting point and improve on top of it.

                Your final answer must be a clean and detailed markdown file strictly following this structure.

                Base Notes must be the truth, and with the context, improve on that. You must provide detailed and well-structured notes.
                **Parameters**:
                    - **Topic**: {topic}
                    - **Base Notes**: {base_notes}
                **Note**: {self._tip_section()}
                """
            ),
            expected_output="Create error-free detailed notes with proper content and sections from base notes",
            agent=agent,
        )
