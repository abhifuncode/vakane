# -*- coding: utf-8 -*-
"""All site content lives here. Edit this file, then run: python3 src/build.py"""

BRAND = {
    "name": "Vakane Engineering",
    "legal": "Vakane Engineering",
    "tagline": "Certification, without the guesswork.",
    "phone": "+91 90000 00000",
    "phone2": "+91 90000 00001",
    "email": "hello@vakane.example",
    "sales_email": "sales@vakane.example",
    "address": "Office 401, Business Centre, Andheri East, Mumbai 400069, India",
    "reg_address": "Registered office address goes here, Mumbai, India",
    "hours": "Mon – Sat, 9:30 am – 7:00 pm IST",
    "whatsapp": "919000000000",
    "socials": {"LinkedIn": "#", "Instagram": "#", "YouTube": "#", "X": "#"},
}

# --------------------------------------------------------------------------
# Service categories (the nine pillars)
# --------------------------------------------------------------------------
CATEGORIES = [
    {
        "slug": "management-system-certification", "kind": "msys", "num": "01",
        "name": "Management System Certification",
        "short": "ISO standards that prove your processes are consistent, safe and auditable.",
        "intro": "A certified management system tells customers, regulators and tender committees that the way you run your business is documented, measured and independently verified. We take you from gap analysis to certificate, and keep you audit-ready every year after.",
    },
    {
        "slug": "industry-specific-certification", "kind": "industry", "num": "02",
        "name": "Industry-Specific Certification",
        "short": "Sector schemes for food, automotive, aerospace, textiles, pharma and more.",
        "intro": "Some markets ask for more than a generic ISO certificate. Food retailers want GFSI-benchmarked schemes, carmakers want IATF 16949, export buyers want Halal or organic proof. We match you to the scheme your buyers actually recognise.",
    },
    {
        "slug": "product-certification", "kind": "product", "num": "03",
        "name": "Product Certification",
        "short": "Marks and approvals that let your product be sold legally — in India and abroad.",
        "intro": "Whether you manufacture in India or import into it, most regulated products need a mark before they reach a shelf. We identify the right standard, manage lab testing, prepare the technical file and deal with the regulator until the licence is in your hands.",
    },
    {
        "slug": "customer-compliance-audit", "kind": "audit", "num": "04",
        "name": "Customer Compliance Audits",
        "short": "Social, ethical and security audits demanded by global brands and retailers.",
        "intro": "Global buyers audit their supply chain for labour practices, safety and security before they place orders. We prepare your site, close the gaps in advance and stay with you through the audit day so findings are minimal and corrective actions are quick.",
    },
    {
        "slug": "business-process-training", "kind": "training", "num": "05",
        "name": "Business Process & Training",
        "short": "Auditor courses, lean tools and process improvement your team can use on Monday.",
        "intro": "Certificates fade if the team behind them doesn't understand the system. Our practical courses build internal capability — from lead auditor qualifications to shop-floor improvement methods — delivered online, in-house or as open public batches.",
    },
    {
        "slug": "accreditation", "kind": "accreditation", "num": "06",
        "name": "Accreditation Support",
        "short": "NABL, NABH and ISO/IEC 17000-series readiness for labs, hospitals and certifiers.",
        "intro": "Accreditation is the certification of the certifiers — and it is demanding. We help testing labs, calibration labs, hospitals, inspection bodies and certification bodies build systems that satisfy assessors the first time.",
    },
    {
        "slug": "inspection-services", "kind": "inspection", "num": "07",
        "name": "Inspection Services",
        "short": "Independent eyes on your goods, factories and shipments — before money changes hands.",
        "intro": "An inspection report is cheap insurance. Our inspectors check quality, quantity, packing and loading against your specification, and send a photo-rich report the same day, so you can release payment or hold a shipment with confidence.",
    },
    {
        "slug": "compliance-reports", "kind": "report", "num": "08",
        "name": "Compliance & ESG Reports",
        "short": "Sustainability, carbon and regulatory disclosures that stand up to scrutiny.",
        "intro": "Investors, lenders and large customers increasingly ask for evidence: emissions data, ESG ratings, BRSR disclosures, CBAM declarations. We collect the data, calculate it properly and present it in the format the requester expects.",
    },
    {
        "slug": "information-security", "kind": "security", "num": "09",
        "name": "Information & Cyber Security",
        "short": "ISO 27001, SOC 2, VAPT and privacy compliance for data-driven businesses.",
        "intro": "Enterprise customers won't share data with a vendor they can't trust. We help technology companies, BPOs and fintechs prove security maturity — through certification, technical testing, privacy assessments and an outsourced data protection officer.",
    },
]

# --------------------------------------------------------------------------
# Individual services.  kind -> which template sections are used.
# fields: slug, name, full (expanded name), cat (category slug), kind,
#         blurb (1–2 sentences), who (who needs it), region (optional),
#         validity, timeline (optional)
# --------------------------------------------------------------------------
S = []

def add(cat, kind, slug, name, full, blurb, who="", region="", validity="", timeline="", tags=None):
    S.append(dict(cat=cat, kind=kind, slug=slug, name=name, full=full, blurb=blurb, who=who,
                  region=region, validity=validity, timeline=timeline, tags=tags or []))

# ---- Management systems -----------------------------------------------------
M = "management-system-certification"
add(M, "msys", "iso-9001", "ISO 9001", "Quality Management System",
    "The world's most widely used business standard. It proves you deliver consistent quality, listen to customers and fix problems at their root.",
    "Any organisation of any size — manufacturers, service providers, traders and public bodies.", validity="3 years, with annual surveillance audits", timeline="4 – 8 weeks")
add(M, "msys", "iso-14001", "ISO 14001", "Environmental Management System",
    "A framework for controlling your environmental footprint — waste, emissions, resource use — and staying ahead of environmental law.",
    "Manufacturers, construction firms, logistics operators and anyone bidding for green-conscious customers.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-45001", "ISO 45001", "Occupational Health & Safety",
    "Shows that you identify workplace hazards systematically and protect the people who work for you.",
    "Factories, construction sites, warehouses, mines and contractors on large projects.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-22000", "ISO 22000", "Food Safety Management System",
    "Combines HACCP principles with a management system to control food safety hazards across the supply chain.",
    "Food processors, packaging makers, caterers, cold-chain and storage providers.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-27001", "ISO/IEC 27001", "Information Security Management System",
    "The benchmark for protecting confidential data. It covers people, process and technology controls, not just IT.",
    "IT and SaaS companies, BPOs, fintechs, healthcare providers and data processors.", validity="3 years, with annual surveillance audits", timeline="8 – 12 weeks")
add(M, "msys", "iso-13485", "ISO 13485", "Medical Devices Quality Management",
    "The quality standard regulators expect from medical device makers, with strict design control and traceability.",
    "Medical device manufacturers, component suppliers, sterilisers and distributors.", validity="3 years, with annual surveillance audits", timeline="8 – 12 weeks")
add(M, "msys", "iso-50001", "ISO 50001", "Energy Management System",
    "A structured way to measure energy use, set targets and cut power and fuel bills year on year.",
    "Energy-intensive industries, commercial buildings and designated consumers.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-22301", "ISO 22301", "Business Continuity Management",
    "Proves you can keep critical operations running through disruption — outages, disasters or supplier failure.",
    "Banks, data centres, outsourcing firms and critical suppliers.", validity="3 years, with annual surveillance audits", timeline="8 – 12 weeks")
