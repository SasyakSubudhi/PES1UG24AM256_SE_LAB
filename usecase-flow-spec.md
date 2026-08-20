# Use-Case Flow Specification

## Use Case: Log Maintenance Ticket
**Primary Actor:** Hostel Resident
**Related Use Cases:** «include» Attach Photo Evidence · «extend» Flag as Emergency

### Preconditions
- The resident is authenticated and logged into the ticketing system.
- The resident has a valid, active room assignment on file.

### Postconditions
- A new ticket exists with a unique ticket ID, timestamp, and status = "Open".
- The ticket is routed to the Maintenance Warden's queue, filtered by issue category.
- The resident receives a confirmation notification containing the ticket ID.

### Main Success Scenario
1. The resident selects "New Ticket" from the dashboard.
2. The system presents the ticket form, with the resident's room number pre-filled, plus fields for issue category, severity, description, and photo upload.
3. The resident selects an issue category (plumbing, electrical, or carpentry).
4. The resident selects a severity level (Low, Medium, High, or Critical).
5. The resident attaches photo evidence of the issue. **«include» Attach Photo Evidence** — this sub-flow (file picker, upload, and format/size validation) always executes as part of ticket creation.
6. The resident submits the ticket.
7. The system validates that all mandatory fields (room number, category, severity) are present.
8. The system generates a unique ticket ID and records the creation timestamp.
9. The system sets the ticket status to "Open" and routes it to the appropriate Warden queue based on category.
10. The system sends a confirmation notification to the resident containing the ticket ID.

### Alternate Flow A1: Emergency Flag («extend»)
**Trigger:** At step 4, the resident selects severity = "Critical".

1. The system offers an additional option: "Flag as Emergency." **«extend» Flag as Emergency** — this is an optional extension point on the base use case, only available when severity is Critical.
2. The resident selects "Flag as Emergency."
3. The system marks the ticket as emergency priority, placing it ahead of standard queue ordering.
4. The system immediately sends an SMS/push notification to the on-duty warden, in addition to standard queue routing.
5. The flow resumes at Main Success Scenario step 6 (resident submits the ticket).

### Notes
- The «include» relationship is mandatory: every ticket submission passes through the photo-attachment sub-flow, regardless of severity.
- The «extend» relationship is conditional: the emergency-flag sub-flow only becomes available/relevant when the base use case reaches step 4 with severity = Critical, per the use-case diagram's extension point.
