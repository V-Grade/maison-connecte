// create the module and name it scotchApp, ngRoute et firebase sont des dépendances
var scotchApp = angular.module('scotchApp', ['ngRoute','firebase']);

// configure our routes
// .config ajoute une action lors du chargement du module
scotchApp.config(function($routeProvider) {
	$routeProvider

		// route for the home page
		.when('/pieces', {
			templateUrl : 'pages/piece1.html',
			controller  : 'mainController'
		})

		// route for the about page
		.when('/graphes', {
			templateUrl : 'pages/piece2.html',
			controller  : 'testController'
		})

		// route for the contact page
		.when('/historique', {
			templateUrl : 'pages/piece3.html',
			controller  : 'mainController'
		});
});

// create the controller and inject Angular's $scope
scotchApp.controller('mainController', function($scope, $firebase) {
	// create a message to display in our view
	//$scope.message = 'Everyone come and see how good I look!';
	// connect to firebase 
	var ref = new Firebase("https://projet-maison-co-test.firebaseio.com/data");  
	var fb = $firebase(ref);

	// sync as object 
	var syncObject = fb.$asObject();

	// three way data binding
	syncObject.$bindTo($scope, 'data');

	
});
scotchApp.controller('testController', function($scope) {
	
	var ref = new Firebase("https://projet-maison-co-test.firebaseio.com/data");

	// ----------------------- GRAPH SALLE -----------------------
	var x_salle = [];
	var y_salle = [];

	// x array with time
    ref.child("graph/liste_salle1/2").on("value", function(snapshot) {
     x_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle2/2").on("value", function(snapshot) {
     x_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle3/2").on("value", function(snapshot) {
     x_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle4/2").on("value", function(snapshot) {
     x_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle5/2").on("value", function(snapshot) {
     x_salle.push(snapshot.val());
     console.log(x_salle);
    });

    // y array with temp
	ref.child("graph/liste_salle1/0").on("value", function(snapshot) {
     y_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle2/0").on("value", function(snapshot) {
     y_salle.push(snapshot.val());
    });

	ref.child("graph/liste_salle3/0").on("value", function(snapshot) {
     y_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle4/0").on("value", function(snapshot) {
     y_salle.push(snapshot.val());
    });

    ref.child("graph/liste_salle5/0").on("value", function(snapshot) {
     y_salle.push(snapshot.val());
     console.log(y_salle);
    });

    	//order time with temp
		var list = [];
		for (var j = 0; j < x_salle.length; j++) 
		    list.push({'x_salle_val': x_salle[j], 'y_salle_val': y_salle[j]});

		list.sort(function(a, b) {
		    return ((a.x_salle_val < b.x_salle_val) ? -1 : ((a.x_salle_val == b.x_salle_val) ? 0 : 1));
		});

		for (var k = 0; k < list.length; k++) {
		    x_salle[k] = list[k].x_salle_val;
		    y_salle[k] = list[k].y_salle_val;
		}

		console.log(x_salle);
		console.log(y_salle);

	var trace1 = {
		x: x_salle,
		y: y_salle,
		type : 'scatter'
	};	

	var data_salle = [trace1];

	x_salle = [];
	y_salle = [];

	Plotly.newPlot('myDiv', data_salle);

		// ----------------------- GRAPH CUISINE -----------------------
	var x_cuisine = [];
	var y_cuisine = [];

	// x array with time
    ref.child("graph/liste_cuisine1/2").on("value", function(snapshot) {
     x_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine/2").on("value", function(snapshot) {
     x_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine3/2").on("value", function(snapshot) {
     x_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine4/2").on("value", function(snapshot) {
     x_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine5/2").on("value", function(snapshot) {
     x_cuisine.push(snapshot.val());
     console.log(x_cuisine);
    });

    // y array with temp
	ref.child("graph/liste_cuisine1/0").on("value", function(snapshot) {
     y_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine2/0").on("value", function(snapshot) {
     y_cuisine.push(snapshot.val());
    });

	ref.child("graph/liste_cuisine3/0").on("value", function(snapshot) {
     y_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine4/0").on("value", function(snapshot) {
     y_cuisine.push(snapshot.val());
    });

    ref.child("graph/liste_cuisine5/0").on("value", function(snapshot) {
     y_cuisine.push(snapshot.val());
     console.log(y_cuisine);
    });

    	//order time with temp
		var list = [];
		for (var j = 0; j < x_cuisine.length; j++) 
		    list.push({'x_cuisine_val': x_cuisine[j], 'y_cuisine_val': y_cuisine[j]});

		list.sort(function(a, b) {
		    return ((a.x_cuisine_val < b.x_cuisine_val) ? -1 : ((a.x_cuisine_val == b.x_cuisine_val) ? 0 : 1));
		});

		for (var k = 0; k < list.length; k++) {
		    x_cuisine[k] = list[k].x_cuisine_val;
		    y_cuisine[k] = list[k].y_cuisine_val;
		}

		console.log(x_cuisine);
		console.log(y_cuisine);

	var trace1 = {
		x: x_cuisine,
		y: y_cuisine,
		type : 'scatter'
	};	

	var data_cuisine = [trace1];

	x_cuisine = [];
	y_cuisine = [];

	Plotly.newPlot('myDiv2', data_cuisine);

		// ----------------------- GRAPH CHAMBRE -----------------------
	var x_chambre = [];
	var y_chambre = [];

	// x array with time
    ref.child("graph/liste_chambre1/2").on("value", function(snapshot) {
     x_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre/2").on("value", function(snapshot) {
     x_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre3/2").on("value", function(snapshot) {
     x_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre4/2").on("value", function(snapshot) {
     x_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre5/2").on("value", function(snapshot) {
     x_chambre.push(snapshot.val());
     console.log(x_chambre);
    });

    // y array with temp
	ref.child("graph/liste_chambre1/0").on("value", function(snapshot) {
     y_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre2/0").on("value", function(snapshot) {
     y_chambre.push(snapshot.val());
    });

	ref.child("graph/liste_chambre3/0").on("value", function(snapshot) {
     y_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre4/0").on("value", function(snapshot) {
     y_chambre.push(snapshot.val());
    });

    ref.child("graph/liste_chambre5/0").on("value", function(snapshot) {
     y_chambre.push(snapshot.val());
     console.log(y_chambre);
    });

    	//order time with temp
		var list = [];
		for (var j = 0; j < x_chambre.length; j++) 
		    list.push({'x_chambre_val': x_chambre[j], 'y_chambre_val': y_chambre[j]});

		list.sort(function(a, b) {
		    return ((a.x_chambre_val < b.x_chambre_val) ? -1 : ((a.x_chambre_val == b.x_chambre_val) ? 0 : 1));
		});

		for (var k = 0; k < list.length; k++) {
		    x_chambre[k] = list[k].x_chambre_val;
		    y_chambre[k] = list[k].y_chambre_val;
		}

		console.log(x_cuisine);
		console.log(y_cuisine);

	var trace1 = {
		x: x_chambre,
		y: y_chambre,
		type : 'scatter'
	};	

	var data_chambre = [trace1];

	x_chambre = [];
	y_chambre = [];

	Plotly.newPlot('myDiv3', data_chambre);
});