add(M, "msys", "iso-20000", "ISO/IEC 20000-1", "IT Service Management",
    "Demonstrates disciplined delivery of IT services, from incident handling to change and capacity management.",
    "Managed service providers, IT help desks and internal IT departments.", validity="3 years, with annual surveillance audits", timeline="8 – 12 weeks")
add(M, "msys", "iso-37001", "ISO 37001", "Anti-Bribery Management System",
    "Shows that you have controls in place to prevent, detect and respond to bribery.",
    "Companies working with government, infrastructure contractors and exporters.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-41001", "ISO 41001", "Facility Management System",
    "A standard for running buildings and workplaces efficiently, safely and sustainably.",
    "Facility management companies, real-estate operators and campuses.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-21001", "ISO 21001", "Educational Organisations Management",
    "Helps schools, colleges and training providers show that learners get what they were promised.",
    "Schools, universities, coaching institutes and corporate academies.", validity="3 years, with annual surveillance audits", timeline="6 – 10 weeks")
add(M, "msys", "iso-42001", "ISO/IEC 42001", "AI Management System",
    "The first certifiable standard for responsible artificial intelligence — governance, risk and transparency for AI systems.",
    "Companies building or deploying AI products and models.", validity="3 years, with annual surveillance audits", timeline="8 – 14 weeks")

# ---- Industry specific ------------------------------------------------------
I = "industry-specific-certification"
add(I, "industry", "haccp", "HACCP", "Hazard Analysis & Critical Control Points",
    "A preventive food-safety system that pinpoints where hazards can enter your process and how you control them.",
    "Restaurants, food processors, dairies, bakeries and caterers.", validity="3 years", timeline="3 – 6 weeks")
add(I, "industry", "fssc-22000", "FSSC 22000", "Food Safety System Certification",
    "A GFSI-recognised scheme built on ISO 22000 — the one most global food brands ask their suppliers for.",
    "Food and beverage manufacturers supplying multinational brands and retailers.", validity="3 years", timeline="8 – 12 weeks")
add(I, "industry", "brcgs", "BRCGS", "Brand Reputation Compliance Global Standards",
    "A demanding retailer-led standard for food, packaging and storage, required by most UK and EU supermarkets.",
    "Exporters to UK and European retail chains.", validity="6 – 12 months, graded", timeline="10 – 14 weeks")
add(I, "industry", "gmp", "GMP", "Good Manufacturing Practice",
    "Confirms that products are made and controlled consistently to quality standards appropriate to their use.",
    "Pharma, nutraceutical, cosmetic and food supplement manufacturers.", validity="1 – 3 years", timeline="6 – 10 weeks")
add(I, "industry", "who-gmp", "WHO-GMP", "World Health Organization GMP",
    "GMP aligned to WHO guidelines — often a prerequisite for exporting medicines to emerging markets.",
    "Pharmaceutical manufacturers exporting to Africa, Asia and Latin America.", validity="Typically 3 years", timeline="3 – 6 months")
add(I, "industry", "halal", "Halal", "Halal Certification",
    "Verifies that ingredients, processing and handling meet Islamic dietary requirements.",
    "Food, cosmetic and pharma exporters to the Middle East and South-East Asia.", validity="1 – 2 years", timeline="3 – 6 weeks")
add(I, "industry", "kosher", "Kosher", "Kosher Certification",
    "Certifies that products comply with Jewish dietary law, a powerful signal in US and European retail.",
    "Food ingredient, spice and additive exporters.", validity="1 year", timeline="4 – 8 weeks")
add(I, "industry", "iatf-16949", "IATF 16949", "Automotive Quality Management",
    "The automotive industry's quality standard, mandatory for most tier-one and tier-two suppliers to carmakers.",
    "Auto component manufacturers and their suppliers.", validity="3 years", timeline="4 – 6 months")
add(I, "industry", "as9100", "AS9100", "Aerospace Quality Management",
    "ISO 9001 extended with aviation, space and defence requirements for safety, configuration and risk.",
    "Aerospace and defence component makers and service providers.", validity="3 years", timeline="4 – 6 months")
add(I, "industry", "gots", "GOTS", "Global Organic Textile Standard",
    "Tracks organic fibre from field to finished garment, including environmental and social criteria.",
    "Spinners, weavers, garment exporters and home-textile brands.", validity="1 year", timeline="6 – 10 weeks")
add(I, "industry", "oeko-tex", "OEKO-TEX", "OEKO-TEX Standard 100",
    "Confirms textiles have been tested for harmful substances and are safe for human use.",
    "Textile and apparel manufacturers, especially for babywear and intimates.", validity="1 year", timeline="4 – 6 weeks")
add(I, "industry", "fsc", "FSC", "Forest Stewardship Council Chain of Custody",
    "Proves wood, paper and packaging come from responsibly managed forests.",
    "Paper, packaging, furniture and printing companies.", validity="5 years, with annual audits", timeline="6 – 10 weeks")
add(I, "industry", "organic", "NPOP / NOP Organic", "Organic Production Certification",
    "Certifies organic farming and processing for the Indian (NPOP), US (NOP) and EU markets.",
    "Farmers, producer groups, processors and organic exporters.", validity="1 year", timeline="2 – 4 months")
add(I, "industry", "globalgap", "GLOBALG.A.P.", "Good Agricultural Practice",
    "A farm-level standard for safe, sustainable produce that most European retailers require.",
    "Fruit, vegetable and aquaculture growers and exporters.", validity="1 year", timeline="6 – 10 weeks")
add(I, "industry", "grs", "GRS", "Global Recycled Standard",
    "Verifies recycled content and responsible production across the textile and plastics supply chain.",
    "Recycled polyester, cotton and plastic product manufacturers.", validity="1 year", timeline="6 – 10 weeks")

# ---- Product certification ---------------------------------------------------
P = "product-certification"
def prod(kind, slug, name, full, blurb, who="", region="", validity="", timeline="", tags=None):
    add(P, kind, slug, name, full, blurb, who, region, validity, timeline, tags)

# India
prod("india", "bis-certification", "BIS Certification", "Bureau of Indian Standards",
     "India's national standards body runs several certification schemes. Many electronics, appliances and industrial goods cannot be made, imported or sold without a BIS licence.",
     "Indian manufacturers and foreign manufacturers exporting notified products to India.", "India", "2 years, renewable", "6 – 10 weeks", ["India", "Electronics"])
prod("india", "isi-mark", "ISI Mark", "ISI Mark under BIS Product Certification",
     "The familiar ISI mark is granted under BIS Scheme-I after factory inspection and testing. It is compulsory for products covered by Quality Control Orders.",
     "Manufacturers of cement, steel, cables, appliances, helmets, packaged water, toys and other QCO products.", "India", "1 – 2 years, renewable", "10 – 16 weeks", ["India"])
prod("india", "bis-crs", "BIS CRS Registration", "Compulsory Registration Scheme",
     "A test-and-register scheme for electronics and IT products. Samples are tested at a BIS-recognised lab and the product is registered online — no factory inspection.",
     "Brands, manufacturers and importers of mobiles, laptops, chargers, LED products, batteries and similar goods.", "India", "2 years, renewable", "4 – 8 weeks", ["India", "Electronics"])
