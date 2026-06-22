"""
guidelines.py — The 13 Adjudicative Guidelines from SEAD 4 / Adjudicative Desk Reference.

Source: Security Executive Agent Directive 4 (SEAD 4), effective June 8, 2017.
The Adjudicative Desk Reference (ADR) is published by the Defense Counterintelligence
and Security Agency (DCSA) and is available at public.dcsa.mil.

All content describes what the guidelines cover and what adjudicators are trained
to evaluate. Nothing here predicts, scores, or assesses any individual.
"""
from __future__ import annotations


GUIDELINES: list[dict] = [
    {
        "code": "A",
        "name": "Allegiance to the United States",
        "short": "Commitment to the U.S. constitutional system of government.",
        "what_it_covers": (
            "This guideline addresses whether an individual has demonstrated "
            "commitment to the constitutional and democratic principles underlying "
            "the United States government. It considers advocacy or membership in "
            "groups that work against those principles."
        ),
        "concerns": [
            "Advocacy of violent or unlawful overthrow of the U.S. government",
            "Membership in organizations that advocate such overthrow",
            "Participation in activities designed to harm the U.S. government",
            "Involvement with foreign powers or their agents in ways that create "
            "risk of coercion or exploitation",
            "Sabotage, espionage, or terrorism, or the preparation for such acts",
        ],
        "disqualifying": [
            "Involvement in activities seeking to overthrow, destroy, or substantially "
            "alter the form of government",
            "Membership in an organization that advocates overthrow and active "
            "participation in its activities",
            "Intention to deny certain individuals their Constitutional rights",
        ],
        "mitigating": [
            "The involvement was not serious, minimal in nature, or occurred in the past",
            "The individual was young or pressured into the activity and has since "
            "renounced the involvement",
            "The activity or membership was for academic, journalistic, or "
            "investigative purposes",
        ],
        "adr_section": "Guideline A",
        "interview_topics": [
            "Organizations you have belonged to or contributed to",
            "Your views on the U.S. government and democratic institutions",
            "Any involvement in political activism or advocacy groups",
        ],
    },
    {
        "code": "B",
        "name": "Foreign Influence",
        "short": "Foreign contacts or obligations that could create vulnerability to coercion.",
        "what_it_covers": (
            "This guideline addresses whether foreign contacts, interests, or associations "
            "could create a vulnerability to foreign exploitation or influence. Close and "
            "continuing contact with foreign nationals — particularly those in sensitive "
            "positions or countries with adversarial intelligence programs — receives "
            "careful evaluation. The concern is potential coercion or divided loyalties, "
            "not the foreign contact itself."
        ),
        "concerns": [
            "Close and continuing contact with foreign nationals that could make "
            "the individual susceptible to exploitation or coercion",
            "Financial obligations or assets in a foreign country",
            "Associations with foreign intelligence services",
            "Relatives who are agents of a foreign government or who reside in countries "
            "with significant intelligence threats to the U.S.",
            "Sharing financial interests or business activities with foreign nationals "
            "in ways that could compromise judgment",
        ],
        "disqualifying": [
            "Contact with foreign nationals that creates potential for coercion, "
            "exploitation, or undue influence",
            "Connections with foreign nationals known to be or suspected of being "
            "agents of a foreign power",
            "Close association with foreign nationals in a position to be exploited "
            "by a hostile foreign government",
        ],
        "mitigating": [
            "Foreign contacts are established beyond the individual's control and have "
            "been reported, creating no vulnerability to exploitation",
            "The nature of the contact and relationship is such that it cannot be used "
            "as a basis for exploitation",
            "The identified foreign national had no access to information about "
            "U.S. programs or operations",
            "Contact is with a spouse or immediate family member who is not an "
            "intelligence agent and is not affiliated with a foreign government",
        ],
        "adr_section": "Guideline B",
        "interview_topics": [
            "Foreign family members and their employment or government affiliations",
            "Foreign travel history and contacts made during travel",
            "Financial ties to foreign countries (bank accounts, property, investments)",
            "Relationships with foreign nationals in the U.S.",
            "Whether any foreign contacts have sought classified or sensitive information",
        ],
    },
    {
        "code": "C",
        "name": "Foreign Preference",
        "short": "Acts indicating preference for a foreign country over the United States.",
        "what_it_covers": (
            "This guideline addresses acts that suggest an individual may prefer a "
            "foreign country's interests over those of the United States. Dual citizenship, "
            "by itself, is not disqualifying — the concern is active exercise of rights "
            "or obligations to a foreign country in ways that conflict with U.S. interests."
        ),
        "concerns": [
            "Exercise of dual citizenship in a way that indicates preference for "
            "a foreign country",
            "Accepting a foreign passport and using it for travel",
            "Voting in a foreign government's election while able to vote in U.S. elections",
            "Serving in the armed forces of a foreign country",
            "Seeking, accepting, or acquiring citizenship in a foreign country",
            "Taking an oath of allegiance to a foreign country",
        ],
        "disqualifying": [
            "Formally renouncing U.S. citizenship or acquiring citizenship in another "
            "country to avoid U.S. obligations",
            "Serving in the military of a foreign country without U.S. government sanction",
            "Seeking to acquire or renew a foreign passport after being advised not to",
        ],
        "mitigating": [
            "Dual citizenship was not requested but was acquired automatically by "
            "birth or marriage",
            "The individual has expressed a clear intent to renounce the foreign "
            "citizenship and has taken steps to do so",
            "Foreign citizenship was a requirement of employment approved by the "
            "U.S. government",
            "Use of a foreign passport was necessary for work or safety in a country "
            "that does not recognize U.S. passports",
        ],
        "adr_section": "Guideline C",
        "interview_topics": [
            "Citizenship in any country other than the United States",
            "Foreign passports held or used",
            "Participation in foreign elections",
            "Military service in a foreign country",
            "Naturalization status and process for U.S. citizenship",
        ],
    },
    {
        "code": "D",
        "name": "Sexual Behavior",
        "short": "Sexual conduct that is a criminal offense or creates vulnerability to coercion.",
        "what_it_covers": (
            "This guideline addresses sexual behavior that involves a criminal offense, "
            "indicates a disregard for the law, suggests exploitation or lack of judgment, "
            "or creates potential vulnerability to coercion or exploitation. "
            "Sexual orientation is not a security concern and is not a basis for "
            "security clearance decisions. The concern is solely with conduct that "
            "is criminal or creates vulnerability."
        ),
        "concerns": [
            "Sexual behavior that is a criminal offense under applicable law",
            "Conduct that involves the exploitation of minors",
            "Sexual conduct that creates vulnerability to exploitation or coercion",
            "Conduct that is so compulsive, addictive, or out of control that it "
            "jeopardizes the safety of others",
        ],
        "disqualifying": [
            "Sexual conduct that is criminal under applicable law",
            "Sexual behavior that creates a risk of exploitation, coercion, "
            "or undue influence",
            "Exploitation, manipulation, or victimization of a minor",
        ],
        "mitigating": [
            "The behavior occurred in the past and there is no evidence of "
            "subsequent occurrence",
            "The behavior was not criminal and there is no evidence of current "
            "vulnerability to exploitation",
            "The behavior involved a single incident and is unlikely to recur",
        ],
        "adr_section": "Guideline D",
        "interview_topics": [
            "Any criminal charges or investigations related to sexual conduct",
            "Any civil judgments or restraining orders",
            "(Sexual orientation is NOT a topic adjudicators evaluate)",
        ],
    },
    {
        "code": "E",
        "name": "Personal Conduct",
        "short": "Conduct indicating dishonesty, deception, or poor judgment.",
        "what_it_covers": (
            "This is one of the most broadly applied guidelines. It addresses whether "
            "a person's conduct demonstrates the reliability, trustworthiness, and sound "
            "judgment necessary to handle classified information. Deliberate omissions "
            "or misrepresentations on security forms (SF-86) are a major concern under "
            "this guideline. The whole-person concept is central here — one mistake does "
            "not define a person, but patterns of deception or poor judgment do."
        ),
        "concerns": [
            "Deliberate omissions, misrepresentations, or falsifications on the SF-86 "
            "or in security interviews",
            "A pattern of dishonesty or deception that calls into question reliability",
            "Failure to honor obligations and commitments (financial, professional, "
            "personal)",
            "Associating with people known to be involved in criminal activities",
            "Conduct creating vulnerability to coercion, exploitation, or pressure",
            "A history of poor judgment in personal conduct that suggests unreliability",
        ],
        "disqualifying": [
            "Deliberately providing false or misleading information on a security form",
            "Refusing to cooperate with a security investigation",
            "Behavior indicating significant irresponsibility or untrustworthiness",
            "Personal conduct that involved deliberate disregard for the law",
        ],
        "mitigating": [
            "The individual has made a prompt, good-faith effort to correct the "
            "omission or error",
            "The conduct was unintentional or inadvertent, not deliberate deception",
            "The information was not provided because it was not believed to be material",
            "Conditions contributing to the conduct have been corrected and are unlikely "
            "to recur",
        ],
        "adr_section": "Guideline E",
        "interview_topics": [
            "Accuracy and completeness of the SF-86 form",
            "Any information omitted from the form and why",
            "Past employment history, terminations, or performance issues",
            "Civil court judgments, restraining orders, or civil disputes",
            "Pattern of following through on commitments",
        ],
    },
    {
        "code": "F",
        "name": "Financial Considerations",
        "short": "Inability or unwillingness to live within one's means or meet financial obligations.",
        "what_it_covers": (
            "This guideline addresses whether financial difficulties — whether due to "
            "circumstances outside one's control or voluntary irresponsibility — create "
            "a vulnerability to exploitation. The concern is not poverty or hardship; "
            "the concern is whether financial pressure could make someone susceptible "
            "to selling information or otherwise compromising security. Documented "
            "financial hardship that was temporary and is being addressed is viewed "
            "very differently from chronic financial irresponsibility."
        ),
        "concerns": [
            "Inability or unwillingness to live within one's means",
            "Significant debt load relative to income that creates financial pressure",
            "Failure to file taxes, pay taxes owed, or meet court-ordered payments",
            "History of bankruptcies, foreclosures, or repossessions (especially if recent)",
            "Financial crimes (fraud, embezzlement, theft, passing bad checks)",
            "Unexplained affluence or assets inconsistent with known income",
        ],
        "disqualifying": [
            "A history of not meeting financial obligations or multiple instances of "
            "financial irresponsibility",
            "Deceptive or illegal financial practices, including bankruptcy fraud",
            "Consistent failure to meet financial obligations despite having the resources",
        ],
        "mitigating": [
            "The financial problem was the result of circumstances largely outside "
            "the person's control (medical emergency, layoff, divorce)",
            "The person has acted responsibly and is taking steps to resolve the problem",
            "The person has a reasonable and viable plan to pay off debts",
            "The financial problem no longer exists — debts have been resolved",
            "The problem is isolated and has not occurred recently",
        ],
        "adr_section": "Guideline F",
        "interview_topics": [
            "Outstanding debts, collections accounts, or judgments",
            "Bankruptcy filings and the circumstances leading to them",
            "Tax liens or delinquencies and steps taken to resolve them",
            "Any gambling activity and its financial impact",
            "Assets or income sources that may appear inconsistent with your salary",
        ],
    },
    {
        "code": "G",
        "name": "Alcohol Consumption",
        "short": "Excessive alcohol use suggesting lack of self-control, reliability, or judgment.",
        "what_it_covers": (
            "This guideline addresses whether alcohol consumption rises to a level that "
            "suggests problematic lack of self-control, impaired judgment, or unreliability. "
            "Social drinking is not a concern. The focus is on patterns of excessive use, "
            "alcohol-related incidents (DUI, public intoxication), and whether alcohol "
            "dependence affects professional reliability. Seeking treatment is viewed "
            "as a positive indicator, not a negative one."
        ),
        "concerns": [
            "Alcohol-related incidents (DUI, DWI, public intoxication, disorderly conduct)",
            "Diagnosis of alcohol use disorder or alcohol dependence",
            "Evidence that alcohol use is affecting professional performance, "
            "family relations, or personal health",
            "Consumption of alcohol to the point of impaired judgment that could "
            "jeopardize operations",
        ],
        "disqualifying": [
            "Alcohol-related incidents over multiple years suggesting a pattern",
            "Recent serious alcohol-related incident (within the past year)",
            "Consumption to the point of impaired judgment while on duty or "
            "in sensitive areas",
            "Habitual use that affects reliability, judgment, or relationships",
        ],
        "mitigating": [
            "Alcohol problem is in the past and there is no recent abuse",
            "Positive changes in behavior and no alcohol-related incidents in the past two years",
            "Participation in Alcoholics Anonymous or other alcohol abuse treatment",
            "A favorable prognosis by a licensed medical professional",
            "Coworker and supervisor assessment of performance has been satisfactory",
        ],
        "adr_section": "Guideline G",
        "interview_topics": [
            "Alcohol-related arrests, citations, or incidents",
            "Frequency and quantity of alcohol consumption",
            "Any treatment programs attended and current status",
            "Whether alcohol has affected employment or personal relationships",
        ],
    },
    {
        "code": "H",
        "name": "Drug Involvement and Substance Misuse",
        "short": "Use of illegal drugs or misuse of controlled substances.",
        "what_it_covers": (
            "This guideline addresses use of illegal drugs and misuse of legal substances. "
            "The concern is that illegal drug use demonstrates a willingness to disregard "
            "the law, and that substance dependence can create financial pressure, "
            "impair judgment, and create vulnerability. The guidelines distinguish "
            "between past youthful experimentation (lower concern) and current or recent "
            "use (significant concern). Marijuana remains a Schedule I substance "
            "under federal law regardless of state legalization; adjudicators apply "
            "federal law standards."
        ),
        "concerns": [
            "Illegal drug use at any time while possessing or eligible for a clearance",
            "Recent or ongoing illegal drug use",
            "Drug trafficking, distribution, or manufacturing",
            "Misuse of prescription drugs (using drugs prescribed to others, "
            "or taking more than prescribed)",
            "Drug-related criminal history",
            "Failure to disclose prior drug use on the SF-86",
        ],
        "disqualifying": [
            "Drug use while holding a clearance or in a position of trust",
            "Recent drug use (agencies vary: some require 12-month abstinence, "
            "others longer)",
            "Drug trafficking or distribution",
            "Possession of a Schedule I substance (including marijuana under federal law)",
            "Failure to stop using drugs after being advised it is a condition of "
            "a security clearance",
        ],
        "mitigating": [
            "The drug involvement was not recent",
            "Use was experimental in nature and has not recurred",
            "Voluntary treatment was sought and the person no longer uses drugs",
            "A positive prognosis by a credentialed drug treatment professional",
            "The person has had no criminal offense related to drugs",
        ],
        "adr_section": "Guideline H",
        "interview_topics": [
            "Any use of marijuana or other controlled substances, and when it last occurred",
            "Use of prescription drugs not prescribed to you",
            "Drug-related criminal charges, even if expunged",
            "Whether you intend to use marijuana in the future (federal law applies)",
            "Whether you have been drug tested in prior employment and any results",
        ],
    },
    {
        "code": "I",
        "name": "Psychological Conditions",
        "short": "Mental health conditions that could affect reliability or judgment.",
        "what_it_covers": (
            "This guideline addresses whether an emotional, mental, or personality condition "
            "could affect an individual's reliability, stability, or ability to protect "
            "classified information. Having a mental health condition is not automatically "
            "disqualifying — in fact, seeking mental health treatment is explicitly "
            "encouraged and is viewed as a strength, not a weakness. The concern is "
            "conditions that are undiagnosed, untreated, or that significantly impair "
            "judgment and functioning."
        ),
        "concerns": [
            "A diagnosed mental health condition that is not being treated or "
            "managed and could affect reliability or judgment",
            "A history of behaviors indicating instability or poor self-control",
            "Assessment by a qualified mental health professional that the condition "
            "could affect reliability or ability to protect classified information",
            "Refusal to seek treatment for a condition that could affect reliability",
        ],
        "disqualifying": [
            "Behavior that makes the person a security risk in their current state",
            "A mental health condition that, in the opinion of a qualified professional, "
            "could affect the person's reliability, judgment, or ability to protect "
            "classified information",
        ],
        "mitigating": [
            "The condition was successfully treated and no longer affects reliability",
            "The individual is receiving ongoing treatment and the prognosis is favorable",
            "The condition is in full remission and is unlikely to recur",
            "The condition does not prevent the individual from carrying out their duties",
            "The individual has sought treatment voluntarily — this is always a "
            "positive indicator",
        ],
        "adr_section": "Guideline I",
        "interview_topics": [
            "Mental health treatment history (therapists, psychiatrists, hospitalizations)",
            "Whether current treatment is ongoing and how it is managed",
            "Medications prescribed for mental health conditions",
            "Whether any mental health history was disclosed on the SF-86",
            "(Note: the Executive Order on mental health treatment explicitly states "
            "that seeking treatment should not be a barrier to clearance)",
        ],
    },
    {
        "code": "J",
        "name": "Criminal Conduct",
        "short": "Criminal history suggesting poor judgment, untrustworthiness, or disrespect for the law.",
        "what_it_covers": (
            "This guideline addresses whether a criminal history indicates poor judgment, "
            "disregard for the law, or untrustworthiness. A single minor offense from "
            "many years ago is viewed very differently from a pattern of criminal "
            "conduct or recent serious crimes. Expunged records should still be disclosed "
            "on the SF-86 (the form specifically asks about them). Adjudicators consider "
            "the nature of the offense, recency, and demonstrated rehabilitation."
        ),
        "concerns": [
            "A criminal history suggesting poor judgment or disregard for the law",
            "A pattern of criminal conduct across multiple incidents",
            "Crimes involving dishonesty, theft, fraud, or breach of trust",
            "Crimes involving violence",
            "Criminal conduct that was not disclosed on the SF-86",
            "Probation or parole obligations",
        ],
        "disqualifying": [
            "Serious criminal conduct whether or not a conviction resulted",
            "A pattern of criminal behavior suggesting disregard for the law",
            "Criminal conduct while holding a clearance",
            "Crimes involving violence, dishonesty, or exploitation",
        ],
        "mitigating": [
            "The offense was an isolated incident and did not involve a pattern",
            "The offense occurred in the distant past",
            "The offense was minor and the person has demonstrated rehabilitation",
            "Conditions contributing to the behavior have been corrected",
            "The individual has a record of law-abiding behavior following the incident",
        ],
        "adr_section": "Guideline J",
        "interview_topics": [
            "All arrests, charges, or indictments — even without conviction",
            "Expunged or sealed records (the SF-86 asks for these)",
            "Juvenile records if any were charged as adult offenses",
            "Traffic violations involving alcohol or drugs",
            "Civil or domestic disputes that involved law enforcement",
        ],
    },
    {
        "code": "K",
        "name": "Handling Protected Information",
        "short": "Failure to properly protect or handle classified or sensitive information.",
        "what_it_covers": (
            "This guideline applies specifically to individuals who have previously held "
            "a clearance or handled sensitive information. It addresses whether prior "
            "handling of protected information demonstrated the care, judgment, and "
            "adherence to rules expected of cleared personnel. Inadvertent violations "
            "handled promptly are treated very differently from deliberate or repeated "
            "ones."
        ),
        "concerns": [
            "Unauthorized disclosure of classified information",
            "Deliberate or negligent failure to comply with security regulations",
            "Sharing classified information with unauthorized individuals",
            "Failing to properly store or transport classified material",
            "Failure to report security violations",
        ],
        "disqualifying": [
            "Deliberate unauthorized disclosure of classified information",
            "Repeated or recurring security violations",
            "Deliberate misuse of classified information for personal gain",
            "Failure to report contact with foreign nationals as required",
        ],
        "mitigating": [
            "The violation was inadvertent and the person took immediate corrective action",
            "It was an isolated incident with no pattern of negligence",
            "The information disclosed was not highly classified",
            "The violation was promptly reported and investigated",
            "The individual has not had any subsequent violations",
        ],
        "adr_section": "Guideline K",
        "interview_topics": [
            "Prior clearances held and the circumstances under which they ended",
            "Any security violations, whether formal or informal",
            "Any investigations involving classified information",
            "Security training received and whether procedures were followed",
        ],
    },
    {
        "code": "L",
        "name": "Outside Activities",
        "short": "Involvement in activities that create a conflict of interest or exploit the clearance.",
        "what_it_covers": (
            "This guideline addresses outside employment, organizational memberships, "
            "or other activities that could create conflicts of interest, exploit a "
            "security clearance, or indicate misplaced loyalties. Most outside activities "
            "are not concerns — the focus is on activities that involve foreign "
            "governments, extremist organizations, or potential financial exploitation "
            "of the clearance."
        ),
        "concerns": [
            "Employment or service with a foreign government or its representatives",
            "Active membership in organizations dedicated to opposing the U.S. government",
            "Financial arrangements that create a conflict of interest with employment "
            "duties or loyalty",
            "Fundraising for or support of organizations engaged in illegal activities",
            "Business activities that could exploit or compromise a security clearance",
        ],
        "disqualifying": [
            "Service in a position of responsibility for a foreign government or "
            "its representatives",
            "Active participation in organizations the government designates as "
            "criminal or subversive",
        ],
        "mitigating": [
            "Activities were innocuous and are publicly known",
            "The individual did not know of the illegal or subversive aims of "
            "the organization",
            "Involvement was brief and not recent",
            "No conflict of interest with cleared duties exists",
        ],
        "adr_section": "Guideline L",
        "interview_topics": [
            "Outside employment or consulting work",
            "Service on boards of directors, advisory councils, or foundations",
            "Membership in professional, civic, or fraternal organizations",
            "Any financial relationships with foreign entities",
        ],
    },
    {
        "code": "M",
        "name": "Use of Information Technology Systems",
        "short": "Illegal or unauthorized use of government or organizational IT systems.",
        "what_it_covers": (
            "This guideline addresses unauthorized, illegal, or irresponsible use of "
            "information technology systems — particularly government networks. It became "
            "a formal guideline to address the increasing role of IT in security breaches. "
            "Deliberate policy violations (using personal devices for classified work, "
            "downloading unauthorized software, unauthorized access) are primary concerns. "
            "Casual personal use that is against policy is a minor concern; "
            "hacking or deliberate misuse is a major concern."
        ),
        "concerns": [
            "Illegal access to computer systems or networks",
            "Deliberate misuse of government IT systems for personal gain",
            "Downloading, installing, or using unauthorized software on government systems",
            "Sharing system access credentials with unauthorized individuals",
            "Violations of security policies governing IT use",
        ],
        "disqualifying": [
            "Hacking or unauthorized access to computer systems",
            "Illegal downloading or distribution of copyrighted material on "
            "government systems",
            "Deliberate introduction of malware or denial-of-service attacks",
            "Misuse of government IT systems while holding a clearance",
        ],
        "mitigating": [
            "The behavior was not recent and no subsequent violations have occurred",
            "The violation was minor and not deliberate",
            "The individual demonstrated a good-faith effort to comply with policy",
            "No harm or exploitation resulted from the violation",
        ],
        "adr_section": "Guideline M",
        "interview_topics": [
            "Any unauthorized access to computer systems",
            "Violations of workplace IT policies (e.g., unauthorized software, "
            "personal use on government systems)",
            "Any hacking-related incidents or criminal charges",
            "Whether classified work has ever been done on a non-authorized device",
        ],
    },
]

# Build lookup by code for O(1) access
GUIDELINES_BY_CODE: dict[str, dict] = {g["code"]: g for g in GUIDELINES}


def get_guideline(code: str) -> dict | None:
    """Return a single guideline dict by letter code (A–M), or None if not found."""
    return GUIDELINES_BY_CODE.get(code.upper())


def all_codes() -> list[str]:
    return [g["code"] for g in GUIDELINES]
