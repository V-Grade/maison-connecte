// create the module and name it scotchApp, ngRoute et firebase sont des dépendances
var scotchApp = angular.module('scotchApp', ['ngRoute','firebase']);

// configure our routes
// .config ajoute une action lors du chargement du module
scotchApp.config(function($routeProvider) {
	$routeProvider

		// route for the home page
		.when('/', {
			templateUrl : 'pages/piece1.html',
			controller  : 'mainController'
		})

		// route for the about page
		.when('/piece2', {
			templateUrl : 'pages/piece2.html',
			controller  : 'mainController'
		})

		// route for the contact page
		.when('/piece3', {
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


