### Why you selected these 2 tests for automation over other candidates?

I selected these two tests because they cover the most important user journeys and give the highest value for
automation.

The first priority was business impact — I wanted to automate flows where failures would be most visible to users or
could directly affect betting behavior, trust, or revenue.

I also considered regression value. These are scenarios that are likely to be executed repeatedly as part of future
releases,
so automating them saves time and gives fast feedback.

I also wanted a balance between UI validation and backend/business logic verification,
rather than selecting only simple happy-path UI checks.

### What I Intentionally Left as Manual Only and Why

I intentionally left some scenarios as manual because, given the time and priorities, they would provide lower
automation value compared to the selected core flows.

For example, visual validation such as checking layout alignment, styling issues, label placement, responsiveness, or
general UI presentation is usually better suited for manual testing unless there is a dedicated visual automation
strategy in place.

I also left exploratory scenarios as manual, such as unusual user behavior, rapid/random interaction patterns,
unexpected navigation paths, or trying combinations that are not part of standard business flows. These are areas where
human observation is still more effective.

Edge cases with lower business impact were also deprioritized for automation, such as less common filter combinations,
non-critical validation messages, or rare negative scenarios that are unlikely to regress frequently.

Some scenarios involving unstable or highly dynamic data were also intentionally avoided for automation in the initial
scope, since they can introduce flaky tests without providing enough long-term value.

Examples include:

- cosmetic UI checks
- responsiveness/layout validation
- uncommon filtering combinations
- exploratory betting behavior
- negative edge cases with low business risk
- general usability observations

The goal was to focus automation effort on scenarios that provide the strongest regression protection and highest
business confidence, while keeping more subjective or lower-value checks manual.

### Top Recommendations If This Project Were to Scale

My first recommendation would be to integrate the tests into CI/CD as early as possible.
Even a small smoke suite running on every pull request would provide fast feedback and help catch critical issues before
they reach release testing. A larger regression suite could then run nightly or before deployment.

My second recommendation would be to improve the test data strategy.
For betting flows, stable and predictable test data is very important. I would prefer API-created test users,
controlled wallet balances, predictable upcoming matches, and cleanup after execution.
This would make the tests more reliable and less dependent on manually prepared data.

My third recommendation would be to expand the test layers.
UI tests are useful for validating real user journeys, but they should not carry all the coverage.
I would add more API-level tests for business rules such as stake limits, odds validation, wallet balance updates,
match availability, and error handling. This would make the test suite faster, more stable, and easier to scale.

I would also recommend clarifying ambiguous product rules, especially around odds changes, rebet behavior,
balance synchronization, and match availability.
Clear rules would make test expectations more reliable and reduce false failures.