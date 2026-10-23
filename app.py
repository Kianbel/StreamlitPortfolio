"""
Kirk Ian F. Belciña | Autobiography & Portfolio
CSIT 349 · Section F1 · BSCS-3
Run with:  streamlit run app.py
"""
import base64
import mimetypes
import os
from datetime import date, datetime

import numpy as np
import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Kirk Ian F. Belciña | Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# CONTENT
# ----------------------------------------------------------------------------
NAME = "Kirk Ian F. Belciña"
SECTION = "F1"
PROGRAM = "BSCS-3"
SCHOOL = "Cebu Institute of Technology – University"
BIRTHDAY = date(2006, 10, 20)
PHOTO_PATH = "images/me.png"

SHORT_BIO = (
    "Kirk Ian Belciña, born on October 20, 2006, is a third-year student "
    "of CIT-U studying computer science."
)

AUTOBIOGRAPHY = (
    "Kirk is a 20-year-old computer science student studying at Cebu Institute "
    "of Technology–University. He lives with his parents at Greenbelt Drive, "
    "Quiot, Cebu City. He graduated with honors throughout his elementary, "
    "junior high, and senior high school years at CIT-U.\n\n"
    "Kirk is a man of many hobbies: playing both video games and table-top "
    "games, doing small programming projects like game development, watching "
    "movies, and reading books. He is also an avid science-lover, having "
    "represented CIT-U in CESAFI Science and Physics competitions."
)

SKILLS = pd.DataFrame(
    {
        "Skill": ["Programming fundamentals", "Time management", "Resourcefulness", "Fast learning"],
        "Level": [85, 92, 90, 88],
        "Description": [
            "Solid grasp of core concepts, data structures, and OOP.",
            "Balances academics, competitions, and personal projects.",
            "Finds alternatives and workarounds when plans fall through.",
            "Picks up new tools and frameworks quickly.",
        ],
    }
)

PROJECTS = [
    {
        "title": "Dungeon Scrawl",
        "image": "images/dungeon_scrawl.png",
        "image_pos": "center",  # which part stays visible when cropped: top / center / bottom / "50% 20%"
        "role": "Programmer",
        "tools": ["JavaFX"],
        "type": "Game",
        "link": "https://github.com/Kianbel/DungeonScrawl",
        "link_label": "View on GitHub ↗",
        "summary": "A simple dungeon crawler with GUI made in Java using JavaFX",
        "outcome": "Completed and published as an open repository on GitHub.",
    },
    {
        "title": "Davi Jone's Locker",
        "image": "images/davi_jones_locker.png",
        "image_pos": "center",
        "role": "Programmer",
        "tools": ["Godot"],
        "type": "Game",
        "link": "https://kianbel.itch.io/davi-jones-locker",
        "link_label": "Play on itch.io ↗",
        "summary": "A pirate-themed game developed with the Godot engine.",
        "outcome": "Released and playable on itch.io.",
    },
    {
        "title": "Tn-spector",
        "image": "images/tn_spector.jpg",
        "image_pos": "center",
        "role": "Programmer",
        "tools": ["JavaFX"],
        "type": "Database App",
        "link": "https://github.com/Kianbel/Tn-spector",
        "link_label": "View on GitHub ↗",
        "summary": "An easy-to-use desktop application designed to help users learn and analyze the efficiency of algorithms through visual programming.",
        "outcome": "Completed and published as an open repository on GitHub.",
    },
]

TIMELINE = [
    ("Elementary", "Graduated with honors", "Cebu Institute of Technology – University"),
    ("CESAFI", "Science competitor", "Represented CIT-U in inter-school competitions"),
    ("Junior high", "Graduated with honors", "Cebu Institute of Technology – University"),
    ("Senior high", "Graduated with high honors", "Cebu Institute of Technology – University"),
    ("CESAFI", "Science & Physics competitor", "Represented CIT-U in inter-school competitions"),
    ("Now", "BS Computer Science, 3rd year", "Building games and apps at CIT-U"),
]

HOBBIES: dict[str, str] = {
    "Video games": "Exploring game worlds, mechanics, and design.",
    "Table-top games": "Strategy, stories, and friends around a table.",
    "Game development": "Turning ideas into small playable projects.",
    "Movies": "Always up for a good film.",
    "Books": "Reading for fun and for ideas.",
    "Science": "Competed in CESAFI Science and Physics.",
}

# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
st.session_state.setdefault("dark", False)
st.session_state.setdefault("messages", [])


def toggle_theme():
    st.session_state.dark = not st.session_state.dark


# ----------------------------------------------------------------------------
# THEME  (light by default, switchable)
# ----------------------------------------------------------------------------
THEMES = {
    "light": dict(bg="#FAFAFA", surface="#FFFFFF", fg="#0B0B0F", muted="#6B7280",
                  border="#E5E7EB", accent="#0D791B", soft="#EEF2FF", on_accent="#FFFFFF"),
    "dark": dict(bg="#0B0B0F", surface="#14141B", fg="#F4F4F5", muted="#A1A1AA",
                 border="#26262F", accent="#1AA12C", soft="#1B1B33", on_accent="#0B0B0F"),
}
T = THEMES["dark" if st.session_state.dark else "light"]

variables = ":root{" + "".join(f"--{k.replace('_','-')}:{v};" for k, v in T.items()) + "}"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap');

html, body, .stApp, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: var(--bg); }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"], #MainMenu, footer { visibility: hidden; }
.block-container { max-width: 1080px; padding-top: 1.5rem; padding-bottom: 3rem; }

/* ---------- text ---------- */
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp [data-testid="stMarkdownContainer"] h1,
.stApp [data-testid="stMarkdownContainer"] h2,
.stApp [data-testid="stMarkdownContainer"] h3,
.stApp [data-testid="stMarkdownContainer"] strong,
.stApp [data-testid="stWidgetLabel"] p,
.stApp label, .stApp summary, .stApp summary p { color: var(--fg); }
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] p { color: var(--muted); }
.stApp a { color: var(--accent); }

/* ---------- sidebar ---------- */
[data-testid="stSidebar"] { background: var(--surface); border-right: 1px solid var(--border); }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: var(--fg); }
[data-testid="stSidebarCollapsedControl"] button, [data-testid="stSidebarCollapseButton"] button { color: var(--fg); }

/* ---------- buttons ---------- */
button[data-testid^="stBaseButton-secondary"],
a[data-testid^="stBaseLinkButton-secondary"] {
    background: var(--surface) !important; color: var(--fg) !important;
    border: 1px solid var(--border) !important; border-radius: 999px !important;
    padding: .35rem 1rem; font-weight: 600; white-space: nowrap; transition: all .15s ease;
}
button[data-testid^="stBaseButton-secondary"]:hover,
a[data-testid^="stBaseLinkButton-secondary"]:hover { border-color: var(--accent) !important; color: var(--accent) !important; }
button[data-testid^="stBaseButton-primary"],
a[data-testid^="stBaseLinkButton-primary"] {
    background: var(--accent) !important; color: var(--on-accent) !important;
    border: 1px solid var(--accent) !important; border-radius: 999px !important; font-weight: 600;
}
button[data-testid^="stBaseButton"] p, a[data-testid^="stBaseLinkButton"] p { color: inherit !important; }

/* ---------- text inputs & text areas ---------- */
[data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="textarea"] {
    background-color: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: 12px !important;
}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within { border-color: var(--accent) !important; }
.stApp input, .stApp textarea {
    background-color: transparent !important; color: var(--fg) !important; -webkit-text-fill-color: var(--fg) !important;
    caret-color: var(--accent);
}
.stApp input::placeholder, .stApp textarea::placeholder { color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important; opacity: 1; }

/* ---------- dropdowns (selectbox / multiselect) ---------- */
div[data-baseweb="select"], 
div[data-baseweb="select"] > div,
div[data-baseweb="select"] > div:first-child {
    background-color: var(--surface) !important; 
    border-radius: 12px !important;
}
div[data-baseweb="select"] > div:first-child {
    border: 1px solid var(--border) !important; 
}
div[data-baseweb="select"] > div:hover, 
div[data-baseweb="select"] > div:focus-within { 
    border-color: var(--accent) !important; 
}
[data-baseweb="select"] div, [data-baseweb="select"] span, [data-baseweb="select"] input { 
    color: var(--fg) !important; -webkit-text-fill-color: var(--fg) !important; 
}
[data-baseweb="select"] svg { fill: var(--muted) !important; color: var(--muted) !important; }

