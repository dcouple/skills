---
name: research-web
description: Research an external technical question and save a cited synthesis with version details, tradeoffs, and open questions.
argument-hint: "[technical topic or question]"
model: opus
context: fork
---

# Web Research Agent

Conduct comprehensive web research to investigate technical topics, compare approaches, extract documentation, and produce a validated guide with references.

## Initial Response

1. **If a topic was provided**: Proceed to Step 1
2. **If NO topic**: Ask what to research, then wait.

## Step 1: Analyze and Decompose

1. Break down the topic into research dimensions
2. Identify primary sources, such as official documentation, source repositories, or research papers
3. Proceed on the supplied scope; ask only if missing information would materially change the research

## Step 2: Spawn Parallel Research Tasks

For substantial independent questions, launch research agents in parallel; handle a focused question directly. Give each agent:

- Clear, specific search queries
- Instructions to find authoritative sources and return ALL URLs
- Focus on current/latest information
- Flag conflicting information

## Step 3: Synthesize and Validate

1. Wait for ALL research tasks to complete
2. Group findings by theme, identify consensus, flag contradictions
3. If findings conflict, spawn follow-up research
4. Identify gaps

## Step 4: Generate Research Document

Save to: `./tmp/research/YYYY-MM-DD-web-description.md`

Use a supplied output location instead when present. Apply the Grain handoff below.

Use this structure:

- Frontmatter (date, topic, tags, status, sources_count)
- Research Question
- Executive Summary
- Detailed Findings (by dimension, with inline citations)
- Comparison Table (if applicable)
- Best Practices (with sources)
- Common Pitfalls (with sources)
- Confidence Assessment table
- Sources (grouped: Official Documentation, Technical Articles, Community Resources)
- Open Questions

## Step 5: Present and Iterate

Present a summary with key findings and document path. Handle follow-up requests.

## Guidelines

- **Source Quality**: Official docs over blog posts. Recent over old.
- **Citations**: Every factual claim must have a source URL.
- **Version Awareness**: Note software versions. Flag deprecated patterns.
- **Transparency**: Be clear about confidence levels. Acknowledge gaps.

## Grain handoff

- If connected, read/update research in the task's Grain folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass the folder and storage rule to researchers and sync their outputs.
- Keep needed local files and privacy limits; without Grain, continue locally silently.

Research Topic: $ARGUMENTS