prod("india", "bis-fmcs", "BIS FMCS", "Foreign Manufacturers Certification Scheme",
     "The route for overseas factories to obtain the ISI mark. It involves an Indian representative, factory audit abroad and sample testing in India.",
     "Overseas manufacturers of products under Indian Quality Control Orders.", "India", "1 – 2 years", "4 – 6 months", ["India"])
prod("india", "bis-scheme-x", "BIS Scheme-X", "Scheme X for Machinery & Equipment",
     "A conformity scheme introduced for machinery and electrical equipment safety. It relies on a declaration of conformity backed by testing and audit.",
     "Manufacturers and importers of machinery and electrical equipment covered by the Machinery Safety order.", "India", "Varies by product", "8 – 14 weeks", ["India", "Machinery"])
prod("india", "bis-eco-mark", "ECO Mark", "BIS Eco Mark Scheme",
     "A voluntary label for products that meet both ISI quality requirements and additional environmental criteria.",
     "Manufacturers of paper, plastics, paints, detergents and consumer goods wanting an environmental claim.", "India", "Linked to ISI licence", "10 – 16 weeks", ["India", "Sustainability"])
prod("india", "tec-certification", "TEC Certification", "Telecommunication Engineering Centre — MTCTE",
     "Mandatory testing and certification of telecom equipment before it can be sold or connected to networks in India.",
     "Makers and importers of routers, switches, IoT modules, smart meters and telecom equipment.", "India", "Valid while design unchanged", "6 – 12 weeks", ["India", "Telecom"])
prod("india", "wpc-eta", "WPC ETA Approval", "Equipment Type Approval — Wireless Planning & Coordination",
     "Required for any product using Wi-Fi, Bluetooth or other radio frequencies before import or sale in India.",
     "Importers and brands of wireless and Bluetooth devices.", "India", "Valid while design unchanged", "2 – 4 weeks", ["India", "Electronics"])
prod("india", "ais-certification", "AIS Certification", "Automotive Industry Standards",
     "Type approval and conformity of production for vehicles and automotive components under Indian motor vehicle rules.",
     "Vehicle makers, EV makers and automotive component manufacturers.", "India", "Varies", "8 – 16 weeks", ["India", "Automotive"])
prod("india", "ayush-premium-mark", "AYUSH Premium Mark", "AYUSH Premium Mark",
     "A higher-tier voluntary mark for AYUSH products that meet enhanced quality and safety requirements, useful for export credibility.",
     "Ayurvedic, Siddha, Unani and Homoeopathy product manufacturers.", "India", "3 years", "8 – 12 weeks", ["India", "Healthcare"])
prod("india", "ayush-standard-mark", "AYUSH Standard Mark", "AYUSH Standard Mark",
     "A voluntary mark confirming AYUSH products meet domestic regulatory quality requirements.",
     "AYUSH manufacturers selling primarily in India.", "India", "3 years", "6 – 10 weeks", ["India", "Healthcare"])
prod("india", "icmed-13485", "ICMED 13485", "Indian Certification for Medical Devices",
     "A national certification scheme for medical device quality, combining ISO 13485 with product-specific requirements.",
     "Indian medical device manufacturers.", "India", "3 years", "8 – 14 weeks", ["India", "Healthcare"])
prod("india", "eat-right-campus", "Eat Right Campus", "FSSAI Eat Right Campus",
     "An FSSAI initiative that recognises campuses — offices, colleges, hospitals — that serve safe, healthy food.",
     "Corporate campuses, universities, hospitals and canteens.", "India", "2 years", "6 – 10 weeks", ["India", "Food"])
prod("india", "epr-registration", "EPR Registration", "Extended Producer Responsibility — CPCB",
     "Producers, importers and brand owners of plastic packaging, electronics, batteries and tyres must register for EPR and meet recycling targets.",
     "Producers, importers and brand owners placing covered goods on the Indian market.", "India", "Annual compliance", "2 – 6 weeks", ["India", "Sustainability"])
prod("india", "cdsco-registration", "CDSCO Registration", "Central Drugs Standard Control Organisation",
     "Licences for manufacturing and importing medical devices, drugs and cosmetics in India, handled through the SUGAM portal.",
     "Medical device, drug and cosmetic manufacturers and importers.", "India", "Varies by licence", "6 – 20 weeks", ["India", "Healthcare"])

# Europe / UK
prod("intl", "ce-marking", "CE Marking", "Conformité Européenne",
     "The passport for selling in the European Economic Area. It declares that a product meets every applicable EU directive and regulation.",
     "Exporters of machinery, electronics, toys, medical devices, PPE and construction products to Europe.", "European Union", "Valid while product and law unchanged", "4 – 12 weeks", ["Europe", "Electronics", "Machinery"])
prod("intl", "ukca-marking", "UKCA Marking", "UK Conformity Assessed",
     "Britain's post-Brexit conformity mark for goods placed on the market in England, Scotland and Wales.",
     "Exporters selling regulated products into Great Britain.", "United Kingdom", "Valid while product and law unchanged", "4 – 10 weeks", ["UK"])
prod("intl", "rohs", "RoHS", "Restriction of Hazardous Substances",
     "Limits lead, mercury, cadmium and other hazardous substances in electrical and electronic equipment.",
     "Electronics and electrical equipment exporters to the EU and other RoHS markets.", "European Union", "Ongoing compliance", "2 – 4 weeks", ["Europe", "Electronics", "Sustainability"])
prod("reg", "reach", "REACH", "Registration, Evaluation, Authorisation & Restriction of Chemicals",
     "The EU chemicals regulation. Substances above one tonne per year must be registered, and articles must disclose substances of very high concern.",
     "Chemical exporters and manufacturers of articles sold in Europe.", "European Union", "Ongoing", "4 – 16 weeks", ["Europe", "Chemicals"])
prod("intl", "ped", "PED", "Pressure Equipment Directive",
     "CE conformity for boilers, vessels, piping and valves that operate above 0.5 bar.",
     "Manufacturers of pressure vessels, valves, fittings and heat exchangers.", "European Union", "Varies by module", "6 – 14 weeks", ["Europe", "Machinery"])
prod("intl", "atex", "ATEX", "Equipment for Explosive Atmospheres",
     "Required for equipment and protective systems used in potentially explosive environments such as refineries and mines.",
     "Makers of motors, pumps, lighting and instruments for hazardous areas.", "European Union", "Valid while design unchanged", "8 – 16 weeks", ["Europe", "Machinery"])
prod("intl", "kitemark", "Kitemark", "BSI Kitemark",
     "One of the UK's most trusted quality marks, showing a product is independently tested and continually monitored.",
     "Manufacturers of safety, construction, electrical and consumer products for the UK market.", "United Kingdom", "Ongoing, with surveillance", "8 – 14 weeks", ["UK"])
prod("intl", "wras", "WRAS", "Water Regulations Approval Scheme",
     "Confirms that plumbing products and materials in contact with drinking water meet UK water regulations.",
     "Makers of taps, valves, pipes, fittings and water heaters for the UK.", "United Kingdom", "5 years", "8 – 12 weeks", ["UK"])