[data-baseweb="tag"] { background-color: var(--soft) !important; border-radius: 999px !important; }
[data-baseweb="tag"] span, [data-baseweb="tag"] svg { color: var(--accent) !important; fill: var(--accent) !important; -webkit-text-fill-color: var(--accent) !important; }

/* the open menu (rendered in a popover) */
[data-baseweb="popover"], [data-baseweb="popover"] > div, [data-baseweb="menu"], [data-baseweb="popover"] ul {
    background-color: var(--surface) !important; border-radius: 12px !important;
}
[data-baseweb="popover"] { border: 1px solid var(--border); box-shadow: 0 12px 30px rgba(0,0,0,.12) !important; }
[data-baseweb="popover"] li, [data-baseweb="popover"] li div, [data-baseweb="popover"] li span {
    background-color: transparent !important; color: var(--fg) !important; -webkit-text-fill-color: var(--fg) !important;
}
[data-baseweb="popover"] li:hover, [data-baseweb="popover"] li[aria-selected="true"] { background-color: var(--soft) !important; }

/* ---------- misc widgets ---------- */
[data-testid="stSliderThumbValue"], [data-testid="stSliderTickBarMin"], [data-testid="stSliderTickBarMax"] { color: var(--muted) !important; }
[data-testid="stForm"] { background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 1.4rem; }

/* ---------- accent color for native widgets (replaces Streamlit's default red) ---------- */
[data-testid="stSlider"] div[role="slider"] { background-color: var(--accent) !important; box-shadow: none !important; }
[data-testid="stSlider"] div[role="slider"]:focus-visible { box-shadow: 0 0 0 .2rem var(--soft) !important; }
label[data-baseweb="checkbox"]:has(input:checked) > span:first-child { background-color: var(--accent) !important; border-color: var(--accent) !important; }
label[data-baseweb="radio"]:has(input:checked) > div:first-child { background-color: var(--accent) !important; border-color: var(--accent) !important; }
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within, [data-baseweb="select"] > div:focus-within { box-shadow: 0 0 0 1px var(--accent) !important; }

/* ---------- dark-mode fixes: widgets that stayed white ---------- */
/* checkbox + radio (unchecked state) */
label[data-baseweb="checkbox"] > span:first-child { background-color: var(--surface) !important; border-color: var(--border) !important; }
label[data-baseweb="radio"] > div:first-child { background-color: var(--surface) !important; border-color: var(--border) !important; }

/* expander (header + body) */
[data-testid="stExpander"] details, [data-testid="stExpander"] summary, [data-testid="stExpanderDetails"] {
    background: transparent !important; color: var(--fg) !important;
}
[data-testid="stExpander"] summary:hover { background: var(--soft) !important; }
[data-testid="stExpander"] summary svg { color: var(--muted) !important; fill: var(--muted) !important; }

/* alerts: st.info / st.warning / st.error / st.success */
[data-testid="stAlert"], [data-testid="stNotification"] {
    background: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: 14px !important;
}
[data-testid="stAlert"] *, [data-testid="stNotification"] * { color: var(--fg) !important; }

/* dropdown list (selectbox / multiselect options) */
[data-baseweb="popover"] [role="listbox"], [data-testid="stSelectboxVirtualDropdown"] { background-color: var(--surface) !important; }
[data-baseweb="popover"] [role="option"] { background-color: transparent !important; }
[data-baseweb="popover"] [role="option"] * { color: var(--fg) !important; -webkit-text-fill-color: var(--fg) !important; }
[data-baseweb="popover"] [role="option"]:hover, [data-baseweb="popover"] [role="option"][aria-selected="true"] { background-color: var(--soft) !important; }

/* tables (messages list) */
[data-testid="stTable"], [data-testid="stTable"] table, [data-testid="stTable"] thead,
[data-testid="stTable"] tbody, [data-testid="stTable"] tr { background: transparent !important; }

