# pylint: disable=line-too-long,too-few-public-methods

from googlesearch import search
from langchain.tools import tool


class SearchTools:
    @staticmethod
    @tool("Search the Internet")
    def search_internet(query: str):
        """
        Useful tool to search the internet about a given topic and return relevant results
        """
        top_results_to_return = 5
        results = search(
            query,
            num_results=top_results_to_return,
            sleep_interval=2,
            advanced=True,
        )

        response = []
        for result in results:
            response.append(
                f"""
                url: {result.url},
                title: {result.title},
                description: {result.description},
                """
            )
        if len(response) == 0:
            return "Sorry, I couldn't find anything about the query provided. There could be an error with the search."

        return "\n\n".join(response)
