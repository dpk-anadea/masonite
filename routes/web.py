from masonite.routes import Route

ROUTES = [
    Route.get('/', "WorkspacesController@index").name('index'),
    Route.get('/workspace/create', "WorkspacesController@create").name('create'),
    Route.post('/workspace/store', "WorkspacesController@store").name('store'),
    Route.get('/workspace/@id', "WorkspacesController@show").name('show'),
    Route.get('/workspace/@id/edit', "WorkspacesController@edit").name('edit'),
    Route.post('/workspace/@id/update', "WorkspacesController@update").name('update'),
    Route.get('/workspace/@id/delete', "WorkspacesController@destroy").name('destroy'),

    Route.get('/project', "ProjectController@index").name('projects'),
    Route.get('/project/create', "ProjectController@create").name('project_create'),
    Route.post('/project/store', "ProjectController@store").name('project_store'),
    Route.get('/project/@id', "ProjectController@show").name('project_show'),
    Route.get('/project/@id/edit', "ProjectController@edit").name('project_edit'),
    Route.post('/project/@id/update', "ProjectController@update").name('project_update'),
    Route.get('/project/@id/delete', "ProjectController@destroy").name('project_destroy'),
]
