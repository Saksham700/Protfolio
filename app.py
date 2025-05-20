import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64
from streamlit_lottie import st_lottie
import requests
import json
import time
from datetime import datetime
import numpy as np
import altair as alt

st.set_page_config(
    page_title="Saksham Raj | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

def local_css():
    st.markdown("""
    <style>
    /* Base variables */
    :root {
        --primary-color: #0066cc;
        --secondary-color: #4d94ff;
        --accent-color: #00cccc;
        --text-color: #333333;
        --light-bg: #f8f9fa;
        --card-bg: #ffffff;
        --gradient-bg: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        --dark-text: #f1f1f1;
        --orange-highlight: #ff9a3c;
    }
    
    /* Dark mode variables */
    [data-theme="dark"] {
        --primary-color: #4d94ff;
        --secondary-color: #0066cc;
        --accent-color: #00cccc;
        --text-color: #f1f1f1;
        --light-bg: #1e1e1e;
        --card-bg: #2d2d2d;
        --gradient-bg: linear-gradient(135deg, #2d3436 0%, #000428 100%);
    }
    
    /* Force text to be light on dark backgrounds in dark mode */
    [data-theme="dark"] div {
        color: var(--dark-text) !important;
    }
    
    /* Specific selectors for dark text on dark background issue */
    [data-theme="dark"] p,
    [data-theme="dark"] h1,
    [data-theme="dark"] h2, 
    [data-theme="dark"] h3,
    [data-theme="dark"] h4,
    [data-theme="dark"] h5,
    [data-theme="dark"] h6,
    [data-theme="dark"] span,
    [data-theme="dark"] li {
        color: var(--dark-text) !important;
    }
    
    /* Preserve colored highlights for important text */
    [data-theme="dark"] .orange-text, 
    [data-theme="dark"] .highlight-text-orange, 
    [data-theme="dark"] strong.orange-text {
        color: var(--orange-highlight) !important;
        font-weight: 600;
    }
    
    /* Specific fixes for areas in your screenshot */
    [data-theme="dark"] .stText,
    [data-theme="dark"] .stMarkdown {
        color: var(--dark-text) !important;
    }
    
    /* Target the specific "Who I Am" section */
    [data-theme="dark"] div.main div:first-child h1,
    [data-theme="dark"] div.main div:first-child p {
        color: var(--dark-text) !important;
    }
    
    .main {
        background-image: var(--gradient-bg);
        color: var(--text-color);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .content-container {
        background-color: var(--card-bg);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        margin-bottom: 30px;
        backdrop-filter: blur(5px);
        color: var(--text-color);
    }
    
    .header-container {
        padding: 40px;
        border-radius: 15px;
        background: linear-gradient(to right, #000428, #004e92);
        color: white;
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
    }
    
    .header-container:before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><polygon fill="rgba(255,255,255,0.05)" points="0,100 100,0 100,100"/></svg>');
        background-size: cover;
    }
    
    .header-text h1 {
        font-size: 3.5rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        margin-bottom: 10px;
        color: white; /* Always white for better contrast on the dark header */
    }
    
    .header-text h2 {
        font-size: 1.8rem;
        font-weight: 400;
        margin-bottom: 20px;
        color: #b3d9ff;
    }
    
    .project-card {
        background-color: var(--card-bg);
        border-radius: 10px;
        padding: 25px;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border-left: 5px solid var(--primary-color);
        color: var(--text-color);
    }
    
    .project-card:hover {
        transform: translateY(-7px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.15);
    }
    
    .tech-badge {
        background-color: rgba(0, 102, 204, 0.1);
        color: var(--primary-color);
        border-radius: 20px;
        padding: 6px 12px;
        margin-right: 8px;
        font-size: 0.85em;
        font-weight: 500;
        display: inline-block;
        margin-bottom: 8px;
        border: 1px solid rgba(0, 102, 204, 0.3);
        transition: all 0.2s ease;
    }
    
    [data-theme="dark"] .tech-badge {
        background-color: rgba(77, 148, 255, 0.2);
        border: 1px solid rgba(77, 148, 255, 0.4);
        color: var(--primary-color);
    }
    
    .tech-badge:hover {
        background-color: var(--primary-color);
        color: white;
    }
    
    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        position: relative;
        padding-bottom: 0.8rem;
        color: var(--primary-color);
    }
    
    .section-title:after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100px;
        height: 4px;
        background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
        border-radius: 2px;
    }
    
    /* Special classes for highlighted text that should stay visible */
    .highlight-text {
        color: var(--primary-color);
        font-weight: 600;
    }
    
    .orange-text, 
    [data-theme="dark"] .orange-text {
        color: var(--orange-highlight) !important;
        font-weight: 600;
    }
    
    /* Make sure Data Scientist and other orange text stays visible */
    strong, .strong-text {
        color: var(--orange-highlight) !important;
        font-weight: 600;
    }
    
    .css-1d391kg {
        background-color: #1e3a5f;
    }
    
    .sidebar .sidebar-content {
        background-color: #1e3a5f;
        color: white;
        padding-top: 20px;
    }
    
    [data-theme="dark"] .sidebar .sidebar-content {
        background-color: #152238;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
        background-color: var(--light-bg);
        padding: 10px 10px 0 10px;
        border-radius: 10px 10px 0 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 8px 8px 0 0;
        padding: 12px 20px;
        font-weight: 500;
        color: #555;
        border: 1px solid #ddd;
        border-bottom: none;
    }
    
    [data-theme="dark"] .stTabs [data-baseweb="tab"] {
        background-color: rgba(45, 45, 45, 0.8);
        color: #d1d1d1;
        border: 1px solid #444;
        border-bottom: none;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color);
        color: white;
        border: none;
    }
    
    .skill-progress-container {
        margin-bottom: 15px;
    }
    
    .skill-progress-bar {
        height: 10px;
        background-color: #e0e0e0;
        border-radius: 5px;
        overflow: hidden;
    }
    
    [data-theme="dark"] .skill-progress-bar {
        background-color: #444;
    }
    
    .skill-progress-value {
        height: 100%;
        background: linear-gradient(to right, var(--primary-color), var(--accent-color));
        border-radius: 5px;
    }
    
    .skill-text {
        display: flex;
        justify-content: space-between;
        margin-bottom: 5px;
        color: var(--text-color);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animated {
        animation: fadeIn 0.8s ease-out forwards;
    }
    
    .timeline-container {
        position: relative;
        padding-left: 30px;
    }
    
    .timeline-container::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background: var(--primary-color);
        border-radius: 3px;
    }
    
    .timeline-item {
        position: relative;
        padding-bottom: 30px;
        padding-left: 20px;
        color: var(--text-color);
    }
    
    .timeline-item::before {
        content: "";
        position: absolute;
        left: -30px;
        top: 0;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background: var(--card-bg);
        border: 3px solid var(--primary-color);
    }
    
    .contact-form input, .contact-form textarea {
        background-color: var(--light-bg);
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 15px;
        width: 100%;
        font-size: 16px;
        color: var(--text-color);
    }
    
    [data-theme="dark"] .contact-form input, [data-theme="dark"] .contact-form textarea {
        border-color: #444;
    }
    
    .contact-form input:focus, .contact-form textarea:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 2px rgba(0, 102, 204, 0.25);
        outline: none;
    }
    
    .contact-button {
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 25px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    
    .contact-button:hover {
        background-color: var(--secondary-color);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        text-align: center;
        margin: 30px 0;
    }
    
    .stat-item {
        padding: 20px;
        border-radius: 10px;
        background-color: var(--card-bg);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 22%;
        color: var(--text-color);
    }
    
    [data-theme="dark"] .stat-item {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 5px;
    }
    
    .stat-label {
        font-size: 1rem;
        color: var(--text-color);
    }
    
    [data-theme="dark"] .stat-label {
        color: #d1d1d1;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--light-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    
    /* Dark mode detection */
    @media (prefers-color-scheme: dark) {
        :root:not([data-theme]) {
            --primary-color: #4d94ff;
            --secondary-color: #0066cc;
            --accent-color: #00cccc;
            --text-color: #f1f1f1;
            --light-bg: #1e1e1e;
            --card-bg: #2d2d2d;
            --gradient-bg: linear-gradient(135deg, #2d3436 0%, #000428 100%);
        }
        body, p, h1, h2, h3, h4, h5, h6, span, div {
            color: var(--text-color) !important;
        }
    }
    
    /* Streamlit-specific dark mode compatibility */
    .stApp {
        color: var(--text-color);
    }
    
    .stMarkdown {
        color: var(--text-color) !important;
    }
    
    /* Special class for the Who Am I section */
    .dark-bg-text {
        color: var(--dark-text) !important;
    }
    
    [data-theme="dark"] .dark-bg-text {
        color: var(--dark-text) !important;
    }
    
    /* Make sure orange highlighted elements stay orange */
    [data-theme="dark"] strong,
    [data-theme="dark"] .stronger {
        color: var(--orange-highlight) !important;
    }
    
    @media (max-width: 768px) {
        .header-text h1 {
            font-size: 2.5rem;
        }
        .header-text h2 {
            font-size: 1.5rem;
        }
        .stat-item {
            width: 45%;
            margin-bottom: 15px;
        }
        .stats-container {
            flex-wrap: wrap;
        }
    }
    </style>
    """, unsafe_allow_html=True)
local_css()

def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def create_animated_counter(value, duration=1000, prefix="", suffix=""):
    counter_id = f"counter_{int(time.time() * 1000)}"
    html = f"""
    <div id="{counter_id}" class="stat-number">0</div>
    <script>
        const counterElement = document.getElementById('{counter_id}');
        const finalValue = {value};
        const duration = {duration};
        const stepTime = Math.abs(Math.floor(duration / finalValue));
        let currentValue = 0;   
        function updateCounter() {{
            currentValue += 1;
            counterElement.innerHTML = "{prefix}" + currentValue + "{suffix}";
            if (currentValue < finalValue) {{
                setTimeout(updateCounter, stepTime);
            }}
        }}   
        setTimeout(updateCounter, stepTime);
    </script>
    """
    return html

def create_particle_background():
    return """
    <div id="particles-js" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            particlesJS('particles-js', {
                "particles": {
                    "number": {
                        "value": 80,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#ffffff"
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#000000"
                        },
                    },
                    "opacity": {
                        "value": 0.5,
                        "random": false,
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#ffffff",
                        "opacity": 0.4,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 2,
                        "direction": "none",
                        "random": false,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": true,
                            "mode": "grab"
                        },
                        "onclick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 140,
                            "line_linked": {
                                "opacity": 1
                            }
                        },
                        "push": {
                            "particles_nb": 4
                        },
                    }
                },
                "retina_detect": true
            });
        });
    </script>
    """

def create_typing_animation(text, element="h2", speed=100):
    unique_id = f"typing_{int(time.time() * 1000)}"
    html = f"""
    <{element} id="{unique_id}" class="typing-text"></{element}>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const textElement = document.getElementById('{unique_id}');
            const textArray = "{text}".split('');
            let textIndex = 0;          
            function typeText() {{
                if (textIndex < textArray.length) {{
                    textElement.innerHTML += textArray[textIndex];
                    textIndex++;
                    setTimeout(typeText, {speed});
                }}
            }}         
            setTimeout(typeText, 500);
        }});
    </script>
    <style>
        .typing-text::after {{
            content: '|';
            animation: blink 1s infinite;
        }}
        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0; }}
        }}
    </style>
    """
    return html

def header_section():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown(create_particle_background(), unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1]) 
    with col1:
        st.markdown('<div class="header-text">', unsafe_allow_html=True)
        st.markdown('<h1>Saksham Raj</h1>', unsafe_allow_html=True)
        st.markdown(create_typing_animation("Data Scientist | AI Developer | ML Engineer"), unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 1.1rem; line-height: 1.6;">
        I'm a <span class="highlight-text">data scientist</span> specializing in 
        <span class="highlight-text">AI-powered applications</span>, 
        <span class="highlight-text">computer vision solutions</span>, 
        and <span class="highlight-text">machine learning models</span> for real-world problems. 
        Currently at <span class="highlight-text">Arya.ag</span>, I develop 
        <span class="highlight-text">intelligent AI agents</span> and optimize 
        business processes with cutting-edge technology.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; align-items: center; margin-top: 20px;">
            <div style="background-color: rgba(255,255,255,0.2); padding: 8px 15px; border-radius: 50px; margin-right: 15px;">
                <i class="fas fa-envelope" style="margin-right: 8px;"></i> sakshamraj0170@gmail.com
            </div>
            <div style="background-color: rgba(255,255,255,0.2); padding: 8px 15px; border-radius: 50px;">
                <i class="fas fa-phone" style="margin-right: 8px;"></i> +91-7004028809
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="margin-top: 25px;">
            <a href="https://www.linkedin.com/in/saksham-raj" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" 
                     style="margin-right: 10px; transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.1)'" 
                     onmouseout="this.style.transform='scale(1.0)'">
            </a>
            <a href="https://github.com/sakshamraj" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" 
                     style="margin-right: 10px; transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.1)'" 
                     onmouseout="this.style.transform='scale(1.0)'">
            </a>
            <a href="https://leetcode.com/sakshamraj" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" 
                     style="margin-right: 10px; transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.1)'" 
                     onmouseout="this.style.transform='scale(1.0)'">
            </a>
            <a href="#" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/Resume-PDF-red?style=for-the-badge&logo=adobe&logoColor=white" 
                     style="transition: transform 0.3s ease;" 
                     onmouseover="this.style.transform='scale(1.1)'" 
                     onmouseout="this.style.transform='scale(1.0)'">
            </a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iv4dsx3q.json")  # AI/ML focused animation
        if lottie_coding:
            st_lottie(lottie_coding, height=250, key="coding_animation")
        else:
            st.image("https://via.placeholder.com/250x250.png?text=Saksham+Raj", width=250)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">1+</div>
            <div class="stat-label">Years Experience</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">10+</div>
            <div class="stat-label">Projects Completed</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="stat-item">
            <div class="stat-number">4+</div>
            <div class="stat-label">ML Models Deployed</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def about_section():
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
    tabs = st.tabs(["Professional Profile", "Technical Skills", "Technical Expertise"])  
    with tabs[0]:
        col1, col2 = st.columns([3, 2])   
        with col1:
            st.markdown("""
            <h3>Who I Am</h3>
            <p style="font-size: 1.1rem; line-height: 1.8; text-align: justify;">
                I am a dedicated <strong style="color:#f39c12;">Data Scientist</strong> with a passion for developing 
                <strong style="color:#f39c12;">AI-powered solutions</strong> that solve real-world problems. My journey 
                in the field of data science has equipped me with a unique blend of theoretical knowledge and 
                practical implementation skills.
            </p>
            
            <p style="font-size: 1.1rem; line-height: 1.8; text-align: justify; margin-top: 15px;">
                Currently working at <strong style="color:#f39c12;">Arya.ag</strong>, I focus on leveraging 
                <strong style="color:#f39c12;">computer vision</strong>, <strong style="color:#f39c12;">natural language processing</strong>, 
                and <strong style="color:#f39c12;">machine learning</strong> technologies to optimize agricultural processes 
                and enhance decision-making capabilities for stakeholders in the agriculture industry.
            </p>
            
            <p style="font-size: 1.1rem; line-height: 1.8; text-align: justify; margin-top: 15px;">
                With expertise in <strong style="color:#f39c12;">deep learning architectures</strong>, 
                <strong style="color:#f39c12;">large language models</strong>, and 
                <strong style="color:#f39c12;">computer vision algorithms</strong>, I excel at translating complex 
                business requirements into scalable technical solutions that drive efficiency and innovation.
            </p>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div style="margin-top: 30px; animation: fadeIn 1s ease-out forwards;">
                    <h3>Why Work With Me</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 15px;">
                        <div style="flex: 1; min-width: 200px; padding: 15px; border-radius: 10px; border-left: 4px solid #0066cc;">
                            <h4 style="color: #0066cc; margin-bottom: 10px;">Problem Solver</h4>
                            <p>I approach challenges with analytical thinking and creative solutions, always keeping the end goal in mind.</p>
                        </div>
                        <div style="flex: 1; min-width: 200px; padding: 15px; border-radius: 10px; border-left: 4px solid #0066cc;">
                            <h4 style="color: #0066cc; margin-bottom: 10px;">Continuous Learner</h4>
                            <p>I stay updated with the latest advancements in AI and data science to bring cutting-edge solutions.</p>
                        </div>
                        <div style="flex: 1; min-width: 200px; padding: 15px; border-radius: 10px; border-left: 4px solid #0066cc;">
                            <h4 style="color: #0066cc; margin-bottom: 10px;">Team Player</h4>
                            <p>I excel at collaborating with cross-functional teams to deliver integrated solutions that meet business objectives.</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div style="padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #333;">
                    <h3 style="margin-bottom: 15px;">Areas of Expertise</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                        <span class="tech-badge">Computer Vision</span>
                        <span class="tech-badge">Deep Learning</span>
                        <span class="tech-badge">NLP</span>
                        <span class="tech-badge">LLMs</span>
                        <span class="tech-badge">Data Analysis</span>
                        <span class="tech-badge">Machine Learning</span>
                        <span class="tech-badge">Time Series</span>
                        <span class="tech-badge">AI Systems</span>
                        <span class="tech-badge">Data Visualization</span>
                        <span class="tech-badge">API Development</span>
                        <span class="tech-badge">MLOps</span>
                        <span class="tech-badge">Research</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div style="padding: 20px; border-radius: 10px; border: 1px solid #333;">
                    <h3 style="margin-bottom: 15px;">Professional Interests</h3>
                    <ul style="list-style-type: none; padding-left: 0;">
                        <li style="display: flex; align-items: center; margin-bottom: 15px;">
                            <div style="width: 30px; height: 30px; background-color: #0066cc; border-radius: 50%; display: flex; justify-content: center; align-items: center; margin-right: 15px;">
                                <span style="color: white;">🤖</span>
                            </div>
                            <span>Generative AI & LLM Applications</span>
                        </li>
                        <li style="display: flex; align-items: center; margin-bottom: 15px;">
                            <div style="width: 30px; height: 30px; background-color: #0066cc; border-radius: 50%; display: flex; justify-content: center; align-items: center; margin-right: 15px;">
                                <span style="color: white;">👁️</span>
                            </div>
                            <span>Advanced Computer Vision Systems</span>
                        </li>
                        <li style="display: flex; align-items: center; margin-bottom: 15px;">
                            <div style="width: 30px; height: 30px; background-color: #0066cc; border-radius: 50%; display: flex; justify-content: center; align-items: center; margin-right: 15px;">
                                <span style="color: white;">🧠</span>
                            </div>
                            <span>Reinforcement Learning</span>
                        </li>
                        <li style="display: flex; align-items: center;">
                            <div style="width: 30px; height: 30px; background-color: #0066cc; border-radius: 50%; display: flex; justify-content: center; align-items: center; margin-right: 15px;">
                                <span style="color: white;">⚙️</span>
                            </div>
                            <span>AI for Process Automation</span>
                        </li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div style="padding: 20px; border-radius: 10px; margin-top: 20px; border: 1px solid #333;">
                    <h3 style="margin-bottom: 15px;">Current Focus</h3>
                    <p>My current research and development focus is on:</p>
                    <div style="position: relative; height: 10px; background-color: #333; border-radius: 5px; margin: 15px 0; overflow: hidden;">
                        <div style="position: absolute; height: 100%; width: 85%; background: linear-gradient(to right, #0066cc, #00cccc); border-radius: 5px;"></div>
                    </div>
                    <p style="font-weight: 500; color: #0066cc;">Building AI Agents for Agricultural Optimization</p>
                </div>
                """, unsafe_allow_html=True)
    with tabs[1]:
        st.markdown("<h3>Technical Proficiency</h3>", unsafe_allow_html=True)
        skills = {
            'Python': 90,
            'Machine Learning': 85,
            'Deep Learning': 80,
            'Computer Vision': 75,
            'LLM & GenAI': 85,
            'Data Analysis': 85,
            'SQL': 80,
            'FastAPI': 75,
            'Streamlit': 85,
            'TensorFlow/PyTorch': 80,
            'Spark': 70,
            'MLOps': 75
        }
        df_skills = pd.DataFrame({
            'Skill': list(skills.keys()),
            'Proficiency': list(skills.values())
        })
        df_skills = df_skills.sort_values('Proficiency', ascending=False)
        fig = px.bar(
            df_skills, 
            x='Proficiency', 
            y='Skill', 
            orientation='h',
            color='Proficiency',
            color_continuous_scale='Blues',
            height=450,
            labels={'Proficiency': 'Expertise Level (%)', 'Skill': ''},
            range_color=[50, 100]
        )  
        fig.update_layout(
            xaxis_title="Proficiency Level (%)",
            yaxis_title="",
            coloraxis_showscale=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=10, t=10, b=0),
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                range=[0, 100]
            ),
            yaxis=dict(
                showgrid=False
            ),
            hoverlabel=dict(
                bgcolor="white",
                font_size=14,
                font_family="Segoe UI"
            )
        )
        fig.update_traces(
            texttemplate='%{x}%', 
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Proficiency: %{x}%<extra></extra>'
        )       
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<h3>Skills Breakdown</h3>", unsafe_allow_html=True)
        skills_by_category = {
            'Programming & Development': {
                'Python': 90,
                'SQL': 80,
                'FastAPI': 75,
                'Streamlit': 85,
                'Spark': 70
            },
            'Data Science & AI': {
                'Machine Learning': 85,
                'Deep Learning': 80,
                'Data Analysis': 85,
                'LLM & GenAI': 85,
                'Computer Vision': 75,
                'MLOps': 75
            }
        }    
        tab1, tab2 = st.tabs(list(skills_by_category.keys()))   
        with tab1:
            category = 'Programming & Development'
            labels = list(skills_by_category[category].keys())
            values = list(skills_by_category[category].values())
            fig = go.Figure()        
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name=category,
                line_color='#0066cc',
                fillcolor='rgba(0, 102, 204, 0.2)'
            ))     
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )
                ),
                showlegend=False,
                height=450
            )     
            st.plotly_chart(fig, use_container_width=True)          
        with tab2:
            category = 'Data Science & AI'
            labels = list(skills_by_category[category].keys())
            values = list(skills_by_category[category].values())
            fig = go.Figure()     
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name=category,
                line_color='#00cccc',
                fillcolor='rgba(0, 204, 204, 0.2)'
            ))     
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )
                ),
                showlegend=False,
                height=450
            )     
            st.plotly_chart(fig, use_container_width=True)
    with tabs[2]:
        st.markdown("<h3>Technical Expertise</h3>", unsafe_allow_html=True)
        with st.expander("💡 Machine Learning & AI", expanded=True):
            st.markdown("""
            <div style="padding: 10px 0;">
                <p style="font-size: 1.05rem; line-height: 1.6;">
                Expertise in developing and deploying various machine learning models including:
                </p>
                <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
                    <li><span class="highlight-text">Supervised Learning</span>: Regression, Classification, Ensemble methods</li>
                    <li><span class="highlight-text">Unsupervised Learning</span>: Clustering, Dimensionality Reduction, Anomaly Detection</li>
                    <li><span class="highlight-text">Deep Learning</span>: CNNs, RNNs, Transformers, GANs</li>
                    <li><span class="highlight-text">Reinforcement Learning</span>: Q-Learning, Policy Gradient Methods</li>
                </ul>
                <p style="font-size: 1.05rem; margin-top: 10px;">
                Proficient in <span class="highlight-text">hyperparameter tuning</span>, <span class="highlight-text">model validation</span>, and 
                <span class="highlight-text">performance optimization</span> techniques to ensure robust and reliable models.
                </p>
            </div>
            """, unsafe_allow_html=True)   
        with st.expander("👁️ Computer Vision"):
            st.markdown("""
            <div style="padding: 10px 0;">
                <p style="font-size: 1.05rem; line-height: 1.6;">
                Specialized in developing computer vision solutions for various applications:
                </p>
                <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
                    <li><span class="highlight-text">Object Detection & Recognition</span>: YOLO, Faster R-CNN, RetinaNet</li>
                    <li><span class="highlight-text">Image Segmentation</span>: U-Net, Mask R-CNN, DeepLab</li>
                    <li><span class="highlight-text">Feature Extraction</span>: SIFT, SURF, ORB, Deep Features</li>
                    <li><span class="highlight-text">Video Analysis</span>: Action Recognition, Tracking</li>
                </ul>
                <p style="font-size: 1.05rem; margin-top: 10px;">
                Experience with <span class="highlight-text">OpenCV</span>, <span class="highlight-text">PyTorch Vision</span>, and 
                <span class="highlight-text">TensorFlow's object detection API</span> for implementing production-ready solutions.
                </p>
            </div>
            """, unsafe_allow_html=True)   
        with st.expander("🔠 Natural Language Processing & LLMs"):
            st.markdown("""
            <div style="padding: 10px 0;">
                <p style="font-size: 1.05rem; line-height: 1.6;">
                Expertise in NLP techniques and Large Language Models:
                </p>
                <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
                    <li><span class="highlight-text">Text Processing</span>: Tokenization, Lemmatization, Named Entity Recognition</li>
                    <li><span class="highlight-text">Text Classification</span>: Sentiment Analysis, Topic Modeling</li>
                    <li><span class="highlight-text">Language Models</span>: Working with BERT, GPT, T5, and other transformer-based models</li>
                    <li><span class="highlight-text">LLM Integration</span>: Prompt engineering, fine-tuning, and building applications with LLMs</li>
                </ul>
                <p style="font-size: 1.05rem; margin-top: 10px;">
                Experience with <span class="highlight-text">Hugging Face Transformers</span>, <span class="highlight-text">spaCy</span>, and 
                <span class="highlight-text">LangChain</span> for building sophisticated NLP pipelines and applications.
                </p>
            </div>
            """, unsafe_allow_html=True)   
        with st.expander("📊 Data Analysis & Visualization"):
            st.markdown("""
            <div style="padding: 10px 0;">
                <p style="font-size: 1.05rem; line-height: 1.6;">
                Strong data analysis skills and visualization expertise:
                </p>
                <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
                    <li><span class="highlight-text">Exploratory Data Analysis</span>: Statistical analysis, Pattern recognition</li>
                    <li><span class="highlight-text">Data Cleaning & Preprocessing</span>: Handling missing values, Outlier detection, Feature engineering</li>
                    <li><span class="highlight-text">Visualization</span>: Creating interactive dashboards and insightful visualizations</li>
                    <li><span class="highlight-text">Big Data Processing</span>: Working with large datasets efficiently</li>
                </ul>
                <p style="font-size: 1.05rem; margin-top: 10px;">
                Proficient with <span class="highlight-text">Pandas</span>, <span class="highlight-text">NumPy</span>, 
                <span class="highlight-text">Plotly</span>, <span class="highlight-text">Matplotlib</span>, and <span class="highlight-text">Seaborn</span> 
                for comprehensive data analysis and visualization.
                </p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def experience_section():
    st.markdown("<div class='section-title'>Professional Experience</div>", unsafe_allow_html=True)
    with st.expander("**Data Scientist - 1** | Arya.ag | March 2024 - Present", expanded=True):
        st.markdown("""
        <div class="project-card">
        <ul>
            <li>Developing AI agents to optimize task planning and field team visits using OpenAI API, Google AI Studio, DeepSeek API, LangChain, LangGraph, LangServe, and Crew AI.</li>
            <li>Contributed to AryaQ, a CNN-based application for automating grain quality analysis using YOLO, Custom Vision, and DenseNet.</li>
            <li>Developed dashboards to monitor farm activities, crop growth, and environmental conditions.</li>
            <li>Implemented interactive dashboards for clients and business teams to automate tasks.</li>
            <li>Optimized moisture detection process for classifying plots by implementing a batch API, reducing processing time and cost by 45% and increasing accuracy by 40%.</li>
            <li>Identified agriculture-related companies through clustering and segmentation analysis.</li>
        </ul>
        
        <p><strong>Tech Stack:</strong></p>
        <span class="tech-badge">Python</span>
        <span class="tech-badge">ML/DL</span>
        <span class="tech-badge">LangChain</span>
        <span class="tech-badge">Computer Vision</span>
        <span class="tech-badge">GenAI</span>
        <span class="tech-badge">LLMs</span>
        <span class="tech-badge">FastAPI</span>
        </div>
        """, unsafe_allow_html=True)
    with st.expander("**Associate Trainee** | KPIT Technologies | December 2023 - March 2024"):
        st.markdown("""
        <div class="project-card">
        <p>Worked as an Associate Trainee at KPIT Technologies in Bangalore.</p>
        
        <p><strong>Tech Stack:</strong></p>
        <span class="tech-badge">Python</span>
        <span class="tech-badge">Data Analysis</span>
        </div>
        """, unsafe_allow_html=True)
    with st.expander("**Intern** | High Radius Corporation | May 2023 - November 2023"):
        st.markdown("""
        <div class="project-card">
        <ul>
            <li>Built AI Enabled Application to predict order amount that customers might place in upcoming days.</li>
        </ul>      
        <p><strong>Tech Stack:</strong></p>
        <span class="tech-badge">Python</span>
        <span class="tech-badge">Machine Learning</span>
        <span class="tech-badge">Data Analysis</span>
        </div>
        """, unsafe_allow_html=True)

def projects_section():
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
    <h3>🔊 AI-Powered Call Summary Generator</h3>
    
    <p><strong>Overview:</strong></p>
    <p>An AI-driven application that converts audio recordings of meetings or phone calls into clear, structured summaries. 
    Built using FastAPI and integrated with Google AI Studio API, it handles transcription, speaker diarization, 
    summarization, and intelligent title generation.</p>
    
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>🎙 <strong>Transcription with Speaker Diarization:</strong> Accurately identifies and distinguishes speakers in the audio.</li>
        <li>🧠 <strong>Key Point Summarization:</strong> Automatically generates concise summaries from conversations.</li>
        <li>🏷 <strong>Smart Title Suggestions:</strong> Suggests 3 relevant, AI-generated titles for easy labeling or archiving.</li>
        <li>🌐 <strong>Streamlit UI + REST API:</strong> User-friendly web interface and developer-friendly API.</li>
    </ul>
    
    <p><strong>Tech Stack:</strong></p>
    <span class="tech-badge">FastAPI</span>
    <span class="tech-badge">Python</span>
    <span class="tech-badge">Google AI Studio API</span>
    <span class="tech-badge">Streamlit</span>
    <span class="tech-badge">REST APIs</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
    <h3>📚 Book Passage Analyzer</h3>
    
    <p><strong>Overview:</strong></p>
    <p>A FastAPI-based application that analyzes any given text passage to extract key literary information. 
    It uses Google AI Studio API to generate a summary, identify the author, title, and the book from which the passage may have originated.</p>
    
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>✍️ <strong>Passage Summary Generation</strong></li>
        <li>📖 <strong>Author and Book Name Identification</strong></li>
        <li>🏷 <strong>Relevant Title Suggestion</strong></li>
        <li>🌐 <strong>Streamlit UI + API Integration</strong> for easy use and testing</li>
    </ul>
    
    <p><strong>Tech Stack:</strong></p>
    <span class="tech-badge">FastAPI</span>
    <span class="tech-badge">Python</span>
    <span class="tech-badge">Google AI Studio API</span>
    <span class="tech-badge">Streamlit</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
    <h3>🖼️ Ghibli Art Image Converter</h3>
    
    <p><strong>Overview:</strong></p>
    <p>A creative application that transforms any user-provided image into a Studio Ghibli-style artwork 
    using OpenAI's image generation models. Built with a simple and elegant Streamlit UI for interactive use.</p>
    
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>🎨 <strong>Image Upload & Conversion</strong> to Ghibli Style</li>
        <li>🧠 Powered by <strong>OpenAI's Image Model</strong></li>
        <li>🌐 <strong>Streamlit Interface</strong> for real-time user experience</li>
    </ul>
    
    <p><strong>Tech Stack:</strong></p>
    <span class="tech-badge">OpenAI API</span>
    <span class="tech-badge">Python</span>
    <span class="tech-badge">Streamlit</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
    <h3>🌱 Crop and Fertilizer Prediction System</h3>
    
    <p><strong>Overview:</strong></p>
    <p>Utilized statistical models and integrated multiple datasets to predict optimal crops 
    and recommend suitable fertilizers based on soil composition and geographic data.</p>
    
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>🌾 <strong>Crop Recommendation</strong> based on soil composition</li>
        <li>💧 <strong>Fertilizer Suggestions</strong> for optimal growth</li>
        <li>📊 <strong>Data Integration</strong> from multiple sources</li>
    </ul>
    
    <p><strong>Tech Stack:</strong></p>
    <span class="tech-badge">Python</span>
    <span class="tech-badge">Machine Learning</span>
    <span class="tech-badge">Data Analysis</span>
    <span class="tech-badge">Statistical Modeling</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
    <h3>💸 Data Scientist Salary Prediction</h3>
    
    <p><strong>Overview:</strong></p>
    <p>Developed and optimized ML models to predict data scientist salaries using scikit-learn, 
    TensorFlow, Matplotlib, and Seaborn for data analysis and visualization.</p>
    
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>📈 <strong>Salary Trend Analysis</strong> across different regions and experience levels</li>
        <li>🧠 <strong>ML Model Development</strong> for accurate predictions</li>
        <li>📊 <strong>Interactive Visualizations</strong> of salary factors</li>
    </ul>
    
    <p><strong>Tech Stack:</strong></p>
    <span class="tech-badge">Python</span>
    <span class="tech-badge">scikit-learn</span>
    <span class="tech-badge">TensorFlow</span>
    <span class="tech-badge">Matplotlib</span>
    <span class="tech-badge">Seaborn</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
    <h3>🩺 Stone in Kidney Prediction</h3>
    
    <p><strong>Overview:</strong></p>
    <p>Developed classification model based on urea, pH, calcium, osmosis measurements to predict kidney stone formation.</p>
    
    <p><strong>Key Features:</strong></p>
    <ul>
        <li>🔍 <strong>Medical Parameter Analysis</strong> for risk assessment</li>
        <li>📊 <strong>Classification Model</strong> for accurate prediction</li>
        <li>🧪 <strong>Feature Importance Analysis</strong> of medical parameters</li>
    </ul>
    
    <p><strong>Tech Stack:</strong></p>
    <span class="tech-badge">Python</span>
    <span class="tech-badge">Machine Learning</span>
    <span class="tech-badge">Classification Models</span>
    <span class="tech-badge">Healthcare Analytics</span>
    </div>
    """, unsafe_allow_html=True)

