# Database Migrations
Add a new file to the `migrations` folder that is the next integer increment.

## Adding a new migration
If you want to update the database, add a migration file that will move the database forward.

We use the migrator built into peewee. Please look at the [peewee docs](https://docs.peewee-orm.com/en/latest/peewee/playhouse.html?highlight=migration#schema-migrations) for more information.

## How migrations are applied
* In development: on boot of the app, migrations are run.
* In staging/production: when the app boots migrations are run automatically.

So, generally speaking you don't have to do anything, just add a migration.

## FAQs
### My new migration failed:
> You can delete all tables and let the migrator recreate everything. This is good if your data doesn't matter.

or

> You can undo