from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [
    Route.get('/', "WorkspacesController@index").name('index'),
    Route.get('/workspace/create', "WorkspacesController@create").name('create'),
    Route.post('/workspace/store', "WorkspacesController@store").name('store'),
    Route.get('/workspace/@id', "WorkspacesController@show").name('show'),
    Route.get('/workspace/@id/edit', "WorkspacesController@edit").name('edit'),
    Route.post('/workspace/@id/update', "WorkspacesController@update").name('update'),
    Route.get('/workspace/@id/delete', "WorkspacesController@destroy").name('destroy'),

    Route.get('/workspace/@id/project/create', "ProjectController@create").name('project_create'),
    Route.post('/workspace/@id/project/store', "ProjectController@store").name('project_store'),
    Route.get('/workspace/@id/project/@project_id', "ProjectController@show").name('project_show'),
    Route.get('/workspace/@id//project/@project_id/edit', "ProjectController@edit").name('project_edit'),
    Route.post('/workspace/@id/project/@project_id/update', "ProjectController@update").name('project_update'),
    Route.get('/workspace/@id/project/@project_id/delete', "ProjectController@destroy").name('project_destroy'),
]

ROUTES += Auth.routes()
