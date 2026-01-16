# Autonomous Refactor Plan (BMAD Method)

## Objectives
- Add a headless, autonomous execution layer using Python scripts plus the Claude Agent SDK.
- Preserve existing interactive BMAD workflows and CLI behavior.
- Support parallel, repeatable runs with state, observability, and safe tool gating.
- Align with the Agentic Developer Workflow (ADW) patterns in `/Users/Apple/workplace/TAC/tac-8`.

## Current Architecture Summary
- Workflows are defined as `workflow.yaml` + instructions (`workflow.xml` or `instructions.md`) and are executed by the user or an LLM following `src/core/tasks/workflow.xml`.
- Execution hints already exist in workflow YAML (for example `execution_hints.autonomous: true`) but are not enforced by a headless runner.
- The CLI focuses on installation and packaging; there is no autonomous workflow execution entrypoint.

## Target Architecture

### 1) Agentic Layer (Python, ADW-style)
Mirror the TAC `adws/` structure to keep implementation predictable and composable.

```
adws/
  adw_modules/
    agent.py               # CLI fallback (Claude Code subprocess)
    agent_sdk.py           # Claude Agent SDK wrappers
    workflow_ops.py        # Workflow parsing and execution
    state.py               # adw_state.json + error tracking
    worktree_ops.py        # Optional isolation helpers
    observability.py       # JSONL event stream + hook integration
  adw_triggers/
    adw_trigger_cron_bmad.py
  adw_run_workflow.py      # Headless runner for a single workflow
  adw_run_queue.py         # Process task queue (tasks.md or Notion)
agents/
  {adw_id}/
    adw_state.json
    events.jsonl
    outputs/
specs/
trees/
```

### 2) Workflow Execution Engine (Headless)
Implement a deterministic runner for BMAD workflows:

1. Load `workflow.yaml` and resolve `config_source`.
2. Resolve variables and `installed_path`, `output_folder`, `date`.
3. Load instructions (`workflow.xml` or `instructions.md`) and templates.
4. Execute instructions in order using the logic in `src/core/tasks/workflow.xml`.
5. Handle `template-output` by writing to output files after each section.
6. Respect `execution_hints`:
   - `autonomous: true` -> no blocking prompts
   - `interactive: true` -> require user or stop with "needs input"
7. Record step status and outputs into `agents/{adw_id}/adw_state.json`.

### 3) Headless Agent Runtime (Claude Agent SDK)
Use the Claude Agent SDK as the default runtime with CLI fallback.

- **One-shot steps**: `query()` for single-step prompts.
- **Multi-step workflows**: `ClaudeSDKClient` to keep session continuity.
- **Tool gating**: `allowed_tools=[...]` in `ClaudeAgentOptions`.
- **Headless execution**: `permission_mode="bypassPermissions"` for non-interactive runs.

Example SDK pattern (from Context7):

```python
from claude_agent_sdk import query, ClaudeAgentOptions

async for msg in query(
    prompt="Execute step 2 using the instructions below...",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Write", "Glob"])
):
    handle_message(msg)
```

### 4) Triggers and Queues
Adopt TAC-style triggers to make workflows autonomous:

- `adw_trigger_cron_bmad.py` polls:
  - `tasks.md` (similar to `tac8_app2__multi_agent_todone`)
  - Notion tasks (similar to `tac8_app4__agentic_prototyping`)
  - CI jobs or webhook payloads
- Each task spawns a headless workflow run with its own `adw_id` and worktree.

### 5) Observability and Hooks
Provide a structured event stream and optional Claude hooks:

- `events.jsonl` for per-step activity, tool usage, and errors.
- Optional `.claude/hooks` for external observability (TAC app3 pattern).

## Implementation Phases

### Phase 0: Hardening Prereqs
- Fix update path crash (`bmadDir` before definition).
- Fix dependency resolver path handling for `{project-root}` and XML tasks.
- Add tests for resolver and update flows.

### Phase 1: Minimal Headless Runner
- Create `adws/adw_modules/workflow_ops.py` to parse `workflow.yaml`.
- Implement `adws/adw_run_workflow.py`:
  - Run a single workflow (start with `testarch-atdd`).
  - Produce output + state files in `agents/{adw_id}`.
- Use SDK `query()` for single-step execution.

### Phase 2: Session-Based Execution
- Add `ClaudeSDKClient` support for multi-step workflows.
- Stream responses, detect `ResultMessage` completion.
- Add retry logic for tool errors.

### Phase 3: Queues and Triggers
- Implement `adw_run_queue.py` to process `tasks.md` or Notion.
- Add worktree isolation (`trees/`) to keep runs safe and parallel.
- Support `priority`, `model`, and `workflow` tags in the task queue.

### Phase 4: Observability
- Add structured `events.jsonl` for all runs.
- Optional hook integration for live dashboards.

### Phase 5: Full Coverage
- Expand support to priority workflows:
  - `dev-story`, `create-story`, `sprint-status`, `automate`, `trace`
- Add workflow-specific validation after outputs are generated.

## Proposed CLI Integration
Add a new CLI command that bridges to Python:

```
bmad run-workflow --workflow "_bmad/bmm/workflows/testarch/atdd/workflow.yaml" \
  --project /path/to/project --headless
```

Internally this invokes:
```
python adws/adw_run_workflow.py --workflow ... --project-root ...
```

## Testing Strategy
- Unit tests: variable resolution, config loading, instruction parsing.
- Integration tests: run a minimal workflow with stub outputs.
- E2E tests: headless run on a fixture project using a limited tool allowlist.

## Migration Strategy
- Keep the existing interactive BMAD flow unchanged.
- Add opt-in headless mode via CLI flags or environment variables.
- Document new entrypoints in README + docs.

## Success Criteria
- At least 3 workflows run end-to-end without prompts.
- Each run produces `adw_state.json`, output files, and event logs.
- Headless runs can execute in parallel without file collisions.
