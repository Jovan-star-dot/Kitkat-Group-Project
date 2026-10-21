# Promethean Technology Significance Criteria

## Source status
The distinctions below draw on the assigned course text, *Mastering the Craft of Emerging Technology Adoption*, Chapters 5 and 11, and the Week 6 Assignment 4 brief.

The course text’s core definition is that a Promethean technology dissolves a categorical barrier, rather than merely reducing it, and does so across two or more tiers of human existence. It directs the analyst to test the technology as a usable system, write a barrier statement, apply a suppression test, and then assess six criteria.

The course materials do not specify a numeric cutoff for the six criteria. The four-of-five threshold below is a **proposed operational criterion for this agent**, not an instructor definition.

## Scope
Evaluate the specified Agentic AI system or category described in the case and supported by sources. State the boundary of what is included. Do not generalize from one agent, model, vendor, or application to all AI.

## Decision sequence

### 1. System or component
Determine whether the subject exists as a usable system or is only a component, concept, or unassembled capability. The course text says a component alone should not be evaluated for Promethean status; assess the usable system it belongs to. If the relevant system is not established, qualify the analysis or classify it as `Indeterminate`.

### 2. Barrier statement
Complete this statement using evidence:

> Before this technology, [activity] required [constraint]; this was experienced not merely as an inconvenience but as the definition of [part of human experience].

If the constraint was an ordinary performance limitation, was already recognized as a solvable problem, or cannot be credibly specified, do not treat it as a categorical barrier.

### 3. Suppression test
Ask: if the system disappeared, would the earlier constrained state simply return, or would removal disrupt systems built on the technology?

Evidence that the old state would return with limited disruption supports reduction rather than dissolution. Evidence of durable dependencies and disruption across rebuilt systems supports possible dissolution. Do not treat current popularity or switching inconvenience alone as proof of irreversibility.

### 4. Human-life tiers
Assess whether the barrier is dissolved across at least two of the course text’s tiers:
- biological survival;
- economic activity;
- cognitive and social life.

A demonstrated dissolution in only one tier may support `Breakthrough`, but does not meet the course’s cross-tier condition for a Promethean candidate.

### 5. Six course criteria
Assess every criterion below as `Supported`, `Mixed`, `Unsupported`, or `Unknown`, with a brief evidence basis and counterevidence where available. Do not replace the six separate judgments with a general statement such as “the criteria are insufficient.” If a source does not address a criterion, use `Unknown`; do not infer support from popularity or from a neighboring criterion. Record the six judgments in `general_et_finding`, which is an existing free-text field in the frozen output schema. A genuine barrier dissolution is a gate to the Potentially Promethean classification; the six criterion judgments are still required when that gate is not met so the reviewer can see why.

1. **Order-of-magnitude improvement:** roughly tenfold or greater change in a meaningful dimension of performance, cost, or accessibility.
2. **Widespread impact:** effects across more than one sector of economic, social, or civic life.
3. **Paradigm shift:** changed assumptions previously treated as settled, rather than simply doing an existing activity faster.
4. **Catalytic effect:** further innovations that depend on the technology’s existence.
5. **Democratizing effect:** broader access to a capability previously scarce or exclusive.
6. **Irreversibility:** a durable, rebuilt-on state rather than a temporary trend.

For an emerging technology, irreversibility cannot be confirmed prospectively. Treat it as Unknown unless historical evidence permits a retrospective assessment; do not claim `Confirmed Promethean` as an output label.

## Classification rules

- **Incremental:** Evidence supports gradual or bounded improvement within the existing activity or system. No credible evidence establishes a radical departure or categorical-barrier dissolution.
- **Breakthrough:** Evidence supports a radical departure or meaningful change in what is feasible, but the barrier is reduced rather than dissolved, or dissolution is demonstrated in only one human-life tier. A major technical achievement or market disruption alone does not make the technology Promethean.
- **Potentially Promethean:** The usable-system, credible-barrier, suppression-test, and two-or-more-tier gates are supported. **Proposed criterion:** at least four of the first five six-criteria items are Supported by credible evidence, the remaining item is not contradicted by decisive evidence, and the principal contrary evidence has been considered. Irreversibility remains unconfirmed for an emerging technology.
- **Indeterminate:** Available credible evidence cannot establish the system boundary, barrier, suppression-test result, number of affected tiers, or enough of the criteria to distinguish the levels responsibly. State what evidence is missing and what would resolve the uncertainty.

If evidence establishes meaningful change but fails the proposed Potentially Promethean threshold, use `Breakthrough` only when radical departure or one-tier barrier dissolution is itself supported. Otherwise use `Indeterminate`.

## Confidence
- **High:** The classification gates and decisive criteria are supported by multiple appropriate sources, and the strongest counterevidence does not materially undermine them.
- **Moderate:** The classification is best supported, but material evidence gaps or unresolved counterarguments remain.
- **Low:** Evidence is sparse, indirect, conflicting, stale, or dependent mainly on interested-party claims. If the category cannot be distinguished, classify `Indeterminate` and explain why.

Confidence describes confidence in the classification, not confidence that a forecasted future will occur. When classifying as `Indeterminate`, separate confidence that the evidence is presently insufficient from uncertainty about the technology's eventual significance. Do not describe confidence as Moderate or High merely because the sources are credible if those sources do not address the decisive course tests; use Low confidence in a significance conclusion when the conclusion depends on evidence gaps or indirect proxies.

## Anti-hype rule
Funding, media attention, market excitement, novelty, and vendor claims may identify claims to investigate; alone they do not support a higher classification. Distinguish observed capability and deployment from projections.

## Context rule
The general technology classification is based on general technology evidence and should remain stable across organizations when that evidence is unchanged. Assess application significance and organization-specific implications separately. Potentially Promethean significance is not, by itself, a recommendation to adopt a particular application now.

## Change evidence
Name specific evidence that could raise, lower, or leave the classification unchanged. Examples of evidence categories to monitor include independently verified capability, sustained deployment, cross-sector use, dependency on the system, evidence of substitutability or reversibility, and documented effects across the named human-life tiers. Do not claim these conditions have occurred without sources.
