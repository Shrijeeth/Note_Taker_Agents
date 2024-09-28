from crewai import Crew, Process, Task

from agents import NoteTakerAgents
from tasks import NoteTakingTasks


class NoteTakingCrew:
    def __init__(self, topic, base_notes):
        self.topic = topic
        self.base_notes = base_notes
    
    def run(self):
        agents = NoteTakerAgents()
        tasks = NoteTakingTasks()

        data_collector_agent = agents.data_collector_agent()
        content_writer_agent = agents.content_writer_agent()

        raw_data_preparation_task = tasks.prepare_raw_data(
            data_collector_agent,
            self.topic,
            self.base_notes,
        )
        note_preparation_task: Task = tasks.prepare_detailed_notes(
            content_writer_agent,
            self.topic,
            self.base_notes,
        )

        note_preparation_task.context = [raw_data_preparation_task]

        crew = Crew(
            agents=[data_collector_agent, content_writer_agent],
            tasks=[raw_data_preparation_task, note_preparation_task],
            verbose=True,
            process=Process.sequential
        )
        result = crew.kickoff()
        return result