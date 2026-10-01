# Data Dictionary

This document defines the fields used in the European Soccer
Player Performance Analytics project.

| Field | Description | Type | Source/Derived |
|---|---|---|---|
| PlayerName | Player's displayed name | Text | Source |
| Nation | Player nationality | Text | Source |
| Position | Original source position | Text | Source |
| PositionGroup | Standardized V1 position group | Text | Derived |
| Age | Player age | Decimal | Source |
| ClubName | Club represented | Text | Source |
| CompetitionName | Competition represented | Text | Derived |
| SeasonName | Season represented | Text | Derived |
| MatchesPlayed | Matches appeared in | Integer | Source |
| Starts | Matches started | Integer | Source |
| Minutes | Minutes played | Integer | Source |
| Nineties | Equivalent number of 90-minute matches | Decimal | Source/Derived |
| Goals | Goals scored | Integer | Source |
| Assists | Assists recorded | Integer | Source |
| ExpectedGoals | Expected goals | Decimal | Source |
| ExpectedAssistedGoals | Expected assisted goals | Decimal | Source |
| Shots | Total shots | Integer | Source |
| ShotsOnTarget | Shots on target | Integer | Source |