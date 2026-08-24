# AgentGate — Future Project Abstract

## Status

**Parked future project.** This document preserves the concept until the
analytics server is complete. AgentGate is not part of the analytics server's
current scope and should eventually live in its own repository.

---

## Abstract

AgentGate is a zero-trust runtime and attack lab for AI agents. It sits between
agents and the tools, APIs, databases, and sub-agents they attempt to use. Its
job is to require every agent to prove its identity, connect every proposed
action to a user-authorized task, grant only narrowly scoped and short-lived
access, and record the resulting security decision in a tamper-evident audit
trail.

The project explores a central question:

> How can an autonomous agent remain useful without inheriting all of the
> authority, credentials, and access of the human or system that launched it?

AgentGate assumes that prompts, models, memory, retrieved documents, tools, and
credentials may be compromised. It therefore treats an AI model's output as a
proposal, not as authorization. A separate enforcement layer decides whether
an action is permitted.

The project will include an intentionally vulnerable agent environment so its
controls can be demonstrated against realistic attacks such as prompt
injection, excessive permissions, malicious tools, credential misuse, data
exfiltration, and unsafe sub-agent delegation.

---

## Problem

Traditional applications usually execute predetermined code paths with
permissions assigned to human users or long-running services. Agentic systems
change this model: an AI agent can select tools dynamically, combine data from
untrusted sources, create sub-agents, and take actions at machine speed.

Giving an agent the user's permanent API keys or full account permissions
creates several problems:

- A prompt injection can turn legitimate access into unintended action.
- A compromised tool or retrieved document can redirect the agent's behavior.
- Static credentials can be leaked, copied, or reused outside the original task.
- A child agent can accidentally inherit more authority than it needs.
- It can be difficult to reconstruct who authorized an action and why it ran.
- A mistake can be repeated rapidly without rate limits or human intervention.

Prompt filtering alone cannot solve these problems. Even a manipulated agent
must be prevented from acquiring authority that was never delegated to it.

---

## Project Thesis

Every agent action must satisfy four requirements:

1. **Identity** — Which human, agent, workload, and tool are involved?
2. **Intent** — What user-authorized task is this action serving?
3. **Authority** — Is this exact action allowed on this resource right now?
4. **Accountability** — Can the complete decision and delegation chain be
   reconstructed later?

The model follows these zero-trust principles:

- Never trust an agent merely because it is inside the system.
- Verify identity and authorization on every consequential action.
- Prefer just-in-time access over standing access.
- Apply least privilege to tools, resources, duration, and number of uses.
- Keep authorization outside the model and outside agent-controlled memory.
- Assume that some part of the agentic system has already been compromised.
- Require human approval for high-impact or irreversible operations.

---

## Conceptual Architecture

```text
Human user
    │ creates a task and delegates limited authority
    ▼
Agent orchestrator
    │ proposes a tool action
    ▼
┌──────────────────── AgentGate ────────────────────┐
│ Identity verification                             │
│ Delegation-chain validation                       │
│ Tool and resource registry                        │
│ Policy and risk evaluation                        │
│ Human approval for high-risk actions              │
│ Short-lived capability issuance                   │
│ Rate limits, revocation, and kill switch           │
│ Tamper-evident security event logging              │
└────────────────────────┬───────────────────────────┘
                         ▼
              Approved tool, API, database,
                    or child agent
```

### Principal concepts

- **Human identity:** The person who authorizes the original task.
- **Agent identity:** A unique non-human identity for each running agent.
- **Task:** The bounded objective authorized by the human.
- **Delegation:** The authority passed from a human to an agent or from a parent
  agent to a child agent.
- **Tool registry:** Approved tools, versions, actions, risk levels, and schemas.
- **Policy decision:** An allow, deny, or require-approval result made outside
  the AI model.
- **Capability:** A signed, short-lived, narrowly scoped permission for one kind
  of action.
- **Audit event:** A record tying together identity, task, proposed action,
  policy result, approval, and execution outcome.

### Example capability

```text
subject: agent/research-17
delegated-by: user/james
task: portfolio-report-482
tool: analytics-query
actions: [read]
resources: [portfolio/page-views]
expires: 60 seconds after issuance
max-uses: 5
may-delegate: false
```

Long-lived service credentials should not appear in prompts, agent memory, or
source code. AgentGate, or a separate credential broker, should inject the
credential only after a request is authorized. The agent receives a temporary
capability rather than the underlying secret.

---

## Demonstration Scenario

The primary demonstration will combine a small RAG system with an outbound
communication tool:

1. A user asks a research agent to summarize an approved document collection.
2. The agent receives temporary read-only access to that collection.
3. A retrieved document contains a malicious instruction telling the agent to
   upload private documents to an external URL.
4. The manipulated agent proposes an outbound HTTP action.
5. AgentGate denies the action because the destination is unregistered, the
   task does not permit external transmission, and the agent lacks the required
   capability.
6. The attack lab displays the complete path from user intent and retrieved
   document to proposed action and policy denial.

