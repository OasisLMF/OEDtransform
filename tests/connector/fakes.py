from converter.connector import BaseConnector
from converter.utils.iter import ensure_row_iterable
from tests.config.fakes import fake_transformation_config


class FakeConnector(BaseConnector):
    def __init__(self, data=None, **options):
        super().__init__(fake_transformation_config(), **options)
        self.data = data or []

    def extract(self):
        return self.data

    def load(self, data):
        self.data = list(ensure_row_iterable(data))

    async def aextract(self):
        for row in self.data:
            yield row

    async def aload(self, data):
        self.data = [row async for row in data]