def education_section():
    st.markdown("<div class='section-title'>Education & Certifications</div>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        /* Card animations and styling */
        .edu-card, .cert-card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(5px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #2e6cf0;
        }  
        .edu-card:hover, .cert-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        }
        .progress-container {
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 10px;
            margin: 10px 0;
        }       
        .progress-bar {
            height: 10px;
            background: linear-gradient(90deg, #2e6cf0, #7c4dff);
            border-radius: 10px;
            width: 88.5%;
        }
        .cert-icon {
            display: inline-block;
            width: 40px;
            height: 40px;
            line-height: 40px;
            text-align: center;
            border-radius: 50%;
            margin-right: 10px;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 5px 5px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: rgba(255, 255, 255, 0.1);
            border-bottom: 2px solid #2e6cf0;
        }
    </style>
    """, unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🎓 Education", "📜 Certifications"])   
    with tab1:
        col1, col2 = st.columns([2, 1])     
        with col1:
            st.markdown("""
            <div class="edu-card">
                <h3>Bachelor of Technology</h3>
                <h4>Computer Science Engineering</h4>
                <p>KIIT DU, Bhubaneswar</p>
                <div class="progress-container">
                    <div class="progress-bar"></div>
                </div>
                <p><strong>CGPA: 8.85</strong>/10.0</p>
                <p>2020 - 2024</p>
            </div>
            """, unsafe_allow_html=True)       
        with st.expander("🔍 View Key Coursework"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                - Data Structures & Algorithms
                - Database Management Systems
                - Operating Systems
                - Computer Networks
                - Software Engineering
                """)
            with col2:
                st.markdown("""
                - Machine Learning
                - Artificial Intelligence
                - Cloud Computing
                - Web Development
                - Computer Architecture
                """)    
    with tab2:
        cert_filter = st.multiselect(
            "Filter by platform:",
            ["All", "Coursera", "Udemy", "NPTEL"],
            default=["All"]
        )
        certifications = [
            {"platform": "Coursera", "title": "Machine Learning Specialization", "icon": "🤖", "date": "June 2023"},
            {"platform": "Coursera", "title": "Meta Database Engineering", "icon": "💾", "date": "August 2023"},
            {"platform": "Coursera", "title": "Google Data Analytics", "icon": "📊", "date": "In Progress", "progress": 70},
            {"platform": "Udemy", "title": "Mathematics for Data Science and Data Analysis", "icon": "📈", "date": "May 2023"},
            {"platform": "Udemy", "title": "Mastering Data Visualization", "icon": "📉", "date": "July 2023"},
            {"platform": "Udemy", "title": "Learn Python Programming - Beginner to Master", "icon": "🐍", "date": "April 2023"},
            {"platform": "Udemy", "title": "FastAPI", "icon": "⚡", "date": "September 2023"},
            {"platform": "NPTEL", "title": "An Introduction to Artificial Intelligence", "icon": "🧠", "date": "December 2022"}
        ]
        if "All" not in cert_filter:
            filtered_certs = [cert for cert in certifications if cert["platform"] in cert_filter]
        else:
            filtered_certs = certifications
        cols = st.columns(2)
        for i, cert in enumerate(filtered_certs):
            with cols[i % 2]:
                if "progress" in cert:
                    # For in-progress certifications
                    st.markdown(f"""
                    <div class="cert-card">
                        <div style="display: flex; align-items: center;">
                            <div class="cert-icon">{cert["icon"]}</div>
                            <div>
                                <h4>{cert["title"]}</h4>
                                <p><strong>{cert["platform"]}</strong> • {cert["date"]}</p>
                            </div>
                        </div>
                        <div style="margin-top: 10px;">
                            <div style="display: flex; justify-content: space-between;">
                                <span>Progress</span>
                                <span>{cert["progress"]}%</span>
                            </div>
                            <div class="progress-container">
                                <div class="progress-bar" style="width: {cert["progress"]}%;"></div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="cert-card">
                        <div style="display: flex; align-items: center;">
                            <div class="cert-icon">{cert["icon"]}</div>
                            <div>
                                <h4>{cert["title"]}</h4>
                                <p><strong>{cert["platform"]}</strong> • {cert["date"]}</p>
                            </div>
                        </div>
                        <div style="text-align: right; margin-top: 5px;">
                            <a href="#" style="text-decoration: none;">View Certificate 🔗</a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

def skills_visualization():
    st.markdown("<div class='section-title'>Skills Breakdown</div>", unsafe_allow_html=True)
    skill_categories = {
        'Programming & Development': {
            'Python': 90,
            'R': 75,
            'SQL': 80,
            'FastAPI': 75,
            'Data Structures & Algorithms': 85
        },
        'AI & Machine Learning': {
            'Machine Learning': 85,
            'Deep Learning': 80,
            'CNN': 75,
            'GenAI & LLMs': 85,
            'AI Agents': 80
        },
        'Data Technologies': {
            'Data Analysis': 85,
            'Data Visualization': 80,
            'Data Mining': 75,
            'Apache Airflow': 70,
            'Streamlit': 85
        }
    }
    tabs = st.tabs(list(skill_categories.keys()))  
    for i, (category, skills) in enumerate(skill_categories.items()):
        with tabs[i]:
            categories = list(skills.keys())
            values = list(skills.values())
            categories.append(categories[0])
            values.append(values[0])
            fig = go.Figure()          
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name=category,
                line_color='#0066cc',
                fillcolor='rgba(0, 102, 204, 0.3)'
            ))        
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )
                ),
                showlegend=False,
                height=500,
                margin=dict(l=80, r=80, t=20, b=20)
            )        
            st.plotly_chart(fig, use_container_width=True)
            for skill, level in list(skills.items()):
                st.markdown(f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="width: 150px; font-weight: bold;">{skill}</div>
                    <div style="flex-grow: 1; margin: 0 15px;">
                        <div style="height: 10px; background-color: #e0e0e0; border-radius: 5px;">
                            <div style="height: 10px; width: {level}%; background-color: #0066cc; border-radius: 5px;"></div>
                        </div>
                    </div>
                    <div style="width: 50px; text-align: right;">{level}%</div>
                </div>
                """, unsafe_allow_html=True)