/* ---------- force dark surface on every input widget (filters + contact form) ---------- */
[data-testid="stTextInput"] div, [data-testid="stTextArea"] div,
[data-testid="stSelectbox"] div, [data-testid="stMultiSelect"] div,
[data-testid="stTextInputRootElement"], [data-testid="stTextAreaRootElement"] {
    background-color: var(--surface) !important;
}
[data-testid="stTextInputRootElement"], [data-testid="stTextAreaRootElement"] { border-color: var(--border) !important; }
[data-testid="stMultiSelect"] [data-baseweb="tag"], [data-testid="stMultiSelect"] [data-baseweb="tag"] span {
    background-color: var(--soft) !important;
}
[data-testid="stRadio"] label, [data-testid="stCheckbox"] label, [data-testid="stSlider"] label { background: transparent !important; }

/* ---------- interest pills ---------- */
[data-testid="stButtonGroup"] button, button[data-testid="stBaseButton-pills"] {
    background: var(--surface) !important; border: 1px solid var(--border) !important;
    color: var(--muted) !important; border-radius: 999px !important; padding: .3rem 1rem; font-weight: 600;
}
[data-testid="stButtonGroup"] button:hover { border-color: var(--accent) !important; color: var(--accent) !important; }
[data-testid="stButtonGroup"] button[data-testid="stBaseButton-pillsActive"],
[data-testid="stButtonGroup"] button[aria-checked="true"], [data-testid="stButtonGroup"] button[aria-pressed="true"] {
    background: var(--accent) !important; border-color: var(--accent) !important; color: var(--on-accent) !important;
}
[data-testid="stButtonGroup"] button p, [data-testid="stButtonGroup"] button span, [data-testid="stButtonGroup"] button div { color: inherit !important; }

/* ---------- main navigation tabs (big segmented bar) ---------- */
[data-baseweb="tab-list"] {
    gap: .4rem; padding: .4rem; background: var(--surface);
    border: 1px solid var(--border); border-radius: 999px; box-shadow: 0 2px 10px rgba(0,0,0,.04);
}
button[data-baseweb="tab"] {
    flex: 1; justify-content: center; height: 3rem; margin: 0 !important; padding: 0 1.2rem !important;
    border-radius: 999px; background: transparent !important; transition: background .15s ease;
}
button[data-baseweb="tab"]:hover { background: var(--soft) !important; }
button[data-baseweb="tab"] p { color: var(--muted) !important; font-weight: 700; font-size: 1.05rem; }
button[data-baseweb="tab"]:hover p { color: var(--fg) !important; }
button[data-baseweb="tab"][aria-selected="true"] { background: var(--accent) !important; }
button[data-baseweb="tab"][aria-selected="true"] p { color: var(--on-accent) !important; }
[data-baseweb="tab-highlight"], [data-baseweb="tab-border"] { display: none !important; }
[data-baseweb="tab-panel"] { padding-top: 1.5rem; }

/* ---------- metrics ---------- */
[data-testid="stMetric"] { border-top: 1px solid var(--border); padding-top: .9rem; }
[data-testid="stMetricLabel"] p { color: var(--muted) !important; font-size: .85rem; }
[data-testid="stMetricValue"] { color: var(--fg); font-weight: 700; letter-spacing: -0.02em; }

/* ---------- tables / expander ---------- */
[data-testid="stTable"] table { border-collapse: collapse; width: 100%; }
[data-testid="stTable"] th { color: var(--muted) !important; background: transparent !important; border-bottom: 1px solid var(--border) !important; font-weight: 600; font-size: .82rem; }
[data-testid="stTable"] td { color: var(--fg) !important; border-bottom: 1px solid var(--border) !important; background: transparent !important; }
[data-testid="stExpander"] { background: var(--surface); border: 1px solid var(--border) !important; border-radius: 14px; }
[data-testid="stImage"] img { border-radius: 50%; aspect-ratio: 1/1; object-fit: cover;}

