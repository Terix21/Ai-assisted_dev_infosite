# AI-Assisted Developer Checklist

Use this checklist before committing or merging AI-assisted work.

## 1. Define & Constrain

- [ ] I can explain the user need, acceptance criteria, and failure cases.
- [ ] I checked course or employer policy and use an approved tool.
- [ ] I shared only necessary, permitted context. I did not send credentials, customer records, or private code to an unapproved service.
- [ ] I limited agent access to the necessary files, commands, and development environment.

## 2. Generate

- [ ] I requested a small change with explicit constraints.

## 3. Test & Verify

- [ ] I read the entire diff, including configuration, lockfiles, and tests.
- [ ] I can explain the data flow, decisions, and failure behavior.
- [ ] I included useful comments and a brief file header describing purpose and key assumptions, following repository conventions. Both match the current code.
- [ ] I checked unfamiliar APIs against official documentation for the version in use.
- [ ] I confirmed the exact package, publisher, source, and purpose before installing.
- [ ] I reviewed compatibility, license, maintenance, and advisories.
- [ ] I inspected manifest and lockfile changes, including install scripts and transitive dependencies where relevant.
- [ ] I recorded scan results and investigated findings. A clean scan is limited evidence.
- [ ] I ran the checks myself and inspected their output.
- [ ] I tested happy paths, boundaries, errors, and the wrong user.
- [ ] I checked that the test asserts the intended requirement and fails for the relevant bug.
- [ ] I verified usability, accessibility, and integration behavior where affected.

## 4. Review & Commit

- [ ] The server enforces identity and per-resource authorization.
- [ ] Queries separate data from SQL. Untrusted text does not become executable markup or commands.
- [ ] Secrets stay out of prompts, browser bundles, logs, and Git. I rotate exposed secrets and report exposure.
- [ ] I reviewed untrusted instructions, external calls, and agent actions.
- [ ] A responsible human reviewed correctness, maintainability, and risk. AI review is an additional check.
- [ ] I removed unrelated edits and reviewed the staged diff.
- [ ] I documented tests, limitations, AI use when required, and the recovery plan.
- [ ] I followed the team’s PR and merge process. Data backup and recovery are separate from Git.

> **Never merge code you cannot explain.**

The sequence is: **Define & Constrain → Generate → Test & Verify → Review & Commit**.

*Views expressed are my own and do not necessarily reflect those of my employer.*
