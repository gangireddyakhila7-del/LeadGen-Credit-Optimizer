MOCK_LEADS = [
    {
        "Company": "Innovate AI Solutions",
        "Industry": "Software",
        "Location": "Austin, TX",
        "Tech_Stack": ["Python", "React", "AWS"],
        "AI_Score": 0.95 
    },
    {
        "Company": "WebTech Movers",
        "Industry": "Software",
        "Location": "Austin, TX",
        "Tech_Stack": ["JavaScript", "React", "Node.js"],
        "AI_Score": 0.88  
    },
    {
        "Company": "Texas Oil & Gas Co.",
        "Industry": "Energy",
        "Location": "Dallas, TX", 
        "Tech_Stack": ["SAP", "Oracle"],
        "AI_Score": 0.30 
    },
    {
        "Company": "QuickServe Health",
        "Industry": "Healthcare",
        "Location": "Austin, TX",
        "Tech_Stack": ["Java", "SQL"],
        "AI_Score": 0.55  
    },
    {
        "Company": "Front-End Heroes",
        "Industry": "Software",
        "Location": "San Francisco, CA", 
        "Tech_Stack": ["React", "TypeScript"],
        "AI_Score": 0.90
    },
    {
        "Company": "Pyramid Consulting",
        "Industry": "Software",
        "Location": "Austin, TX",
        "Tech_Stack": ["Python", "Django"],
        "AI_Score": 0.92 
    }
]

def find_hyper_targeted_leads(tech_filter, location_filter):
    """
    Implements the smart dual-filter with AI-Readiness prioritization.
    This logic saves the user from slow, broad scraping.
    """
    print("\n--- Running AI-Guided Dual-Filter Search ---")
    print(f"User Input: Tech Stack '{tech_filter}' in Location '{location_filter}'")

    found_leads = []
    MIN_AI_SCORE = 0.80

    for company in MOCK_LEADS:
        location_match = (company["Location"] == location_filter)
        tech_match = (tech_filter in company["Tech_Stack"])
        ai_match = (company["AI_Score"] >= MIN_AI_SCORE)

        if location_match and tech_match and ai_match:
            found_leads.append(company)

    return found_leads

# Example usage for demonstration:
TECH_INPUT = "React"
LOCATION_INPUT = "Austin, TX"
results = find_hyper_targeted_leads(TECH_INPUT, LOCATION_INPUT)

if results:
    sorted_results = sorted(results, key=lambda x: x['AI_Score'], reverse=True)
    print("\n✅ SUCCESS: Hyper-Targeted Leads Found by AI-Filter!")
    print(f"Total High-Value Leads Found: {len(sorted_results)}")
    print("\n--- High-Value Leads Ready for Enrichment (Maximized Credit Value) ---")
    for lead in sorted_results:
        print(f"  - Company: {lead['Company']}")
        print(f"    Tech Stack: {lead['Tech_Stack']}, Location: {lead['Location']}")
        print(f"    AI-Readiness Score: {lead['AI_Score']}")
else:
    print("\n❌ FAILED: No leads matched all criteria, even with the smart filter.")

print("\n==================================================================")