def contact_section():
    st.markdown("<div class='section-title'>Get In Touch</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
        <h3>Contact Information</h3>
        <p>📧 <strong>Email:</strong> sakshamraj0170@gmail.com</p>
        <p>📱 <strong>Phone:</strong> +91-7004028809</p>
        <p>🔗 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/saksham-raj">linkedin.com/in/saksham-raj</a></p>
        <p>💻 <strong>GitHub:</strong> <a href="https://github.com/sakshamraj">github.com/sakshamraj</a></p>
        <p>👨‍💻 <strong>LeetCode:</strong> <a href="https://leetcode.com/sakshamraj">leetcode.com/sakshamraj</a></p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="project-card">
        <h3>Send Me a Message</h3>
        </div>
        """, unsafe_allow_html=True)    
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")        
            submit_button = st.form_submit_button("Send Message")        
            if submit_button:
                st.success("Thanks for reaching out! I'll get back to you soon.")
def experience_timeline():
    st.markdown("<div class='section-title'>Professional Journey</div>", unsafe_allow_html=True)
    
    # CSS for animations and styling
    st.markdown("""
    <style>
        .timeline-container {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .timeline-item {
            padding: 20px 30px;
            border-radius: 10px;
            margin-bottom: 25px;
            position: relative;
            transition: all 0.3s ease;
            border-left: 5px solid #0066cc;
            background: linear-gradient(145deg, #ffffff, #f0f7ff);
            box-shadow: 0 4px 15px rgba(0, 102, 204, 0.1);
        }
        
        .timeline-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 102, 204, 0.2);
            border-left: 5px solid #00aaff;
        }
        
        .timeline-date {
            color: #0066cc;
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 5px;
            letter-spacing: 1px;
        }
        
        .timeline-title {
            font-size: 20px;
            font-weight: bold;
            margin: 0;
            color: #333;
        }
        
        .timeline-company {
            font-size: 16px;
            color: #555;
            margin-bottom: 10px;
            font-weight: 500;
        }
        
        .timeline-marker {
            position: absolute;
            left: -18px;
            top: 20px;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background-color: #0066cc;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-weight: bold;
            box-shadow: 0 0 0 5px rgba(0, 102, 204, 0.2);
            z-index: 1;
            transition: all 0.3s ease;
        }
        
        .timeline-line {
            position: absolute;
            left: -3px;
            top: 0;
            height: 100%;
            width: 3px;
            background-color: #ddd;
            z-index: 0;
        }
        
        .timeline-description {
            color: #666;
            line-height: 1.6;
        }
        
        .badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin-right: 5px;
            margin-top: 10px;
            background-color: rgba(0, 102, 204, 0.1);
            color: #0066cc;
        }
        
        .details-btn {
            background-color: #0066cc;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.3s ease;
            font-size: 14px;
        }
        
        .details-btn:hover {
            background-color: #0055aa;
        }
        
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }
        
        .animate-in {
            animation: fadeIn 0.5s ease forwards;
        }
    </style>
    """, unsafe_allow_html=True)
    
    timeline_data = [
        {
            'date': 'March 2024 - Present',
            'title': 'Data Scientist - 1',
            'company': 'Arya.ag',
            'description': 'Developing AI solutions for agricultural technology.',
            'skills': ['AI', 'Machine Learning', 'Python', 'Agricultural Tech'],
            'details': 'Working on ML models to predict crop yields and optimize supply chain logistics for farmers. Implementing computer vision solutions for crop disease detection.'
        },
        {
            'date': 'December 2023 - March 2024',
            'title': 'Associate Trainee',
            'company': 'KPIT Technologies',
            'description': 'Training in data science and analysis.',
            'skills': ['Data Analysis', 'Statistical Modeling', 'Python'],
            'details': 'Underwent intensive training in data science fundamentals, statistical analysis, and predictive modeling. Participated in real-world projects applying ML concepts.'
        },
        {
            'date': 'May 2023 - November 2023',
            'title': 'Intern',
            'company': 'High Radius Corporation',
            'description': 'Building AI-enabled applications for order prediction.',
            'skills': ['AI', 'Order Prediction', 'Data Mining'],
            'details': 'Developed and deployed machine learning models for predicting order patterns and optimizing inventory management. Achieved 87% prediction accuracy on test data.'
        },
        {
            'date': '2020 - 2024',
            'title': 'B.Tech Student',
            'company': 'KIIT DU, Bhubaneswar',
            'description': 'Computer Science Engineering with 8.85 CGPA.',
            'skills': ['Computer Science', 'Data Structures', 'Algorithms', 'System Design'],
            'details': 'Specialized in AI and Data Science courses. Completed projects in natural language processing and computer vision. Participated in coding competitions and hackathons.'
        }
    ]
    
    # Create container with timeline line
    st.markdown('<div class="timeline-container"><div class="timeline-line"></div>', unsafe_allow_html=True)
    
    # Display each timeline item with animation delay
    for i, item in enumerate(timeline_data):
        # Create unique keys for each item and its expandable section
        details_key = f"details_{i}"
        expand_key = f"expand_{i}"
        
        # Store expansion state in session state if not already there
        if expand_key not in st.session_state:
            st.session_state[expand_key] = False
        
        # Calculate animation delay
        delay = i * 0.2
        
        # Create the timeline item with animation
        st.markdown(f"""
        <div class="timeline-item animate-in" style="animation-delay: {delay}s">
            <div class="timeline-marker">{i+1}</div>
            <div class="timeline-date">{item['date']}</div>
            <h3 class="timeline-title">{item['title']}</h3>
            <div class="timeline-company">{item['company']}</div>
            <p class="timeline-description">{item['description']}</p>
            <div>
                {"".join([f'<span class="badge">{skill}</span>' for skill in item['skills']])}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add interactive details button and collapsible content
        if st.button(f"Show Details", key=details_key):
            st.session_state[expand_key] = not st.session_state[expand_key]
        
        if st.session_state[expand_key]:
            st.markdown(f"""
            <div style="margin-left: 30px; padding: 15px; background-color: #f9f9f9; 
                        border-radius: 8px; border-left: 3px solid #0066cc; margin-bottom: 20px;">
                <p>{item['details']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Close container
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add interactive chart showing time spent at each position
    st.markdown("<h3 style='margin-top: 40px;'>Time Distribution</h3>", unsafe_allow_html=True)
    
    # Calculate months for each position (approximate)
    def calculate_months(date_range):
        if "Present" in date_range:
            end_date = datetime.now()
            start_date = datetime.strptime(date_range.split(" - ")[0], "%B %Y")
            return (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
        elif " - " in date_range:
            dates = date_range.split(" - ")
            if len(dates[0].split()) == 1:  # Just a year
                start = datetime.strptime(dates[0], "%Y")
                end = datetime.strptime(dates[1], "%Y")
                return (end.year - start.year) * 12
            else:
                start = datetime.strptime(dates[0], "%B %Y")
                end = datetime.strptime(dates[1], "%B %Y")
                return (end.year - start.year) * 12 + end.month - start.month
        return 0
    
    time_data = []
    for item in timeline_data:
        months = calculate_months(item['date'])
        time_data.append({
            "role": f"{item['title']} at {item['company']}",
            "months": months
        })
    df = pd.DataFrame(time_data)
    
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('months:Q', title='Months'),
        y=alt.Y('role:N', title='Position', sort='-x'),
        color=alt.Color('role:N', legend=None, scale=alt.Scale(scheme='blues')),
        tooltip=['role', 'months']
    ).properties(
        width=600,
        height=300,
        title='Experience Duration'
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)

def main():
    header_section()
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        [
            "About Me",
            "Experience",
            "Projects",
            "Skills Breakdown",
            "Education & Certifications",
            "Professional Journey",
            "Contact"
        ]
    )
    if page == "About Me":
        about_section()
    elif page == "Experience":
        experience_section()
    elif page == "Projects":
        projects_section()
    elif page == "Skills Breakdown":
        skills_visualization()
    elif page == "Education & Certifications":
        education_section()
    elif page == "Professional Journey":
        experience_timeline()
    elif page == "Contact":
        contact_section()
    st.markdown("---")
    st.markdown(
        "© Saksham Raj ",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
