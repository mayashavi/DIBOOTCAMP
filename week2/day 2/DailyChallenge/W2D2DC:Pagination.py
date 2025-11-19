import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []

        self.items = items
        self.page_size = page_size
        self.current_page = 0  # 0-based index
        self.total_pages = math.ceil(len(items) / page_size)

    def get_visible_items(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
    # user enters 1-based page number
        self.current_page = page_num - 1
        return self

    def first_page(self):
        self.current_page = 0
        return self

    def last_page(self):
        self.current_page = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
        return self

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        return self
