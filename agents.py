# pylint: disable=line-too-long
import os

from textwrap import dedent
from crewai import Agent, LLM

from tools.search_tools import SearchTools


class NoteTakerAgents:
    def __init__(self):
        self.data_collector_llm = LLM(
            model=os.getenv("DATA_COLLECTOR_MODEL"),
            base_url=os.getenv("DATA_COLLECTOR_ENDPOINT"),
            temperature=0.5,
        )

        self.content_writer_llm = LLM(
            model=os.getenv("CONTENT_WRITER_MODEL"),
            base_url=os.getenv("CONTENT_WRITER_ENDPOINT"),
            temperature=0.5,
        )

    def data_collector_agent(self):
        return Agent(
            role="Data Collector",
            backstory=dedent(
                """
                Expert Data Collector who is responsible for collecting data and cleaning data for a given topic and base notes given by the user to prepare the detailed notes.
                I have decades of experience collecting accurate and error free data based on sample notes provided.
                """
            ),
            goal=dedent(
                """
                Collect and create a raw data for the given topic which can then be used to prepare detailed notes.
                Include base notes / subscript provided and the topic to fetch appropriate data.
                Filter out unnecessary and unwanted data from the raw data which are not related to topic and base notes.
                """
            ),
            tools=[SearchTools.search_internet],
            llm=self.data_collector_llm,
            allow_delegation=True,
            verbose=True,
        )

    def content_writer_agent(self):
        return Agent(
            role="Content Writer",
            backstory=dedent(
                """
                Expert Content Writer who is responsible to preparing detailed and well written notes based on topic, base notes and raw data provided.
                I have decades of experience in content writing and have published many articles online.
                """
            ),
            goal=dedent(
                """
                Create detailed, well documented notes in markdown format based on data and topics provided.
                The notes must be in English and free of gramatical issues.
                Notes must be in markdown format strictly.
                Notes must contain all the content from base notes strictly.
                Notes must be split into logical Headings, Sub Headings and relevant source codes accordingly.
                Notes must explained in detail and easy to understand.
                """
            ),
            llm=self.content_writer_llm,
            allow_delegation=True,
            verbose=True,
        )