This scenario demonstrates the project's main claim: the AI can be manipulated
without the overall system surrendering its authority.

Additional attack scenarios may include:

- Reuse of an expired or already-consumed capability.
- An agent requesting access to an unrelated database resource.
- A child agent attempting to exceed its parent's delegated permissions.
- A registered tool changing its schema or version unexpectedly.
- Repeated purchases or messages stopped by rate and spending limits.
- Attempts to access a tool after the human activates the kill switch.

---

## Proposed MVP

The first version should be small enough to understand completely and run
locally:

- A lightweight API service acting as the AgentGate enforcement point.
- Human, agent, task, tool, and resource identities.
- Signed, short-lived capability tokens.
- Policy checks for action, resource, task, expiration, usage count, and
  delegation.
- A registry containing approved tools and versions.
- A mock RAG/document-search tool.
- A mock outbound HTTP, email, or purchasing tool.
- An approval queue for high-risk actions.
- Per-agent rate limits and a global kill switch.
- A SQLite security-event store with hash-linked records for tamper evidence.
- A small dashboard showing identities, delegations, decisions, and attacks.
- Automated tests for allowed actions and expected denials.

The initial agent may be scripted or use a hosted model. The security model
should not depend on a particular LLM provider or agent framework.

---

## Non-Goals for the MVP

- Building a general-purpose identity provider or secrets vault.
- Training or hosting a large language model.
- Detecting every possible prompt injection through content classification.
- Replacing network, operating-system, or container security.
- Supporting every agent framework or tool protocol.
- Claiming that an LLM can reliably determine whether its own intent is safe.
- Building production-grade distributed infrastructure before the policy model
  has been validated locally.

---

## Success Criteria

The MVP will be successful when it can demonstrate that:

- Every agent and tool call has a unique, verifiable identity.
- An agent cannot call an unregistered tool.
- An agent cannot exceed the scope or lifetime of its delegated authority.
- A child agent cannot receive more authority than its parent possesses.
- Long-lived tool credentials are never exposed to the agent.
- High-risk actions require explicit human approval.
- A prompt-injected agent is prevented from exfiltrating protected data.
- Revocation and the kill switch stop later actions immediately.
- A viewer can reconstruct why an action was allowed or denied.
- Security behavior is verified with repeatable attack tests.

---

## Possible Later Extensions

- An MCP-aware gateway that validates tool schemas and arguments.
- SPIFFE/SPIRE workload identities and automatically rotated certificates.
- An external policy engine such as Open Policy Agent.
- Relationship-based delegation using OpenFGA.
- Integration with a dedicated secrets vault.
- Cryptographically signed tool manifests and supply-chain verification.
- Risk-adaptive policies based on destination, data sensitivity, and behavior.
- Canary agents and sandboxed tool execution.
- OpenTelemetry traces correlated with security decisions.
- A public capture-the-flag or educational attack lab.
- Formal tests proving that delegated permissions can only become narrower.

---

## Relationship to the Analytics Server

AgentGate should remain separate from the analytics server. The current project
has its own purpose, lifecycle, and Raspberry Pi constraints. Its infrastructure
lessons—Linux administration, Docker, persistence, HTTPS, secrets, health
checks, backups, and CI/CD—will provide useful preparation for AgentGate.

The Raspberry Pi 2 should not initially be expected to run model inference, a
vector database, and the complete AgentGate stack. Development should begin on
the main laptop. A later experiment could place a lightweight authorization
gateway and audit store on the Pi while agents and models run elsewhere, making
the enforcement point independent of the system it governs.

---

## Open Decisions for the Future

- Which agent framework, if any, should be used for the demonstration?
- Should the first capability format use JWTs, macaroons, or a custom learning
  format?
- Should policies begin as application code or use OPA from the start?
- How should task intent be represented without relying on free-form model text?
- Which operations always require human approval?
- What constitutes sufficient tamper evidence for the learning version?
- Should the initial tool interface be plain HTTP, MCP, or both?
- Which parts should run on the Pi, laptop, or a hosted service?

---

## Restart Point

When the analytics server is complete, resume this project by:

1. Creating a separate AgentGate repository.
2. Writing three concrete allowed-action examples and three denied-action
   examples.
3. Defining the human-to-agent and agent-to-agent delegation rules.
4. Threat-modeling the RAG prompt-injection demonstration.
5. Building the smallest gateway that can authorize one mock tool call.
6. Adding attack scenarios one control at a time.

---

## Initial References

- [IBM Technology — Securing AI Agents with Zero Trust](https://youtu.be/d8d9EZHU7fw)
- [OWASP — Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [OWASP — Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
- [SPIFFE Concepts](https://spiffe.io/docs/latest/spiffe/concepts/)
- [Open Policy Agent — API Authorization](https://www.openpolicyagent.org/docs/http-api-authorization)
- [OpenFGA — Relationship-Based Access Control](https://openfga.dev/docs/learn/rebac)
