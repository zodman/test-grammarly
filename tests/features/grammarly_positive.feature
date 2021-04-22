Feature: Grammarly works
Scenario: Check if grammarly works well
		Given grammarly activated
		When User access to grammarly checker and type a incorrect word
		Then grammarly should notice about the mistypo
