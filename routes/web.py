from masonite.routes import Route

ROUTES = [
    Route.get('/', "WorkspacesController@index").name('index'),
    Route.get('/createworkspace', "WorkspacesController@create").name('create'),
    Route.post('/storeworkspace', "WorkspacesController@store").name('store'),
    Route.get('/workspace/@id', "WorkspacesController@show").name('show'),
    Route.get('/edit/@id', "WorkspacesController@edit").name('edit'),
    Route.post('/update/@id', "WorkspacesController@update").name('update'),
    Route.get('/delete/@id', "WorkspacesController@destroy").name('destroy'),
]
