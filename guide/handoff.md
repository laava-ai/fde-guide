# 3. Hand it over

A dispatcher must be able to keep working when suggestions stop. Before the pilot, rehearse one normal request and one failed request with the person who will operate the desk.

| Operator question | Answer for this exercise |
|---|---|
| What happens on an error or timeout? | Show the request in the existing manual queue. The dispatcher can complete it there. |
| What happens if a request arrives twice? | Reuse its ticket ID. Show a single suggestion for the same ticket and version. |
| What can we measure? | Count suggestions, corrections, required reviews missed and time spent per request. Record the rule version and the final decision. |
| What triggers a stop? | For this trial, a suggested queue on a suspected account incident triggers a pause and review by the desk lead. |
| How do we recover? | Turn suggestions off, finish open tickets manually and check the affected cases before restarting. |

## Make a pilot decision

For the supplied baseline, write **hold**. T06 would send an account incident directly to a queue. A corrected example file establishes the expected behavior. A pilot decision also needs a repeatable implementation and results on fresh cases.

Draft a one-paragraph handoff to the desk lead. Include the baseline result, an unresolved failure, who owns the next trial and how the operator can stop it. Ask a teammate to follow the fallback using only your handoff. If they have to guess where the request goes, revise it.

[Back to the guide](../README.md) · [Engineering handoff and test planning](../library/microsoft--code-with-engineering-playbook/README.md)