prod("intl", "basec", "BASEC", "British Approvals Service for Cables",
     "A specialist cable certification recognised across the UK, Middle East and Africa.",
     "Cable and wire manufacturers.", "United Kingdom", "Ongoing, with surveillance", "10 – 16 weeks", ["UK", "Electrical"])
prod("intl", "vde", "VDE", "Verband der Elektrotechnik",
     "A respected German mark for electrical safety, often requested by European distributors.",
     "Manufacturers of cables, components, appliances and lighting.", "Germany", "Ongoing, with surveillance", "8 – 14 weeks", ["Europe", "Electrical"])
prod("intl", "dinplus", "DINplus", "DIN CERTCO DINplus",
     "A quality mark that goes beyond basic standards, common for wood pellets, pipes and construction products.",
     "Manufacturers selling into German-speaking markets.", "Germany", "Ongoing, with surveillance", "8 – 12 weeks", ["Europe"])
prod("intl", "enplus", "ENplus", "ENplus Wood Pellet Certification",
     "The leading quality scheme for wood pellets, covering production, storage and delivery.",
     "Pellet producers and traders.", "Europe", "Annual audits", "8 – 12 weeks", ["Europe", "Sustainability"])
prod("intl", "epal", "EPAL", "European Pallet Association",
     "Licensing for manufacturing and repairing EPAL Euro pallets to an exact specification.",
     "Pallet manufacturers and repairers.", "Europe", "Ongoing, with inspections", "6 – 10 weeks", ["Europe"])
prod("intl", "vds-approval", "VdS Approval", "VdS Schadenverhütung",
     "A German approval for fire protection and security products, widely accepted by insurers.",
     "Makers of fire alarms, sprinklers, extinguishing systems and security devices.", "Germany", "Ongoing, with surveillance", "10 – 20 weeks", ["Europe", "Fire & Safety"])
prod("intl", "e-mark", "E-Mark", "UNECE Vehicle Type Approval",
     "Type approval for vehicles and components under UNECE regulations, accepted across Europe and many other countries.",
     "Automotive component and accessory manufacturers.", "Europe / UNECE", "Valid while design unchanged", "8 – 16 weeks", ["Europe", "Automotive"])
prod("intl", "bre-global", "BRE Global", "BRE Global Certification",
     "Third-party approval for fire, security and construction products, listed in the UK's Red Book.",
     "Building, fire and security product manufacturers.", "United Kingdom", "Ongoing, with surveillance", "10 – 20 weeks", ["UK", "Fire & Safety"])
prod("intl", "cares", "CARES", "Certification Authority for Reinforcing Steels",
     "Product conformity certification for reinforcing steel and related products used in construction.",
     "Steel mills, fabricators and rebar suppliers.", "United Kingdom", "Ongoing, with surveillance", "10 – 16 weeks", ["UK", "Construction"])
prod("intl", "lwg", "Leather Working Group", "LWG Environmental Audit",
     "An environmental audit and rating for leather tanneries, requested by most global footwear and fashion brands.",
     "Tanneries and leather traders.", "Global", "Annual audit", "6 – 10 weeks", ["Global", "Sustainability"])

# Americas
prod("intl", "ul-certification", "UL Certification", "Underwriters Laboratories",
     "The best-known safety mark in North America. Retailers, insurers and inspectors frequently insist on it.",
     "Exporters of electrical products, components and appliances to the US and Canada.", "USA / Canada", "Ongoing, with factory follow-ups", "8 – 16 weeks", ["USA", "Electrical"])
prod("intl", "etl-certification", "ETL Listing", "ETL Listed Mark",
     "An alternative to UL that proves compliance with North American safety standards, issued by a recognised testing lab.",
     "Electrical, HVAC and lighting manufacturers.", "USA / Canada", "Ongoing, with factory follow-ups", "6 – 12 weeks", ["USA", "Electrical"])
prod("intl", "csa-certification", "CSA Certification", "Canadian Standards Association",
     "The main safety mark for electrical and gas products sold in Canada, also accepted in the US.",
     "Exporters of electrical, gas and plumbing products to Canada.", "Canada", "Ongoing, with factory follow-ups", "8 – 16 weeks", ["Canada", "Electrical"])
prod("intl", "csa-w47-1", "CSA W47.1", "Welding Company Certification",
     "Canadian certification for companies that perform fusion welding of steel structures.",
     "Steel fabricators and welding contractors supplying Canadian projects.", "Canada", "Annual review", "8 – 12 weeks", ["Canada", "Construction"])
prod("intl", "fcc-certification", "FCC Certification", "Federal Communications Commission",
     "Required for electronic devices sold in the US to ensure they don't cause harmful radio interference.",
     "Makers of wireless, IoT and electronic devices for the US.", "USA", "Valid while design unchanged", "3 – 6 weeks", ["USA", "Electronics"])
prod("reg", "fda-food-registration", "US FDA Food Facility Registration", "FDA Food Facility Registration",
     "Every facility that makes, packs or stores food for US consumption must register with the FDA and appoint a US agent.",
     "Food, spice, beverage and supplement exporters to the US.", "USA", "Renew every 2 years", "1 – 2 weeks", ["USA", "Food"])
prod("reg", "fda-device-registration", "US FDA Device Registration", "FDA Establishment Registration & Device Listing",
     "Medical device establishments must register and list their devices with the FDA before export to the US.",
     "Medical device manufacturers and exporters.", "USA", "Annual renewal", "1 – 3 weeks", ["USA", "Healthcare"])
prod("reg", "fda-drug-registration", "US FDA Drug Registration", "FDA Drug Establishment Registration & NDC Listing",
     "Drug establishments must register, list products and obtain National Drug Codes before shipping to the US.",
     "Pharmaceutical, API and OTC drug manufacturers.", "USA", "Annual renewal", "2 – 4 weeks", ["USA", "Healthcare"])
prod("reg", "fda-cosmetic-registration", "US FDA Cosmetic Registration", "Cosmetic Facility Registration & Product Listing",
     "Under MoCRA, cosmetic facilities and products marketed in the US must be registered and listed with the FDA.",
     "Cosmetic and personal care exporters to the US.", "USA", "Biennial renewal", "1 – 3 weeks", ["USA", "Healthcare"])
prod("reg", "fda-510k", "US FDA 510(k)", "Premarket Notification",
     "Demonstrates that a new medical device is substantially equivalent to a device already legally marketed in the US.",
     "Makers of Class II (and some Class I) medical devices.", "USA", "One-time clearance", "4 – 9 months", ["USA", "Healthcare"])
prod("reg", "canada-mdl", "Health Canada MDL", "Canadian Medical Device Licence",
     "Class II–IV devices need a Medical Device Licence, supported by MDSAP certification, before sale in Canada.",
     "Medical device manufacturers exporting to Canada.", "Canada", "Annual renewal", "3 – 6 months", ["Canada", "Healthcare"])
prod("intl", "nom-certification", "NOM Certification", "Norma Oficial Mexicana",
     "Mexico's mandatory technical standards for electrical, electronic, textile and consumer products.",
     "Exporters of regulated goods to Mexico.", "Mexico", "1 year, renewable", "6 – 12 weeks", ["Mexico"])
prod("intl", "nema", "NEMA", "National Electrical Manufacturers Association",
     "NEMA ratings define enclosure protection and electrical product performance expected by North American buyers.",
     "Makers of enclosures, motors, plugs and electrical equipment.", "USA", "Valid while design unchanged", "4 – 8 weeks", ["USA", "Electrical"])
