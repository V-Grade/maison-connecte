// création du module scotchApp, ngRoute et firebase sont des dépendances
var scotchApp = angular.module('scotchApp', ['ngRoute','firebase','scotchApp.controllers']);

// configuration des routes
// .config ajoute une action pendant le chargement du module
scotchApp.config(function($routeProvider) {
	$routeProvider

		.when('/', {
			templateUrl : 'pages/piece0.html',
			controller  : 'mainController'
		})

		.when('/pieces', {
			templateUrl : 'pages/piece1.html',
			controller  : 'mainController'
		})

		.when('/graphes', {
			templateUrl : 'pages/piece2.html',
			controller  : 'tempController'
		})

		.when('/graphes2', {
			templateUrl : 'pages/piece3.html',
			controller  : 'humController'
		});
});


scotchApp.controller('mainController', function($scope, $firebase) {

	// connection à firebase 
	var ref = new Firebase("https://projet-maison-co-test.firebaseio.com/data");  
	var fb = $firebase(ref);

	// synchronisation en tant qu'objet 
	var syncObject = fb.$asObject();

	// three way data binding
	syncObject.$bindTo($scope, 'data');

	
});
