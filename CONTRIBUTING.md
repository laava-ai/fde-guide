# Contributing

Laava reviews changes through GitHub pull requests. To suggest an exercise, describe the decision a learner will make, supply a fictional example, and show how another person can check the result. Use English for guide text.

For a reading suggestion, add a source card under `library/` and link to it in the topic index. Explain what question the source helps answer. Pin reading links to the reviewed commit, record its date and identify the upstream licence. Link to the publisher's copy of the material.

Before opening a pull request, check the links and run the worked example from the repository root.

```sh
python3 scripts/check.py
python3 exercises/intake/score.py exercises/intake/baseline.csv
```

Use fictional records for exercises. Contributors retain copyright in their original work and contribute it under the repository's Apache License 2.0.