prod("intl", "certipur-us", "CertiPUR-US", "CertiPUR-US Foam Certification",
     "Certifies that flexible polyurethane foam is made without certain harmful chemicals and meets emission limits.",
     "Foam, mattress and furniture manufacturers exporting to the US.", "USA", "Annual", "6 – 10 weeks", ["USA"])
prod("intl", "fm-approval", "FM Approvals", "FM Global Approval",
     "Testing and certification for fire protection, electrical and building products, valued by insurers worldwide.",
     "Fire protection, roofing and hazardous-location equipment makers.", "Global", "Ongoing, with audits", "3 – 9 months", ["USA", "Fire & Safety"])
prod("intl", "sefa", "SEFA", "Scientific Equipment & Furniture Association",
     "Performance standards for laboratory furniture, fume hoods and casework.",
     "Lab furniture and fume hood manufacturers.", "Global", "Valid while design unchanged", "6 – 10 weeks", ["USA"])
prod("intl", "esd-s20-20", "ANSI/ESD S20.20", "Electrostatic Discharge Control Programme",
     "Certifies a facility's programme for protecting sensitive electronics from electrostatic damage.",
     "Electronics manufacturers, EMS providers and handlers of sensitive components.", "Global", "3 years", "8 – 12 weeks", ["Electronics"])

# Asia, Middle East, Africa
prod("intl", "ccc-certification", "CCC Mark", "China Compulsory Certificate",
     "China's mandatory safety mark for listed products, from electronics to auto parts, before import or sale.",
     "Exporters of listed products to mainland China.", "China", "5 years, with annual follow-ups", "3 – 6 months", ["China", "Electronics"])
prod("intl", "kc-certification", "KC Mark", "Korea Certification",
     "South Korea's integrated certification mark for electrical safety and electromagnetic compatibility.",
     "Electronics and electrical exporters to South Korea.", "South Korea", "Valid while design unchanged", "6 – 12 weeks", ["Korea", "Electronics"])
prod("intl", "g-mark", "G-Mark", "Gulf Conformity Mark",
     "Required for low-voltage electrical products and toys sold across the GCC states.",
     "Exporters of electrical appliances and toys to the Gulf.", "GCC", "Valid while design unchanged", "6 – 10 weeks", ["Middle East"])
prod("intl", "saso-saber", "SASO / SABER", "Saudi Product Safety Programme",
     "Saudi Arabia's online conformity system. Products need a Product Certificate and a Shipment Certificate before customs clearance.",
     "Every exporter of regulated goods to Saudi Arabia.", "Saudi Arabia", "1 year (product), per shipment", "2 – 6 weeks", ["Middle East"])
prod("reg", "sfda", "SFDA Approval", "Saudi Food & Drug Authority",
     "Registration and listing of food, drugs, medical devices and cosmetics for the Saudi market.",
     "Food, pharma, device and cosmetic exporters to Saudi Arabia.", "Saudi Arabia", "Varies by product", "4 – 16 weeks", ["Middle East", "Healthcare", "Food"])
prod("intl", "eqm", "Emirates Quality Mark", "ECAS / EQM",
     "The UAE's conformity scheme for regulated products, with a voluntary quality mark for higher assurance.",
     "Exporters of regulated products to the UAE.", "UAE", "1 year", "4 – 8 weeks", ["Middle East"])
prod("intl", "kucas", "KUCAS", "Kuwait Conformity Assurance Scheme",
     "Kuwait's certificate of conformity programme for imported regulated products.",
     "Exporters of regulated goods to Kuwait.", "Kuwait", "Per shipment / 1 year", "2 – 4 weeks", ["Middle East"])
prod("intl", "soncap", "SONCAP", "Standards Organisation of Nigeria Conformity Assessment",
     "Nigeria's pre-export conformity programme. Regulated goods need a product certificate and a SONCAP certificate per shipment.",
     "Exporters of regulated goods to Nigeria.", "Nigeria", "Per shipment / 1 year", "2 – 4 weeks", ["Africa"])
prod("intl", "eac-certification", "EAC Certification", "Eurasian Conformity (TR CU / GOST R)",
     "The single conformity mark for the Eurasian Economic Union — Russia, Kazakhstan, Belarus, Armenia and Kyrgyzstan.",
     "Exporters of machinery, electronics, food and consumer goods to the EAEU.", "Eurasian Union", "1 – 5 years", "4 – 10 weeks", ["Russia"])
prod("reg", "kkdik", "KKDIK", "Turkey Chemical Registration",
     "Turkey's REACH-like chemicals regulation requiring registration of substances imported or produced above one tonne per year.",
     "Chemical exporters to Turkey.", "Turkey", "Ongoing", "8 – 20 weeks", ["Chemicals"])
prod("intl", "who-pqs", "WHO PQS", "WHO Performance, Quality & Safety",
     "Prequalification of immunisation equipment — cold-chain fridges, cool boxes, syringes — for UN procurement.",
     "Makers of vaccine cold-chain and injection equipment.", "Global", "Varies", "6 – 12 months", ["Healthcare", "Global"])
prod("intl", "fairtrade", "Fairtrade", "Fairtrade Certification",
     "Assures buyers that producers received fair prices and work under decent conditions.",
     "Producer organisations and traders of coffee, tea, cocoa, cotton, spices and more.", "Global", "3 years, with audits", "3 – 6 months", ["Global", "Sustainability"])
prod("intl", "proterra", "ProTerra", "ProTerra Non-GMO Standard",
     "Certifies non-GMO and sustainably produced feed and food ingredients across the supply chain.",
     "Soy, grain and feed producers and processors.", "Global", "1 year", "6 – 10 weeks", ["Global", "Food"])

# ---- Customer compliance audits ------------------------------------------------
A = "customer-compliance-audit"
add(A, "audit", "smeta-audit", "SMETA", "Sedex Members Ethical Trade Audit",
    "The most widely shared ethical audit format, covering labour, health and safety, environment and business ethics.",
    "Suppliers to UK and European retailers and brands.")
add(A, "audit", "amfori-bsci", "amfori BSCI", "Business Social Compliance Initiative",
    "A social audit system used by hundreds of European importers to assess factory working conditions.",
    "Garment, toy, footwear and home-goods suppliers.")
add(A, "audit", "slcp", "SLCP", "Social & Labor Convergence Program",
    "A converged assessment that replaces multiple brand audits with one verified data set.",
    "Apparel and footwear factories.")
add(A, "audit", "wca-audit", "WCA", "Workplace Conditions Assessment",
    "An audit of labour, health and safety, environment and management systems used by many US buyers.",
    "Suppliers to US retailers and importers.")
add(A, "audit", "sa8000", "SA8000", "Social Accountability Standard",
    "A certifiable standard for decent work, based on ILO conventions and human rights norms.",
    "Manufacturers seeking a recognised social certification.")
add(A, "audit", "ctpat", "C-TPAT", "Customs-Trade Partnership Against Terrorism",
    "A supply-chain security audit that helps US importers qualify for faster customs processing.",
    "Exporters shipping to the United States.")
add(A, "audit", "higg-fem", "Higg FEM", "Higg Facility Environmental Module",
    "A self-assessment and verification of environmental performance — energy, water, waste and chemicals.",
    "Apparel and footwear facilities.")
