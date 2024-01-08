"""Workspaces Migration."""

from masoniteorm.migrations import Migration


class Workspaces(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('workspaces') as table:
            table.increments("id")
            table.string('name')
            table.text('description')
            table.boolean('is_active').default(False)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('workspaces')
