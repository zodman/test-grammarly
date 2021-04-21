Feature: Grammarly works
Scenario: Check if grammarly works well
		When User access to grammarly checker and type a incorrect word
		Then grammarly should notice about the error
		And show the correct word
