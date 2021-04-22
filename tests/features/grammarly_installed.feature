@not_installed
Feature: Check if grammarly is installed
Scenario: with a chrome browser with grammarly installed
	Given a url like google.com
	When wait for the webpage is fully loaded
	Then check if the body property contains data-gr-ext-installed property
