# pylint: disable=too-few-public-methods

import time


class MarkdownTools:
    @staticmethod
    def save_markdown(topic, task_output):
        """
        Useful tool to store result as markdown
        """
        ts = round(time.time())
        filename = f"./outputs/{topic}-{ts}.md"
        with open(filename, "w+", encoding="utf-8") as file:
            file.write(task_output)
        print(f"Output Saved as {filename}")
