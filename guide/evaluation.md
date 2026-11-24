# 2. Evaluate the first version

Start with the cheapest approach that could meet the need. The sample baseline sends requests that mention an invoice or charge to billing and requests about passwords or sign-in to access. It checks billing words first. The file contains the resulting suggestions for eight fictional requests.

Run this command from the root of the repository.

```sh
python3 exercises/intake/score.py exercises/intake/baseline.csv
```

The baseline matches **5 of 8** expected decisions. It also suggests a queue for **3 of 4** requests that require human review. The second number matters because this desk wants a human to handle sensitive or ambiguous requests. A single accuracy figure hides that failure.

## Investigate the errors

1. Read the request and the expected decision for each mismatch. Identify the assumption that failed. T05 combines two topics. T06 reports a possible account incident. T08 lacks enough information to pick a queue.
2. Copy the baseline to a new CSV. Change the three suggestions to `review` and score the copy. The exercise result should be 8 of 8, with zero required reviews missed.
3. Propose a change that could produce those corrections on unseen requests. Ask a second person to write four fresh examples, including one single-topic request that should still go straight to a queue. Label them together before testing the change.
4. Record the version, case set, exact matches, missed reviews and number of suggestions sent to a queue. A system that sends every request to review avoids missed reviews and gives the dispatcher little help.

Correcting the sample predictions checks that you understand the desk's policy. Use the fresh cases to assess your proposed change. For a real pilot, collect representative examples with the workflow owner and keep the final evaluation set separate from development.

[Next: hand it over](handoff.md) · [Evaluation case design](../library/openai--evals/README.md)