/* ---------- custom blocks ---------- */
.stApp .brand { font-weight: 800; font-size: 1.15rem; letter-spacing: -0.03em; color: var(--fg); padding-top: .35rem; }
.stApp .brand span { color: var(--accent); }
.stApp .pill {
    display: inline-flex; align-items: center; gap: .5rem; padding: .35rem .85rem;
    background: var(--soft); color: var(--accent); border-radius: 999px;
    font-size: .8rem; font-weight: 600; margin-bottom: 1.2rem;
}
.stApp .pill::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: var(--accent); }
.stApp .hero-title { font-size: clamp(2.3rem, 5vw, 3.9rem); font-weight: 800; letter-spacing: -0.04em; line-height: 1.05; color: var(--fg); margin: 0; }
.stApp .hero-title em { font-family: 'Instrument Serif', serif; font-style: italic; font-weight: 400; color: var(--accent); letter-spacing: -0.01em; }
.stApp .hero-sub { color: var(--muted); font-size: 1.05rem; line-height: 1.6; margin: 1.1rem 0 1.4rem 0; max-width: 520px; }
.stApp .avatar {
    width: 100%; aspect-ratio: 1/1; border-radius: 100%; background: var(--soft);
    border: 1px solid var(--border); display: flex; align-items: center; justify-content: center;
    font-size: 4.5rem; font-weight: 800; color: var(--accent); letter-spacing: -0.04em;
}
.stApp .eyebrow { color: var(--accent); font-weight: 700; font-size: .78rem; letter-spacing: .12em; text-transform: uppercase; margin-top: 1.2rem; }
.stApp .h2 { color: var(--fg); font-size: 1.9rem; font-weight: 800; letter-spacing: -0.03em; margin: .2rem 0 1rem 0; }
.stApp .muted { color: var(--muted); }
.stApp .card {
    background: var(--surface); border: 1px solid var(--border); border-radius: 20px;
    padding: 1.4rem; min-height: 290px; overflow: hidden;
    transition: transform .2s ease, border-color .2s ease;
}
.stApp .card .thumb {
    width: calc(100% + 2.8rem); aspect-ratio: 16 / 9;
    margin: -1.4rem -1.4rem 1rem -1.4rem; border-bottom: 1px solid var(--border);
    background-size: cover; background-repeat: no-repeat; background-position: center;
}
.stApp .card .thumb-ph {
    display: flex; align-items: center; justify-content: center; width: calc(100% + 2.8rem); aspect-ratio: 16 / 9;
    margin: -1.4rem -1.4rem 1rem -1.4rem; background: var(--soft); color: var(--accent);
    font-size: 2.6rem; font-weight: 800; letter-spacing: -0.04em; border-bottom: 1px solid var(--border);
}
.stApp .card:hover { transform: translateY(-3px); border-color: var(--accent); }
.stApp .card .num { color: var(--muted); font-weight: 600; font-size: .8rem; }
.stApp .card h3 { color: var(--fg); font-size: 1.3rem; font-weight: 700; letter-spacing: -0.02em; margin: .5rem 0 .2rem 0; }
.stApp .card p { color: var(--muted); font-size: .93rem; line-height: 1.55; margin: .6rem 0; }
.stApp .tag { display: inline-block; background: var(--soft); color: var(--accent); padding: .15rem .65rem; border-radius: 999px; font-size: .75rem; font-weight: 600; margin: .15rem .25rem .15rem 0; }
.stApp .tl { border-left: 2px solid var(--border); padding: 0 0 1.2rem 1.2rem; margin-left: .3rem; position: relative; }
.stApp .tl::before { content: ""; position: absolute; left: -6px; top: 4px; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }
.stApp .tl small { color: var(--accent); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; font-size: .72rem; }
.stApp .tl b { display: block; color: var(--fg); }
.stApp .tl span { color: var(--muted); font-size: .9rem; }
.stApp .skill { margin-bottom: 1.1rem; }
.stApp .skill .row { display: flex; justify-content: space-between; font-weight: 600; color: var(--fg); font-size: .95rem; }
.stApp .skill .row span { color: var(--muted); font-weight: 500; }
.stApp .skill .track { height: 6px; background: var(--border); border-radius: 999px; margin: .45rem 0 .3rem 0; overflow: hidden; }
.stApp .skill .fill { height: 100%; background: var(--accent); border-radius: 999px; }
.stApp .skill small { color: var(--muted); }
.stApp .fact { background: var(--soft); color: var(--fg); border-radius: 14px; padding: .8rem 1rem; font-size: .92rem; margin-top: .6rem; }
.stApp .footer { text-align: center; color: var(--muted); font-size: .82rem; padding: 3rem 0 0 0; }
"""
scheme = "dark" if st.session_state.dark else "light"
st.markdown(f"<style>{variables}:root{{color-scheme:{scheme};}}{CSS}</style>", unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def heading(eyebrow: str, title: str):
    st.markdown(f'<div class="eyebrow">{eyebrow}</div><div class="h2">{title}</div>', unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def image_data_uri(path: str):
    """Read a local image and return a base64 data URI (needed to embed it inside HTML cards)."""
    if not path or not os.path.exists(path):
        return None
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def project_thumb(p: dict) -> str:
    """Card image that covers its box (like CSS background-size: cover), or a placeholder if the file is missing."""
    uri = image_data_uri(p.get("image", ""))
    if uri:
        pos = p.get("image_pos", "center")  # e.g. "top", "bottom", "left center", "50% 20%"
        return f'<div class="thumb" role="img" aria-label="{p["title"]} screenshot" style="background-image:url({uri});background-position:{pos}"></div>'
    initials = "".join(w[0] for w in p["title"].split()[:2]).upper()
    return f'<div class="thumb-ph">{initials}</div>'


def skills_chart(df: pd.DataFrame, kind: str):
    """Vega-Lite chart that follows the current light/dark theme."""
    axis = dict(labelColor=T["muted"], titleColor=T["muted"], gridColor=T["border"],
                domainColor=T["border"], tickColor=T["border"], labelFont="Inter", titleFont="Inter")
    y_nom = {"field": "Skill", "type": "nominal", "sort": None, "title": None, "axis": {"labelLimit": 220}}
    x_lvl = {"field": "Level", "type": "quantitative", "scale": {"domain": [0, 100]}, "title": "Level (%)"}
    if kind == "Bar":
        layers = [{"mark": {"type": "bar", "cornerRadiusEnd": 6, "color": T["accent"], "height": 18},
                   "encoding": {"y": y_nom, "x": x_lvl}}]
    elif kind == "Lollipop":
        layers = [
            {"mark": {"type": "rule", "color": T["border"], "strokeWidth": 3},
             "encoding": {"y": y_nom, "x": x_lvl, "x2": {"datum": 0}}},
            {"mark": {"type": "point", "filled": True, "size": 220, "color": T["accent"], "opacity": 1},
             "encoding": {"y": y_nom, "x": x_lvl}},
        ]
    else:  # Line
        layers = [{"mark": {"type": "line", "point": {"filled": True, "size": 90}, "color": T["accent"], "strokeWidth": 3},
                   "encoding": {"x": {"field": "Skill", "type": "nominal", "sort": None, "title": None,
                                      "axis": {"labelAngle": -20, "labelLimit": 120}},
                                "y": {"field": "Level", "type": "quantitative", "scale": {"domain": [0, 100]}, "title": "Level (%)"}}}]
    spec = {
        "data": {"values": df[["Skill", "Level"]].to_dict("records")},
        "layer": layers,
        "height": 60 * len(df) if kind != "Line" else 260,
        "background": "transparent",
        "config": {"view": {"stroke": None}, "axis": axis},
    }
    st.vega_lite_chart(spec, use_container_width=True, theme=None)


# ----------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"**{NAME}**")
    st.caption(f"{PROGRAM} · Section {SECTION}")
    st.divider()
    st.markdown("**Customize the skills view**")
    chart_kind = st.radio("Chart style", ["Bar", "Lollipop", "Line"])
    min_skill = st.slider("Minimum skill level", 0, 100, 0, step=5)
    show_desc = st.checkbox("Show descriptions", value=True)

# ----------------------------------------------------------------------------
# TOP BAR
# ----------------------------------------------------------------------------
brand_col, _, theme_col = st.columns([4, 3, 1.3], vertical_alignment="center")
brand_col.markdown('<div class="brand">kirk<span>.</span>belcina</div>', unsafe_allow_html=True)
theme_col.button(
    "☀️ Light" if st.session_state.dark else "🌙 Dark",
    on_click=toggle_theme,
    key="theme_btn",
    help="Switch between light and dark mode",
)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
st.write("")
hero_l, hero_r = st.columns([1.7, 1], gap="large", vertical_alignment="center")

with hero_l:
    st.markdown(
        f"""
