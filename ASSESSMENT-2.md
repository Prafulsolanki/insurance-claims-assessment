Assessment-2: System Explanation
1. System Overview

This system processes FNOL (First Notice of Loss) insurance documents automatically.
It extracts important claim information, validates mandatory fields, and routes claims to the correct workflow based on predefined business rules.

2. System Workflow

The system follows a step-by-step approach: FNOL document (PDF) is provided as input Text is extracted from the document Important fields such as policy number, claim type, and estimated damage are identified Mandatory fields are validated Business rules are applied Final routing decision is generated in JSON format

3. Edge Cases Handling

Some special situations include: Missing mandatory fields Unclear or unreadable document text Missing damage estimate Ambiguous claim description In such cases, the system routes the claim to Manual Review to avoid incorrect automation.

4. Business Rules Explanation

If estimated damage is less than ₹25,000, the claim is sent to Fast-track If mandatory information is missing, it is sent to Manual Review If fraud-related keywords are found, it is flagged for Investigation Injury-related claims are routed to a Specialist Queue

5. Future Improvements

The system can be enhanced by: Adding OCR support for scanned documents Using AI/LLM models for better text understanding Implementing fraud detection using machine learning Storing claims in a database for tracking and analytics