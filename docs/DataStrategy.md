# Data Strategy

## Project

European Soccer Player Performance Analytics

## Version 1 Scope

Season: 2025-26

Competitions:
- La Liga
- UEFA Champions League

## Primary Research Question

How do players perform relative to their position, playing
time, competition, and peers?

## Data Grain

One row will initially represent one player's season-level
performance for one club, competition, and season.

Player + Club + Competition + Season

Match-level data is outside the initial V1 scope and may be
added in a later version.

## Position Groups

- Goalkeeper
- Defender
- Midfielder
- Forward

For players with multiple listed positions, V1 will use the
first listed position as the primary position group.

## Metric Categories

### Playing Time
- Matches Played
- Starts
- Minutes
- Nineties

### Attack
- Goals
- Assists
- Non-Penalty Goals
- Expected Goals
- Non-Penalty Expected Goals
- Expected Assisted Goals
- Shots
- Shots on Target

### Passing and Creation
- Passes Completed
- Passes Attempted
- Pass Completion Percent
- Progressive Passes
- Key Passes
- Shot-Creating Actions

### Possession and Progression
- Touches
- Carries
- Progressive Carries
- Successful Take-Ons
- Progressive Passes Received

### Defense
- Tackles
- Interceptions
- Blocks
- Clearances
- Recoveries
- Aerial Duels Won

### Goalkeeping
- Goals Against
- Saves
- Save Percent
- Clean Sheets
- Clean Sheet Percent
- Post-Shot Expected Goals
- Goals Prevented

Final metric availability will depend on the source data.

## Derived Metrics

Examples include:

- GoalsPer90
- AssistsPer90
- GoalContributionsPer90
- ExpectedGoalsPer90
- ShotsPer90
- ShotsOnTargetPer90
- ProgressivePassesPer90
- ProgressiveCarriesPer90
- TacklesPer90
- InterceptionsPer90

Derived metrics will be calculated from source values whenever
possible rather than blindly relying on precomputed fields.

## Minimum-Minute Rules

La Liga leaderboards:
900 minutes

Champions League leaderboards:
450 minutes

Player profile:
No minimum

Direct player comparisons:
No minimum, but playing time must be displayed.

## Data Sources

Primary analytical source:
FBref

Secondary Champions League validation source:
UEFA

Metrics from different providers will not be treated as
identical unless their definitions are confirmed to match.

## Data Integrity Principles

- Preserve original raw files.
- Never manually alter raw source data.
- Store cleaned data separately.
- Document all transformations.
- Preserve totals before calculating rates.
- Track missing values rather than inventing replacements.
- Record source and competition for every observation.
- Validate unusual results before presenting them.