**ChatGPT:**

Totally. Here’s a **practical playbook** + **copy-paste snippets** for when a model “zoom-collapses” (locks onto a narrow slice and loses the bigger frame).

* * *

Spot it fast (symptoms)
-----------------------

* Answers optimize a sub-task while ignoring the stated goal.
    
* Re-decides already-decided constraints (“should we use auth?”).
    
* Argues edge cases; drops acceptance criteria.
    
* Can’t summarize the plan in <8 bullets.
    

* * *

Quick triage (what to do right now)
-----------------------------------

### 1) Force a zoom-out (30-second nudge)

```
Zoom out. Restate: Goal, Scope (in/out), Constraints, Decisions (locked), Acceptance Criteria (≤5 bullets), Risks (≤3).
Then: say which part of my last ask you’re answering and why.
```

### 2) Re-anchor to a single source of truth (use when drift repeats)

```
Create/refresh a CONTEXT SNAPSHOT (≤350 tokens):
- Goal
- Scope (in/out)
- Constraints
- Decisions (LOCKED)
- Acceptance Criteria (≤5)
- Open Questions (≤3)
- Next 3 Tasks
Treat the SNAPSHOT as SoT. If my ask conflicts with it, flag the conflict before proceeding.
```

### 3) Demand assumptions & options (break fixation)

```
List assumptions you’re relying on (≤5). For each, say impact if false.
Give 2–3 options to proceed, ranked, with trade-offs. Then recommend one.
```

### 4) Guard the output shape (so it can’t meander)

```
Answer format only:
1) Checklist (≤7 items) that must be true at the end.
2) Steps to satisfy each item.
3) Risks & mitigations (≤3).
4) Next 3 Actions.
No narrative; no restating prior content.
```

* * *

Prevention presets (drop these at start of a task)
--------------------------------------------------

### A) “Quality governor” (general)

```
Quality rules:
- Use the latest SNAPSHOT as the sole SoT.
- Label lines **SoT** (from SNAPSHOT/citations) or **Inf** (inference).
- If facts may be post-2024, browse & cite.
- Be concise, determinate; prefer checklists over prose.
- Surface top 3 risks/assumptions; end with Next 3 Actions.
```

### B) Engineering / spec work

```
Before proposing a solution:
1) Confirm Goal, Constraints (perf/security), Interfaces, Acceptance Criteria.
2) Identify Decisions already locked.
3) Show an outline first; wait for “Proceed”.
```

### C) Research / planning

```
Map the space first:
- Axes (what dimensions matter)
- Options per axis
- Conflict points / trade-offs
Then synthesize a recommendation with cited facts.
```

* * *

Recovery patterns (when it’s already off the rails)
---------------------------------------------------

### Hard reset (keep intent, drop clutter)

```
Distill a CLEAN BRIEF (≤300 tokens): Goal, Decisions (LOCKED), Constraints, Acceptance Criteria (≤5), Exclusions.
Proceed using only the CLEAN BRIEF; list gaps before answering.
```

### Thread health-check (use every ~10 turns)

```
Health-check this thread:
- What’s our Goal in one sentence?
- What are the current Decisions (LOCKED)?
- What’s the next irreversible choice?
- What info do you need from me (≤3 items)?
If any are unclear, ask before proceeding.
```

* * *

Task-specific anti-collapse nudges
----------------------------------

### Coding

```
Anchor to tests: propose 3–5 acceptance tests first. No code until tests are approved.
```

### Product spec

```
Return only: Problem, Non-Goals, Constraints, Success Metrics, Milestones. ≤250 tokens total.
```

### Debugging

```
State competing root-cause hypotheses (≤3), evidence for/against, and the next discriminating test.
```

* * *

One-liners (use inline mid-chat)
--------------------------------

* “You’re optimizing the wrong sub-problem; re-anchor to the Goal and Acceptance Criteria.”
    
* “List what you’re assuming about the context that isn’t in the SNAPSHOT (≤5).”
    
* “Stop generating; give me 3 options with trade-offs and pick one.”
    

* * *

If you want, I’ll **instantiate a SNAPSHOT v1 for our Git/PR workflow** right now so you can try the nudges live.