<div class="pill">{PROGRAM} · Section {SECTION} · CIT-U</div>
<h1 class="hero-title">Hi, I'm Kirk.</h1>
<p class="hero-sub">{SHORT_BIO}</p>
""",
        unsafe_allow_html=True,
    )
    b1, b2, b3,  = st.columns([0.6, 0.6, 1.5])
    # Use :material/icon_name:
    b1.link_button("GitHub", "https://github.com/Kianbel", icon=":material/code:")
    b2.link_button("Itch.io", "https://kianbel.itch.io/", icon=":material/sports_esports:")
    b3.download_button(
        "Download autobiography",
        data=f"{NAME}\n{PROGRAM} · Section {SECTION}\n\n{SHORT_BIO}\n\n{AUTOBIOGRAPHY}",
        file_name="kirk_belcina_autobiography.txt",
        icon=":material/download:"
    )

with hero_r:
    if os.path.exists(PHOTO_PATH):
        st.image(PHOTO_PATH, caption=NAME)
    else:
        st.markdown('<div class="avatar">KB</div>', unsafe_allow_html=True)

st.write("")
today = date.today()
age = today.year - BIRTHDAY.year - ((today.month, today.day) < (BIRTHDAY.month, BIRTHDAY.day))
m1, m2, m3 = st.columns(3, gap="large")
m1.metric("Age", f"{age}")
m2.metric("Program", "BSCS-3")
m3.metric("Projects", len(PROJECTS))

st.write("")
st.write("")

# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_about, tab_skills, tab_projects, tab_contact = st.tabs(["About", "Skills", "Projects", "Contact"])

# ---------------------------- ABOUT -----------------------------------------
with tab_about:
    left, right = st.columns([1.4, 1], gap="large")

    with left:
        heading("Autobiography", "My story")
        st.write(AUTOBIOGRAPHY)

        heading("Interests", "Things I enjoy")
        picked = st.pills("Tap an interest", list(HOBBIES), selection_mode="multi",
                          default=[k for k in HOBBIES.keys()], label_visibility="collapsed") or []
        for h in picked:
            st.markdown(f'<div class="muted"><b style="color:var(--fg)">{h}</b> · {HOBBIES[h]}</div>',
                        unsafe_allow_html=True)

    with right:
        heading("Education & milestones", "The journey")
        for when, title, desc in TIMELINE:
            st.markdown(f'<div class="tl"><small>{when}</small><b>{title}</b><span>{desc}</span></div>',
                        unsafe_allow_html=True)

# ---------------------------- SKILLS ----------------------------------------
with tab_skills:
    heading("Skills", "What I'm good at")
    filtered = SKILLS[SKILLS["Level"] >= min_skill]

    if filtered.empty:
        st.warning("No skills match the minimum level in the sidebar.")
    else:
        c1, c2 = st.columns([1, 1.2], gap="large")
        with c1:
            for _, r in filtered.iterrows():
                desc = f"<small>{r['Description']}</small>" if show_desc else ""
                st.markdown(
                    f'<div class="skill"><div class="row">{r["Skill"]}<span>{r["Level"]}%</span></div>'
                    f'<div class="track"><div class="fill" style="width:{r["Level"]}%"></div></div>{desc}</div>',
                    unsafe_allow_html=True,
                )
        with c2:
            skills_chart(filtered, chart_kind)

        with st.expander("View as table"):
            st.table(filtered[["Skill", "Level"]].set_index("Skill"))
    st.caption("Ratings are my own self-assessment.")

# ---------------------------- PROJECTS --------------------------------------
with tab_projects:
    heading("Portfolio", "Selected projects")

    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    f1, f2 = st.columns([2, 1])
    tool_filter = f1.multiselect("Filter by tool", all_tools, placeholder="All tools")
    type_filter = f2.selectbox("Type", ["All"] + sorted({p["type"] for p in PROJECTS}))

    shown = [
        (i, p) for i, p in enumerate(PROJECTS, 1)
        if (not tool_filter or any(t in p["tools"] for t in tool_filter))
        and (type_filter == "All" or p["type"] == type_filter)
    ]

    if not shown:
        st.info("No projects match those filters.")
    else:
        cols = st.columns(3, gap="medium")
        for col, (i, p) in zip(cols, shown):
            with col:
                tags = "".join(f'<span class="tag">{t}</span>' for t in p["tools"])
                st.markdown(
                    f"""
