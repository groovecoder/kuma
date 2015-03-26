import random

from locust import HttpLocust, TaskSet, task


class YahooSearchBehavior(TaskSet):
    query_file = 'search_terms.txt'

    def __init__(self, parent):
        self.query_lines = open(self.query_file, 'r').read().splitlines()
        return super(YahooSearchBehavior, self).__init__(parent)

    @task(1)
    def search_json_api(self):
        query = random.choice(self.query_lines)
        self.client.get("/en-US/search.json?highlight=false&q=%s" % query)


class YahooLocust(HttpLocust):
    task_set = YahooSearchBehavior
