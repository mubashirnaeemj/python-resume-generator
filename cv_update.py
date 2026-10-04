from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

PAGE_W, PAGE_H = A4
MARGIN = 12.5 * mm

DARK      = colors.HexColor("#1a1a2e")
ACCENT    = colors.HexColor("#2563eb")
MID       = colors.HexColor("#374151")
LIGHT     = colors.HexColor("#6b7280")
RULE_CLR  = colors.HexColor("#2563eb")

def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=8.5, leading=12,
                textColor=MID, spaceAfter=0, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

name_style      = S("name",      fontName="Helvetica-Bold", fontSize=20,
                     textColor=DARK, leading=24, alignment=TA_CENTER)
contact_style   = S("contact",   fontSize=7.8, textColor=LIGHT,
                     alignment=TA_CENTER, leading=11)
summary_style   = S("summary",   fontSize=8.2, leading=11.6,
                     textColor=MID, alignment=TA_JUSTIFY)
section_style   = S("section",   fontName="Helvetica-Bold", fontSize=8,
                     textColor=ACCENT, leading=10, spaceBefore=2)
job_title_style = S("jobtitle",  fontName="Helvetica-Bold", fontSize=8.8,
                     textColor=DARK, leading=11)
company_style   = S("company",   fontSize=8.2, textColor=LIGHT, leading=10)
bullet_style    = S("bullet",    fontSize=8.1, leading=10.8, leftIndent=9,
                     firstLineIndent=-7, textColor=MID, alignment=TA_JUSTIFY)
proj_name_style = S("projname",  fontName="Helvetica-Bold", fontSize=8.5,
                     textColor=DARK, leading=11)
proj_body_style = S("projbody",  fontSize=8, leading=10.6,
                     textColor=MID, alignment=TA_JUSTIFY)
skill_label     = S("skilllbl",  fontName="Helvetica-Bold", fontSize=8,
                     textColor=DARK, leading=11)
skill_val       = S("skillval",  fontSize=8, textColor=MID, leading=10.4)
cert_style      = S("cert",      fontSize=8, textColor=MID, leading=10.4)
date_style      = S("date",      fontSize=7.8, textColor=LIGHT,
                     alignment=TA_RIGHT, leading=11)

def section_header(title):
    return [
        Spacer(1, 2),
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=0.6, color=RULE_CLR,
                   spaceAfter=3, spaceBefore=1),
    ]

def job_row(title, company_date):
    data = [[Paragraph(title, job_title_style),
             Paragraph(company_date, date_style)]]
    t = Table(data, colWidths=["68%", "32%"])
    t.setStyle(TableStyle([
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 1),
    ]))
    return t

def proj_row(name, date):
    data = [[Paragraph(name, proj_name_style),
             Paragraph(date, date_style)]]
    t = Table(data, colWidths=["68%", "32%"])
    t.setStyle(TableStyle([
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 1),
    ]))
    return t

def bullet(text):
    return Paragraph(f"• {text}", bullet_style)

def skill_row(label, value):
    data = [[Paragraph(label, skill_label), Paragraph(value, skill_val)]]
    t = Table(data, colWidths=["23%", "77%"])
    t.setStyle(TableStyle([
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
    ]))
    return t

def tools_line(text):
    return Paragraph(
        f"<font color='#6b7280'><i>{text}</i></font>", proj_body_style)

story = []
story.append(Spacer(1, 1))
story.append(Paragraph("MUBASHIR NAEEM JANJUA", name_style))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "mubashirnaeemj@gmail.com  ·  Islamabad, Pakistan  ·  +92 330 381 8395  ·  "
    "<a href='https://www.linkedin.com/in/mubashir-naeem-251595280/'>LinkedIn</a>  ·  "
    "<a href='https://github.com/mubashirnaeemj'>GitHub</a>  ·  "
    "<a href='https://mubashir-naeem-janjua.lovable.app'>Portfolio</a>",
    contact_style))
story.append(Spacer(1, 5))
story.append(HRFlowable(width="100%", thickness=1.2, color=DARK,
                         spaceAfter=4, spaceBefore=0))

story += section_header("Professional Summary")
story.append(Paragraph(
    "AI Automation Developer with 1+ year of production experience building LLM-powered integrations "
    "with Salesforce: a FastAPI, PostgreSQL and Celery platform that has placed 8,000+ "
    "ElevenLabs voice-agent calls, a real-time sales-assist app, and n8n lead-enrichment and "
    "SMS follow-up workflows. Backed by data training (5-month Jawan Pakistan analytics program, Google Data "
    "Analytics and SQL certificates, Power BI, Tableau and pandas projects) and a final-year "
    "medical-imaging web app (DenseNet121, 93% test accuracy, Flask + MySQL).",
    summary_style))

