from peewee import Model, ModelSelect

import storage.db


class Base(Model):
    @staticmethod
    def parse_multiple_results(results: ModelSelect):
        response = []
        for result in results:
            response.append(result)

        return response

    class Meta:
        database = storage.db.db
    pass