<div class="card">
{project_thumb(p)}
<div class="num">0{i} · {p['type']}</div>
<h3>{p['title']}</h3>
<div class="muted">Role · <b>{p['role']}</b></div>
<div style="margin-top:.5rem">{tags}</div>
<p>{p['summary']}</p>
<p><b>Outcome:</b> {p['outcome']}</p>
</div>
""",
                    unsafe_allow_html=True,
                )
                st.link_button(p["link_label"], p["link"])

    st.write("")
    with st.expander("Tools used across projects"):
        counts = pd.Series([t for p in PROJECTS for t in p["tools"]]).value_counts().rename_axis("Tool").reset_index(name="Projects")
        spec = {
            "data": {"values": counts.to_dict("records")},
            "mark": {"type": "bar", "cornerRadiusEnd": 6, "color": T["accent"], "height": 18},
            "encoding": {"y": {"field": "Tool", "type": "nominal", "sort": "-x", "title": None},
                         "x": {"field": "Projects", "type": "quantitative", "axis": {"tickMinStep": 1}}},
            "height": 40 * len(counts), "background": "transparent",
            "config": {"view": {"stroke": None},
                       "axis": dict(labelColor=T["muted"], titleColor=T["muted"], gridColor=T["border"],
                                    domainColor=T["border"], tickColor=T["border"], labelFont="Inter")},
        }
        st.vega_lite_chart(spec, use_container_width=True, theme=None)

# ---------------------------- CONTACT ---------------------------------------
with tab_contact:
    heading("Contact", "Say hello")
    cf, ci = st.columns([1.5, 1], gap="large")

    with cf:
        with st.form("contact_form", clear_on_submit=True):
            n1, n2 = st.columns(2)
            visitor = n1.text_input("Your name *")
            email = n2.text_input("Your email")
            topic = st.selectbox("Topic", ["General feedback", "Project inquiry", "Collaboration", "Just saying hi"])
            rating = st.slider("Rate this portfolio", 1, 5, 5)
            reply = st.radio("Reply preference", ["Email me back", "No reply needed"], horizontal=True)
            message = st.text_area("Message *", height=130, placeholder="Write something…")
            agree = st.checkbox("I agree to have my message stored for this session.")
            submitted = st.form_submit_button("Send message", type="primary")

        if submitted:
            if not visitor.strip() or not message.strip():
                st.error("Please fill in your name and message.")
            elif not agree:
                st.warning("Please tick the checkbox to send your message.")
            else:
                st.session_state.messages.append(
                    {"Time": datetime.now().strftime("%b %d, %H:%M"), "Name": visitor.strip(),
                     "Topic": topic, "Rating": "★" * rating, "Message": message.strip()}
                )
                st.success(f"Thanks, {visitor.strip()}! Your message was sent.")
                st.balloons()

    with ci:
        st.markdown(
            f"""
<div class="card" style="min-height:0">
<div class="num">About this site</div>
<h3>{NAME}</h3>
<p>{PROGRAM} · Section {SECTION}<br>{SCHOOL}</p>
<p><a href="https://github.com/Kianbel" target="_blank">github.com/Kianbel</a><br>
<a href="https://kianbel.itch.io" target="_blank">kianbel.itch.io</a></p>
<p>Built with Streamlit for CSIT 349.</p>
</div>
""",
            unsafe_allow_html=True,
        )

    if st.session_state.messages:
        st.write("")
        st.markdown("**Messages this session**")
        st.table(pd.DataFrame(st.session_state.messages).set_index("Time"))
        avg = np.mean([len(m["Rating"]) for m in st.session_state.messages])
        st.caption(f"Average rating: {avg:.1f} / 5")

# ----------------------------------------------------------------------------
st.markdown(f'<div class="footer">© {today.year} {NAME} · {PROGRAM} · Section {SECTION}</div>',
            unsafe_allow_html=True)