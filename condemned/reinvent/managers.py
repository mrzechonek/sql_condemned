from django.db import models
from django.db import connection

class PaginationManager(models.Manager):
    def pages(self, page_size, order_by):
        assert order_by in self.model._meta.get_all_field_names()

        cursor = connection.cursor()
        cursor.execute("""
            WITH pages AS (
                SELECT
                    (row_number() OVER (ORDER BY "{order_by}") - 1) / %s AS page,
                    "{db_table}".*
                FROM "{db_table}"
            )
            SELECT DISTINCT
                page,
                first_value("{order_by}") OVER pagination AS "from",
                last_value("{order_by}") OVER pagination AS "to"
            FROM pages
            WINDOW pagination AS (PARTITION BY page)
            ORDER BY page""".format(db_table=self.model._meta.db_table, order_by=order_by),
            [page_size])

        return cursor.fetchall()