story += section_header("Professional Experience")

story.append(job_row("AI Automation Developer — Axioware", "Jan 2026 – Present"))
story.append(Spacer(1, 2))
story.append(bullet(
    "Built an n8n lead-enrichment pipeline (Jan – Feb 2026): researched each business via Google "
    "and web data, used OpenAI to write pain points, value propositions, objection handlers and "
    "call, email and SMS scripts, scored and tiered each lead, stored it in Airtable and added "
    "notes in Close.com. API calls had retries and central logging, with single-lead and batch modes."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Built the dispatch and data layer of an AI outbound-calling platform (FastAPI, Celery, "
    "PostgreSQL, ElevenLabs): 8,000+ calls placed May – Sep 2026 (peak 1,275 in a day), with "
    "post-call LLM analysis synced to Salesforce, Google Sheets and PostgreSQL."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Built a real-time sales-assist desktop app (Electron): live dual-channel audio transcribed "
    "with Deepgram, LLM-suggested replies, and Salesforce lead context pulled by phone number."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Built a generative-AI video pipeline (Zapier, OpusClip, ChatGPT) that turns raw footage into "
    "platform-ready clips in ~5 minutes and auto-posts to Instagram, Facebook and YouTube "
    "(tested on 50+ videos)."))

story += section_header("Education")

edu_data = [
    [Paragraph("<b>SMIU, Karachi</b> — BS Artificial Intelligence (CGPA: 3.05)", skill_val),
     Paragraph("Feb 2022 – Jan 2026", date_style)],
    [Paragraph("Government Islamia Degree College, Karachi — FSC in Computer Science", skill_val),
     Paragraph("Sep 2019 – Aug 2021", date_style)],
]
edu_t = Table(edu_data, colWidths=["72%", "28%"])
edu_t.setStyle(TableStyle([
    ("VALIGN",    (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING",  (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING",   (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0), (-1,-1), 2),
]))
story.append(edu_t)

story += section_header("Key Projects")

story.append(proj_row("AI-Powered Calling Platform + Call Rubric Scoring", "Mar 2026"))
story.append(Paragraph(
    "Backend for an AI outbound-calling service: Celery-beat dispatch with per-job time windows, "
    "local-presence caller IDs, voicemail redial, and ElevenLabs post-call webhooks storing calls "
    "in a 9-table PostgreSQL schema and syncing to Salesforce and Sheets. Call-scoring pipeline "
    "(smrtPhone, faster-whisper, LLM rubric, Chatter post). React/TypeScript scheduler and "
    "analytics dashboard (Lovable base, 5 s refresh).",
    proj_body_style))
story.append(tools_line(
    "FastAPI · Celery · PostgreSQL · ElevenLabs · Salesforce · Claude · OpenAI · "
    "faster-whisper · React · TypeScript · Lovable"))
story.append(Spacer(1, 2))

story.append(KeepTogether([
    proj_row("AI Lead Follow-up Automation (n8n)", "April 2026"),
    Paragraph(
        "Five connected n8n workflows around an ElevenLabs calling setup: business-hours routing of "
        "inbound calls, Zapier lead intake with local-presence outbound calls, a Twilio SMS agent "
        "(Claude Sonnet 4.6 classifies replies, qualifies sellers, extracts lead data), Calendly "
        "booking links, and post-call Claude scoring logged to Google Sheets and Salesforce Chatter.",
        proj_body_style),
    tools_line("n8n · ElevenLabs · Twilio · Claude · Calendly · Salesforce · Google Sheets · Zapier"),
]))
story.append(Spacer(1, 2))

story.append(proj_row("Real-Time AI Calling Assistant (Electron Desktop App)", "May 2026"))
story.append(Paragraph(
    "Windows desktop app capturing live dual-channel audio, transcribing via Deepgram "
    "in real-time, and surfacing LLM-generated dialogue suggestions with Salesforce lead "
    "context pulled by phone number lookup — enabling sales agents to close leads more "
    "effectively on live calls.",
    proj_body_style))
story.append(tools_line(
    "Electron · Node.js · Deepgram API · Anthropic Claude API · "
    "Salesforce CRM API"))
story.append(Spacer(1, 3))

# ---- Final Year Project (updated) ----
story.append(KeepTogether([
    proj_row("AI-Based Ulcer Classification System (Final Year Project)", "2025 – 2026"),
    Paragraph(
        "Built a web app for 8-class GI endoscopy image classification — fine-tuned "
        "DenseNet121 in two phases to 93% test accuracy (225/242 images, macro F1 0.93), "
        "with Grad-CAM heatmaps and a 65% confidence threshold. Flask + MySQL backend "
        "(4-table SQLAlchemy schema, doctor/admin portals) stores each prediction and "
        "emails a ReportLab PDF report to the patient through an n8n webhook.",
        proj_body_style),
    tools_line(
        "TensorFlow/Keras · DenseNet121 · Grad-CAM · Flask · SQLAlchemy · MySQL · "
        "ReportLab · n8n"),
]))

# ---- Jawan Pakistan data analytics projects (new) ----
jp_head_tbl = Table([[
    Paragraph("DATA ANALYTICS PROJECTS",
              section_style),
    Paragraph("<a href='https://github.com/mubashirnaeemj/Data-Analytics-Projects'>"
              "<font color='#2563eb'>Code on GitHub</font></a>", date_style),
]], colWidths=["80%", "20%"])
jp_head_tbl.setStyle(TableStyle([
    ("VALIGN",       (0,0), (-1,-1), "BOTTOM"),
    ("LEFTPADDING",  (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ("TOPPADDING",   (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0), (-1,-1), 0),
]))
jp_header = [Spacer(1, 2), jp_head_tbl,
             HRFlowable(width="100%", thickness=0.6, color=RULE_CLR,
                        spaceAfter=3, spaceBefore=1)]

story.append(KeepTogether(jp_header + [
    proj_row("Retail Sales Dashboard — Power BI and Tableau", ""),
    Paragraph(
        "Built the same dashboard in both tools on 99,457 retail transactions across 10 "
        "malls: KPI cards, Top-5 mall and category views, payment, gender and monthly "
        "charts, slicers and filters. Clothing drives 45% of revenue, two malls 40%, and "
        "Technology 23% from just 5% of transactions.",
        proj_body_style),
    tools_line("Power BI · DAX · Power Query · Tableau · Excel"),
]))
story.append(Spacer(1, 3))

story.append(KeepTogether([
    proj_row("Python Data Projects — PS4 Games Sales Analysis and Flipkart Scraper", ""),
    Paragraph(
        "Cleaned and explored 1,034 PS4 games in pandas with 8 Matplotlib/Seaborn charts: "
        "Activision led publishers, Action (23.0%) edged Shooter (22.7%), and "
        "North America–Europe sales correlated at 0.82 versus about 0.4 for Japan. Plus "
        "a Selenium scraper for 40 Flipkart listings.",
        proj_body_style),
    tools_line("Python · pandas · Matplotlib · Seaborn · Selenium · Jupyter"),
]))

story += section_header("Skills")

story.append(skill_row("AI & Automation:",
    "n8n · Zapier · Celery · OpenAI · Claude · ElevenLabs Voice Agents · Deepgram STT · LLM Integration"))
story.append(skill_row("Backend & Integration:",
    "FastAPI · Python · PostgreSQL · SQLite · REST APIs · Webhooks · "
    "Salesforce API · Google Sheets API"))
story.append(skill_row("Data & ML:",
    "SQL · MySQL · pandas · Matplotlib · Seaborn · Tableau · DAX · Selenium · "
    "TensorFlow/Keras"))
story.append(skill_row("Frontend & Delivery:",
    "Electron · React · TypeScript · Tailwind CSS · Lovable · Power BI · Railway (production deployment)"))

cert_header = section_header("Certifications & Leadership")

cert_cell = [
    Paragraph(
        "<b>Google Data Analytics Professional Certificate</b> — Coursera, Feb 2025 "
        "(<a href='https://coursera.org/verify/professional-cert/QWMM3GLRPHDE'>"
        "<font color='#2563eb'>verify</font></a>)",
        cert_style),
    Spacer(1, 1),
    Paragraph(
        "<b>Certified Data Analytics Course Using AI</b> — Jawan Pakistan, "
        "Aug – Dec 2024",
        cert_style),
    Spacer(1, 2),
    Paragraph("<b>Intermediate SQL</b> — DataCamp, Oct 2024", cert_style),
]
lead_cell = Paragraph(
    "<b>AI Student Club (AISC)</b> — Lead Member, Nov 2024 – Feb 2025<br/>"
    "Organised technical workshops (Python, SQL, ML) for 20+ students; led "
    "5-person team building the sign language CV system — owned task allocation, "
    "drove model training pipeline, and delivered faculty presentation.",
    cert_style)

cert_lead_data = [[cert_cell, lead_cell]]
cl_t = Table(cert_lead_data, colWidths=["48%", "52%"])
cl_t.setStyle(TableStyle([
    ("VALIGN",    (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING",  (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING",   (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0), (-1,-1), 0),
]))
story.append(KeepTogether(cert_header + [cl_t]))

output_path = "CV.pdf"
doc = SimpleDocTemplate(
    str(output_path), pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=9 * mm, bottomMargin=8 * mm,
)
doc.build(story)
print(f"✓ PDF written to: {output_path}")