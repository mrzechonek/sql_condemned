class AdjacencyListMixin(object):
    def parents(self, link_column=None):
        model = type(self)

        if link_column is None:
            rel, = (r for r in model._meta.related_objects if r.to == model)
            parent_link, = rel.get_joining_columns()
            _, link_column = parent_link

        assert link_column in model._meta.get_all_field_names()

        kwargs = dict(
            db_table=self._meta.db_table,
            pk_column=self._meta.pk.column,
            link_column=link_column
        )

        return model.objects.raw("""
            WITH RECURSIVE adjacency AS (
                SELECT
                    0 as level,
                    "{db_table}".*
                FROM "{db_table}"
                WHERE "{pk_column}" = %s

                UNION ALL

                SELECT
                    level+1,
                    parent.*
                FROM adjacency
                JOIN "{db_table}" parent ON
                    adjacency."{link_column}" = parent."{pk_column}"
            )
            SELECT * FROM adjacency
            WHERE level > 0
            ORDER BY level ASC""".format(**kwargs),
            [self.pk])
