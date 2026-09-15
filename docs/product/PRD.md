# Product Requirements Document

## 1. Product

**Real Estate Lead Management & AI Qualification System**

## 2. Problem

Real-estate enquiries often arrive as unstructured messages. Sales staff
need to manually understand the customer's needs, capture information,
decide which leads deserve immediate attention, and follow up.

The system should automate the repetitive parts while keeping sales
staff in control.

## 3. Product Goal

Build a small, reliable system that:

1.  Receives customer enquiries.
2.  Understands customer intent.
3.  Extracts important property and customer requirements.
4.  Stores leads in a central database.
5.  Qualifies and scores leads.
6.  Responds to customers.
7.  Notifies the sales team when appropriate.
8.  Supports human follow-up.
9.  Tracks lead progress.

## 4. Target Users

### Customer

A person interested in buying, renting, selling, or enquiring about
property.

### Sales User

A member of the real-estate sales team who reviews, assigns, contacts,
and follows up with leads.

### Administrator

A user responsible for configuration, access, integrations, and
operational oversight.

## 5. Example Enquiries

-   "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget
    is around ₦80 million."
-   "Do you have any 2-bedroom apartments in Ikeja?"
-   "I need land around Ibadan, preferably below ₦20 million."
-   "Hello, I want to buy a house."

## 6. Lead Information

### Customer

-   Name
-   Email
-   Phone

### Property

-   Property type
-   Bedrooms
-   Location
-   Budget
-   Buy/rent

### Intent

-   Buying
-   Renting
-   Selling
-   Land
-   Property enquiry
-   Human-agent request

### Timing

-   Immediately
-   Within 1 month
-   Within 3 months
-   Just researching

## 7. Functional Requirements

### FR-001 Receive Message

The system must accept customer messages.

### FR-002 Understand Intent

The system must identify the likely customer intent.

### FR-003 Extract Requirements

The system should extract available structured requirements without
inventing missing information.

### FR-004 Store Lead

The system must persist lead data in PostgreSQL.

### FR-005 Qualify Lead

The system must calculate a deterministic lead score and classification.

### FR-006 Respond

The system must generate a useful response or clarification question.

### FR-007 Notify Sales

The system must notify sales for leads meeting notification rules.

### FR-008 Follow Up

Sales users must be able to create and track follow-ups.

### FR-009 Track Progress

Lead status and relevant activities must be persisted.

## 8. Non-Functional Requirements

-   Reliable persistence
-   Validated inputs
-   Clear API contracts
-   Secure handling of secrets
-   Observable failures
-   Testable business rules
-   Recoverable integration failures
-   Simple VPS deployment
-   Maintainable code

## 9. User Journey

``` text
Customer message
→ extraction
→ validation
→ lead update
→ qualification
→ response
→ sales notification
→ follow-up
→ status update
```

## 10. MVP Scope

Included:

-   Customer messaging/enquiry flow
-   Lead storage
-   AI extraction
-   Deterministic qualification
-   Sales notification
-   Sales lead view
-   Follow-up tracking
-   PostgreSQL
-   n8n automation
-   Docker/VPS deployment

Not initially included:

-   Complex property marketplace
-   Payments
-   Advanced recommendation engine
-   Multi-region infrastructure
-   Microservices

## 11. Acceptance Criteria

The MVP is successful when a realistic customer enquiry can travel
through the system from message receipt to stored lead, qualification,
response, and sales notification.

## 12. Success Metrics

Initial operational metrics:

-   Percentage of messages processed successfully
-   Percentage of leads stored successfully
-   AI extraction validation failure rate
-   Lead qualification completion rate
-   Notification success rate
-   Follow-up completion rate
-   End-to-end customer journey success rate

## 13. Assumptions

-   PostgreSQL is the system of record.
-   n8n is used for orchestration.
-   AI provider can return structured output.
-   Sales users have access to the sales interface.
-   The first deployment is a single VPS.

## 14. Future Scope

Potential future capabilities should be evaluated from real usage before
implementation.