add(A, "audit", "fama-audit", "FAMA / Brand Audits", "Brand-specific ethical and quality audits",
    "Preparation for retailer-specific audit programmes from leading entertainment, retail and grocery brands.",
    "Suppliers onboarding with large global retailers.")
add(A, "audit", "grs-ccs-audit", "Scope Certificates", "Textile Exchange RCS / CCS / OCS",
    "Chain-of-custody audits for recycled and organic content claims in textiles.",
    "Spinners, fabric mills and garment exporters.")

# ---- Business process & training ------------------------------------------------
T = "business-process-training"
add(T, "training", "lead-auditor-training", "Lead Auditor Courses", "ISO 9001 / 14001 / 45001 / 27001 Lead Auditor",
    "Five-day accredited-format courses that qualify participants to plan and lead third-party audits.",
    "Quality professionals, consultants and aspiring auditors.", timeline="5 days")
add(T, "training", "internal-auditor-training", "Internal Auditor Training", "ISO Internal Auditor",
    "Practical two-day courses that teach employees to audit their own management system effectively.",
    "Teams maintaining an ISO certified system.", timeline="2 days")
add(T, "training", "six-sigma", "Lean Six Sigma", "Yellow, Green & Black Belt",
    "Data-driven problem solving that reduces defects and variation, taught through real project work.",
    "Engineers, operations managers and improvement teams.", timeline="2 – 10 days")
add(T, "training", "5s-kaizen", "5S & Kaizen", "Workplace Organisation & Continuous Improvement",
    "Simple, visual methods that make shop floors safer, cleaner and more productive within weeks.",
    "Factories, warehouses and service centres.", timeline="1 – 3 days")
add(T, "training", "documentation-support", "Process Documentation", "SOPs, manuals and process mapping",
    "We document how your business really works — procedures, work instructions and flowcharts that people actually follow.",
    "Growing companies formalising operations.")
add(T, "training", "gap-assessment", "Gap Assessment", "Readiness and gap analysis",
    "An independent check of where you stand against a standard or customer code, with a prioritised action plan.",
    "Any organisation planning certification or a customer audit.")

# ---- Accreditation ----------------------------------------------------------------
AC = "accreditation"
add(AC, "accreditation", "nabl-accreditation", "NABL", "ISO/IEC 17025 for Testing & Calibration Labs",
    "Accreditation that proves your lab produces technically valid results, required for regulatory and many commercial tests.",
    "Testing labs, calibration labs and in-house quality labs.", timeline="6 – 9 months")
add(AC, "accreditation", "nabh-accreditation", "NABH", "Hospitals & Healthcare Providers",
    "India's benchmark for patient safety and quality of care, increasingly linked to insurance empanelment.",
    "Hospitals, clinics, diagnostic centres and AYUSH hospitals.", timeline="6 – 12 months")
add(AC, "accreditation", "iso-15189", "ISO 15189", "Medical Laboratories",
    "Quality and competence requirements for pathology and diagnostic labs.",
    "Pathology labs, diagnostic chains and hospital labs.", timeline="6 – 9 months")
add(AC, "accreditation", "iso-17020", "ISO/IEC 17020", "Inspection Bodies",
    "Accreditation for organisations that perform inspection — of products, plants, installations or processes.",
    "Third-party inspection agencies.", timeline="6 – 9 months")
add(AC, "accreditation", "iso-17065", "ISO/IEC 17065", "Product Certification Bodies",
    "Requirements for bodies that certify products, processes and services.",
    "Organisations establishing a product certification body.", timeline="9 – 12 months")
add(AC, "accreditation", "iso-17021", "ISO/IEC 17021-1", "Management System Certification Bodies",
    "Requirements for bodies that audit and certify management systems.",
    "Organisations establishing an ISO certification body.", timeline="9 – 15 months")

# ---- Inspection ------------------------------------------------------------------
IN = "inspection-services"
add(IN, "inspection", "pre-shipment-inspection", "Pre-Shipment Inspection", "Final random inspection",
    "A random sample check of finished, packed goods against your order before the balance payment is released.",
    "Importers and buyers sourcing from Indian factories.")
add(IN, "inspection", "during-production-inspection", "During Production Inspection", "In-line inspection",
    "Catch defects early while production is still running, when correction is cheapest.",
    "Buyers placing large or first-time orders.")
add(IN, "inspection", "container-loading", "Container Loading Supervision", "Loading check",
    "We verify quantity, packing and loading conditions, then witness the container being sealed.",
    "Exporters and importers of high-value or fragile goods.")
add(IN, "inspection", "factory-audit", "Factory Audit", "Supplier capability evaluation",
    "An on-site check of a supplier's legal status, capacity, quality systems and working conditions before you sign.",
    "Buyers onboarding new suppliers.")
add(IN, "inspection", "third-party-inspection", "Third-Party Inspection", "Engineering & project inspection",
    "Stage-wise inspection of equipment and materials — welding, NDT witness, dimensional and functional tests.",
    "EPC contractors, project owners and equipment buyers.")
add(IN, "inspection", "pre-export-verification", "Pre-Export Verification", "PVoC / CoC programmes",
    "Conformity verification for shipments to countries that require a certificate before customs clearance.",
    "Exporters to Kenya, Uganda, Tanzania, Iraq, Egypt and other PVoC markets.")

# ---- Compliance & ESG reports ---------------------------------------------------
R = "compliance-reports"
add(R, "report", "brsr-reporting", "BRSR Reporting", "Business Responsibility & Sustainability Report",
    "SEBI-mandated ESG disclosure for listed companies — and increasingly requested from their value chain.",
    "Listed companies and their key suppliers.")
add(R, "report", "carbon-footprint", "Carbon Footprint", "GHG Inventory — Scope 1, 2 & 3",
    "A defensible calculation of your greenhouse gas emissions following the GHG Protocol or ISO 14064.",
    "Exporters, manufacturers and companies with net-zero commitments.")
add(R, "report", "cbam-reporting", "CBAM Reporting", "EU Carbon Border Adjustment Mechanism",
    "Embedded-emissions data that EU importers need from suppliers of steel, aluminium, cement, fertilisers and more.",
    "Indian exporters of CBAM-covered goods to Europe.")
add(R, "report", "ecovadis", "EcoVadis Rating", "Sustainability rating support",
    "We help you prepare evidence and policies to earn a stronger EcoVadis scorecard.",
    "Suppliers asked by multinational customers to be rated.")
add(R, "report", "lca-epd", "LCA & EPD", "Life Cycle Assessment & Environmental Product Declaration",
    "Quantifies a product's environmental impact from raw material to disposal, published as a verified EPD.",
    "Building product, packaging and industrial goods manufacturers.")
add(R, "report", "esg-assessment", "ESG Assessment", "Readiness and materiality assessment",
    "A practical review of your environmental, social and governance position, with a roadmap investors can follow.",
    "Companies preparing for funding, IPO or customer due diligence.")

# ---- Information security -------------------------------------------------------
SEC = "information-security"
add(SEC, "security", "security-certification", "Security Certification", "ISO 27001, ISO 27701 & PCI DSS",
    "End-to-end support to certify your information security and privacy management, from scoping to audit.",
    "SaaS providers, BPOs, payment companies and data processors.")
