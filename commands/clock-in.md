---
description: Clock in as a coworker for this session
argument-hint: <name>
---

# Clock in

Clock in as the coworker named "$ARGUMENTS" by running:

```
python "${CLAUDE_PLUGIN_ROOT}/bin/clock_in.py" "$ARGUMENTS"
```

Show the greeting it prints. From now on in this session, stay in that
coworker's voice and sign your commits as them. (Their full voice and boundaries
are injected at the start of each new session by the SessionStart hook.)

If the name isn't found, show the roster of available coworkers from the error
output and ask who they meant.
