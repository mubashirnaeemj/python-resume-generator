from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

PAGE_W, PAGE_H = A4
MARGIN = 14 * mm

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
summary_style   = S("summary",   fontSize=8.2, leading=12.5,
                     textColor=MID, alignment=TA_JUSTIFY)
section_style   = S("section",   fontName="Helvetica-Bold", fontSize=8,
                     textColor=ACCENT, leading=10, spaceBefore=5)
job_title_style = S("jobtitle",  fontName="Helvetica-Bold", fontSize=8.8,
                     textColor=DARK, leading=11)
company_style   = S("company",   fontSize=8.2, textColor=LIGHT, leading=10)
bullet_style    = S("bullet",    fontSize=8.1, leading=11.5, leftIndent=9,
                     firstLineIndent=-7, textColor=MID, alignment=TA_JUSTIFY)
proj_name_style = S("projname",  fontName="Helvetica-Bold", fontSize=8.5,
                     textColor=DARK, leading=11)
proj_body_style = S("projbody",  fontSize=8, leading=11.5,
                     textColor=MID, alignment=TA_JUSTIFY)
skill_label     = S("skilllbl",  fontName="Helvetica-Bold", fontSize=8,
                     textColor=DARK, leading=11)
skill_val       = S("skillval",  fontSize=8, textColor=MID, leading=11)
cert_style      = S("cert",      fontSize=8, textColor=MID, leading=11)
date_style      = S("date",      fontSize=7.8, textColor=LIGHT,
                     alignment=TA_RIGHT, leading=11)