add(SEC, "security", "soc-2", "SOC 2 Readiness", "AICPA SOC 2 Type I & Type II",
    "Prepare controls and evidence for a SOC 2 attestation — the report US enterprise customers ask for.",
    "SaaS and cloud companies selling to US customers.")
add(SEC, "security", "vapt", "VAPT", "Vulnerability Assessment & Penetration Testing",
    "Ethical hackers test your applications, networks and cloud for exploitable weaknesses before attackers do.",
    "Any business with web apps, mobile apps or internet-facing systems.")
add(SEC, "security", "privacy-assessment", "Privacy Assessment", "DPDP Act, GDPR & risk assessment",
    "Map personal data, assess risk and close the gaps against India's DPDP Act, GDPR and contractual obligations.",
    "Businesses processing customer or employee personal data.")
add(SEC, "security", "compliance-automation", "Compliance Tooling", "GRC platform setup",
    "Set up a governance, risk and compliance platform so evidence collection and monitoring run on autopilot.",
    "Teams managing multiple frameworks or frequent audits.")
add(SEC, "security", "dpo-as-a-service", "DPO as a Service", "Outsourced Data Protection Officer",
    "A qualified, independent data protection officer on retainer — without the cost of a full-time hire.",
    "SMEs and start-ups that need a DPO under GDPR or DPDP.")

SERVICES = S

# --------------------------------------------------------------------------
# Country guides
# --------------------------------------------------------------------------
COUNTRIES = [
    ("europe", "Europe (EU)", "EU", "The single market applies one set of rules across 27 member states plus EEA countries. CE marking, RoHS and REACH form the backbone of product compliance.", ["ce-marking", "rohs", "reach", "ped", "atex", "e-mark", "vde"]),
    ("usa", "United States", "US", "No single national mark — instead, federal agencies (FDA, FCC) and nationally recognised test labs (UL, ETL) govern different product groups.", ["ul-certification", "etl-certification", "fcc-certification", "fda-food-registration", "fda-device-registration", "fda-510k"]),
    ("united-kingdom", "United Kingdom", "UK", "Great Britain uses UKCA marking alongside recognition of CE for many goods, plus respected voluntary marks like Kitemark and WRAS.", ["ukca-marking", "kitemark", "wras", "basec", "bre-global", "cares"]),
    ("canada", "Canada", "CA", "Electrical products need a mark from an accredited body like CSA, and medical devices need a Health Canada licence.", ["csa-certification", "csa-w47-1", "canada-mdl", "ul-certification"]),
    ("china", "China", "CN", "The CCC mark is compulsory for listed product categories, with factory inspections and annual follow-ups.", ["ccc-certification"]),
    ("south-korea", "South Korea", "KR", "The KC mark consolidates safety and EMC requirements for electrical and electronic products.", ["kc-certification"]),
    ("russia", "Russia & EAEU", "RU", "The EAC mark covers the Eurasian Economic Union with certificates or declarations under technical regulations.", ["eac-certification"]),
    ("saudi-arabia", "Saudi Arabia", "SA", "All regulated imports pass through the SABER platform; food, drugs and devices are handled by the SFDA.", ["saso-saber", "sfda", "g-mark"]),
    ("uae", "United Arab Emirates", "AE", "MoIAT runs the ECAS conformity scheme and the Emirates Quality Mark; GCC G-Mark applies to some electrical goods.", ["eqm", "g-mark"]),
    ("kuwait", "Kuwait", "KW", "Imported regulated goods need conformity certificates under the KUCAS programme.", ["kucas", "g-mark"]),
    ("mexico", "Mexico", "MX", "NOM standards are mandatory for electrical, electronic, textile and many consumer products.", ["nom-certification"]),
    ("brazil", "Brazil", "BR", "INMETRO and ANATEL oversee product safety and telecom approvals; certification must be issued by a Brazilian-accredited body.", []),
    ("nigeria", "Nigeria", "NG", "The SONCAP programme requires a product certificate and a per-shipment certificate for regulated goods.", ["soncap"]),
    ("kenya", "Kenya", "KE", "KEBS runs a Pre-Export Verification of Conformity programme; shipments need a Certificate of Conformity.", ["pre-export-verification"]),
    ("uganda", "Uganda", "UG", "UNBS requires a Certificate of Conformity for regulated imports under its PVoC programme.", ["pre-export-verification"]),
    ("tanzania", "Tanzania", "TZ", "TBS operates a pre-shipment verification programme for regulated imports.", ["pre-export-verification"]),
    ("egypt", "Egypt", "EG", "Exporters must register factories with GOEIC for many consumer products before shipping.", ["pre-export-verification"]),
    ("algeria", "Algeria", "DZ", "Imported goods are subject to conformity checks; certificates of conformity are commonly requested at customs.", ["pre-export-verification"]),
    ("morocco", "Morocco", "MA", "A Verification of Conformity programme applies to industrial products listed by the ministry.", ["pre-export-verification"]),
    ("cameroon", "Cameroon", "CM", "ANOR operates a pre-shipment conformity assessment programme for imports.", ["pre-export-verification"]),
    ("india", "India (for importers)", "IN", "Foreign brands selling in India need BIS, WPC, CDSCO or EPR approvals depending on the product — usually through an Indian authorised representative.", ["bis-certification", "bis-crs", "bis-fmcs", "wpc-eta", "cdsco-registration", "epr-registration"]),
]

