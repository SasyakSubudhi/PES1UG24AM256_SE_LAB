# Requirements Table — Hostel Maintenance & Issue Ticketing System
Problem Statement #07 | Campus & Academic Operations
Actors: Hostel Resident, Maintenance Warden

## Functional Requirements

| ID | Priority | Description | Acceptance Criteria | Rationale |
|----|----------|--------------|----------------------|-----------|
| FR-001 | High | The system shall allow a Hostel Resident to log a maintenance ticket by specifying room number, issue category (plumbing / electrical / carpentry), severity level, and an optional photo attachment. | **Pass:** Ticket is created with a unique ticket ID, all mandatory fields are validated, and it is routed to the warden queue. **Fail:** A ticket submitted without a room number or category is accepted. | Structured intake data lets the warden triage and route tickets without back-and-forth clarification, and geo/room tagging is the basis for dispatch. |
| FR-002 | High | The system shall allow the Maintenance Warden to assign an available technician to an open ticket based on issue category and current workload. | **Pass:** Ticket status changes to "Assigned", with technician name and ETA visible to the resident. **Fail:** Ticket remains unassigned after the warden confirms the assignment action. | Manual, unstructured dispatch is the main source of delay in hostel maintenance; formalizing assignment keeps ownership traceable. |
| FR-003 | Medium | The system shall allow residents to view real-time status updates (Open, Assigned, In Progress, Resolved, Closed) for tickets they submitted. | **Pass:** The status view reflects the latest warden update within 5 minutes. **Fail:** The status shown to the resident does not match backend records. | Reduces repeat queries/complaints to the hostel office and builds resident trust in the process. |
| FR-004 | High | The system shall require the reporting resident to confirm satisfactory resolution before a ticket transitions to "Closed". | **Pass:** A ticket only becomes Closed after resident sign-off (with optional rating/comment). **Fail:** A warden can close a ticket unilaterally without resident confirmation. | Prevents tickets from being closed prematurely and gives residents the final say on whether the issue was actually fixed. |
| FR-005 | Medium | The system shall maintain a searchable ticket history per room/resident, filterable by status, category, and date range. | **Pass:** Search returns results accurately matching the filter criteria. **Fail:** Closed tickets are missing or duplicated in the history view. | Supports recurring-issue detection (e.g. repeated plumbing failures in the same room) and audit needs for hostel administration. |

## Non-Functional Requirements

| ID | Type | Description | Acceptance Criteria | Rationale |
|----|------|--------------|----------------------|-----------|
| NFR-001 | Performance & Reliability | The system shall automatically trigger SMS/email escalation alerts to senior wardens when a high-priority ticket remains unresolved beyond a 24-hour SLA window. | **Pass:** Escalation alert fires within 5 minutes of SLA breach under simulated load. **Fail:** Alert is not sent, or is sent to the wrong recipient. | Guarantees critical issues (e.g. electrical hazards) get timely intervention instead of sitting silently in a queue. |
| NFR-002 | Security & Data Privacy | The system shall restrict ticket assignment, status override, and closure actions to authenticated Maintenance Warden accounts; residents may only view and act on their own tickets. | **Pass:** Role-based access tests confirm residents cannot view or modify other residents' tickets or perform warden-only actions. **Fail:** A role-escalation attempt succeeds in testing. | Protects resident privacy (room numbers, photos) and prevents accidental or malicious tampering with the maintenance workflow. |
