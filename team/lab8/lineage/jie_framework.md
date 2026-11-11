{
  "version": "1.0",
  "scope": "Assess a specified application, organization, adoption stage and time horizon. This is a proposed rubric, not a certification standard.",
  "ratings": {
    "unknown": "Evidence absent, stale or materially conflicting; never convert to zero.",
    "0": "Verified absent or unacceptable.",
    "1": "Intent or plan exists; capability not demonstrated.",
    "2": "Capability demonstrated for the bounded pilot.",
    "3": "Capability demonstrated at intended production scale, with ongoing monitoring."
  },
  "dimensions": [
    {
      "id": "leadership_sponsorship",
      "name": "Leadership / sponsorship",
      "assess": "Accountable executive, strategic outcome, decision rights and visible sponsorship",
      "evidence": "Signed charter, sponsor attendance and decision log",
      "accountable_role": "Executive sponsor",
      "gate": "A named empowered sponsor accepts the scoped outcome and escalation duties"
    },
    {
      "id": "skills",
      "name": "Skills",
      "assess": "Role coverage, practical competence, training and support capacity",
      "evidence": "Skills matrix, observed task assessments and training plan",
      "accountable_role": "People / learning lead",
      "gate": "Required roles demonstrate safe task performance and know when to escalate"
    },
    {
      "id": "workflow_process",
      "name": "Workflow / process",
      "assess": "Current and future workflows, handoffs, human review, exceptions and fallback",
      "evidence": "Process map, SOP, exception drill and baseline metrics",
      "accountable_role": "Process owner",
      "gate": "Rehearsed workflow has human review and a workable fallback"
    },
    {
      "id": "infrastructure_data",
      "name": "Infrastructure / data",
      "assess": "Integration, access, data quality, privacy, reliability and recovery",
      "evidence": "Data profiling, access review, integration and recovery test results",
      "accountable_role": "IT / data owner",
      "gate": "Approved data and access meet scoped quality, security and recovery needs"
    },
    {
      "id": "resources_budget",
      "name": "Resources / budget",
      "assess": "Implementation and recurring costs, staff time, procurement and contingency",
      "evidence": "Approved lifecycle budget, staffing allocations and vendor terms",
      "accountable_role": "Budget owner",
      "gate": "Funding and staff cover delivery, support and contingency for the assessment horizon"
    },
    {
      "id": "governance_risk",
      "name": "Governance / risk",
      "assess": "Risk assessment, legal obligations, assurance, monitoring and stop authority",
      "evidence": "Risk register, control tests, required approvals and incident exercise",
      "accountable_role": "Risk / compliance owner",
      "gate": "Required approvals and tested controls cover material harms; stop authority is assigned"
    },
    {
      "id": "culture_change",
      "name": "Culture / change",
      "assess": "User participation, trust, incentives, communication and resistance",
      "evidence": "Representative user feedback, engagement plan and adoption measures",
      "accountable_role": "Change lead",
      "gate": "Affected groups participate, understand impacts and have a feedback and support route"
    },
    {
      "id": "operating_ownership",
      "name": "Operating ownership",
      "assess": "Accountability after launch, service levels, incidents, maintenance and vendor exit",
      "evidence": "Accepted RACI, service runbook, on-call roster and exit exercise",
      "accountable_role": "Service owner",
      "gate": "Named owner accepts ongoing service, incident, maintenance and exit responsibilities"
    }
  ],
  "decision_rules": {
    "insufficient_evidence": "Any dimension unknown: request evidence; do not declare readiness.",
    "not_ready": "Any dimension 0 or 1, or any unmet applicable gate: remediate before the requested stage.",
    "pilot_ready": "All eight dimensions at least 2, all pilot gates met, bounded scope, human oversight, stop criteria and rollback verified.",
    "scale_ready": "All eight dimensions 3 and all production gates met with evidence at intended scale.",
    "aggregation": "Report every dimension and minimum rating; never average away a blocker."
  },
  "assessment_fields": [
    "dimension_id",
    "rating",
    "rationale",
    "evidence_reference",
    "evidence_date",
    "confidence",
    "gap",
    "action",
    "action_owner",
    "due_date",
    "gate_status",
    "current_strengths",
    "organizational_failure_gaps"
  ],
  "strength_fields": [
    "current_capability",
    "evidence_reference",
    "evidence_date",
    "adoption_enabling_mechanism",
    "scope_and_limits"
  ],
  "failure_gap_fields": [
    "condition",
    "evidence_status",
    "evidence_reference",
    "failure_mechanism_assuming_technology_works",
    "business_or_stakeholder_consequence",
    "severity_and_rationale",
    "affected_stakeholders",
    "dependencies",
    "mitigation",
    "action_owner",
    "proposed_due_date",
    "closure_evidence",
    "measurable_warning_trigger"
  ],
  "analysis_rules": [
    "Assess strengths and failure gaps for every dimension; summarize material findings across dimensions.",
    "Separate current demonstrated organizational strengths from plans and vendor capabilities.",
    "Distinguish verified deficiencies from evidence unknowns; label hypothetical failure mechanisms.",
    "Do not invent strengths or gaps; explicitly state when none are evidenced within scope.",
    "Assume technology meets technical performance requirements when assessing organizational failure mechanisms.",
    "Strengths cannot offset unrelated readiness blockers.",
    "Low organizational readiness must not be reported as low technology maturity or poor application fit.",
    "High maturity or supported application fit does not establish organizational readiness.",
    "Do not merge maturity, fit and readiness into one score; explain cross-layer constraints by causal source."
  ],
  "separate_findings": {
    "technology_maturity_capability": {
      "output_field": "general_et_finding",
      "basis": "Technology-level evidence only; unknown without supporting rubric and evidence."
    },
    "technology_application_fit": {
      "output_field": "application_finding",
      "classifications": [
        "supported",
        "conditional",
        "unsupported",
        "insufficient evidence"
      ],
      "basis": "Demonstrated capabilities compared with explicit application requirements; state synthetic assumptions."
    },
    "organizational_readiness": {
      "output_field": "organization_specific_finding",
      "basis": "Eight organizational dimensions and stage-specific gates; independent of maturity and fit."
    },
    "shared_required_fields": [
      "finding",
      "scope",
      "evidence_references",
      "confidence",
      "unknowns"
    ],
    "recommendation_rule": "Restate fit and readiness separately, then explain joint action; do not proceed while material technical or organizational conditions remain unmet."
  },
  "readiness_action_plan": {
    "output_field": "recommendation_management_implication",
    "priority_tiers": {
      "P0": "Mandatory safety, legal or operating gates blocking the requested stage.",
      "P1": "Other material failure risks and prerequisite capabilities.",
      "P2": "Improvements after earlier conditions are met."
    },
    "ordering": "Within tiers use consequence severity, dependency order and time criticality; explain uncertainty. All required conditions remain blocking regardless of rank.",
    "action_fields": [
      "rank",
      "priority_tier",
      "dimension_id",
      "linked_gap_or_unknown_and_evidence",
      "required_change_or_evidence_request",
      "failure_prevented_and_priority_rationale",
      "accountable_owner",
      "owner_status_assigned_inferred_or_proposed",
      "ownership_basis",
      "ownership_confidence",
      "supporting_roles",
      "dependencies_and_sequence",
      "proposed_timing_or_due_date",
      "measurable_acceptance_evidence",
      "stage_blocked"
    ],
    "ownership_rule": "Infer roles from supplied responsibility and authority, explain the basis, and mark inference. Use names only when supported. Ambiguity requires explicit management assignment of one accountable owner.",
    "closing_fields": [
      "immediate_next_action",
      "owner_confirmation_and_closure_decision_authority",
      "conditions_before_proceeding"
    ],
    "no_gap_rule": "State no material remediation evidenced; retain only justified proceeding or maintenance conditions."
  },
  "required_evidence_request": {
    "dimension_id": "resources_budget",
    "factor": "Funding approval authority",
    "status_in_supplied_profiles": "unknown",
    "question": "Who has delegated authority to approve this pilot's implementation and ongoing support spending? Please provide the current delegation-of-authority or budget approval record showing the accountable role, spending limit, scope and effective date.",
    "do_not_infer_from": [
      "sponsor enthusiasm",
      "executive title",
      "IT access authority",
      "staffing responsibility",
      "budget existence"
    ],
    "required_output_locations": [
      "organization_specific_finding",
      "recommendation_management_implication",
      "abstention_or_more_information_needed"
    ],
    "decision_effect": "Preserve explicitly stipulated approved budget as a strength; qualify pilot readiness on that stipulation. Require authority evidence before new spend, budget changes or scale. Unverified/disputed authorization leaves the relevant gate unresolved."
  }
}