# --------------------------------------------------------------------------
# Insights (news / blog)
# --------------------------------------------------------------------------
ARTICLES = [
    {
        "slug": "bis-vs-isi-explained",
        "title": "BIS, ISI and CRS: three names, one regulator",
        "tag": "India", "date": "18 Nov 2026", "read": "5 min",
        "excerpt": "Why some products need a factory audit and others only need a lab report — and how to tell which route applies to you.",
        "body": [
            ("p", "If you have ever been told your product 'needs BIS', you probably had follow-up questions. Is that the same as the ISI mark? Does someone have to visit your factory? How long does it take? The confusion is understandable, because the Bureau of Indian Standards runs several different schemes under one name."),
            ("h2", "BIS is the regulator, not the mark"),
            ("p", "The Bureau of Indian Standards is India's national standards body. It writes Indian Standards (IS) and operates the conformity schemes that check products against them. When people say 'BIS certification', they usually mean one of the schemes below."),
            ("h2", "Scheme-I: the ISI mark"),
            ("p", "This is the classic route. BIS officers inspect the factory, draw samples, have them tested and — if everything conforms — grant a licence to apply the ISI mark. Products like cement, steel, helmets, packaged drinking water and many appliances follow this path. It takes longer, but the mark is widely recognised by consumers."),
            ("h2", "CRS: register, don't inspect"),
            ("p", "The Compulsory Registration Scheme covers electronics and IT goods. There is no factory visit. Instead, samples are tested at a BIS-recognised lab and the product is registered online. The 'Standard Mark' with a registration number then goes on the product. It is faster, but every model and every factory location needs its own registration."),
            ("h2", "How to know which applies"),
            ("p", "Start with the product's HS code and description, then check the relevant Quality Control Order. The order names the Indian Standard and the scheme. If you are unsure, send us the product details — we will confirm the route and the realistic timeline before you spend anything on testing."),
        ],
    },
    {
        "slug": "ce-marking-in-six-steps",
        "title": "CE marking in six steps, without the jargon",
        "tag": "Europe", "date": "04 Nov 2026", "read": "6 min",
        "excerpt": "A plain-English walk-through for exporters who need to put a CE mark on a product for the first time.",
        "body": [
            ("p", "CE marking can look intimidating from the outside. In practice, most exporters follow the same six steps. The work is in getting each one right."),
            ("h2", "1. Identify the directives and regulations"),
            ("p", "A single product can fall under several laws at once — a smart kettle may touch the Low Voltage Directive, EMC, Radio Equipment, RoHS and Ecodesign. Missing one is the most common mistake."),
            ("h2", "2. Find the harmonised standards"),
            ("p", "Harmonised standards give a 'presumption of conformity'. Testing to them is the most straightforward way to show compliance."),
            ("h2", "3. Decide if a Notified Body is needed"),
            ("p", "Many products can be self-declared. Higher-risk products — certain machinery, medical devices, pressure equipment, PPE — need an independent Notified Body."),
            ("h2", "4. Test the product"),
            ("p", "Testing should be done by a competent lab. Keep the full reports; you will need them."),
            ("h2", "5. Build the technical file"),
            ("p", "The technical file holds drawings, risk assessment, test reports, user manual and the bill of materials. Authorities can ask for it for ten years after the last unit is placed on the market."),
            ("h2", "6. Sign the Declaration of Conformity and affix the mark"),
            ("p", "The manufacturer signs the EU Declaration of Conformity, then applies the CE mark at the correct size and proportions. If you are outside the EU, you may also need an EU-based responsible person."),
        ],
    },
    {
        "slug": "preparing-for-iso-stage-2",
        "title": "What auditors look for in an ISO stage 2 audit",
        "tag": "ISO", "date": "21 Oct 2026", "read": "4 min",
        "excerpt": "Stage 1 checks your paperwork. Stage 2 checks whether people actually follow it. Here is how to prepare.",
        "body": [
            ("p", "Most organisations pass the stage 1 document review without trouble. Stage 2 is different: the auditor walks the floor, talks to staff and follows records from start to finish."),
            ("h2", "Evidence over intent"),
            ("p", "An auditor is not interested in what you plan to do. They want to see records showing what you have done — at least two to three months of them."),
            ("h2", "People who know the policy"),
            ("p", "Expect operators and clerks to be asked what the quality policy means for their job. They don't need to recite it; they need to explain it in their own words."),
            ("h2", "A completed internal audit and management review"),
            ("p", "These two activities are non-negotiable before certification. Make sure findings from the internal audit have been acted on and the review minutes show real decisions."),
            ("h2", "Corrective actions that reach the root cause"),
            ("p", "When something went wrong, show how you found the underlying reason and changed the system so it won't happen again. That is the heart of every ISO standard."),
        ],
    },
    {
        "slug": "cbam-for-indian-exporters",
        "title": "CBAM: what Indian steel and aluminium exporters need now",
        "tag": "ESG", "date": "09 Oct 2026", "read": "5 min",
        "excerpt": "Your European customers are asking for embedded-emissions data. Here is what to collect and how to calculate it.",
        "body": [
            ("p", "The EU's Carbon Border Adjustment Mechanism asks importers to report — and eventually pay for — the carbon embedded in certain goods. The data has to come from the producer, which means from you."),
            ("h2", "Which goods are covered"),
            ("p", "Iron and steel, aluminium, cement, fertilisers, hydrogen and electricity, along with some downstream products. Check your CN codes against the annex."),
            ("h2", "What data you need"),
            ("p", "Direct emissions from your installation, indirect emissions from electricity, and the emissions embedded in key precursors you buy in. All of it allocated to the specific goods you ship."),
            ("h2", "Why accuracy matters"),
            ("p", "Default values set by the EU are deliberately conservative. Actual, well-documented data almost always works out better for your customer — and makes you the easier supplier to buy from."),
        ],
    },
    {
        "slug": "soc2-vs-iso27001",
        "title": "SOC 2 or ISO 27001? Choosing for your SaaS company",
        "tag": "Security", "date": "26 Sep 2026", "read": "4 min",
        "excerpt": "Both prove security maturity. Which one you need first depends mostly on where your customers are.",
        "body": [
            ("p", "Founders often ask which security certification to pursue first. The honest answer: the one your next big customer asks for."),
            ("h2", "ISO 27001"),
            ("p", "An international certificate with a public register. Preferred in Europe, India, the Middle East and Asia. It certifies a management system — how you identify and treat risk."),
            ("h2", "SOC 2"),
            ("p", "An attestation report issued by a licensed CPA firm. Standard in the US. A Type II report covers how controls operated over a period, usually six to twelve months."),
            ("h2", "Do both, efficiently"),
            ("p", "The control sets overlap heavily. Build once, map to both, and collect evidence in one place. Most of our clients achieve the second framework in a fraction of the time the first one took."),
        ],
    },
    {
        "slug": "epr-plastic-packaging",
        "title": "EPR for plastic packaging: a checklist for brand owners",
        "tag": "India", "date": "12 Sep 2026", "read": "3 min",
        "excerpt": "Registration is only the start. Here is what annual EPR compliance actually involves.",
        "body": [
            ("p", "Any producer, importer or brand owner introducing plastic packaging into India must register on the CPCB portal. But the real work is annual."),
            ("h2", "Your annual checklist"),
            ("p", "Report the quantity and category of plastic packaging you placed on the market. Buy and file EPR certificates from registered recyclers to meet your targets. Meet recycled-content obligations for rigid packaging. File the annual return on time."),
            ("h2", "Common pitfalls"),
            ("p", "Misclassifying packaging categories, underestimating imported packaging, and buying certificates from unverified sources. Each can lead to environmental compensation charges."),
        ],
    },
]

TEAM = [
    ("Founder & Managing Director", "Leads strategy, key accounts and regulator relationships."),
    ("Head of Product Certification", "Oversees BIS, CE, UL and international market access projects."),
    ("Head of Management Systems", "Lead auditor across ISO quality, environment, safety and security standards."),
    ("Head of ESG & Security", "Runs carbon, ESG reporting and information security engagements."),
]

FAQ_HOME = [
    ("How do I know which certification my product needs?",
     "Send us your product description, HS code if you have it, and the markets you want to sell in. Within one business day we'll tell you which approvals apply, which are mandatory, and a realistic timeline and budget."),
    ("Do you issue certificates yourselves?",
     "We are a consulting and facilitation partner. Certificates are issued by the relevant regulator or an accredited certification body. We prepare you, manage the process end to end and coordinate with the issuing body, so you deal with one team."),
    ("How long does certification take?",
     "It depends on the scheme. A US FDA facility registration can be done in days; an ISO 9001 certificate typically takes four to eight weeks; a BIS factory licence or CCC mark can take several months. Each service page shows a typical range."),
    ("Is your pricing fixed?",
     "Yes. After scoping, you receive a written quote that separates our professional fee from government, lab and certification-body fees. No surprises halfway through."),
    ("Do you work with overseas manufacturers?",
     "Yes. We act as the Indian authorised representative for foreign manufacturers seeking BIS, WPC, CDSCO and EPR approvals, and we help Indian exporters reach markets worldwide."),
]
