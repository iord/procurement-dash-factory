# Data Sources Analysis

## 1. TED (Tenders Electronic Daily) - EU

### Dataset Types:
- **Contract Notices** - New tender opportunities
- **Contract Award Notices** - Awarded contracts
- **Prior Information Notices** - Advance notices
- **Qualification System Notices** - Supplier qualifications
- **Design Contests** - Architecture/design competitions
- **Concession Notices** - Service concessions

### Total Datasets: **~500,000 tenders/year**

### Key Fields:
- Tender ID, Title, Description
- CPV Codes (product/service classification)
- Country, Region, City
- Contracting Authority
- Value (EUR)
- Deadline Date
- Award Date, Winner
- Document Links

### Top Interim Facts for Users:
1. **Total Active Tenders** - Currently open opportunities
2. **Total Value** - Sum of all tender values
3. **Average Tender Value** - Mean contract size
4. **Top 5 Countries by Volume** - Most active markets
5. **Top 5 Categories (CPV)** - Most common procurement types
6. **Deadline This Week** - Urgent opportunities
7. **Recent Awards** - Last 30 days
8. **Win Rate by Company** - Success metrics

---

## 2. SAM.gov (System for Award Management) - USA

### Dataset Types:
- **Contract Opportunities** - Federal opportunities
- **Entity Registrations** - Registered vendors
- **Exclusions** - Debarred entities
- **Federal Hierarchy** - Agency structure
- **Wage Determinations** - Labor standards
- **Assistance Listings** - Grant programs

### Total Datasets: **~100,000 opportunities/year**

### Key Fields:
- Notice ID, Title, Description
- NAICS Codes (industry classification)
- Agency, Office
- Set-Aside Type (Small Business, 8(a), etc.)
- Place of Performance
- Value Range
- Response Deadline
- Point of Contact

### Top Interim Facts for Users:
1. **Open Opportunities** - Active federal contracts
2. **Set-Aside Opportunities** - Small business specific
3. **Total Estimated Value** - Government spend
4. **Top Agencies** - Most active departments
5. **Top NAICS Codes** - Industry focus
6. **Upcoming Deadlines** - Next 7/30 days
7. **Recently Posted** - Last 24 hours
8. **Contract Awards** - Recent winners

---

## 3. KIMDIS (Central Electronic Registry of Public Contracts) - Greece

### Dataset Types:
- **Open Tenders** - Active procurements
- **Restricted Procedures** - Qualified bidders only
- **Direct Awards** - Non-competitive contracts
- **Framework Agreements** - Multi-year contracts
- **Dynamic Purchasing Systems** - Ongoing supplier lists
- **Contract Modifications** - Changes to existing contracts

### Total Datasets: **~30,000 tenders/year**

### Key Fields:
- Tender Code (ADA)
- Title, Subject
- CPV Codes
- Contracting Authority
- Budget (EUR)
- Submission Deadline
- Evaluation Criteria
- Legal Framework

### Top Interim Facts for Users:
1. **Active Greek Tenders** - Open opportunities
2. **Total Budget** - Available funding
3. **Top Contracting Authorities** - Most active buyers
4. **Regional Distribution** - By prefecture
5. **Category Breakdown** - By CPV
6. **Average Contract Size** - Typical values
7. **Tender Type Distribution** - Open vs Restricted
8. **Deadline Calendar** - Upcoming submissions

---

## 4. Diavgeia (Transparency Portal) - Greece

### Dataset Types:
- **Decisions** - All public decisions
- **Expenditures** - Payment records
- **Appointments** - Personnel changes
- **Licenses** - Permits and authorizations
- **Contracts** - Signed agreements
- **Budget Approvals** - Financial decisions

### Total Datasets: **~2 million decisions/year**

### Key Fields:
- ADA (Unique ID)
- Decision Type
- Organization
- Subject
- Amount (if applicable)
- Date Published
- Legal Basis
- Related Documents

### Top Interim Facts for Users:
1. **Total Decisions Published** - Transparency metric
2. **Total Expenditure** - Public spending
3. **Top Organizations** - Most active entities
4. **Decision Type Breakdown** - Categories
5. **Recent Contracts** - Last signed
6. **Budget Allocations** - By ministry
7. **Compliance Rate** - Publishing timeliness
8. **Document Availability** - Access statistics

---

## Unified Dashboard Template

### Key Performance Indicators (Top Row):
```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│  Active Tenders │   Total Value   │  Avg. Contract  │ Urgent (7 days) │
│     12,543      │   EUR 45.2B     │   EUR 3.6M      │      234        │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

### Visualization Tabs (Power BI Style):
1. **Overview** - KPIs + Timeline + Geography
2. **By Category** - CPV/NAICS breakdown, treemap
3. **By Region** - Country/State map, regional trends
4. **By Value** - Distribution, large contracts
5. **Timeline** - Trends, seasonality, forecasts
6. **Winners** - Award analytics, top contractors

### Minimal Scrolling Layout:
- Fixed header with KPIs
- Tab navigation below KPIs
- Single screen per tab
- All charts visible without scrolling
- Responsive grid layout (2x2 or 3x2)
