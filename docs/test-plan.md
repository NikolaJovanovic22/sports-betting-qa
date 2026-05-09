Test scenarios:

### 001 Match List shows only upcoming matches

This test validates that only upcoming matches are available for bet placement.

#### Priority: Critical

#### Risk Rationale:

The risk behind this validation is critical because displaying expired, live-locked, suspended,
or already finished matches for betting may lead to invalid bet submissions, financial inconsistencies,
regulatory violations, and poor user experience.

Steps:

1. Navigate to Upcoming Football Matches list
2. Scroll to the list to validate match data including its status

Expected Result:

- Each match shows status "UPCOMING"
- Matches with status "PAST" should not be visible on the list

### 002 Stake minimum and maximum limits validation

This test validates stake amount boundaries to ensure users can place bets only within the allowed minimum and maximum
limits.

#### Priority: High

#### Risk Rationale:

Stake validation is considered a high-risk area because incorrect handling of betting limits may lead to financial loss,
regulatory compliance issues, fraud exposure, and inconsistent user experience.

#### Steps:

1. Select upcoming football match from the match list
2. Click on odds to select outcome for betting
3. Try to set stake over €100 or lower than €1

Expected result:

- Stake minimum per bet is €1
- Stake maximum per bet is €100

Steps:

### 003 Single Bet Placement for upcoming match

This test verifies that a user can successfully place a single bet on an upcoming football match
using valid betting selections and stake values.

#### Priority: Critical

#### Risk Rationale:

Single bet placement is a high-risk and business-critical workflow,
because it directly impacts financial transactions, user trust, regulatory compliance, and revenue generation.

#### Steps:

1. Select upcoming football match from the match list
2. Validate if the match shows such data: home/away team; kickoff data/time label; odds
3. Click on odds to select outcome for betting
4. Enter stake value within Bet Slip and validate if Potential Payout is calculated correctly (multiply the odds by the
   stake)
5. Click Place Bet

Expected Result:

- Bet Placed Successfully!
- Success Receipt dialog appears and shows details:
  Bet ID
  Match details
  Selection
  Stake
  Odds at placement
  Potential payout
  Placement timestamp
- User Balance value is reduced for the applied stake value.

### 004 Error Handling by Rebet action

This test validates the rebet functionality in error-handling scenarios,
ensuring users can successfully retry a failed single bet placement action
without causing inconsistent system behavior or duplicate transactions.

#### Priority: Critical

#### Risk Rationale:

This area is considered high-risk because failed bet placement flows involve transaction recovery,
wallet synchronization, backend stability, and user trust.

#### Steps:

1. Select upcoming football match from the match list
2. Click on odds to select outcome for betting
3. Enter desired stake value referring to user balance
4. Open devtool browser console to change throttling settings in Network tab
5. Choose Offline mode in throttling dropdown menu
6. Click Place Bet
   error model dialog appears: Something went wrong
   available options: Rebet; Close

7. Enable network full speed by choosing No throttling in Network settings
8. Click Rebet

#### Expected result:

- Bet placed successfully!
- Rebet is error handling action which allows user to retry failed request for Place Bet action.

### 005 Filter matches by date and odds range

This test validates match filtering by date range and odds.

#### Priority: Medium

#### Risk Rationale:

This area is risk-sensitive because incorrect filtering may show unavailable, irrelevant,
or financially incorrect betting options, which can directly affect user decision-making,
bet placement accuracy, and business revenue.

#### Steps:

1. Navigate to Upcoming Football Matches list
2. Filter matches between May 17th and May 31st; choose this date range from data filter popover
3. Open Odds Filter popover to set min value on 3,30; then apply the filter settings

#### Expected result:

- Upcoming Football Matches list shows only filtered match: Marseille - Monaco