def section_header(title):
    return [
        Spacer(1, 4),
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
    t = Table(data, colWidths=["28%", "72%"])
    t.setStyle(TableStyle([
        ("VALIGN",    (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
    ]))
    return t

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
    "AI Automation Engineer with 1+ year of production experience designing and deploying "
    "enterprise-grade AI workflows that eliminate manual processes and drive measurable "
    "business outcomes. Proven ability to architect end-to-end automation systems — from "
    "LLM-powered outreach pipelines to real-time AI voice agents — integrating REST APIs, "
    "CRM platforms (Salesforce), and generative AI at scale. Operates across the full stack: "
    "backend systems (FastAPI, PostgreSQL), workflow automation (n8n, Zapier), and AI APIs "
    "(OpenAI, Anthropic Claude, ElevenLabs, Deepgram). Builds automation that runs in production, not just demos.",
    summary_style))

story += section_header("Professional Experience")

story.append(job_row("AI Automation Developer — Axioware", "Jan 2026 – Present"))
story.append(Spacer(1, 2))
story.append(bullet(
    "Engineered an AI automation workflow using n8n and 10+ REST APIs (Google Places, "
    "OpenAI GPT-4o, Twilio, Salesforce) to autonomously enrich leads and generate "
    "AI-powered cold call scripts — processing 100–200 leads per engagement with zero "
    "manual effort, a task that would have taken days to complete manually."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Architected a production-grade AI calling platform (FastAPI + PostgreSQL + Celery) "
    "with ElevenLabs voice agents, replacing manual outbound calling by autonomously "
    "executing up to 500 calls/day, logging post-call LLM analysis via Deepgram directly "
    "into Salesforce Chatter and Google Sheets, and surfacing real-time KPIs on a live "
    "analytics dashboard."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Built a real-time AI agent (Electron desktop app) that captured live dual audio "
    "streams, transcribed speech via Deepgram, and delivered LLM-generated next-dialogue "
    "suggestions in real-time — enabling sales agents to close leads more effectively "
    "through instant Salesforce CRM context surfaced by phone number lookup."))
story.append(Spacer(1, 1.5))
story.append(bullet(
    "Developed a generative AI video automation pipeline using Zapier, OpusClip, and "
    "ChatGPT that processed raw footage into platform-ready clips in ~5 minutes per video "
    "and auto-distributed content across Instagram, Facebook, and YouTube — validated "
    "across 50+ videos during testing."))

story.append(Spacer(1, 5))

story += section_header("Education")

edu_data = [
    [Paragraph("<b>SMIU, Karachi</b> — BS Artificial Intelligence (CGPA: 3.05)", skill_val),
     Paragraph("Sep 2022 – Jan 2026", date_style)],
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

story.append(proj_row("AI-Powered Calling Platform + Call Rubrix", "Feb 2026 – Jun 2026"))
story.append(Paragraph(
    "Deployed an autonomous outbound calling system that replaced manual sales dialling — "
    "executing up to 500 AI-driven calls/day via ElevenLabs voice agents, with "
    "Celery-scheduled retry logic, post-call LLM analysis, and automatic sync into "
    "Salesforce Chatter and Google Sheets.",
    proj_body_style))
story.append(Paragraph(
    "<font color='#6b7280'><i>FastAPI · PostgreSQL · Celery · Railway · ElevenLabs · "
    "Deepgram · Salesforce API · Google Sheets API · OpenAI · Python</i></font>",
    proj_body_style))
story.append(Spacer(1, 4))

story.append(proj_row("Real-Time AI Calling Assistant (Electron Desktop App)", "Mar 2026"))
story.append(Paragraph(
    "Windows desktop app capturing live dual-channel audio, transcribing via Deepgram "
    "in real-time, and surfacing LLM-generated dialogue suggestions with Salesforce lead "
    "context pulled by phone number lookup — enabling sales agents to close leads more "
    "effectively on live calls.",
    proj_body_style))
story.append(Paragraph(
    "<font color='#6b7280'><i>Electron · Node.js · Deepgram API · Anthropic Claude API · "
    "Salesforce CRM API</i></font>",
    proj_body_style))
story.append(Spacer(1, 4))

story.append(proj_row("AI-Based Ulcer Classification System (Final Year Project)", "2025 – 2026"))
story.append(Paragraph(
    "Built a full-stack diagnostic support system for 8-class GI ulcer classification from "
    "endoscopic images — fine-tuned a DenseNet121 model to 92%+ test accuracy with Grad-CAM "
    "explainability, shipped a Flask + MySQL backend with role-based doctor/admin portals, "
    "and automated patient reporting via n8n (PDF generation, email delivery, Google Sheets "
    "logging). Usability-tested with 14 medical professionals (82.8 SUS score).",
    proj_body_style))
story.append(Paragraph(
    "<font color='#6b7280'><i>TensorFlow/Keras · DenseNet121 · Grad-CAM · Flask · MySQL · "
    "n8n · JavaScript</i></font>",
    proj_body_style))

story += section_header("Skills")

story.append(skill_row("AI & Automation:",
    "n8n · Zapier · Celery · OpenAI GPT-4o · ElevenLabs Voice Agents · Deepgram STT · "
    "Prompt Engineering · Generative AI · LLM Integration · AI Agent Development"))
story.append(skill_row("Backend & Integration:",
    "FastAPI · Python · PostgreSQL · SQLite · REST APIs · Webhooks · "
    "Salesforce API · Google Sheets API · Pandas"))
story.append(skill_row("Frontend & Delivery:",
    "Electron · Next.js · Tailwind CSS · Lovable · Power BI"))
story.append(skill_row("Cloud & Infrastructure:",
    "Railway (production deployment) · AWS (in progress)"))

story += section_header("Certifications & Leadership")

cert_lead_data = [[
    Paragraph(
        "<b>Google Data Analytics Professional Certificate</b> — Coursera, Feb 2025",
        cert_style),
    Paragraph(
        "<b>AI Student Club (AISC)</b> — Lead Member, Nov 2024 – Feb 2025<br/>"
        "Organised technical workshops (Python, SQL, ML) for 20+ students; led "
        "5-person team building the sign language CV system — owned task allocation, "
        "drove model training pipeline, and delivered faculty presentation.",
        cert_style),
]]
cl_t = Table(cert_lead_data, colWidths=["46%", "54%"])
cl_t.setStyle(TableStyle([
    ("VALIGN",    (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING",  (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING",   (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0), (-1,-1), 0),
]))
story.append(cl_t)

output_path = "CV.pdf"
doc = SimpleDocTemplate(
    str(output_path), pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=12 * mm, bottomMargin=10 * mm,
)
doc.build(story)
print(f"✓ PDF written to: {output_path}")