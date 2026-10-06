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
    "mubashirnaeemj@gmail.com  ·  Karachi, Pakistan  ·  +92 330 381 8395  ·  "
    "<a href='https://www.linkedin.com/in/mubashir-naeem-251595280/'>LinkedIn</a>  ·  "
    "<a href='https://github.com/mubashirnaeemj'>GitHub</a>  ·  "
    "<a href='https://mubashir-naeem-janjua.lovable.app'>Portfolio</a>",
    contact_style))
story.append(Spacer(1, 5))
story.append(HRFlowable(width="100%", thickness=1.2, color=DARK,
                         spaceAfter=4, spaceBefore=0))

story += section_header("Professional Summary")
story.append(Paragraph(
    "AI Automation Developer and BS Artificial Intelligence graduate (SMIU), building AI-driven "
    "integrations and data systems at Axioware since January 2026. Designed the dispatch and data "
    "layer of a FastAPI, Celery and PostgreSQL calling platform that placed 5,400+ ElevenLabs calls "
    "to 1,577 Salesforce leads, and built n8n workflows for lead enrichment, Claude-based SMS "
    "qualification and call scoring. Final-year project: a medical-imaging web app (DenseNet121, "
    "93% test accuracy, Flask + MySQL).",
    summary_style))

story += section_header("Professional Experience")

story.append(job_row("AI Automation Developer — Axioware", "Jan 2026 – Present"))
story.append(Spacer(1, 2))
story.append(bullet(
    "Automated lead enrichment in n8n (Jan – Feb 2026): researched each business through Google and "
    "web data, generated pain points, value propositions, objection handlers and call, email and SMS "
    "scripts with OpenAI, scored and tiered every lead, and wrote results to Airtable and Close.com, "
    "with retries, central logging and single-lead or batch runs."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Built the dispatch and data layer of an AI outbound-calling platform (FastAPI, Celery, "
    "PostgreSQL, ElevenLabs): 5,400+ calls placed to 1,577 Salesforce leads (peak 1,275 in one day), "
    "with post-call LLM analysis stored for 3,600+ calls and synced to Salesforce and Google Sheets."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Developed a real-time sales-assist desktop app (Electron) that transcribes both sides of a live "
    "call with Deepgram and pulls the caller's Salesforce record by phone number to suggest replies "
    "with an LLM."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Automated video repurposing with Zapier, OpusClip and ChatGPT: raw footage became "
    "platform-ready clips in ~5 minutes each and was auto-posted to Instagram, Facebook and YouTube "
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

story.append(proj_row("AI Calling Platform + Call Rubric Scoring", "Mar 2026"))
story.append(Paragraph(
    "Built the Celery-beat dispatch (per-job time windows, voicemail redial, 85 local-presence caller "
    "IDs) and ElevenLabs post-call webhooks that write each call to a 9-table PostgreSQL schema and "
    "sync to Salesforce and Sheets. Added a rep-call scoring pipeline (smrtPhone, faster-whisper, LLM "
    "rubric, Chatter post) and a React/TypeScript admin dashboard on a Lovable base (9 KPI cards, "
    "2 charts, 5 s refresh).",
    proj_body_style))
story.append(tools_line(
    "FastAPI · Celery · PostgreSQL · ElevenLabs · Salesforce · Claude · OpenAI · "
    "faster-whisper · React · TypeScript · Lovable"))
story.append(Spacer(1, 2))

story.append(KeepTogether([
    proj_row("AI Lead Follow-up Automation (n8n)", "April 2026"),
    Paragraph(
        "Built five n8n workflows (75+ nodes) around an ElevenLabs calling setup: inbound call routing "
        "by business hours, outbound calls from 242 local-presence numbers, a Twilio SMS agent (Claude "
        "Sonnet 4.6 classifies replies, qualifies sellers, extracts lead data), Calendly booking links, "
        "and post-call Claude scoring logged to Google Sheets and Salesforce Chatter.",
        proj_body_style),
    tools_line("n8n · ElevenLabs · Twilio · Claude · Calendly · Salesforce · Google Sheets · Zapier"),
]))
story.append(Spacer(1, 2))

story.append(proj_row("Real-Time AI Calling Assistant (Electron Desktop App)", "May 2026"))
story.append(Paragraph(
    "Developed a Windows desktop app that captures live dual-channel audio, transcribes it with "
    "Deepgram in real time, and shows LLM-generated reply suggestions beside the caller's Salesforce "
    "record, found by phone number.",
    proj_body_style))
story.append(tools_line(
    "Electron · Node.js · Deepgram API · Anthropic Claude API · Salesforce CRM API"))
story.append(Spacer(1, 3))

story.append(KeepTogether([
    proj_row("AI-Based Ulcer Classification System (Final Year Project)", "2025 – 2026"),
    Paragraph(
        "Fine-tuned DenseNet121 in two phases on 8 GI endoscopy classes to 93% test accuracy (225/242 "
        "images, macro F1 0.93) and built a Flask + MySQL web app (4 tables, doctor/admin roles) that "
        "rejects predictions under 65% confidence, shows Grad-CAM heatmaps, and emails a PDF report "
        "to the patient through an n8n webhook.",
        proj_body_style),
    tools_line(
        "TensorFlow/Keras · DenseNet121 · Grad-CAM · Flask · SQLAlchemy · MySQL · "
        "ReportLab · n8n"),
]))

jp_head_tbl = Table([[
    Paragraph("DATA ANALYTICS PROJECTS", section_style),
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
        "Built the same dashboard in Power BI and Tableau on 99,457 retail transactions from 10 malls "
        "(KPI cards, Top-5 views, slicers, filters). Found that Clothing drove 45% of revenue, two "
        "malls 40%, and Technology 23% from only 5% of transactions.",
        proj_body_style),
    tools_line("Power BI · DAX · Power Query · Tableau · Excel"),
]))
story.append(Spacer(1, 3))

story.append(KeepTogether([
    proj_row("Python Data Projects — PS4 Games Sales Analysis and Flipkart Scraper", ""),
    Paragraph(
        "Cleaned and analyzed 1,034 PS4 games in pandas with 8 Matplotlib/Seaborn charts: Action "
        "(23.0%) narrowly led Shooter (22.7%), and North America–Europe sales correlated at 0.82 "
        "versus about 0.4 for Japan. Also scraped 40 Flipkart listings with Selenium.",
        proj_body_style),
    tools_line("Python · pandas · Matplotlib · Seaborn · Selenium · Jupyter"),
]))

story += section_header("Skills")

story.append(skill_row("Backend & Data:",
    "Python · SQL · PostgreSQL · MySQL · FastAPI · Flask · Celery · SQLAlchemy · REST APIs · Webhooks"))
story.append(skill_row("AI & ML:",
    "Claude and OpenAI APIs · LLM prompt design · TensorFlow/Keras · Grad-CAM · faster-whisper"))
story.append(skill_row("Integration & Automation:",
    "n8n · Zapier · Salesforce · ElevenLabs · Twilio · Calendly · Google Sheets API · Selenium"))
story.append(skill_row("Analytics & Frontend:",
    "pandas · Power BI · Tableau · DAX · Matplotlib · Seaborn · React · TypeScript · Tailwind · "
    "Electron · Railway"))

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
    "Led a 5-person team building a sign-language recognition system (task allocation, "
    "model-training pipeline, faculty presentation) and ran Python, SQL and ML workshops "
    "for 20+ students.",
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