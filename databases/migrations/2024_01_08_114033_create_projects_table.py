"""CreateProjectsTable Migration."""

from masoniteorm.migrations import Migration


class CreateProjectsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('projects') as table:
            table.increments('id')
            table.text('name')

            table.integer('workspace_id').unsigned()
            table.foreign('workspace_id').references('id').on('workspaces')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("projects")
