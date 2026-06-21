# /knowledge/knowledge_base.py
# This single file holds our exact chunked and sourced library for the AI to read. Ik it's lengthy but this is what we need to train it on.

rove_chunks = [
    # =========================================================================
    # SECTION 0: INTRODUCTION (PAGES 1-4)
    # =========================================================================
    {
        "text": """Welcome to Rove Member Support.
This Standard Operating Procedures (SOP) guide serves as the primary reference for all Member Support Representatives. It outlines the processes, standards, and best practices required to deliver a consistent, high-quality member experience while accurately supporting Rove's products and services.""",
        "source": "Introduction - Introduction"
    },
    {
        "text": """Rove is a travel rewards platform that helps members earn and redeem Rove Miles across flights, hotels, shopping, and loyalty program transfers. By combining travel booking, rewards earning, and flexible redemption options into a single platform, Rove helps travelers get more value from every trip and purchase.
Member Support plays a critical role in that experience. Our goal is not only to resolve issues, but to build trust, create clarity, and ensure every member feels supported throughout their journey.""",
        "source": "Introduction - About Rove"
    },
    {
        "text": """Our mission is to deliver fast, accurate, and empathetic support while helping members get the maximum value from Rove. Every interaction should leave the member more confident in both their resolution and in Rove itself.
Every interaction should leave the member feeling:
Heard
Understood
Reassured
Supported
We strive to provide service that is:
Calm and professional
Empathetic and respectful
Accurate and transparent
Efficient and solution-oriented
While we always advocate for our members, we must also set realistic expectations, follow company policies, and communicate clearly about what is and is not possible.""",
        "source": "Introduction - Our Support Philosophy"
    },
    {
        "text": """This guide exists to:
Ensure consistent member experiences
• Standardize support processes and procedures
Improve documentation and accountability
Reduce errors and duplicate work
Provide clear escalation paths
Help agents confidently resolve member issues
All Member Support Representatives are expected to follow the procedures outlined in this document and refer to it whenever handling member inquiries.""",
        "source": "Introduction - Purpose of This SOP"
    },
    {
        "text": """A core principle of Member Support at Rove is ownership. The agent assigned to a ticket is responsible for driving that issue toward resolution, even when assistance is required from another team, supplier, or partner. Escalating an issue does not transfer ownership.
Agents are expected to:
Follow up on open issues
Maintain accurate documentation
Communicate updates proactively
Ensure members are not left without information or next steps""",
        "source": "Introduction - Ticket Ownership & Accountability"
    },
    {
        "text": """This SOP is organized into the following sections:
1. Communication Standards
2. Atlas & Inbox Procedures
3. Response Time & Follow-Up Standards
4. Ticket Documentation
5. Ticket Statuses & Ticket Management
6. Support Contacts
7. Refunds & Compensation FAQ
8. Miles Transfer FAQ
9. Hotel Procedures
10. Flight Procedures
11. Shopping Procedures
12. Miles & Account Procedures
13. Document Information & Conclusion
Together, these sections provide the policies, workflows, and resources needed to effectively support Rove members across all products and services.""",
        "source": "Introduction - Contents of This SOP"
    },
    {
        "text": """Member support processes evolve as Rove grows. This SOP should be treated as a living document and may be updated periodically to reflect new products, features, suppliers, policies, and operational improvements.
If you identify outdated information, process gaps, or opportunities for improvement, notify your manager or team lead so the SOP can continue to improve alongside the member experience.""",
        "source": "Introduction - Continuous Improvement"
    },

    # =========================================================================
    # SECTION 1: COMMUNICATION STANDARDS (PAGES 5-13)
    # =========================================================================
    {
        "text": """Every member interaction should make the member feel:
Heard
Understood
Reassured
Supported
Every response should follow the GARAC formula:
Greet → Acknowledge → Reassure → Act → Close""",
        "source": "Communication Standards - Response Formula"
    },
    {
        "text": """Every responses should follow the GARAC formula:
Greet → Acknowledge → Reassure → Act → Close
Greet      Hi [Name], thank you for reaching out.
Acknowledge      I understand how frustrating that must be.
Reassure      I'll be happy to look into this for you.
Act      Here's what I'll do next...
Close      Please let me know if there's anything else I can help with.

Every member interaction should include all five elements whenever possible. Even when delivering unfavorable news, agents should acknowledge the member's concern, provide reassurance, explain the next step, and close professionally.

All responses should:
Follow the response formula (Greet → Acknowledge → Reassure → Act → Close);
Use approved tone and phrasing, and;
Align with Rove’s policies and current information.""",
        "source": "Communication Standards - Approved Guidelines"
    },
    {
        "text": """Our goal is not simply to respond to members. Our goal is to move every issue closer to resolution. Every response should accomplish at least one of the following:
Answer a question.
Gather missing information.
Provide a meaningful update.
Set clear expectations.
Advance the case toward resolution.
Avoid sending responses that do not move the issue forward.""",
        "source": "Communication Standards - Resolution Over Response"
    },
    {
        "text": """Even when another party controls the outcome, remain engaged and supportive throughout the process. Agents should avoid simply redirecting the member elsewhere when they can provide helpful guidance, verified information, or direct resources.
When possible, provide the member with the relevant information directly and include a direct link to the source. Only share information that has been confirmed as accurate.
Avoid: You'll need to contact the airline.
Prefer: The airline manages this type of request directly, but I'd be happy to explain the process and point you in the right direction.
Avoid: Please go to the hotel's website to confirm the bed type for this room rate.
Prefer: According to the hotel's website [embedded direct link], this room type has a King bed.
Rule of thumb: Do not make the member do extra work when the information can be verified and shared by the agent.""",
        "source": "Communication Standards - Taking Ownership"
    },
    {
        "text": """When responding to member concerns, we want to avoid sounding cold and robotic. Every interaction should include an empathetic response, clear reassurance, and some kind of resolution.
Preferred: 
Let me see what I can do to help
Could you please
Let me clarify
According to the booking terms
What I can do is
We are still awaiting a response
Let me find out.

Avoid:
That’s not our fault 
You need to
As I already said
Per policy
You can’t
No update
I don't know

When writing to a member, ask yourself: If I were the member receiving this message, would I feel informed, supported, and confident that someone is helping me? If the answer is no, revise the response before sending.
 """,
        "source": "Communication Standards - Tone Is Everything"
    },
    {
        "text": """When a member reports a problem, acknowledge the concern before requesting additional information.
Avoid: Send me the booking number.
Prefer: I'm sorry you're having trouble with your reservation. Could you please provide the booking number so I can look into this for you?
This one rule alone can make responses feel dramatically more human.""",
        "source": "Communication Standards - Acknowledge Before Asking"
    },
    {
        "text": """When requesting information from a member, explain why it is needed and avoid sounding demanding.
Avoid:
• Send your confirmation number.
Provide a screenshot.
We need proof.
Prefer:
• Could you please provide your confirmation number so I can investigate this further?
When you have a moment, could you send a screenshot of the error you're seeing?
To help us review this with the merchant, could you please provide a copy of your receipt?

Read your response before sending and ask yourself: "Could any part of this be interpreted as blaming, criticizing, or arguing with the member?" If the answer is yes, rewrite it.""",
        "source": "Communication Standards - Request Information Politely"
    },
    {
        "text": """The following phrases often come across as dismissive, defensive, or argumentative and should be avoided:
As I already explained...
As stated previously...
You need to...
You should have...
That's not our fault.
There's nothing we can do.
Per policy...
Unfortunately, that's your responsibility.
Like I said...
I already told you...
You must have...
Calm down.

Instead of:

You entered the wrong information.
You failed to complete the purchase. 
You didn’t read the booking terms.
That’s what you selected at checkout. 

Prefer:

It appears the information entered does not match the booking. 
It looks like the purchase may not have been completed successfully. 
The booking was made under the terms selected at checkout. 
Based on the reservation details, the booking was confirmed as non-refundable. 
""",
        "source": "Communication Standards - Phrases To Avoid"
    },
    {
        "text": """Answer the member's question directly. Avoid unnecessary jargon. Use short paragraphs. Clearly explain next steps. End with a clear action or expectation.""",
        "source": "Communication Standards - Keep Responses Clear and Concise"
    },
    {
        "text": """If an issue cannot be resolved immediately:
Explain what is happening.
Explain what action is being taken.
Provide a realistic timeline.
Commit to a follow-up date whenever possible.
Never send: No update.
Instead: We are still awaiting a response from the hotel. I know waiting isn't ideal and I appreciate your patience. I will follow up again no later than tomorrow at 3:00 PM ET.""",
        "source": "Communication Standards - Never Leave the Member Hanging"
    },
    {
        "text": """Never reference internal processes, systems, or team structures that are not relevant to the member.
Always use the verbiage MILES. Rove rewards flights, hotels, and shopping with miles. Always refer to rewards as miles. NEVER POINTS.
→ Company: Rove
→ Currency: Rove Miles (always capitalize Miles here)
Maintain Supplier Confidentiality: Never mention Nuitee, Tripedge, Duffel, Wildfire, or Loyalize directly. Refer to them as the hotel partner, airline, or merchant.""",
        "source": "Communication Standards - Member-Facing Language Standards"
    },
    {
        "text": """
Never promise:
● Refund approvals
● Supplier decisions
● Resolution timelines you do not control
Instead: We've submitted your request to the hotel and expect a response within 24–48 hours.
Not: You should receive your refund tomorrow.
In a situation where there is nothing more to be done, maintain empathy while setting clear expectations.
Instead: I understand this isn't the outcome you were hoping for. Based on the booking terms, no additional options are currently available, but I'm happy to answer any questions you may have.
Not: I completely understand your frustration. Let me take another look at this and see if there's anything more we can do.""",
        "source": "Communication Standards - Set Accurate Expectations"
    },
    {
        "text": """Writing Standards:
● Use complete sentences.
● Use proper grammar and spelling.
● Avoid slang.
● Avoid excessive exclamation marks.
● Avoid emojis unless specifically approved.
● Proofread before sending.
For example, avoid: Hey!! Lemme check that for u 🙂
Prefer: Hi [Name], I'd be happy to look into that for you.""",
        "source": "Communication Standards - Writing Standards"
    },
    {
        "text": """Handling Escalated Members:
If a member is upset:
Remain calm.
Do not argue.
Acknowledge their frustration.
Focus on solutions.
Avoid matching the member's tone.
Never: As I already explained…
Instead: I understand your concerns. Let me clarify what options are available.
""",
        "source": "Communication Standards - Handling Escalated Members"
    },
        {
        "text": """Personalize Every Interaction:
Whenever possible:
● Address the member by name.
● Reference the specific booking or issue.
● Avoid generic or copy-pasted sounding responses.
Instead of: We are reviewing your request.
Use: [Member Name], we are currently reviewing your hotel refund request and will provide an update by tomorrow.""",
        "source": "Communication Standards - Personalize Every Interaction"
    },
    {
        "text": """Always directly answer the member's question whenever possible.
● Do not bury the answer in multiple paragraphs.
● If the answer is no, say so professionally and explain why.
● If the answer is unknown, explain what information is still needed.
Avoid: Thank you for reaching out. We understand your concern and appreciate your patience while we investigate.
Prefer: The booking is non-refundable based on the terms selected at checkout. However, I have contacted the hotel to request an exception and will update you within 24 hours.""",
        "source": "Communication Standards - Answer the Question First"
    },
    {
        "text": """When You Don't Know, Verify:
● Never guess.
● Never assume policy details, supplier decisions, or account information.
● Verify before responding.
● If verification is required, tell the member what you are checking and when they can expect an update.

Avoid: I think the miles should post tomorrow.
Prefer: I'm verifying the status of your miles with our team and will provide an update within 24 hours.
""",
        "source": "Communication Standards - When You Don't Know, Verify"
    },
    {
        "text": """Read Before Replying:
This sounds obvious, but it's often the root cause of repeat complaints. Before replying, confirm that you have:
● Read the member's entire message.
● Reviewed all previous correspondence.
● Reviewed relevant notes and ticket history.
● Confirmed the booking details.
● Answered every question the member asked.
A good rule: If a member asked three questions, your response should address all three questions.""",
        "source": "Communication Standards - Read Before Replying"
    },

    # =========================================================================
    # SECTION 2: ATLAS & INBOX PROCEDURES (PAGES 14-18)
    # =========================================================================
    {
        "text": """Atlas Overview
● Atlas is Rove’s central platform for managing all member interactions across flights, hotels, and shopping.
● It helps us clearly understand each member’s needs and deliver a resolution quickly, all while going above and beyond to provide exceptional service.
● Every interaction is tracked in Atlas to ensure visibility, accountability, and accurate record keeping.
● All tickets, notes, escalations, and member communications must be documented in Atlas.""",
        "source": "Atlas & Inbox Procedures - Atlas Overview"
    },
    {
        "text": """Inbox Procedures: Standard Ticket Workflow:
1. Assign a ticket to yourself from the Unassigned inbox.
2. Review member history and previous interactions.
3. Add relevant tag(s) and priority to said ticket.
4. Respond to the member, and try to resolve any open tickets right away.
5. Update notes, tags, and status to said ticket.""",
        "source": "Atlas & Inbox Procedures - Inbox Procedures: Standard Ticket Workflow"
    },
    {
        "text": """Inbox Procedures: Before you respond, verify the following:
Assign the ticket to yourself.
Check member profile to review previous tickets, notes, and booking history.
Add appropriate tag(s) and priority.
Internal Collaboration: Use internal notes and sidebars to communicate with teammates without involving the member.
Maintain supplier confidentiality.
Use approved Rove terminology.""",
        "source": "Atlas & Inbox Procedures - Inbox Procedures: Before you respond, verify the following"
    },
    {
        "text": """Supplier Confidentiality
NEVER mention:
Nuitee
Tripedge
Duffel
Wildfire 
Loyalize

Instead, refer to them as:
Hotel partner
Airline
Merchant
""",
        "source": "Atlas & Inbox Procedures - Supplier Confidentiality"
    },
    {
        "text": """Rove Terminology Standards
Refer to rewards as miles, NEVER points. Capitalize “Miles” when referring to Rove Miles.
→ Company = Rove
→ Currency = Rove Miles 
""",
        "source": "Atlas & Inbox Procedures - Rove Terminology Standards"
    },
    {
        "text": """Types of Inboxes - Team Inboxes:
These are the inboxes that should include all team members. 
They are:
● All: all open tickets
● Unassigned
● My Tickets
● Tickets Needing Reply
● Bot Resolutions (temporary to monitor tickets that the AI bot has “resolved” and closed)
● Missing Miles (for only missing miles requests that haven’t been submitted)
● Pending
● Snoozed
● Archived (archived are the closed tickets)""",
        "source": "Atlas & Inbox Procedures - Types of Inboxes: Team Inboxes"
    },
    {
        "text": """Types of Inboxes - Personal Inboxes:
You may create inboxes to help you organize your tickets and respond to users more efficiently. Please make these inboxes visible to only yourself.
Some examples of inboxes would be:
● My Urgent Tickets (To be able to reference and check in more frequently on responses/updates to urgent ticket)
● My Pending Tickets (To check in throughout your shift, though maybe less frequently than My Urgent Tickets)
● My Snoozed Tickets (If you utilize the snooze option, seeing all “reminders” to yourself in one place)
● Unassigned - No Missing Miles tickets (This is useful for seeing new tickets come in that need a response right away (without having to scroll through all the missing miles tickets to find them))
NOTE: If a personal inbox is no longer useful, delete it.""",
        "source": "Atlas & Inbox Procedures - Types of Inboxes: Personal Inboxes"
    },
    {
        "text": """Forwarding Requests to Other Rove Team Members:
Do not provide internal Rove email addresses to members. If a member wants to contact a specific team member:
● Direct them to support@rove.com, and we will forward it to the proper person.
● Tag the appropriate person on the ticket or let them know about it.
● If they ask about an increased referral offer, send them the canned response.""",
        "source": "Atlas & Inbox Procedures - Forwarding Requests to Other Rove Team Members"
    },

    # =========================================================================
    # SECTION 3: RESPONSE TIME & FOLLOW-UP STANDARDS (PAGES 19-20)
    # =========================================================================
    {
        "text": """Every member inquiry must be tracked, documented, and followed through to completion. If another team member were to take over a ticket at any point, they should be able to immediately understand the issue, actions taken, current status, and next steps. All Member Support Representatives are expected to strictly adhere to Rove’s follow-up standards.""",
        "source": "Response Time & Follow-Up Standards - Overview"
    },
    {
        "text": """Service Level Expectations (SLA’s):
Channel: Target First Response Time:
Email/Ticket Within 4-6 hours.
Live Chat Within 1 hour.
Escalations Within 1 hour
Social Media Within 4 hours
These are maximum response times. Respond sooner whenever possible.""",
        "source": "Response Time & Follow-Up Standards - Service Level Expectations"
    },
    {
        "text": """No Silent Tickets: 
        Members should never be left wondering whether their issue is still being worked on. 
        
        If there is no update from a supplier, hotel, airline, or internal team, you must:
● Provide a status update anyway.
● Reconfirm the next follow-up date.
● Reassure the member that the case remains active.
If a resolution is not reached within the initial conversation, the ticket status must be clearly tracked. Your notes should allow another representative to instantly know what’s going on, what’s been done, and what needs to happen next, without needing to ask additional questions. Every interaction must include clear, structured notes in the system. 
""",
        "source": "Response Time & Follow-Up Standards - No Silent Tickets"
    },
    {
        "text": """Follow-Up Standards: 
        EVERY unresolved ticket must include:
Current status
Next action required
Assigned owner
Clear deadline
Follow-up every 24 hours minimum, even with no update.

If any of these elements are missing, the ticket is considered incomplete.
""",
        "source": "Response Time & Follow-Up Standards - Follow-Up Standards"
    },
    {
        "text": """Daily Ticket Management:
At the beginning of each shift:

● Review all assigned open tickets.
● Review tickets awaiting follow-up.
● Review escalated cases.
● Prioritize tickets approaching SLA deadlines.

Before ending each shift:

● Update all active tickets.
● Schedule outstanding follow-ups.
● Reassign tickets when necessary.
● Verify notes are complete.""",
        "source": "Response Time & Follow-Up Standards - Daily Ticket Management"
    },
    {
        "text": """Escalate Immediately When:
● Legal threats are made
● Media inquiries are received
● Chargebacks are mentioned
● Fraud is suspected
● A member requests management review
● A member reports discrimination or safety concerns""",
        "source": "Response Time & Follow-Up Standards - Escalate Immediately When"
    },

    # =========================================================================
    # SECTION 4: TICKET DOCUMENTATION, Statuses, & Management (PAGES 21-27)
    # =========================================================================
    {
        "text": """The representative assigned to a ticket is responsible for:
● Monitoring progress
● Following up as required
● Updating ticket notes
● Communicating with the member
● Ensuring resolution or proper reassignment
Tickets should never be abandoned or assumed to be handled by another team member without documented reassignment.""",
        "source": "Ticket Documentation - Ticket Ownership"
    },
    {
        "text": """Documentation Standards:
Every ticket update must include:

1. Summary of request (what the member asked for)
2. Key details (booking type (hotel, flight, etc.), dates, providers, constraints or exceptions)
3. Actions taken (contacts made, policies reviewed, escalations submitted, etc.)
4. Outcome/status (pending/resolved/escalated)
5. Next steps and timeline (what happens next and when)
Additionally, include when applicable:
● Supplier booking ID
● Slack thread links
● Screenshots or screen recordings
● Internal guidance received through Slack or other channels""",
        "source": "Ticket Documentation - Documentation Standards"
    },
    {
        "text": """Documentation Requirements for Unresolved Tickets:
If another representative takes over a ticket, they should immediately understand:
● What happened
● What has been done
● Current status
● What happens next
Every interaction must contain structured notes that make handoffs seamless.
""",
        "source": "Ticket Documentation - Documentation Requirements for Unresolved Tickets"
    },
    {
        "text": """Documentation Example:
Poor Example
● Member asked about refund.
● Emailed hotel.

Problems:
● Missing booking details
● Missing status
● Missing next steps
● Missing follow-up date

Good Example
● Member requested refund for Booking #12345.
● Non-refundable hotel reservation for June 15–18.
● Contacted hotel requesting goodwill exception.
● Awaiting hotel response.
● Member updated.
● Follow-up scheduled for June 9.

The bad tracking example causes delays, member distrust, and a poor member experience. The good tracking example streamlines efficiency, eliminates misunderstandings, and builds member confidence. 
""",
        "source": "Ticket Documentation - Documentation Example"
    },
    {
        "text": """Ticket Statuses & Ticket Management: Lifecycle
Every ticket must have a clear lifecycle:
Open → In Progress → Waiting → Resolved

Open: New ticket requiring action.
In Progress: Actively being worked on.
Waiting: Pending merchant/member response.
Resolved: Issue fully completed and confirmed.
""",
        "source": "Ticket Statuses & Ticket Management - Lifecyle"
    },
    {
        "text": """Pending Tickets:
Use pending when:
● Waiting on member response 
● Waiting on follow-up from a vendor
● Missing miles requests already submitted and won’t have a follow up available for at least a few weeks
● Any issue that doesn’t currently require action from Rove

Pending tickets leave the Open inbox and return to Open when a reply is received.

Open tickets are only tickets that need a response back from us (if someone responds to a Pending ticket it goes back to Open). 
""",
        "source": "Ticket Statuses & Ticket Management - Pending Tickets"
    },
    {
        "text": """Snoozed Tickets:
Use Snooze when: 
● You need a personal reminder to check on the ticket status, or follow up before your shift ends
● You don’t anticipate needing to hand off to another team member 
    ● You can snooze these for 24 hours if it’s the beginning of your shift
    ● If it’s the end of your shift, make sure to snooze for fewer hours so it un-snoozes during the hours of your next work day

Do not use Snooze for urgent tickets requiring active monitoring by another shift.

""",
        "source": "Ticket Statuses & Ticket Management - Snoozed Tickets"
    },
    {
        "text": """Shift Handoffs for Urgent Tickets:
If an urgent ticket cannot be resolved before your shift ends:
1. Leave the ticket open
2. Do not Snooze for 24 hours 
3. Do not mark as Pending 
4. Tag the next shift representative in ticket notes if you need constant monitoring
5. Copy relevant CS team members on emails and Slack threads
6. Leave any relevant information they would need to resolve in the notes 

The monitoring representative may temporarily reassign the ticket and then return ownership when appropriate.
""",
        "source": "Ticket Statuses & Ticket Management - Shift Handoffs for Urgent Tickets:"
    },
    {
        "text": """Closing Tickets:
Close tickets when:
● The issue is resolved 
● No further action is required
● The member has not responded within 24 hours on a non-urgent issue 
    ● Pending or snoozed tickets only
● Duplicate tickets have already been addressed 

Before closing a chat ticket, notify the member. 

Examples:
● "Is there anything else I can assist you with today? If not, I will go ahead and close this chat.”
● “Just checking in since I haven’t heard back from you. I’ll go ahead and close this chat for now, but if you need any more help, please feel free to reach out anytime."

NOTE: If the ticket is assigned to someone else but you resolve the issue for the user, try to let whoever is assigned to the ticket close it. 
""",
        "source": "Ticket Statuses & Ticket Management - Closing Tickets"
    },
    {
        "text": """Ticket Closure Requirements:
Tickets involving supplier action must remain open until resolution is confirmed. Do not close a ticket when:

● Waiting for supplier response
● Waiting for hotel confirmation number
● Waiting for cancellation approval
● Waiting for modification approval
● Waiting for refund confirmation
● Waiting for member acknowledgment of supplier outcome

A ticket may only be closed when:
● The requested action has been completed, or
● The member has been informed of the final outcome, and
● All required documentation has been recorded in Atlas.

""",
        "source": "Ticket Statuses & Ticket Management - Ticket Closure Requirements"
    },
    {
        "text": """Merging Tickets:
Merge tickets when:
The user has submitted multiple tickets regarding the same subject/issue
The user has reached out from multiple accounts 

NOTE: When merging tickets, make sure the member is aware that you are already working on their request, especially if they have reached out multiple times via chat. Merged tickets may appear to disappear from the member’s view, so use caution when merging tickets from upset or frustrated users.
""",
        "source": "Ticket Statuses & Ticket Management - Merging Tickets"
    },
    # =========================================================================
    # SECTION 5: SUPPORT CONTACTS (PAGES 28-43)
    # =========================================================================
    {
        "text": """General Information:
Rove Merchant Code: 7011 - Hotels & Lodging 
""",
        "source": "Support Contacts - General Information"
    },
    {
        "text": """Nuitee (Hotel Bookings)  
Contact Directory: 
Urgent Cases & Same-Day Waivers 

Email: emergencies@nuitee.com
Use for:
● Urgent cases where check-in is within 3 days, but the guest is not currently at or on the way to the hotel
● Refund requests due to an issue from Nuitee’s end
● Same-day waiver requests, when the guest is not on-site or en route 
● Emergency situations that require urgent supplier assistance before check-in

Do not use for:
● Guests currently at the hotel
● Guests currently on their way to the hotel
● On-the-spot/check-in issues requiring immediate in-resort assistance
● Refund requests due to personal reasons 

Note: If the guest is already at the hotel or on the way there, use the on-the-spot/in-resort contact instead.

Guest on site/En Route to Hotel
Email: inresort@nuitee.com

Use for:
● Guests currently at the hotel
● Guests on the way to the hotel 
● Immediate check-in related issues

Do not use for:
● Refund or waiver requests. 
● If the refund is requested due to a personal reason not related to an issue on our end, please email: member-support@nuitee.com 

Standard Support
Email: member-support@nuitee.com

Use for:
● Non-urgent requests
● General booking assistance 
● Refund requests due to personal reasons of the guest

Escalations 
Email: escalations@nuitee.com

Use only when:
● The appropriate support channel above has already been contacted
● The SLA has passed
● You have not received a response
● The issue remains unresolved
● The proposed resolution is unsatisfactory

Please remember that operations@nuitee.com will no longer be in use. 
""",
        "source": "Support Contacts - Nuitee (Hotel Bookings) --> Contact Directory"
    },
    {
        "text": """Phone Support (Urgent)
Phone number: +1 844 727 0478 (English)
Please CALL Nuitee if the guest cannot check in for their reservation. This line is for immediate help!
""",
        "source": "Support Contacts - Phone Support (Urgent)"
    },
    {
        "text": """Additional Nuitee Contacts:
Direct Contacts:
● khouche@nuitee.com
Level 2 Escalations:
● A.hajji@nuitee.com 
● ali.ops@nuitee.com
""",
        "source": "Support Contacts - Additional Nuitee Contacts"
    },
    {
        "text": """Escalate Immediately When:
● The hotel is unresponsive
● The supplier refuses a refund for a supplier-caused error
● The guest cannot check in
● The guest is stranded
● No reservation found
""",
        "source": "Support Contacts - Escalate Immediately When"
    },
    {
        "text": """Important Notes:
New email threads required:
When contacting any Nuitee inbox, always send a new email rather than replying to an existing thread. This helps ensure your request is received and handled by the appropriate team without delay. 

Team Visibility:
For all Nuitee requests:
● CC support-team@rove.com 
● On urgent issues, we recommend CC’ing Max as well

Nuitee Request Portal:
Track open Nuitee requests here: https://nuitehelp.zendesk.com/hc/en-us/requests 
    ● Note: you will need to create a password the first time you access the portal.
""",
        "source": "Support Contacts - Important Notes"
    },
    {
        "text": """TripEdge
Primary Contact:
Ethan Sayre and Linda Wee 
Phone: +52 984 206 3000
Contact through the designated Slack channel when needed. 

Do not contact TripEdge for:
● Booking modifications
● Name additions
● Special requests
Follow established support procedures for these request types.
""",
        "source": "Support Contacts - TripEdge"
    },
    {
        "text": """Duffel (Flights)
Duffel Link

Standard Support Process:
Most flight requests should first be reviewed in the Duffel portal to confirm the booking details, order status, fare rules, ticketing status, and any available self-service options.

When additional support is needed from Duffel, agents should contact Duffel through the appropriate channel: Chat or Email.

Use Duffel Chat for:

● Voluntary exchanges
● Voids
● Voluntary refunds
● Priority cases within 72 hours of booking or departure

Use Duffel Email for:

● Voluntary exchanges or refunds where a waiver is required, such as medical reasons
● Schedule changes
● Name corrections
● Ancillaries, including seat reservations or baggage
● Adding infant or child tickets
● Other complex cases or technical issues

Important: Before contacting Duffel, agents should gather all relevant booking details, member context, requested changes, fare rules, and supporting documentation when applicable. Do not promise any refund, exchange, waiver, or airline approval until Duffel or the airline has confirmed the outcome.

Modifications and Cancellations:
Requests for:
● Flight cancellations
● Flight modifications
Must be submitted through the Duffel website. 

Email Management:
After submitting a request through Duffel:
1. Wait for the confirmation email from Duffel.
2. Reply directly to that email thread. 
3. CC the entire Rove Support team.
This ensures visibility across the support team and allows others to assist if necessary. 
""",
        "source": "Support Contacts - Duffel (Flights)"
    },
    #ERROR TROUBLESHOOTING SUBTAB
    {
        "text": """Error Troubleshooting & Internal Escalations
         Workflow Error Monitoring
All All Member Support Representatives should have access to the #workflow-errors Slack channel. This channel is used to monitor booking and system errors that require investigation.""",
        "source": "Support Contacts -> Error Troubleshooting - Workflow Error Monitoring"
    },
    {
        "text": """Errors in this channel will either be:
● Duffel Flight Booking Errors
○ Flight booking failures or processing issues originating from Duffel.
● TripEdge Hotel Booking Errors
○ Hotel booking failures or processing issues originating from TripEdge.
○ For assistance, reach out in #tripedge-support channel
● LiteAPI Hotel Booking Errors
○ Hotel booking failures or processing issues originating from LiteAPI.
○ For assistance, reach out in #liteapi channel""",
        "source": "Support Contacts -> Error Troubleshooting - Booking Errors Types"
    },
    {
        "text": """Getting Assistance in the #support-team Channel
If you aren’t able to resolve an issue yourself, these are the steps to follow to get an engineer (or someone else) to take a look and assist. 

Step 1: Research the Issue First
Before asking for assistance:
● Search Slack for previous discussions. 
● Search Atlas for similar tickets or resolutions.
● Use keywords specific to the issue.
● Review any relevant SOP documentation.

Many common questions have already been answered and can be resolved without escalation.

Try to keep posts in #support-team to a minimum. Reducing repetitive questions helps keep the channel organized and makes important information easier for everyone to find.
If you cannot find the answer, or cannot troubleshoot the issue yourself after trying the best you can, then you can post in #support-team channel.""",
        "source": "Support Contacts -> Error Troubleshooting -> Getting Assistance in the #support-team Channel - Step 1: Research the Issue First"
    },
    {
        "text": """Step 2: Attempt Basic Troubleshooting
Before escalating:
● Review the booking details.
● Confirm the issue is reproducible.
● Verify the correct supplier, booking ID, and member information.
● Attempt any troubleshooting steps outlined in the SOP.

If you are still unable to determine the cause or resolution, proceed to Step 3.""",
        "source": "Support Contacts -> Error Troubleshooting -> Getting Assistance in the #support-team Channel - Step 2: Attempt Basic Troubleshooting"
    },
    {
        "text": """Step 3: Post in #support-team
If the issue cannot be resolved after reviewing available resources and completing basic troubleshooting, escalate internally for assistance.
For general support questions, post in #support-team. Keep your message concise while still providing all information needed for someone to help.
Include:
● Brief description of the issue
● Specific question or assistance needed
● User ID
● Booking ID
● Trip ID (for shopping-related issues)
● Screen recording or screenshots, if applicable
● Relevant links or documentation
● Any troubleshooting already performed

Good Example:
“Member unable to complete hotel booking. Error appears after payment submission.
User ID: 12345
Booking ID: ABC123
Supplier: TripEdge
Troubleshoo details listed above, along with any screenshots, screen recordings, error messages, links, or steps to reproduce the issue.
After submitting the ClickUp request, add the ClickUp link to the member’s internal ticket notes so the support team can track the status and follow up appropriately.""",
        "source": "Support Contacts -> Error Troubleshooting -> Getting Assistance in the #support-team Channel - Step 3: Post in #support-team"
    },
    
    {
        "text": """Step 4: Tag the Appropriate Team
Rule of thumb: Use ClickUp for Product/Engineering requests that need to be tracked;
use Slack tags for urgent visibility, clarification, or time-sensitive support.
Engineer On-Call: Each month an on-call schedule is published and pinned in #support-team.
When engineering assistance is needed:
● Create a ClickUp request if the issue requires Product or Engineering review, investigation, or follow-up.
● Tag the engineer currently on call in Slack when the issue is urgent, time-sensitive, or requires immediate visibility.
● Reference the member ticket, issue, and ClickUp task directly.
● Include all relevant details, screenshots, screen recordings, error messages, and troubleshooting already completed.ProcessLookupError

Tag @Engineers immediately only when:
● The issue is urgent
● The issue is time-sensitive
● Multiple members are affected
● The issue appears to be a widespread outage or system problem
If the on-call engineer does not respond and assistance is urgently needed, escalate to @engineers.

Tag @Support if you believe another member of Member Support may know the answer. You should also tag @support when a resolution or clarification would benefit the entire Member Support team. Note: @support includes Member Support team members only.
""",
        "source": "Support Contacts -> Error Troubleshooting -> Getting Assistance in the #support-team Channel - Step 4: Tag the Appropriate Team"
    },
    {
        "text": """Step 5: Link Slack Discussions to the Ticket
If there is a corresponding Atlas ticket:
● Copy the Slack thread link.
● Paste the thread link into the Atlas ticket notes.
This allows anyone reviewing or following up on the case to quickly access the full internal discussion and troubleshooting history.""",
        "source": "Support Contacts -> Error Troubleshooting -> Getting Assistance in the #support-team Channel - Step 5: Link Slack Discussions to the Ticket"
    },
    {
        "text": """Step 6: Monitor and Follow Up
After escalating:
● Monitor the Slack thread for responses.
● Follow up with the member as updates become available.
● Keep Atlas notes updated.

If no response is received within one business day:
● Reply in the Slack thread to follow up.
● Re-tag the appropriate person if necessary.
If additional follow-up is needed:
● Set a Slack reminder for yourself.
● Ensure the ticket remains assigned and actively monitored until resolution.
""",
        "source": "Support Contacts -> Error Troubleshooting -> Getting Assistance in the #support-team Channel - Step 6: Monitor and Follow Up"
    },
    {
        "text": """Expected Response Times
The response times below are internal guidelines and may vary depending on workload, supplier response times, and issue severity.
Internal Teams:
Team                         Expected Response Time
Member Support Team          Same business day
On-Call Engineer             Within 1 business day
@Engineers (urgent issues)   As soon as available
Management Escalations       Same business day""",
        "source": "Support Contacts -> Error Troubleshooting - Expected Response Times: Internal Teams"
    },
    {
        "text": """Suppliers:
Supplier                        Expected Response Time
Nuitee - In Resort / Urgent     Typically within 4 hours
Nuitee - Standard Cases         Within 1 business day
TripEdge Typically              same business day
LiteAPI                         Varies by issue
Hotel Direct Contact            Varies by property
Airline (via Duffel)            Can take several business days""",
        "source": "Support Contacts -> Error Troubleshooting - Expected Response Times: Suppliers"
    },
    {
        "text": """Follow-Up Expectations
If no response is received within the expected timeframe:
● Follow up through the original communication channel.
● Update the Atlas ticket with the follow-up.
● Notify the member that the request remains in progress.
● Continue monitoring until a response is received.

Members should never be left without updates simply because we are waiting on a supplier or internal team.

No Silent Tickets: Any ticket awaiting a response from a supplier, engineer, or another team member should receive member updates at least once every 24 hours, even if there is no new information available.
Example:
"We are still awaiting a response from our hotel partner. We have followed up again today and will continue monitoring the request closely. We will provide another update no later than tomorrow."
""",
        "source": "Support Contacts -> Error Troubleshooting - Follow-up Expectations"
    },
    {
        "text": """Ticket Ownership & Escalations
Ownership Principle: If you’re wondering who should follow up, it’s probably you.

Escalating an issue does not transfer ownership of the ticket.

The agent assigned to the ticket remains responsible for:
● Member communication
● Internal follow-up
● Supplier follow-up
● Updating Atlas notes
● Driving the issue toward resolution

When a Ticket Is Escalated

If a ticket is escalated to:
● Engineering
● Another Member Support Representative
● A Team Lead
● Management
● A Supplier
● A Hotel
● An Airline
The original assigned agent remains responsible for monitoring progress and communicating updates to the member unless ownership is explicitly reassigned.
""",
        "source": "Support Contacts -> Error Troubleshooting - Ticket Ownership & Escalations"
    },
    {
        "text": """
Ownership Transfer
Ownership should only change when:
● A manager requests reassignment.
● Another agent formally accepts ownership.
● The issue is transferred to a specialized team.
● Shift coverage procedures require reassignment.

Ownership transfers should be documented in Atlas notes.
""",
        "source": "Support Contacts -> Error Troubleshooting -  Ownership Transfer"
    },
    {
        "text": """
Follow-Up Responsibilities
The assigned agent should:
● Monitor Slack threads.
● Monitor supplier responses.
● Follow up when response deadlines are missed.
● Set reminders when necessary.
● Ensure the member receives updates throughout the process.
""",
        "source": "Support Contacts -> Error Troubleshooting -  Follow-Up Responsibilities"
    },
    {
        "text": """
Escalation Is Not Resolution
Submitting a request to Engineering, a supplier, or another team does not complete the task.
The ticket should remain assigned and actively monitored until:
● The issue is resolved.
● The member has been informed of the outcome.
● All documentation has been completed.

Incorrect: Agent sends a message to Engineering and assumes Engineering will handle member updates.

Correct: Agent escalates to Engineering, monitors the Slack thread, follows up when necessary, updates the member, and closes the ticket only after the issue is resolved.
""",
        "source": "Support Contacts -> Error Troubleshooting -  Escalation Is Not Resolution"
    },
    #Supplier Escalation Guidelines SUBTAB
    {
        "text": """
Supplier Escalation Guidelines
Before contacting a supplier, always determine whether the issue can be resolved internally.
""",
        "source": "Support Contacts -> Supplier Escalation Guidelines"
    },
    {
        "text": """
Internal Resolution First
Agents should first verify whether the action can be completed through Rove systems before contacting the supplier.
Examples:
● Refundable reservation cancellations that can be canceled through the CS Panel
● Reservation lookups available in Atlas or the CS Panel
● Member information updates that do not require supplier involvement

""",
        "source": "Support Contacts -> Supplier Escalation Guidelines - Internal Resolution First"
    },
    {
        "text": """
Supplier Escalation Required
Contact the supplier when:
● Internal cancellation fails
● The reservation cannot be modified internally
● Hotel confirmation information is missing
● A non-refundable cancellation exception is being requested
● A hotel approval is required
● The supplier must authorize a refund, modification, or waiver
""",
        "source": "Support Contacts -> Supplier Escalation Guidelines - Supplier Escalation Required"
    },
    {
        "text": """
Escalation Documentation
Whenever a supplier is contacted:
● Record the supplier contacted
● Record the date and time
● Record the method of contact (email, phone, Slack, etc.)
● Attach any supplier responses to the Atlas ticket
● Document next steps and expected follow-up timeline
""",
        "source": "Support Contacts -> Supplier Escalation Guidelines - Escalation Documentation"
    },
    # =========================================================================
    # SECTION 6: Refunds & Compensation FAQ (PAGES 44-58)
    # =========================================================================
    #SUBSECTION 1 in refunds & compensation FAQ: REFUND POLICIES
    {
        "text": """Refund Policy Overview
General Refund Timeline:
Refunds are typically processed within 5–10 business days after being issued, depending on the member’s bank or financial institution.""",
        "source": "SECTION 1: REFUND POLICIES -> Refund Policy Overview - General Refund Timeline"
    },
    {
        "text": """Never Promise Refunds
Agents must never:
● Promise a refund before it has been approved.
● Guarantee supplier reimbursement.
● Guarantee compensation.
● Commit to refund timelines outside of published policy.
● Represent a refund as approved when supplier approval is still pending.
● Always clearly explain what has been approved, what is pending, and what actions are being taken.

Instead, use language such as:
"We have submitted your request and will update you as soon as we receive a response." """,
        "source": "SECTION 1: REFUND POLICIES -> Refund Policy Overview - Never Promise Refunds"
    },
    {
        "text": """Refund Eligibility Workflow
Use the following workflow when evaluating any refund request:
Step 1: Determine Eligibility
● Is the reservation refundable?
● Is the request within the cancellation window?
● Does supplier approval apply?

Step 2: Confirm Cancellation Status
● Has the reservation been successfully canceled?
● If not, resolve the cancellation first.
Step 3: Review Rove Miles Usage
● Were Rove Miles used?
● If yes, follow the Rove Miles Refund Policy.
Step 4: Determine Refund Type
● Self-service refund
● Manual refund
● Supplier-authorized refund
● Exception case
Step 5: Process & Document
● Process refund
● Notify member
● Record notes
● Update tracking logs""",
        "source": "SECTION 1: REFUND POLICIES - Refund Eligibility Workflow"
    },
    {
        "text": """Self-Service Refunds (User-Initiated)
Members may process refunds through their account only when:
● The reservation is refundable.
● The request is within the cancellation window.
When a member successfully cancels through self-service:

● The reservation is automatically canceled in our system.
● The refund is automatically initiated.
● No additional action is required unless the member reports an issue.""",
        "source": "SECTION 1: REFUND POLICIES - Self-Service Refunds (User-Initiated)"
    },
    {
        "text": """Rove Miles Refund Policy
When This Applies
This process applies whenever:
● Used Rove Miles toward a flight or hotel reservation, and
● The reservation is later canceled, and
● The user is expecting a refund.""",
        "source": "SECTION 1: REFUND POLICIES -> Rove Miles Refund Policy - When This Applies"
    },
    {
        "text": """Full Refunds
Rove Miles are valued at $0.02 (2 cents) per mile.
The value of any miles used must be deducted from the refund amount before processing.""",
        "source": "SECTION 1: REFUND POLICIES -> Rove Miles Refund Policy - Full Refunds"
    },
    {
        "text": """Calculation Formula
Miles Used × $0.02 = Miles Value
Refund Amount − Miles Value = Final Refund Amount
Agents may use ChatGPT or a calculator to complete this calculation.
Example
Example Ticket Link
Miles Used: 1,770
1,770 × $0.02 = $35.40
If the original refundable amount is $202.49, then:
$202.49 − $35.40 = $167.09
Final Refund Amount: $167.09""",
        "source": "SECTION 1: REFUND POLICIES -> Rove Miles Refund Policy - Calculation Formula & Example"
    },
    {
        "text": """Member Communication Requirements
The user must be informed that miles were used on the canceled reservation.
Before processing the refund, explain:
● Number of miles used
● Miles valuation ($0.02 per mile)
● Total amount deducted from the refund
● Final refund amount
Obtain acknowledgment or confirmation from the user before completing the refund.""",
        "source": "SECTION 1: REFUND POLICIES -> Rove Miles Refund Policy - Member Communication Requirements"
    },
    {
        "text": """Documentation
● Record the miles calculation and refund details in the CS Panel.
● Add corresponding notes to the Refund Tracker for auditing and reference.""",
        "source": "SECTION 1: REFUND POLICIES -> Rove Miles Refund Policy - Documentation"
    },
    {
        "text": """Refunds Involving Rove Miles
If the user spent Rove Miles prior to cancellation:
● Inform the user that the miles were spent before the refund was processed.
● Advise the user that Rove Miles are valued at $0.02 (2 cents) per mile.
● Multiply the number of miles spent by $0.02 to calculate the monetary value.
● Inform the user of the amount that will be deducted from the refund total.""",
        "source": "SECTION 1: REFUND POLICIES - Refunds Involving Rove Miles"
    },
    {
        "text": """Alternative Rebooking Option
As an alternative option to deducting miles from the refund:
● The member may apply the value of the spent miles toward a new reservation.
● The new reservation must be equal to or greater than the value of the miles spent.
● In this case, the miles may be deducted from the new reservation instead of the refund.""",
        "source": "SECTION 1: REFUND POLICIES - Alternative Rebooking Option"
    },
    {
        "text": """Partial Refunds for Mile-Paid Reservations
This typically occurs when:
● Hotel dates are shortened
● Rooms are downgraded
● Supplier issues a partial refund
If the user is issued a refund from Nuitee/Tripedge for a partial amount in $ but the user paid in miles (example: changing reservation to fewer days), then calculate their refund according to the booking type, as detailed below.
Calculating Rove Rate Refunds
Rove Rate bookings are valued at 1.3 cents per mile.
Formula:
New Supplier Rate ÷ .013
Round up to the nearest 1,000 miles.
Subtract this new amount from their original User Paid miles. 
Calculating Loyalty Eligible Refunds
Loyalty Eligible bookings are valued at 1.5 cents per mile.
Formula:
New Supplier Rate ÷ .015
Round up to the nearest 1,000 miles.
Subtract this new amount from their original User Paid miles.
Example
User paid 49,000 miles for 5 nights on a Rove rate hotel
User wanted to change to 3 nights
Nuitee quoted $420 for 3 nights
$420 divided by .013 = 32,307 > Round up to 33,000 (new price)
49,000 - 33,000 = 16,000 miles refunded to the user""",
        "source": "SECTION 1: REFUND POLICIES - Partial Refunds for Mile-Paid Reservations & Calculations"
    },
    {
        "text": """Exception Cases
Guest Required to Pay Hotel Again
This applies when:
● The guest is unable to check in upon arrival.
● The hotel cannot locate the reservation.
● The reservation contains a supplier error.
● The guest must pay again or secure alternate accommodations.
We get a full refund of the original booking + the difference in what the guest paid for the new booking and the supplier rate on the original booking.""",
        "source": "SECTION 1: REFUND POLICIES -> Exception Cases - Guest Required to Pay Hotel Again Overview"
    },
    {
        "text": """Resolution
Obtain:
● Proof of payment
● Replacement reservation confirmation (if applicable)
Then:
● Request supplier cancellation without penalty.
● Request supplier reimbursement for the rate difference.
● Refund the member accordingly.""",
        "source": "SECTION 1: REFUND POLICIES -> Exception Cases - Guest Required to Pay Hotel Again Resolution Steps"
    },
    {
        "text": """Example
A user books a non-refundable hotel and pays at booking. The supplier is Nuitee and you can see that:
    ● User paid $200
    ● Supplier price $160
When the guest arrives at the hotel, they cannot find their reservation or there is an error. They end up paying again directly to the hotel at a rate of $220.

Member Paid Hotel Directly: $220
We request Nuitee cancels the reservation for free and covers the difference in rate.
Supplier Reimbursement:
Nuitee’s difference in rate: $60 ($220 – $160). 
Supplier should reimburse Rove $60.
Member Refund:
Original Booking Refund: $200
Additional Rate Difference: $20
Total Member Refund: $220
The user would keep the miles from the hotel booking in this case, as the difference of $40 in margin covers the miles.""",
        "source": "SECTION 1: REFUND POLICIES -> Exception Cases - Guest Required to Pay Hotel Again Example"
    },
    {
        "text": """Chargeback Prevention
Whenever a refund amount differs from what a member expects:
● Clearly explain the refund calculation.
● Provide a breakdown of any miles deductions.
● Explain applicable supplier policies.
● Obtain written acknowledgment whenever possible.
Proper documentation helps protect against future chargebacks and disputes.""",
        "source": "SECTION 1: REFUND POLICIES -> Exception Cases - Chargeback Prevention"
    },
    {
        "text": """Compensation Policy
Guiding Principles
Compensation should:
● Be reasonable and proportional.
● Resolve member dissatisfaction.
● Be documented.
● Be issued consistently.
● Avoid creating unreasonable expectations.
● Whenever possible, compensation should be obtained from the supplier first.

Compensation can be provided for hotel issues or flight booking issues, like

● Hotel mapping issue (wrong hotel booked)
● Issues with guest’s room or hotel
● Check-in issues
● Overbooking situations
● Flight booking issues
● And many more
There is a plan to standardize the amount given for each specific scenario, but until then, please log all compensation given to users (either Rove Miles or cash given) in this spreadsheet. 

https://docs.google.com/spreadsheets/d/15ZUidfWEvtbiyHty422v4B9O9GgmrSzGrDB70vB6w-U/edit?gid=0#gid=0

*Please note: Only add compensation given out of our own pocket, not compensation provided by Nuitee/Tripedge or the hotel.""",
        "source": "SECTION 1: REFUND POLICIES -> Compensation Policy - Guiding Principles"
    },
    {
        "text": """Types of Compensation
Supplier-Funded Compensation
Examples:
● Hotel-approved refund
● Airline-approved refund
● Supplier goodwill credit

Supplier-funded compensation should be passed through to the member.

Rove-Funded Compensation
Examples:
● Service recovery
● Booking issues
● Member inconvenience
● Goodwill gestures
Compensation may be issued as:
● Rove Miles
● Cash""",
        "source": "SECTION 1: REFUND POLICIES -> Compensation Policy - Rove-Funded Compensation"
    },
    {
        "text": """Compensation Authority Matrix (Example)
Compensation Amount                Approval Required
Up to 2,500 Rove Miles                Member Support Agent
2,501–10,000 Rove Miles              Team Lead
10,001+ Rove Miles                  Manager
Any Cash Compensation              Manager Approval
$250+ Cash Compensation         Director Approval
These thresholds are examples and may be adjusted as the support team grows.""",
        "source": "SECTION 1: REFUND POLICIES -> Compensation Policy - Compensation Authority Matrix (Example)"
    },
    {
        "text": """Compensation Tracking
All Rove-funded compensation must be recorded in the Compensation Tracker.
Include:
● Ticket ID
● Member Name
● Reason
● Compensation Amount
● Agent Name
● Date Issued
Do not record compensation provided by:
● Hotels
● Airlines
● Nuitee
● Tripedge
● Other suppliers
Only track compensation paid directly by Rove.""",
        "source": "SECTION 1: REFUND POLICIES -> Compensation Policy - Compensation Tracking"
    },
    {
        "text": """Hotel Complaint Compensation
Common Scenarios
● Cleanliness issues
● Broken room items
● Missing amenities
● Maintenance concerns
● Service complaints
● Other issues unrelated to the Rove booking

Important Policy
These issues are ultimately the responsibility of the hotel, and it’s on the hotel to provide compensation that we can then issue to the guests. 
Refunds are not automatically owed simply because a member reports dissatisfaction. It is technically not our/the supplier's responsibility to cover these kinds of hotel issues, and a refund isn't owed typically unless the hotel approves it with the guest.
The hotel should be given an opportunity to resolve the issue before compensation is considered.
Rove may choose to provide goodwill compensation when:
● The hotel is unresponsive.
● The hotel refuses reasonable assistance.
● The member experienced significant inconvenience.
● A service recovery gesture is appropriate.""",
        "source": "SECTION 1: REFUND POLICIES -> Compensation Policy - Hotel Complaint Compensation & Policy"
    },
    {
        "text": """Agent Workflow
Step 1: Gather Evidence
Request:
● Photos
● Videos
● Emails
● Text messages
● Other supporting documentation
Get any kind of evidence of the issues at the hotel and/or evidence of their report to hotel staff before reaching out to the supplier.

Step 2: Confirm Hotel Notification
Determine whether the member reported the issue while staying at the property.
Examples:
● Front desk complaint
● Hotel manager involvement
● Room change request
This step is important in order to give the hotel a chance to provide a resolution like a different room or other compensation.

Step 3: Encourage Hotel Resolution
Gently let the guest know that:
● The hotel controls room operations.
● The hotel is best positioned to provide compensation.
it is the hotel's responsibility to compensate in these cases
encourage the guest to continue reaching out to the hotel for approval

● Rove will assist in seeking a resolution.

Step 4: Escalate to Supplier
Provide all supporting documentation when contacting the supplier.""",
        "source": "SECTION 1: REFUND POLICIES -> Compensation Policy - Hotel Complaint Agent Workflow"
    },

    # =========================================================================
    # SUBSECTION 2 in refunds & compensation FAQ: REFUND PROCEDURES
    # =========================================================================
    {
        "text": """Manual Refund Processing (Agent-Assisted)
Manual refunds are required when:
● Self-service cancellation fails.
● Additional verification is required.
● Supplier involvement is required.
● An exception case exists.

Step 1: Identify Reservation
Ask the user for the Reference ID if it was not provided.
Use the Reference ID to locate the booking in the system.

Step 2: Verify Cancellation Status
Confirm that the reservation has been successfully canceled in our system.
In some cases, a user-initiated cancellation may show an error and not fully process, prompting the user to contact support for manual review.

Step 3: Review Rove Miles Usage
Determine whether any miles adjustments are required.
Check whether Rove Miles were applied to the reservation.
Verify whether the miles were used or remain unused.

Step 4: Locate Payment Intent ID
Navigate to the user’s account in the CS Panel.
Open Stripe Payments.
Locate the Payment Intent ID associated with the reservation.

Step 5: Process Refund
Copy the Payment Intent ID.
Select Stripe Search from the left-hand panel.
Paste the Payment Intent ID into the search bar.
Process the refund for the appropriate amount.""",
        "source": "SECTION 2: REFUND PROCEDURES - Manual Refund Processing (Agent-Assisted)"
    },
    {
        "text": """Flight Refunds & Cancellations
Flights cannot always be canceled directly by the user and may require manual handling.
Step 1: Gather Flight Information
Obtain:
● Flight confirmation code (if it was not provided or if it is unclear which flight needs to be canceled)
● Passenger information (if needed)
Step 2: Cancel in Duffel
● Log in to Duffel
● Select Manage This Order
● Select Cancellation Quote""",
        "source": "SECTION 2: REFUND PROCEDURES -> Flight Refunds & Cancellations - Steps 1 to 2"
    },
    {
        "text": """Step 3: Determine Eligibility
Void Within 24 Hours (US DOT Guidelines):
● If the flight is within 24 hours of booking, select VOID via Duffel’s Live Chat function. 
● Delete the pre-filled sentence and enter: “Please cancel right away. No quote is needed as this is a void within 24 hours.”
Outside 24-Hour Period:

Submit a cancellation quote through the appropriate channel: Chat or Email. Leave the pre-filled sentence intact and request the quote. 
Use Duffel Chat for:
● Voluntary exchanges
● Voids
● Voluntary refunds
● Priority cases within 72 hours of booking or departure
Use Duffel Email for:

● Voluntary exchanges or refunds where a waiver is required, such as medical reasons
● Schedule changes
● Name corrections
● Ancillaries, including seat reservations or baggage
● Adding infant or child tickets
● Other complex cases or technical issues

Important: Before contacting Duffel, agents should gather all relevant booking details, member context, requested changes, fare rules, and supporting documentation when applicable. Do not promise any refund, exchange, waiver, or airline approval until Duffel or the airline has confirmed the outcome.""",
        "source": "SECTION 2: REFUND PROCEDURES -> Flight Refunds & Cancellations - Step 3: Determine Eligibility"
    },
    {
        "text": """Step 4: Member Approval
● Duffel will respond with the applicable refund amount.
● Present this information to the guest.
● Obtain confirmation from the guest before proceeding with the cancellation.
Step 5: Refund Processing
If Duffel confirms a refund has already been issued, but it has not yet appeared in the Duffel wallet:
● Refund the member immediately.

If Duffel is awaiting airline reimbursement:
● Follow up after one week.
● Refund the member once Duffel confirms reimbursement has been received.
● If Duffel confirms they issued a refund but it hasn’t posted to the Duffel wallet yet, go ahead and refund the user (per Max)
● If Duffel says they submitted a refund request to the airline and are waiting for the airline to refund them, wait at most 1 week then follow up with Duffel.  As soon as Duffel confirms they processed the refund back to us, refund the user.""",
        "source": "SECTION 2: REFUND PROCEDURES -> Flight Refunds & Cancellations - Steps 4 to 5"
    },
    {
        "text": """Documentation Requirements
Before closing any refund or compensation case, verify:
● Refund amount is correct.
● Miles calculations are documented.
● Member has been informed.
● Atlas notes are complete.
● Refund Tracker has been updated.
● Compensation Tracker has been updated (if applicable).
● Supplier correspondence has been attached.
No refund or compensation case should be closed without complete documentation.""",
        "source": "SECTION 2: REFUND PROCEDURES - Documentation Requirements"
    },
    {
        "text": """Hotel Complaint Response Template
Thank you for reaching out to Rove Support. We are sorry to hear that your stay did not meet your expectations and understand how frustrating that can be.
To help assist, could you please confirm whether you spoke with the hotel's management team regarding the issue? Hotel management is best equipped to address on-site concerns such as cleanliness, maintenance, room conditions, missing amenities, or service-related matters.
If you have not yet spoken with a manager, we kindly encourage you to do so and let us know the outcome. If the issue was not resolved, please provide any photos, videos, emails, or other documentation of the issue, along with the name of the manager or staff member you spoke with, if available.
As a third-party booking provider, we do not manage the hotel and cannot independently authorize monetary compensation. Any refund or compensation must be approved by the hotel directly. Once we receive the information above, we will be happy to review the details and assist further.""",
        "source": "SECTION 2: REFUND PROCEDURES - Hotel Complaint Response Template"
    },
    # =========================================================================
    # SECTION 7: Miles Transfer FAQ (PAGES 58-61)
    # =========================================================================
    {
        "text": """List of Transfer Partners
Rove Miles Transfers
Eligible Transfer Programs
● Rove Miles may only be transferred out to participating “miles and points” loyalty programs.""",
        "source": "Miles Transfer FAQ - Eligible Transfer Programs"
    },
    {
        "text": """Transfer Timing and Processing
● Air India transfers are not instant and may require additional processing time -- up to 5 days. Transfers to all other partner airlines are generally instant.
● If a transfer is not instant, the delay is typically due to the airline conducting a fraud review.
● For Japan Airlines - JAL Mileage Bank, they typically have a rule that JMB accounts must be open 60 days before redeeming miles for awards.  HOWEVER, it is different with Rove transfers. Please note JAL transfer message on site:
    ● Rove transfers will be available to be redeemed after 6 PM Japan Standard Time on the date of enrollment or 6 PM Japan Standard Time the following business day.

If this message is still on Japan Airlines, it will disappear based on the above timeframe, so let the user know to re-check later.""",
        "source": "Miles Transfer FAQ - Transfer Timing and Processing"
    },
    {
        "text": """Delayed Transfers
● If a transfer has not completed after 2-3 days, the user should be instructed to contact Rove support.
● Reach out to engineers to check the status of the transfer.""",
        "source": "Miles Transfer FAQ - Delayed Transfers"
    },
    {
        "text": """Fraud Review Thresholds
● Some airline partners may automatically initiate fraud reviews for transfers of 200,000 miles or more.
● These reviews are conducted solely by the airline and may result in additional processing time before the transfer is completed.""",
        "source": "Miles Transfer FAQ - Fraud Review Thresholds"
    },
    {
        "text": """Internal Rove Miles Transfers (Transfers between Users)
We can transfer miles between two user accounts. Rules for internal transfers:
● Double check the IDs and accounts for both users before proceeding
● Each user can only send miles to other users 3 times annually
● Each user can only receive miles from other users 3 times annually
● Maximum 200,000 miles per transaction
● Minimum to transfer between accounts: 2,000 miles, up to 3 times annually (per Max)""",
        "source": "Miles Transfer FAQ - Internal Rove Miles Transfers Rules"
    },
    {
        "text": """Other notes on user-to-user transfers:
● Only allow users to transfer miles to someone else; they cannot have another user’s miles transferred into their account without approval directly from the other account holder (like if both users are cc’d on the email)
● Note the transfer on the two account pages so we can keep track of how many more transfers they can make""",
        "source": "Miles Transfer FAQ - Internal Rove Miles Transfers Tracking & Approvals"
    },
    # =========================================================================
    # SECTION 8: Hotel Procedures (PAGES 62-77)
    # =========================================================================
    
    {
        "text": """Hotel Procedures
1. Hotel Miles Earning Policy
Example case: Ticket Link

Standard Hotel Bookings
Miles post based on the booking’s cancellation policy:
● Non-refundable bookings: Miles are added immediately after booking (including bonus).
● Refundable bookings: Bonus miles and the normal miles for the stay are added after the stay is completed, typically within 1 day after checkout.
● Promotional or bonus miles: Bonus miles are not shown in pending; they are added manually.""",
        "source": "Hotel Procedures - Hotel Miles Earning Policy: Standard Hotel Bookings"
    },
    {
        "text": """Loyalty Eligible Bookings
For Loyalty Eligible bookings, miles post 8–12 weeks after checkout for both refundable and non-refundable reservations. 
Where users can find the Loyalty Eligible rates:

Loyalty Eligible rates:
● Can be searched and booked on the website at least 48 hours in advance.
● Appear in a separate tab from Rove Rate options on the room and rate selection page.
● Prompt the user to add their hotel loyalty number during checkout.
● May offer “pay at hotel,” making the hotel the merchant of record.
● Are useful for users who want to use a hotel-branded credit card, hotel credit, or receive loyalty benefits.
If a user selects a Rove Rate room at a Loyalty Eligible hotel, a checkout disclaimer will explain that the rate does not come with loyalty benefits. Example of the disclaimer:""",
        "source": "Hotel Procedures - Hotel Miles Earning Policy: Loyalty Eligible Bookings"
    },
    {
        "text": """Member Response: Miles Posting
Use the following response when a member asks when hotel miles post:
“Non-refundable hotels earn miles immediately after booking. Refundable hotels will earn miles once your stay is completed. Loyalty Eligible bookings may take 8–12 weeks after checkout for miles to post.”
When responding to members, always set expectations using the longest published timeline.""",
        "source": "Hotel Procedures - Hotel Miles Earning Policy: Member Response - Miles Posting"
    },
    {
        "text": """2. Hotel Cancellation Overview
Before handling any cancellation request, agents must first confirm:
● Booking reference code
● Booking policy
● Refundability
● Cancellation deadline
● Supplier
● Whether Rove Miles have already posted or been used
Agents can search for the booking in the CS Panel using:
● Booking reference
● User ID from Atlas
● User phone number
● User email
Only cancel the reservation the member specifically requests to cancel.""",
        "source": "Hotel Procedures - Hotel Cancellation Overview"
    },
    {
        "text": """Cancelling Refundable Reservations
 
Refundable bookings can be cancelled directly from the user’s account under “My Trip.” The refund will be automatic and will process within 5-10 business days. 

If a user is unable to cancel a refundable reservation themselves:
1. Make sure the refund deadline has not passed. 
2. Cancel within the panel located on the hotel booking screen (see image). 
3. Refund payment and cancel pending miles if not already done. 
4. Note: You do not need to reach out to the supplier to cancel a refundable reservation if you have the ability to cancel on the panel internally. 
5. If you run into an issue cancelling, contact the engineering team to look into it. 

If the guest is unable to cancel from their end, you may cancel manually on the booking page (see more below).""",
        "source": "Hotel Procedures - Hotel Cancellation Overview: Cancelling Refundable Reservations"
    },
    {
        "text": """3. Refundable Hotel Cancellation Workflow
When This Applies
Use this workflow when:
● The reservation is refundable.
● The cancellation deadline has not passed.
● The member wants to cancel the hotel booking.
Example ticket: Ticket link

Step 1: Request Booking Reference
If the member has not provided the booking reference, ask:
“Hi, can you please provide the short booking reference code for the reservation you’d like to cancel?”
Make sure the member confirms which reservation they want canceled.
Step 2: Confirm Refundability
In the CS Panel:
● Search the booking reference.
● Confirm the reservation is refundable.
● Confirm the cancellation deadline has not passed.
● Confirm the supplier booking ID if needed.""",
        "source": "Hotel Procedures - Refundable Hotel Cancellation Workflow: Steps 1 to 2"
    },
    {
        "text": """Step 3: Cancel the Reservation
If the booking can be canceled internally:
● Cancel the reservation from the hotel booking screen in the CS Panel.
● Cancel pending miles if not already done.
● Refund payment if the booking was paid to Rove.
If the booking cannot be canceled internally:
● Contact the appropriate supplier.
● If there is a technical issue preventing cancellation, contact Engineering.
Tag Kevin in Atlas & DM him in Slack once the cancellation request is sent or confirmed. 
Step 4: Notify Member
Once cancellation is confirmed, send:
“Your reservation has been cancelled successfully. Refunds typically process within 5–10 business days, depending on your bank or financial institution. Thank you for using Rove!”
Step 5: Document and Close
Before closing the ticket:
● Add internal notes confirming cancellation.
● Include refund timeline communicated to the member.
● Tag relevant team members if needed.
● Close the ticket once no further action is required.""",
        "source": "Hotel Procedures - Refundable Hotel Cancellation Workflow: Steps 3 to 5"
    },
    {
        "text": """4. Supplier-Assisted Refundable Cancellations
In some cases, a refundable reservation may need to be canceled through the supplier.
Nuitee Cancellation Request
For non-urgent matters, email member-support@nuitee.com. 
For urgent matters, email emergencies@nuitee.com. 
Emails should include: 
● Short booking reference
● Supplier booking ID
● Cancellation request
Example:
“Hello Nuitee Team,
Please cancel the following reservation:
Short booking ref: [Booking Reference]
Supplier booking ID: [Supplier Booking ID]
Thank you.”

Internal Notification
Once the cancellation request is sent or confirmed:
● Tag @Kevin in Atlas.
● DM Kevin in Slack with the ticket link.
● Keep the Atlas ticket open until cancellation is confirmed.""",
        "source": "Hotel Procedures - Supplier-Assisted Refundable Cancellations"
    },
    {
        "text": """5. Non-Refundable Hotel Bookings
Standard Policy
Non-refundable bookings are not automatically eligible for cancellation or refund.
Member response:
“This reservation was booked under a non-refundable rate and is not eligible for a refund under the booking terms. I understand this situation is frustrating. I’d be happy to explore whether any exceptions may be available.”
Agents must not promise cancellation, refund approval, or supplier flexibility.

Supplier or Hotel Approval Required
Non-refundable cancellations are at the discretion of the hotel and must be confirmed with the  supplier (Nuitee or TripEdge). Do not promise the user the reservation can be cancelled, as the hotel may decide to adhere to their non-refundable policy and deny the cancellation.
When escalating:
● Confirm the booking policy.
● Identify the supplier.
● Include the supplier ID in the ticket and link if possible.
● Contact the appropriate supplier using the Supplier ID from the CS panel.
● CC the entire support team.
● Document all supplier communication in Atlas.""",
        "source": "Hotel Procedures - Non-Refundable Hotel Bookings Standard Policy & Supplier or Hotel Approval Recquired"
    },
    {
        "text": """6. Non-Refundable Cancellation Request Procedure
Use this workflow when a member wants to cancel a non-refundable hotel booking.
Step 1: Confirm Member Agreement
Before contacting the supplier, the member must agree to the terms in the canned response:
“Confirm Cancellation Terms - STEP 1”
Do not proceed until the member replies with clear confirmation, such as:
● “Yes”
● “Confirmed”
● “I agree”
Note: This canned response includes a request for approval from the hotel. 
Step 2: Provide Hotel Approval Template
Send the canned response:
“Template for Hotel Cancellation Approval”
This gives the member clear language to use when requesting cancellation approval from the hotel.
Step 3: Contact Supplier
If hotel approval is received or supplier escalation is appropriate:
● Contact the correct supplier.
● Include supplier booking ID.
● Attach proof of hotel approval if provided.
● Document all steps in Atlas.
Step 4: Handle Miles Before Refund
If the hotel or supplier approves cancellation free of charge:
● Check whether the member has used the miles earned from the stay.
● If the member still has enough miles, deduct the miles and process the approved refund.
● If the member does not have enough miles, inform them that the miles value will be deducted from the refund at a rate of $0.02 per mile.
● Get member confirmation before processing.""",
        "source": "Hotel Procedures - Non-Refundable Cancellation Request Procedure: steps 1-4"
    },
    {
        "text": """7. Non-Refundable Modification Request Procedure
Use this workflow when a member wants to modify a non-refundable reservation, such as changing dates.
Just like cancellations, we need to ask the users to agree to certain terms before we try to modify their non-refundable reservations with the suppliers.
Step 1: Confirm Member Agreement
Before contacting the supplier, the member must agree to the terms presented and provide instructions on getting approval from the hotel in this canned response:
“Confirm Modification Terms - STEP 1”
Step 2: Provide Hotel Modification Template
Provide a template with clear language for requesting approval from the hotel. Send:

“Template for Hotel Modification Approval”
Step 3: Escalate to Supplier
If appropriate:
● Contact the correct supplier.
● Include supplier booking ID.
● Provide hotel approval if available.
● Document all communication in Atlas.
If the hotel cannot modify the dates/details of the existing booking, but agrees to cancel, make sure they are aware of all terms listed for cancelling.""",
        "source": "Hotel Procedures - Non-Refundable Modification Request Procedure Steps"
    },
    {
        "text": """Important Note
For last-minute changes, especially same-day check-in changes, it may be better to advise the member to request cancellation instead and they can rebook themselves.
Same-day modifications are difficult for suppliers to complete and should not be promised.""",
        "source": "Hotel Procedures - Non-Refundable Modification Request Procedure Important Note"
    },
    {
        "text": """8. Member-Initiated Non-Refundable Conversion
Example ticket: Ticket link
Some members may ask to change a refundable reservation to non-refundable so they can receive miles immediately.
Note: Users have the option to make some refundable stays non-refundable during check out. The panel will show this. These reservations can be cancelled within 24 hours of making the booking. Within 24 hours, you may cancel on the booking page and issue the refund. 
Step 1: Confirm the Request
Use:

“Just to confirm, are you asking to change your refundable booking to a non-refundable one so you can earn your miles right away? I’d be happy to help with that. Please keep in mind that once a booking is changed to non-refundable, cancellation or refunds will no longer be possible. If you’d like to move forward, could you please confirm this and share your booking reference number with me?”

Step 2: Collect Booking Reference
Ask the guest to provide their booking reference. If the member cannot locate it, search the CS Panel using available member details.
If the guest does not know the hotel policy, search the code in the Rove CS panel to confirm reservation details and policy.""",
        "source": "Hotel Procedures - Member-Initiated Non-Refundable Conversion Steps 1 to 2"
    },
    {
        "text": """Step 3: Obtain Explicit Written Approval
The member must clearly confirm that they want to proceed.
Acceptable confirmation:
    “Yes, I want to change to non-refundable.”
Always include the cancellation warning before the guest consents. Do not proceed without explicit written confirmation.

Step 4: Escalate Internally
● Tag Kevin in the Atlas ticket.
● DM Kevin in Slack with the ticket link.
● Request conversion to non-refundable.
Step 5: Follow Up
Once submitted, tell the member:
    “Thank you for confirming. I’ve submitted your request and the change will reflect in your booking within 24 hours.”
Once Kevin confirms the update:
● Follow up with the guest to confirm miles posting.
● Update Atlas notes.
● Thank the member for booking with Rove.
● Close the ticket.""",
        "source": "Hotel Procedures - Member-Initiated Non-Refundable Conversion Steps 3 to 5"
    },
    {
        "text": """9. Reservation Not Found by Hotel
Use this workflow when the guest is at the hotel and the hotel cannot locate the reservation.
Member Response
    “We’ll reach out to our hotel partner right away to get the hotel’s confirmation number so your booking can be identified. This process usually takes less than 4 hours, and we’ll update you as soon as we have the confirmation number.”
Step 1: Locate Booking
If the guest does not provide the booking reference:
● Open their profile using the User ID from Atlas.
● Search the CS Panel for the booking.
● Locate the supplier booking ID.
Step 2: Contact Supplier
For Nuitee:
● Call the escalations phone number.
● Email inresort@nuitee.com.
● Include supplier booking ID and member name.
● CC support-team@rove.com

For TripEdge:
● Reach out in the TripEdge Slack channel.""",
        "source": "Hotel Procedures - Reservation Not Found by Hotel Workflow Steps 1 to 2"
    },
    {
        "text": """Step 3: Keep Ticket Open
Keep the ATLAS ticket open while waiting for supplier confirmation.
Nuitee support usually replies quickly, but allow up to 4 hours. If you are not receiving a response from Nuitee after emailing, escalate in #liteapi Slack channel or have team leads/management escalate in Nuitee WhatsApp.

Step 4: Respond to Guest
Once the supplier provides the hotel confirmation number, reply:
    “We’ve confirmed your booking with the hotel. Your hotel confirmation number is [XXXX].”
Include any additional check-in information provided by the supplier.

Step 5: Close Ticket
Close the ticket once:
● The guest has the hotel confirmation number.
● The issue is resolved.
● Notes are documented in Atlas.""",
        "source": "Hotel Procedures - Reservation Not Found by Hotel Workflow Steps 3 to 5"
    },
    {
        "text": """Reservation Not Found Severity Guidelines
Reservation Not Found cases should be prioritized based on the member's VIP/travel status.
Critical Priority
Use Critical Priority when:
● The member is currently at the hotel
● The member is en route to the hotel
● Check-in is scheduled within the next 24 hours
Actions:
● Contact supplier immediately
● Escalate through supplier urgent channels
● Keep ticket assigned and actively monitored
● Provide updates to the member at least every 60 minutes until resolved""",
        "source": "Hotel Procedures - Reservation Not Found Severity Guidelines: Critical Priority"
    },
    {
        "text": """High Priority
Use High Priority when: Check-in is within 24–72 hours.
Actions: Escalate to supplier same day. Monitor until hotel confirmation number is obtained.
Standard Priority
Use Standard Priority when: Check-in is more than 72 hours away.
Actions: Follow normal supplier escalation procedures.""",
        "source": "Hotel Procedures - Reservation Not Found Severity Guidelines: High & Standard Priority"
    },
    {
        "text": """10. Price Match Requests
Hotel price matching is not currently available.
Member response:
    “Hotel price match isn’t available yet, but it will be coming soon.”""",
        "source": "Hotel Procedures - Price Match Requests"
    },
    {
        "text": """11. Hotel Compensation Tracking
Any compensation paid by Rove must be logged in the Hotel Comp Tracker.
Track compensation when Rove provides:
● Rove Miles
● Cash reimbursement
● Rebooking support paid out of Rove’s pocket
● Other goodwill compensation
Do not track compensation paid by:
● Nuitee
●TripEdge
● The hotel
● Any other supplier
Only track compensation funded directly by Rove.""",
        "source": "Hotel Procedures - Hotel Compensation Tracking"
    },
    {
        "text": """12. Hotel Procedure Best Practices
Agents should always:
● Confirm the booking policy before taking action.
● Verify the cancellation deadline.
● Only cancel the reservation specified by the member.
● Avoid promising refunds, cancellations, or modifications before approval.
● Keep internal notes clear and complete.
● Tag relevant team members when escalation is needed.
● Communicate timelines clearly to the member.
● Keep tickets open while supplier confirmation is pending.
● Document supplier responses in Atlas.""",
        "source": "Hotel Procedures - Hotel Procedure Best Practices"
    },
    {
        "text": """13. Atlas Documentation Requirements
Before resolving any hotel-related ticket, verify that Atlas notes include:
● Booking reference
● Supplier booking ID
● Supplier contacted (if applicable)
● Actions taken
● Member communication sent
● Refund or cancellation status
● Any escalation performed
● Final resolution
Incomplete documentation may result in duplicate work, missed follow-ups, or inaccurate reporting.""",
        "source": "Hotel Procedures - Atlas Documentation Requirements"
    },
    {
        "text": """14. Engineering Escalation
Escalate to Engineering when:
● Refundable reservations cannot be canceled internally
● The CS Panel displays incorrect booking data
● Miles are not posting according to policy
● Reservation information is missing despite confirmed bookings
● Internal tools fail to complete a normally supported action
Document the Engineering escalation in Atlas and leave the ticket open until resolution or workaround is provided.""",
        "source": "Hotel Procedures - Engineering Escalation"
    },
    # =========================================================================
    # SECTION 9: Flight Procedures (PAGES 78-92)
    # =========================================================================
    {
        "text": """Flight Procedures
Flight Policies & FAQs
Flight Miles Posting Policy
Miles for flight bookings are awarded only after travel has been completed.
Member Response:
    "Miles for flights are added after you travel. Once your flight is complete, your miles will automatically appear in your account." """,
        "source": "Flight Procedures - Flight Miles Posting Policy"
    },
    {
        "text": """Airline Partners & Loyalty Programs
Rove supports:
● 70+ airline partners
● 12 transfer partners
Member Response:
    "Rove Miles can be used with over 70 airlines worldwide. You can also transfer them to 12 partner loyalty programs for additional travel rewards." """,
        "source": "Flight Procedures - Airline Partners & Loyalty Programs"
    },
    {
        "text": """Triple-Dip Earnings
Cash flight bookings earn rewards in three ways:
● Rove booking multiplier
● Airline miles
● Credit card rewards
Member Response:
    "When you book cash flights through Rove, you earn in three ways — through Rove's booking multiplier, airline miles, and your credit card rewards." """,
        "source": "Flight Procedures - Triple-Dip Earnings"
    },
    {
        "text": """Flight Price Match Policy
Rove currently price matches flights booked directly with airlines.
Member Response:
    "Yes, we can price match flights booked directly with airlines. I can review your itinerary and help you submit a price match request." """,
        "source": "Flight Procedures - Flight Price Match Policy"
    },
    {
        "text": """Flight Modifications & Corrections
Important Policy
Agents must never guarantee:
● Name changes
● Name corrections
● Airline waivers
● Flight modifications
All requests remain subject to airline approval.""",
        "source": "Flight Procedures -> Flight Modifications & Corrections - Important Policy"
    },
    {
        "text": """Name Correction vs Name Change
Name Correction (May Be Approved)
Examples:
● Missing middle name
● Added middle name
● Missing title
● Minor spacing issue
● First and last name reversed
If there are no spelling errors and the passenger identity remains unchanged, a correction may not be required.

Name Change (Usually Not Allowed)
Examples:
● Different first name
● Different last name
● Passenger substitution
● Significant spelling error
Most airlines do not allow name changes after ticketing.
Member Response:
    "Most airlines don't allow name changes once a ticket is issued. If your flight is soon, the fastest option is to contact the airline directly to see whether they can accommodate your request." """,
        "source": "Flight Procedures -> Flight Modifications & Corrections - Name Correction vs Name Change"
    },
    {
        "text": """Required Documentation
When a name correction is required:
● Request government-issued identification.
● Passport for international travel.
● Driver's license or government-issued ID for domestic travel.
● Submit documentation to Duffel.
● Await airline review and approval.
Do not promise approval before the airline responds.""",
        "source": "Flight Procedures -> Flight Modifications & Corrections - Required Documentation"
    },
    {
        "text": """Flight Cancellations
24-Hour Cancellation Policy
Many airlines offer cancellation within 24 hours of booking, but eligibility varies by:
● Airline
● Fare rules
● Departure date
● Applicable regulations
Member Response:
    "Many airlines allow free cancellation within 24 hours, but it depends on your ticket rules. I can review your booking to confirm whether your fare is eligible."
Always verify eligibility before promising cancellation or refund options.""",
        "source": "Flight Procedures - Flight Cancellations"
    },
    {
        "text": """Flight Disruptions & Schedule Changes
Overview
Flight disruptions are typically controlled by the airline rather than Rove.
Common disruptions include:
● Flight cancellations
● Flight delays
● Schedule changes
● Missed connections
● Aircraft changes
● Route changes
● Involuntary rebookings
Our role is to help members understand their options, coordinate with the airline or supplier when necessary, and advocate for a resolution whenever possible.""",
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Overview"
    },
    {
        "text": """Important Policy
Agents must never guarantee:
● Refund approval
● Airline compensation
● Rebooking approval
● Schedule change waivers
● Alternative flight availability
Final decisions are determined by the airline.""",
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Important Policy"
    },
    {
        "text": """Flight Cancellation by the Airline
Use this workflow when the airline cancels the member's flight.
Step 1: Verify Cancellation
Confirm:
● Flight number
● Date
● Airline status
Verify whether the cancellation has been officially processed by the airline.

Step 2: Determine Available Options
Airlines typically offer one or more of the following:
● Rebooking on another flight
● Flight credit
● Refund
● Alternate routing
Available options vary by airline and fare rules.

Step 3: Contact Supplier if Needed
If the booking was made through Rove and options are unclear:
● Contact Duffel
● Request available options
● Document all responses in Atlas
Member Response
    "I’m sorry to hear your flight was canceled. I’m reviewing the options currently being offered by the airline and will update you as soon as I have more information." """,
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Flight Cancellation by the Airline Workflow (steps)"
    },
    {
        "text": """Significant Flight Delay
Use this workflow when the member experiences a substantial delay.
Step 1: Verify Delay
Confirm:
● Flight number
● Scheduled departure time
● Updated departure time
Step 2: Determine Impact
Identify whether the delay causes:
● Missed connection
● Overnight stay
● Major itinerary disruption
Step 3: Review Airline Options
Depending on the airline, options may include:
● Rebooking
● Travel credit
● Meal vouchers
● Hotel accommodations
These benefits vary by airline and are not guaranteed.
Member Response
    "I understand how frustrating delays can be. I’m reviewing the options available through the airline and will let you know what assistance may be available." """,
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Significant Flight Delay Workflow"
    },
    {
        "text": """Schedule Changes
A schedule change occurs when the airline changes:
● Departure time
● Arrival time
● Flight number
● Routing
● Aircraft
Minor Schedule Changes
Examples:
● Small departure time adjustments
● Aircraft changes with no itinerary impact
Typically no action is required.
Major Schedule Changes
Examples:
● Significant departure time changes
● Missed connections
● Added layovers
● Routing changes
Resolution Process
1. Review the updated itinerary.
2. Determine whether airline alternatives are available.
3. Contact Duffel if clarification is needed.
4. Present available options to the member.
Member Response
    "The airline has updated your itinerary. I’m reviewing the available options and will let you know whether alternative flights or other accommodations may be available." """,
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Schedule Changes"
    },
    {
        "text": """Missed Connections
Airline-Caused Missed Connection
If a missed connection was caused by:
● Airline delay
● Airline schedule change
● Airline operational issue
The airline may provide:
● Rebooking
● Alternate routing
● Additional assistance
Contact Duffel if assistance is required.

Member-Caused Missed Connection
Examples:
● Arriving late to the airport
● Voluntarily changing plans
● Missing boarding
These situations are generally subject to the fare rules of the ticket.
Refunds and rebooking options are not guaranteed.""",
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Missed Connections"
    },
    {
        "text": """Same-Day Travel Emergencies
Critical Priority Cases
Treat the following as urgent:
● Member currently at airport
● Flight departing within 24 hours
● Airline cancellation while traveling
● Missed connection during travel
● Member stranded due to disruption

Agent Responsibilities
● Prioritize the ticket immediately.
● Contact supplier urgent channels when applicable.
● Keep the member updated frequently.
● Do not leave the ticket unassigned.""",
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Same-Day Travel Emergencies"
    },
    {
        "text": """Documentation Requirements
For all flight disruptions, document:
● Flight number
● Airline
● Original itinerary
● Updated itinerary
● Member impact
● Supplier communication
● Resolution offered
● Final outcome
All communication and decisions should be recorded in Atlas notes.""",
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Documentation Requirements"
    },
    {
        "text": """Service Recovery Guidelines
When a member experiences a significant disruption, consider whether a goodwill gesture may be appropriate according to the Compensation Policy.
Examples may include:
● Extended resolution times
● Poor member experience
● Significant inconvenience not otherwise addressed
Any Rove-funded compensation must follow the Compensation Policy and Compensation Authority Matrix.""",
        "source": "Flight Procedures -> Flight Disruptions & Schedule Changes - Service Recovery Guidelines"
    },

    # =========================================================================
    # TAB: Flight Procedures -> Sub-tab: Duffel
    # =========================================================================
    {
        "text": """Duffel Overview
What is Duffel?

Duffel is the platform Rove uses to manage, verify, and service flight bookings made through the Rove website.

Member Support Representatives use Duffel to review flight reservations, verify ticket status, submit service requests, and communicate with airline partners when changes are required.

What Agents Can Do in Duffel
Agents may use Duffel to:
● Confirm that a flight booking exists and is valid.
● Verify that a ticket has been issued and marked “confirmed.”
● Check booking and ticket status.
● Submit modification requests (e.g., correcting name spelling, passenger details).
● Confirm whether a refund or cancellation is available (handled by Duffel or Kevin, not directly by agents). 
● Re-send or confirm that the guest has received their e-ticket.
● Communicate with airline partners through Duffel support requests.""",
        "source": "Flight Procedures -> Duffel - Overview and Agent Capabilities"
    },
    {
        "text": """What Agents Cannot Do in Duffel
Agents cannot:
● Directly issue refunds.
● Directly approve cancellations.
● Directly modify airline reservations.
● Override airline policies.
● Guarantee airline approval of requests.
● Issue airline credits or vouchers.
These actions are controlled by the airline and/or Duffel.
Always avoid promising outcomes before approval has been received.""",
        "source": "Flight Procedures -> Duffel - Agent Limitations"
    },
    {
        "text": """Common Duffel Workflows
Confirm a Flight Booking
Use this workflow when:
● A member asks whether their reservation is valid.
● A member reports they never received confirmation.
● A member is concerned that their booking did not process correctly.
Process
1. Search for the reservation in Duffel.
2. Open the order.
3. Verify the order status is marked Confirmed.
4. Verify that a ticket has been issued to the guest.
If both conditions are met, the reservation is considered successfully ticketed.""",
        "source": "Flight Procedures -> Duffel - Workflow: Confirm a Flight Booking"
    },
    {
        "text": """Verify Ticket Issuance
Use this workflow when:
● The ticket status shows pending or not issued.
● The booking appears incomplete.
● The member cannot locate their ticket.
Process
1. Open the reservation in Duffel.
2. Confirm whether a ticket has been issued.
3. If the ticket has not been issued, submit a request to Duffel for ticket issuance.
4. Document the request in Atlas.""",
        "source": "Flight Procedures -> Duffel - Workflow: Verify Ticket Issuance"
    },
    {
        "text": """Request Flight Modifications
Use this workflow when:
● Passenger information is incorrect.
● A name correction is needed.
● The member is requesting assistance with reservation changes (cancellation or refund).
Process
1. From the Overview page, select the flight.
2. Click Manage This Order.
3. Select the appropriate request type.
4. Submit the request through Duffel.
This creates a support request directly with Duffel.""",
        "source": "Flight Procedures -> Duffel - Workflow: Request Flight Modifications"
    },
    {
        "text": """Flight Name Corrections
Name Correction Not Required
No correction is typically required when the only difference involves:
● Middle name included or omitted
● Title included or omitted
● Minor spacing variations
● First and last names reversed
● Formatting differences with no spelling errors

Name Correction Required

If the discrepancy could affect passenger identification:
1. Request identification from the traveler.
2. Passport for international flights.
3. Government-issued ID or driver's license for domestic flights.
4. Submit documentation to Duffel.
Do not promise approval until the airline responds.""",
        "source": "Flight Procedures -> Duffel - Flight Name Corrections"
    },
    {
        "text": """Refunds & Cancellations
Use this workflow when:
● A member requests cancellation.
● A member requests a refund.
● The airline cancels a flight.
● A cancellation quote is needed.
Process
1. Open the reservation in Duffel.
2. Review available cancellation or refund options.
3. Submit a cancellation quote request if applicable.
4. Await supplier response.
Actual refund processing is handled by Duffel and/or authorized Rove personnel.
Agents should never promise refund approval before confirmation is received.""",
        "source": "Flight Procedures -> Duffel - Workflow: Refunds & Cancellations"
    },
    {
        "text": """Confirm Refund Status
Use this workflow when:
● A member is following up on a refund.
● A cancellation has already been approved.
● Refund status needs to be verified.
Process
1. Open the order in Duffel.
2. Review refund status.
3. Confirm refund progress.
4. Verify status internally before providing final updates to the member.
Always confirm with Kevin before communicating final refund details to the guest.""",
        "source": "Flight Procedures -> Duffel - Workflow: Confirm Refund Status"
    },
    {
        "text": """E-Ticket Verification
Use this workflow when:
● A member reports they never received their ticket.
● A member requests another copy of their e-ticket.
Process
1. Verify the ticket has been issued.
2. Confirm the member's email address.
3. Re-send or verify delivery of the e-ticket.
4. Document any actions taken in Atlas.""",
        "source": "Flight Procedures -> Duffel - Workflow: E-Ticket Verification"
    },
    {
        "text": """Ticket Ownership
Submitting a request through Duffel does not transfer ownership of the member issue.
The assigned Member Support Representative remains responsible for:
● Monitoring the request.
● Following up with Duffel when necessary.
● Updating the member.
● Documenting progress in Atlas.
● Driving the issue through resolution.

Duffel Help Resources:
Cancelling an Order
Refunds in Duffel
Duffel Help Centre
How do I check if an order is confirmed?""",
        "source": "Flight Procedures -> Duffel - Ticket Ownership & Help Resources"
    },
    # =========================================================================
    # SECTION 10: : Shopping Procedures (PAGES 93-122)
    # =========================================================================
    {
        "text": """Shopping Procedures
Use Miles, Not Points
Members may refer to rewards as "points." Member-facing communications should always use the term Rove Miles. Rove rewards flights, hotels, and shopping with miles.

Always refer to rewards as miles. 

Wildfire and Loyalize
Rove uses two sources for shopping: Wildfire and Loyalize. Please do not mention these sources to the user. Refer to the “merchant.”

Wildfire and Loyalize do not use the term “miles,” so try to refrain from using that term in internal correspondence with them. They technically offer cashback, but you can just call them “rewards.” 

Never Promise Merchant Approval
● Agents must never guarantee:
● Merchant approval
● Miles posting
● Merchant reversals
● Missing miles claim approval

Final decisions are determined by the merchant. 

One Request, One Owner
If a member submits multiple shopping requests, assign all related requests to the same Member Support Representative whenever possible to ensure consistency and improve the member experience.""",
        "source": "Shopping Procedures - Guidelines and Communication Policies"
    },
    {
        "text": """Shopping Miles Timeline
Shopping miles move through several stages before becoming available.
Clicked:
A Clicked status means:
● The member clicked through Rove to visit the merchant.
● A purchase may have been completed but has not yet tracked.
● The merchant has not yet reported the transaction.
For recent purchases, this is normal.

Expected Timeline: 24 hours to 10 days

Member Response
"For recent purchases, miles usually begin pending within 24 hours, but with some merchants it can take up to 10 days for pending miles to appear. Please allow for the full 10 days for your purchase to show." """,
        "source": "Shopping Procedures -> Shopping Miles Timeline - Clicked Status"
    },
    {
        "text": """Pending:
A Pending status means:
● The purchase has successfully tracked.
● The merchant has acknowledged the transaction.
● We are waiting for the merchant to approve and pay the commission.
Expected Timeline: 30–100 days
Travel and event purchases may take longer because validation often occurs after travel or event completion.
Member Response
"Your purchase has successfully tracked and is currently pending approval from the merchant. Miles from shopping typically post within 30–100 days. As soon as they process it, your miles will be posted." """,
        "source": "Shopping Procedures -> Shopping Miles Timeline - Pending Status"
    },
    {
        "text": """Available:
An Available status means:
● The merchant approved the transaction.
● Miles have been awarded.
● Miles should now appear in the member's available balance.
No further action is required.

Failed or Disqualified:
A Failed or Disqualified status means the merchant determined the purchase did not qualify for rewards.
Common reasons include:
● Returned purchases
● Cancelled subscriptions
● Excluded products
● Violation of merchant terms
● Another rewards source receiving credit
These cases should be reviewed before any escalation is submitted.""",
        "source": "Shopping Procedures -> Shopping Miles Timeline - Available and Failed Statuses"
    },
    {
        "text": """Shopping Miles Troubleshooting
Missing Miles (Less Than 10 Days)
No escalation is required.
Member Response:
"Shopping miles usually begin pending within 24 hours, but some merchants may take up to 10 days. Your purchase is still within the normal processing window."
Close the ticket after reassuring the member.""",
        "source": "Shopping Procedures -> Shopping Miles Troubleshooting - Missing Miles (<10 Days)"
    },
    {
        "text": """Missing Miles (More Than 10 Days)
Example Ticket: Ticket Link
Merchants require a 10-day wait before escalation. Posting after reporting can take 4-8 weeks. If the purchase is more than 10 days old and miles haven't been posted, have the member submit a report from their account under Shopping Trip by clicking the merchant/purchase and entering the required details. 
Member Response
    “If your miles have not appeared after 10 days, please submit a Missing Miles report from your account so our team can help investigate. You can do this by going to your Shopping Trips, selecting the merchant/purchase, and entering the required details. Once submitted, merchant investigations typically take 4–8 weeks.”
    Leave the ticket open if escalation is required.""",
        "source": "Shopping Procedures -> Shopping Miles Troubleshooting - Missing Miles (>10 Days)"
    },
    {
        "text": """Incorrect Miles Amount
Before escalating:
● Verify promotional multipliers.
● Check historical offer rates.
● Confirm earning method.
● Review merchant exclusions.
Do not submit claims when the discrepancy appears to be caused by a Rove promotional multiplier.

Miles Not Confirmed
Before escalating:
● Confirm purchase has been pending for at least 100 days.
● Confirm miles have not already posted.
● Review travel and event purchase exceptions.
Travel and event purchases should be evaluated based on the travel or event date rather than purchase date.""",
        "source": "Shopping Procedures -> Shopping Miles Troubleshooting - Incorrect Miles & Miles Not Confirmed"
    },
    {
        "text": """Failed or Disqualified Transactions
Before escalating:
● Review merchant exclusions.
● Confirm purchase was completed.
● Confirm purchase was made from an eligible location.
● Verify no returns or cancellations occurred.
If necessary, review Atlas session recordings to verify purchase location and eligibility.""",
        "source": "Shopping Procedures -> Shopping Miles Troubleshooting - Failed or Disqualified Transactions"
    },
    {
        "text": """Timeframe
Agent Response / Workflow
24 hours to 10 days
Pending miles can take up to 10 days to appear. Some merchants report more slowly, so please allow the full 10 days for your purchase to show.

More than 10 days
Ask the member to submit a form via the My Shopping Trips page

After escalation
Merchant follow-up can take 4 to 8 weeks. Example: “We are still awaiting a reply from the merchant. Please allow 4–8 weeks for them to investigate.”

30 to 100 days
Miles from shopping can take up to 30 to 100 days to post. As soon as the merchant processes it, your miles will be posted. Miles from Travel & Event Ticket purchases can take longer than 100 days, as the miles do not start pending until the travel or event has been completed/consumed.

More than 100 days
Escalate again or follow up with the merchant if no resolution. Reassure the member that Rove is continuing to track with them.""",
        "source": "Shopping Procedures - Timeframe and Agent Response Workflow Table"
    },
    # =========================================================================
    # SUBTAB: Shopping Procedures -> Sub-tab: Merchant Submission Process
    # =========================================================================
    {
        "text": """Merchant Submission Process (Wildfire & Loyalize)
Overview
Shopping rewards are processed through merchant partners. Internally, these partners may refer to rewards as cashback or commissions.
Terminology Guidelines
Member-Facing Language
Always use:
● Rove Miles
● Miles
● Rewards
Never use:
● Cashback
● Commission
Merchant-Facing Language
When communicating with Wildfire or Loyalize:
● Use cashback or rewards terminology when appropriate.
● Avoid referring to rewards as miles unless necessary.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Overview and Terminology"
    },
    {
        "text": """Important Reminder
Do not automatically assume every member claim is valid.
Before submitting any request:
● Verify the information independently.
● Review the purchase details.
● Review previous tickets.
● Review merchant terms and exclusions.
Provider Comparison Table:

Item                                          Wildfire                  Loyalize
Receipt Required                               Yes                      Sometimes
Browser Extension Transactions                Usually Yes                Usually No
Member Auto-Population Required                 No                       Yes
Merchant Auto-Population Required               No                      Yes
Investigation Timeline                     Typically 4 to 8 weeks       Typically up to 8 weeks
Uses Cashback Terminology                       Yes                        Yes""",
        "source": "Shopping Procedures -> Merchant Submission Process - Provider Comparison Table"
    },
    {
        "text": """Missing Miles Submission Workflow
Ticket Assignment
When a Missing Miles request is submitted:
Step 1: Assign Ownership
Assign the request to yourself in:
● The Ticket that is made when someone submits a request
● CS Dashboard
Both records should always have the same assignee.
One Request, One Owner
If a member has submitted multiple shopping requests:
● Assign all related requests to yourself whenever possible.
● This improves consistency and member experience.
Helpful Tip
The easiest process is:
1. Assign yourself to the ticket.
2. Copy the Order Number from the submission.
3. Enter the Order Number into the CS Dashboard in Shopping Reports.
4. Assign yourself in the CS Dashboard.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Ticket Assignment: Missing Miles Submission Workflow Steps 1"
    },
    {
        "text": """Step 2: Verify the Request
Before submitting:
● Review the member's information.
● Review the purchase details.
● Confirm sufficient documentation exists.
● Confirm the request has not already been submitted.
● Check that the purchase is not showing in their transactions list.
● Verify if there is any additional information needed to submit a claim.
Search:
● Previous tickets
● Wildfire
● Loyalize
Duplicate submissions should be avoided whenever possible.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Missing Miles Submission Workflow Step 2"
    },
    {
        "text": """Step 3: Submit to Merchant
Submit the request to the appropriate merchant partner:
● Wildfire
● Loyalize
Determine based on what the request says in the Shopping Dashboard.
Wildfire Requirement
Always CC support-team@rovemiles.com on Wildfire submissions.

Step 4: Document Submission
After submitting: Update Dashboard
Change status to: Reported to Merchant
Make a note in the ticket to include:
● Submission date
● Merchant used
● Direct link to submission (if possible)
● Summary of request
Important: Always include the submitted purchase link in Atlas notes for quick future reference.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Missing Miles Submission Workflow Steps 3 to 4"
    },
    {
        "text": """Step 5: Notify Member
Inform the member:
● Request has been submitted.
● Merchant review has begun.
● Timeline for the merchant’s decision; investigation typically takes 4–8 weeks.
Use the approved canned responses when available.
Step 6: Snooze or Pending
After submission:
● Snooze the ticket or mark it pending.
● Remove it from active queues while awaiting merchant response.
Step 7: Merchant Response
When a response is received:
1. Review the decision.
2. Send the appropriate canned response.
3. Update Atlas.
4. Close the Shopping Dashboard request.
Status should be updated to: Closed""",
        "source": "Shopping Procedures -> Merchant Submission Process - Missing Miles Submission Workflow Steps 5 to 7"
    },
    {
        "text": """Bot Submission Reminder
If a member states the bot already submitted their request, disregard this since we submit manually. If the ticket doesn’t have a note indicating it was submitted, do not assume it was.
Verify:
● Atlas notes
● Dashboard status
● Merchant records
If no submission documentation exists, assume the request still requires processing. Requests should always match and be assigned to the same person. 
Add the link of the submitted purchase to the Atlas ticket so it is visible and easy to check.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Bot Submission Reminder"
    },
    {
        "text": """Claim Validation Requirements
Before submitting any request, ensure the claim type is correct. Submitting the wrong claim type can significantly delay resolution.
If you immediately notice a claim was submitted incorrectly:
● Close the request.
● Resubmit using the correct claim type.
Incorrect Miles Claims
Verify Promotional Multipliers
Before submitting, check:
● Past Commission Promotions
● Historical merchant offer
● Current merchant offer
In this case, check the Past Commission Promotions for the date they made the purchase and the current offer for that merchant where they originally clicked.

Do not submit if the missing miles appear to be related to a Rove promotional multiplier.
Consult Engineering if historical offer verification is needed.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Claim Validation Requirements"
    },
    {
        "text": """Verify Purchase Method
Confirm how the purchase was made:
● Browser extension
● Shopping page
Transactions tracked through the browser extension should be associated with Wildfire. 
If the report says Loyalize in the dashboard but they say they purchased through the browser extension, they may have made the purchase through the shopping page instead. Check the shopping page offers to see if it lines up with their earning rate.
Review Offer Terms
Confirm:
● Eligible categories
● Excluded products
● Merchant-specific restrictions
Check the categories on the offer and make sure what they purchased wasn’t excluded in the terms.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Purchase Method Verification"
    },
    {
        "text": """Missing Miles Claims
Before submitting, confirm the purchase does not already appear in the member's transaction list.
If the transaction exists, the issue may require a different claim type.
Miles Not Confirmed Claims
Before submitting, verify:
● Purchase has remained pending for at least 100 days past the date of purchase.
● Miles are still showing as pending and have not already posted.
Travel & Event Purchases
The exception is travel/event purchases which don’t start pending until after dates of travel or event. 
Loyalize:
● Validation occurs approximately 60 days after travel or event completion.
● Payment generally occurs around day 80.
Wildfire:
● The 30–100 day timeline begins after the travel or event date.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Missing Miles vs Miles Not Confirmed"
    },
    {
        "text": """Failed or Disqualified Claims
Before submitting, verify:
● Purchase was eligible.
● No excluded products were purchased.
● No returns occurred.
● No cancellations occurred.
● No subscription cancellation occurred.
Geographic Eligibility
Verify the purchase was made through the eligible version of the merchant's site. 
Purchases made outside of the U.S. may not be attributed correctly. Rove cannot guarantee rewards for purchases made outside supported regions. 
Atlas session recordings can help verify browsing location.
User Flagging
If Wildfire or Loyalize confirms a user was disqualified due to cancellation or return activity:
● Add a note to the user's profile in the CS Dashboard.
● Document the merchant's reason for disqualification.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Failed or Disqualified Claims Verification"
    },
    {
        "text": """Additional Documentation Requirements
Request additional information before submitting if:
● Receipt is incomplete.
● Order number is missing.
● Travel dates are missing.
● Event dates are missing.
● Merchant eligibility cannot be verified.
Even when a receipt is not required for submission, review it carefully.
Receipts often contain more accurate information than member-provided details.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Additional Documentation Requirements"
    },
    {
        "text": """Merchant Decisions & Member Communication
Merchant Decisions
Wildfire and Loyalize may provide limited explanations when denying claims.
Examples:
● Another marketing channel received credit.
● Purchase was non-commissionable.
● Merchant could not validate the transaction.
In many cases, Rove cannot obtain additional details beyond the merchant's explanation. 
Unless you think some of the information the merchant based their decision on was incorrect, we must simply relay their decision to the users. We sometimes do not have the ability to clarify further.  
Best Practice
Relay the merchant's decision accurately. Do not speculate or create alternative explanations.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Merchant Decisions Communication"
    },
    {
        "text": """Escalated Member Concerns
If a member disputes a merchant decision:
● Use the appropriate canned response by typing #MissingMiles.
● Review prior team responses.
● Use the saved response titled "Follow Up - Non-Commissionable Decision" when applicable.
Escalate internally if you believe the merchant's decision may be based on incorrect information.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Escalated Member Concerns"
    },
    {
        "text": """Goodwill Miles Policy
In limited circumstances, Rove may award goodwill miles even when a merchant denies the claim. Goodwill miles should be used sparingly, and only after claim validity has been verified.
Eligible Scenarios:
Missing Miles Submitted Too Late
● Missing Miles claim submitted more than 90 days after purchase.
● Applies only to Missing Miles claims.
● Does not apply to:
  - Miles Not Confirmed claims
  - Travel purchases
  - Event purchases
Small Denied Purchases
● Purchase value under $15
● Merchant denied the claim
● Member otherwise appears eligible""",
        "source": "Shopping Procedures -> Merchant Submission Process - Goodwill Miles Policy Eligible Scenarios"
    },
    {
        "text": """Approval Requirements
Up to 250 Miles
May be awarded without approval if:
● Member has not previously received goodwill miles.
● Total goodwill award remains under 250 miles.
250–1,000 Miles
If between 250-1,000 miles, or the user has been given goodwill miles before, approval is required from Max or Arhan.
Maximum Allowance
Members should not receive more than 1,000 goodwill miles under this policy.
Documentation
Whenever goodwill miles are awarded, record:
● Number of miles awarded
● Purchase involved
● Reason for award
● Approval received (if required)
Add notes to the member's account and Atlas ticket.""",
        "source": "Shopping Procedures -> Merchant Submission Process - Goodwill Miles Policy Approval Requirements"
    },

    # =========================================================================
    # TAB: Shopping Procedures -> Sub-tab: Wildfire Guidelines
    # =========================================================================
    {
        "text": """Wildfire-Specific Guidelines
Overview
Wildfire is one of Rove's shopping partners used to track and validate eligible shopping transactions.
When communicating with Wildfire:
● Use cashback or rewards terminology.
● Do not use the term "miles."
Follow Wildfire's documentation requirements before submitting any claim.
Wildfire Quick Reference
Issue Submit? Claim Type
Purchase <10 days old No Wait
Not Pending after 10 days Yes Untracked Order
Wrong amount pending Yes Incorrect Cashback Rate
Pending >100 days Yes Delayed Cashback Payout
Missing promo multiplier No Escalate internally
Non-U.S. purchase No Not eligible
Missing order number No Request documentation""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Overview and Quick Reference Table"
    },
    {
        "text": """Wildfire Claim Types
When submitting a request through Wildfire, select the claim type that best matches the issue.
Untracked Order
Use when:
● A purchase does not appear as Pending.
● At least 10 days have passed since purchase.
Incorrect Cashback Rate
Use when:
● The purchase tracked successfully.
● The reported cashback amount is incorrect.
● The pending amount is lower than expected.
● The pending amount shows as zero.
Before submitting, verify:
● Merchant offer terms
● Eligible categories
● Promotional multipliers
● Purchase method""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Claim Types Part 1"
    },
    {
        "text": """Delayed Cashback Payout
Use when:
● Miles remain Pending.
● More than 100 days have passed since the transaction became Pending.
Other
Use only when no standard claim type accurately describes the issue.""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Claim Types Part 2"
    },
    {
        "text": """Required Documentation
Wildfire requires supporting documentation for all investigations.
Do not submit a claim until all required information has been obtained.
Required Information
The receipt or order confirmation must include:
● Purchase date
● Purchased items
● Order number
● Purchase subtotal
Travel & Event Purchases
For travel or event-related purchases, also obtain:
● Travel date
● Event date
Missing Information
If documentation is incomplete:
● Contact the member.
● Request a new receipt or order confirmation.
Do not submit the claim until all required information has been received.
Important: The order number is mandatory for investigation and merchant escalation.""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Required Documentation"
    },
    {
        "text": """Wildfire Validation Checklist
Before submitting any claim, verify:
● The merchant is correct.
● The purchase date is correct.
● The purchase falls within the attribution window.
● The purchase has not already been reported.
● The claim has not already been resolved.
● There is reasonable confidence the purchase should have tracked.
If a merchant offer only applies to first-time purchases, verify the member has not previously completed a qualifying purchase through Rove.
International Orders
Rove shopping offers are intended for U.S.-based purchases unless otherwise specified.
Before submitting:
● Confirm the purchase was made through the U.S. version of the merchant's website.
● Verify the member's purchase location when necessary.
Do not submit claims for purchases made outside eligible regions.""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Validation Checklist"
    },
    {
        "text": """Incorrect Miles & Promotional Multipliers
Before submitting an Incorrect Cashback Rate claim:
Verify Promotional Multipliers
Some discrepancies are caused by Rove promotions rather than merchant tracking.
Check:
● Historical merchant offers
● Past Commission Promotions
● Current merchant rates
Important: Do not submit claims to Wildfire when the missing rewards appear to be caused by a Rove promotion.
Instead:
● Escalate to Engineering
● Escalate to Arhan when appropriate
Wildfire does not manage Rove promotional bonuses.""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Incorrect Miles & Promotional Multipliers"
    },
    {
        "text": """Sub-$15 Purchases
Wildfire may review purchases under $15, but merchant approval is not guaranteed.
Before submission, verify:
● Valid receipt exists
● Eligible products were purchased
● Attribution requirements were met
● No duplicate claim exists
● The purchase should have reasonably tracked
Member Communication
Do not speculate about approval likelihood. Continue to communicate that:
● The claim is under review.
● The merchant is investigating.
● Additional escalation may be required.
Use the approved canned responses.
Expectations
Merchant response rates for low-value purchases may be limited and resolution timelines may be extended. Always set conservative expectations with members.""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Sub-$15 Purchases"
    },
    {
        "text": """Provider Verification
Before submitting any shopping claim, verify the correct provider in the CS Dashboard. Transactions originating from the browser extension are generally associated with Wildfire.
If the dashboard and member explanation appear inconsistent:
● Verify the purchase method.
● Review transaction details.
● Confirm the correct provider before submission.
Submitting claims to the wrong provider can significantly delay resolution.
Always use the provider listed in the CS Dashboard unless further investigation confirms otherwise.

Wildfire Payout Timeline:""",
        "source": "Shopping Procedures -> Wildfire Guidelines - Provider Verification & Timeline"
    },

    # =========================================================================
    # TAB: Shopping Procedures -> Sub-tab: Loyalize Guidelines
    # =========================================================================
    {
        "text": """Loyalize-Specific Guidelines
Overview
Loyalize is one of Rove's shopping partners used to track, validate, and process shopping rewards.
When communicating with Loyalize:
● Use cashback or rewards terminology.
● Do not use the term "miles."
● Follow Loyalize's claim submission requirements and investigation timelines.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Overview"
    },
    {
        "text": """Loyalize Claim Types
When submitting a claim through Loyalize, select the claim type that most accurately reflects the issue.
Missing Cashback
Use when:
● The transaction appears in Pending status.
● Cashback amount is $0.
Before submitting, first determine whether the $0 amount is expected.
Review:
● Offer terms
● Excluded products
● Coupon usage
● Merchant restrictions
● Disqualification indicators
Do not submit a claim if there is a clear reason the transaction is ineligible.
Incorrect Cashback Amount
Use when:
● A cashback amount is pending.
● The amount does not appear to match the offer terms.
Before submitting:
● Review the original offer.
● Review category exclusions.
● Review promotional terms.
● Confirm the earning rate was calculated correctly.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Claim Types Part 1"
    },
    {
        "text": """Untracked Transaction
Use when:
● The transaction has not appeared as Pending.
● More than 10 days have passed since purchase.
Delayed Cashback
Use when:
● The transaction remains Pending.
● More than 100 days have passed since Pending status began.
Before submitting:
● Verify the rewards have not already posted.
● Verify the transaction is still showing as Pending.
Other
Use only when no standard claim type accurately describes the issue.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Claim Types Part 2"
    },
    {
        "text": """Submission Requirements
Important Submission Rule
Do not submit a claim if:
● The member ID does not populate automatically.
● The merchant does not populate automatically.
These are indicators that:
● The click may not have tracked.
● The incorrect merchant may have been selected.
● The request may contain invalid information.
Important: Do not submit the claim to Wildfire simply because Loyalize cannot locate the member or merchant. The issue must be investigated first.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Submission Requirements"
    },
    {
        "text": """Troubleshooting: User or Merchant Does Not Populate
If the member or merchant does not populate automatically:
Step 1: Verify Provider
Confirm the transaction actually belongs to Loyalize.
Check:
● Member transaction history
● Shopping Dashboard
● Provider listed in the report
Step 2: Verify Purchase Date
Review:
● Purchase date
● Receipt date
● Click date
These dates should align reasonably with one another.
Step 3: Verify Click Attribution
Review the Shopping Report.
Compare:
● Clicked At timestamp
● Purchase timestamp
Confirm the member selected the correct transaction when submitting the claim.
Step 4: Check for Existing Submissions
Before creating a new request:
Review:
● Loyalize request history
● Zendesk submissions
● Historical submission logs
Duplicate requests should be avoided whenever possible.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Troubleshooting: User or Merchant Does Not Populate"
    },
    {
        "text": """Merchant Policies & Validation Rules
U.S. Purchases Only
Rove shopping offers are intended for U.S.-based purchases unless otherwise specified. We cannot guarantee rewards for purchases made outside the United States.
Before submitting:
● Confirm purchase eligibility.
● Verify purchase location when necessary.
● Review Atlas session recordings if additional verification is needed.
Coupon & Promotional Code Usage
Using coupon codes, promotional codes, or discounts not approved by the merchant may result in:
● Reduced rewards
● $0 rewards
● Transaction disqualification
Always review the merchant's offer terms before escalating a claim.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Merchant Policies & Coupons"
    },
    {
        "text": """Terminology Guidelines
Member-Facing Language
Always use:
● Rove Miles
● Miles
● Rewards
Merchant-Facing Language
Use:
● Cashback
● Rewards
Do not refer to rewards as miles when communicating with Loyalize.
Merchant Investigation Timelines
Once a claim has been submitted:
● Loyalize generally allows merchants up to 8 weeks to investigate.
● Follow-up requests should be limited during this review period.
Additional follow-up should only occur when:
● New information is available.
● Documentation needs to be added.
● Existing information needs correction.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Terminology and Timelines"
    },
    {
        "text": """Member Updates
If a member requests an update during the review period, use language such as:
"Your request is currently under review by the merchant. Merchant investigations may take up to 8 weeks, and we will provide updates as soon as additional information becomes available."
Best Practices
Always:
● Verify the correct provider before submitting.
● Verify click attribution.
● Verify purchase eligibility.
● Review offer exclusions.
● Check for duplicate submissions.
● Set conservative expectations.
● Document all actions in Atlas.
Never:
● Promise merchant approval.
● Promise rewards will be awarded.
● Submit claims without validating the information.
● Submit to another provider simply because a request cannot be located.""",
        "source": "Shopping Procedures -> Loyalize Guidelines - Member Updates and Best Practices"
    },
    # =========================================================================
    # SECTION 11: Miles & Account Procedures(PAGES 123-136)
    # =========================================================================
    {
        "text": """Rove Miles & General Procedures
Overview
This section covers:
● Rove Miles
● Referral Program
● Account Management
● Login Assistance
● General Member Questions
● Common Member-Facing Responses
For hotel, flight, shopping, and refund-specific procedures, refer to the applicable SOP sections.

Links to most common affiliate referrals: Affiliate Referral Codes


Rove Miles Quick Reference:
Topic | Quick Answer
Referral bonus | Earned after referred user earns 250 miles
Referral commission | 10 percent for first 6 months
Shopping pending | 30 to 100 days
Flight miles | After travel
Hotel miles (non-refundable) | At booking
Hotel miles (refundable) | After stay
Loyalty Eligible hotel miles | 8 to 12 weeks after checkout""",
        "source": "Rove Miles & General Procedures - Overview & Quick Reference"
    },
    {
        "text": """Rove Miles & Referral Program
What Are Rove Miles?
Rove Miles are flexible travel rewards that can be used for:
● Flights
● Hotels
● Transfer partners
Member Response
"Rove Miles are flexible travel rewards you can use like a digital currency for flights and hotels."

Using Rove Miles
Members may:
● Redeem miles for flights
● Redeem miles for hotels
● Transfer miles to eligible loyalty partners
Member Response
"You can redeem Rove Miles for flights, hotels, or transfer them to partner loyalty programs."

Transfer Partners
Rove Miles may be transferred to participating loyalty programs.
Member Response
"You can transfer Rove Miles to a variety of airline and hotel loyalty programs. Most transfers occur at a 1:1 ratio, with some exceptions such as Accor."
Refer to the most current partner list for up-to-date transfer options and transfer ratios.""",
        "source": "Rove Miles & General Procedures - Rove Miles Description & Redemptions"
    },
    {
        "text": """Referral Program
How Referrals Work
New Member Reward
When a new member signs up using a referral link:
● They receive the current referral signup bonus.
● Standard bonus is typically 500 miles unless otherwise specified by a promotion.
Referrer Reward
The referrer receives:
● A referral bonus after the referred member earns 250 miles through eligible Rove travel or shopping activity.
● 10 percent of the miles earned by the referred member during their first 6 months.
Important: Referrers do not receive their referral bonus immediately when someone signs up. The referred member must first earn 250 miles through eligible activity.
Member Response
"When someone signs up using your referral link, they'll receive the signup bonus immediately. You'll receive your referral bonus once they earn 250 miles through eligible activity, and you'll also earn 10% of the miles they collect during their first six months." """,
        "source": "Rove Miles & General Procedures - Referral Program Mechanics"
    },
    {
        "text": """Missing or Pending Referral Miles
If a member believes referral miles are missing, request:
● Referral link
● Name of referred member
● Phone number associated with the account
Member Response
"Referral and bonus miles are added manually. Please share the referral link, phone number, or name associated with the referral so we can investigate."

Referral Link Requests
Members interested in enhanced referral offers must be reviewed by the Marketing Team.
Send the canned response: “Affiliate Referral Request”
Important: Rove referral campaigns are currently intended for U.S.-based audiences.Requests involving non-U.S. audiences should be reviewed carefully before approval.""",
        "source": "Rove Miles & General Procedures - Missing Referrals & Link Requests"
    },
    {
        "text": """Adding Referral Miles for New Signups
Step 1: Confirm Referral Link
If the member claims they signed up through a referral link but did not receive the bonus, request the referral URL.
Step 2: Verify Existing Referral Status
Review the member account. If a referral is already attached, no additional referral may be added.
If no referral exists, add the referral associated with the provided URL.
Step 3: Notify Member
Referral Added:
"Thank you for sharing your referral link. We've successfully applied the referral to your account."
Referral Already Exists:
"We're unable to apply this referral because a referral has already been associated with your account."

Referral Codes
Important: Rove uses referral links rather than referral codes.
Member Response
"Rove referrals work through referral links rather than referral codes. Sign-up must be completed through the referral link." """,
        "source": "Rove Miles & General Procedures - Adding Referral Miles and Referral Codes Policy"
    },
    {
        "text": """Pending Miles Questions
Shopping Miles Still Pending
Shopping rewards often remain pending while merchants validate transactions and pay commissions.
Standard Timeline
● Pending usually begins within 24 hours
● Some merchants may take up to 10 days
● Final posting may take 30–100 days
Member Response
"Shopping miles typically begin pending within 24 hours, although some merchants may take up to 10 days. Final posting depends on when the merchant validates the purchase and pays the commission, which may take 30–100 days."
Resolution
● Confirm timeline with member.
● Answer any remaining questions.
● Close ticket if no additional action is required.""",
        "source": "Rove Miles & General Procedures - Pending Shopping Miles Questions"
    },
    {
        "text": """Account Management
Delete My Account
Account deletion is completed through: Remove Information in the CS Panel.
Member Response
"We're sorry to see you go. We'll remove all personally identifiable information associated with your account. Only your phone number will be retained for fraud prevention purposes. This process typically takes 3–5 business days." """,
        "source": "Rove Miles & General Procedures - Account Deletion Process"
    },
    {
        "text": """Account Recovery: Lost Phone Number
When This Applies
Use this workflow when a member can no longer access the phone number associated with their account.
Step 1: Verify Identity
Request:
● Associated email address
● Previous phone number
For fraud prevention, the member must send an email from the email address associated with the account to: support@rovemiles.com 
The email must include the previous phone number.
Step 2: Internal Escalation
● Tag Kevin in Atlas.
● Send Kevin a Slack message with the ticket link.
● Include verified member information.
Step 3: Update Member
"Thank you for providing your information. I've escalated your request to our internal team and we'll follow up once the account recovery process has been completed."
Step 4: Close Ticket
After internal confirmation:
"Your account recovery request has been completed. Please let us know if you experience any further issues accessing your account." """,
        "source": "Rove Miles & General Procedures - Lost Phone Number Account Recovery Workflow"
    },
    {
        "text": """Login Assistance
General Login Help
Member Response
"If you already have an account, use the same sign-in/sign-up button and enter your email address and password. If you're having trouble accessing your account, please confirm your registered email address or try resetting your password."

OTP Code Not Received
Step 1:
Ask the member to:
1. Log out
2. Log back in
3. Request a new code

Step 2 (iPhone):
If the issue continues:
1. Open Settings
2. Select Apps
3. Open Messages
4. Open RCS Messaging
5. Turn RCS Messaging Off
6. Request a new code""",
        "source": "Rove Miles & General Procedures - Login Assistance & OTP Troubleshooting"
    },
    {
        "text": """Payment & Refund Questions
Refund Timeline
Member Response
"Refunds are returned to the original payment method and typically process within 5–10 business days."

Change Card Used for Booking
Member Response
"Once a booking has been charged, the payment cannot be transferred to a different card. You may use another card for incidental charges at the hotel."

General Rove FAQs
How Does Rove Make Money?
Member Response
"Rove works with merchants and travel partners who pay us commissions. We return a portion of that value to members in the form of Rove Miles."

Mobile App
Member Response
"Rove does not currently have a mobile app. For now, all features are available through the website." """,
        "source": "Rove Miles & General Procedures - Payment, Refund & FAQ Responses"
    },
    {
        "text": """Member Verification Requirements
"The more sensitive the request, the stronger the verification required."
Member verification is required whenever an account change, security-sensitive action, or account recovery request is being performed.
The purpose of verification is to:
● Protect member accounts
● Prevent fraud
● Prevent unauthorized account access
● Ensure account changes are made only at the request of the account owner
When in doubt, verify before making account changes.

Verification Principles
Agents should never:
● Change account information without verification.
● Provide account-specific information to an unverified individual.
● Remove account security protections without verification.
● Assume a member owns an account simply because they know basic account details.
If verification cannot be completed, escalate the case to a Team Lead or Manager.""",
        "source": "Rove Miles & General Procedures - Verification Requirements & Principles"
    },
    {
        "text": """Verification Levels
Level 1: Standard Verification
Use for general account questions and non-sensitive inquiries.
Examples:
● Referral questions
● Miles posting questions
● General booking questions
● Shopping inquiries
Verification may include:
● Confirming email address
● Confirming phone number
● Confirming booking reference
No additional verification is typically required.
Level 2: Sensitive Account Actions
Use when the member is requesting changes to their account.
Examples:
● Updating account information
● Referral adjustments
● Manual miles adjustments
● Reviewing account-specific activity
Verify at least two of the following:
● Email address
● Phone number
● Booking reference
● Recent transaction information
If information does not match, do not proceed.""",
        "source": "Rove Miles & General Procedures - Verification Levels 1 and 2"
    },
    {
        "text": """Level 3: Account Recovery & Security Requests
Use for high-risk requests involving account access.
Examples:
● Lost phone number
● Cannot receive login code
● Account recovery
● Account merge requests
● Suspected unauthorized access
Required Verification
The member must send an email from the email address currently associated with the account.
The email should include:
● Full name
● Previous phone number
● Description of the issue
Internal Escalation
Once verification is completed:
● Document verification in Atlas.
● Escalate according to the Account Recovery workflow.
Do not make account changes before verification is completed.""",
        "source": "Rove Miles & General Procedures - Verification Level 3"
    },
    {
        "text": """Account Deletion Requests
Before deleting account information:
Verify:
● Member email address
● Member phone number
If there is any concern regarding account ownership, escalate before proceeding.
Documentation
Atlas notes should indicate:
● Verification completed
● Method of verification
● Date completed
● Agent completing verification
Name Corrections for Flight Bookings
When requesting a name correction, verify passenger identity through:
● Passport (international flights)
● Government-issued ID (domestic flights)
Do not submit name correction requests without supporting documentation when documentation is required by the airline.""",
        "source": "Rove Miles & General Procedures - Verification for Account Deletion & Flight Name Corrections"
    },
    {
        "text": """Fraud & Suspicious Activity
Escalate immediately if:
● Member cannot verify account ownership.
● Multiple individuals claim ownership of the same account.
● Account activity appears suspicious.
● Member requests access to another person's account.
● Information provided conflicts with account records.
Do not make changes to the account until guidance is received.
Documentation Requirements
Whenever verification is performed, document:
● Verification method used
● Information verified
● Any supporting documentation received
● Any escalation performed
Example Atlas Note:
Identity verified via account email and phone number. Member provided confirmation from associated email address. Account recovery request escalated to Kevin for review.
Proper documentation ensures future agents can understand what verification steps were completed.""",
        "source": "Rove Miles & General Procedures - Fraud Escalation & Verification Documentation"
    },
    # =========================================================================
    # SECTION 12: Document Info & Conclusion (PAGES 137-141)
    # =========================================================================
    {
        "text": """Document Information

Version: 1.0
Last Updated: June 12, 2026
Document Owner: Rove Member Support Leadership
Review Frequency: Quarterly

Revision History

Version 1.0 — Initial SOP release
Version 1.1 — """,
        "source": "Document Info & Conclusion - Administrative Information"
    },
    {
        "text": """Final Notes:

This SOP serves as the primary reference guide for Member Support operations at Rove.
While no document can cover every situation, the principles outlined throughout this guide
should be used to inform decision-making when handling member interactions. When uncertain,
prioritize accuracy, empathy, clear communication, and proper documentation.
Remember:
● Follow established procedures.
● Set realistic expectations.
● Document thoroughly.
● Escalate appropriately.
● Maintain ownership of your tickets.
● Treat every member interaction as an opportunity to strengthen trust in Rove.
As Rove continues to grow, this SOP will evolve alongside our products, partners, and support
processes. Team members are encouraged to identify opportunities for improvement and share
feedback to help ensure this document remains accurate, effective, and useful.""",
        "source": "Document Info & Conclusion - Final Notes & Core Operational Principles"
    },
    {
        "text": """Notes & General Info
 
To be added to the rest of the document as needed.

● Partial Refund Calculation (for hotel rate adjustment)
● How to confirm booking and provide HCN without contacting hotel - in panel here:
● TO ADD: Banning Users for disputes/chargebacks
● What to do when a hotel is overbooked (process including hotel options provided by
supplier, refunds, canned responses, etc)
● Partial refund for flight with miles boost""",
        "source": "Document Info & Conclusion - Notes & General Info"
    },
]