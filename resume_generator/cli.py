#!/usr/bin/env python3
"""
Resume CLI Generator
A command-line tool to generate professional resumes in PDF format.
"""

import json
import os
import sys
from pathlib import Path
try:
    # Python 3.9+
    from importlib.resources import files
except ImportError:
    # Python 3.7-3.8
    from importlib_resources import files
from jinja2 import Environment, BaseLoader
from weasyprint import HTML


class StringTemplateLoader(BaseLoader):
    """Custom Jinja2 loader to load templates from strings."""
    
    def __init__(self, template_string):
        self.template_string = template_string
    
    def get_source(self, environment, template):
        return self.template_string, None, lambda: True


def get_template_content():
    """Get the HTML template content from the package."""
    try:
        # Try to read from package resources
        template_files = files('resume_generator') / 'templates' / 'resume_template.html'
        return template_files.read_text(encoding='utf-8')
    except:
        # Fallback: embed template directly
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }}'s Resume</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.5;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 30px;
            background: white;
        }

        /* Header Section */
        .header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 20px;
        }

        .header h1 {
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }

        .contact-info {
            font-size: 14px;
            color: #555;
            margin-bottom: 5px;
        }

        .contact-info a {
            color: #2c3e50;
            text-decoration: none;
        }

        /* Section Styling */
        .section {
            margin-bottom: 25px;
        }

        .section-title {
            font-size: 16px;
            font-weight: bold;
            color: #2c3e50;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 15px;
            padding-bottom: 5px;
            border-bottom: 1px solid #bdc3c7;
        }

        /* Profile Section */
        .profile-text {
            font-size: 14px;
            text-align: justify;
            line-height: 1.6;
            color: #444;
        }

        /* Education Section */
        .education-item {
            margin-bottom: 12px;
        }

        .education-item .degree {
            font-weight: bold;
            font-size: 14px;
            color: #2c3e50;
        }

        .education-item .institution {
            font-size: 13px;
            color: #555;
        }

        .education-item .details {
            font-size: 12px;
            color: #666;
            margin-top: 2px;
        }

        /* Experience Section */
        .experience-item {
            margin-bottom: 18px;
        }

        .experience-item .role {
            font-weight: bold;
            font-size: 14px;
            color: #2c3e50;
        }

        .experience-item .company {
            font-size: 13px;
            color: #555;
            margin-bottom: 5px;
        }

        .experience-item .duration {
            font-size: 12px;
            color: #666;
            font-style: italic;
            margin-bottom: 5px;
        }

        .experience-item .description {
            font-size: 13px;
            color: #444;
            line-height: 1.5;
        }

        .experience-item ul {
            margin-top: 5px;
            padding-left: 20px;
        }

        .experience-item li {
            font-size: 12px;
            margin-bottom: 3px;
            color: #444;
        }

        /* Skills Section */
        .skills-category {
            margin-bottom: 15px;
        }

        .skills-category .category-title {
            font-weight: bold;
            font-size: 13px;
            color: #2c3e50;
            margin-bottom: 5px;
        }

        .skills-list {
            font-size: 12px;
            color: #444;
            line-height: 1.4;
        }

        /* Projects Section */
        .project-item {
            margin-bottom: 15px;
        }

        .project-item .project-title {
            font-weight: bold;
            font-size: 14px;
            color: #2c3e50;
            margin-bottom: 3px;
        }

        .project-item .project-tech {
            font-size: 12px;
            color: #666;
            font-style: italic;
            margin-bottom: 5px;
        }

        .project-item .project-description {
            font-size: 12px;
            color: #444;
            line-height: 1.5;
        }

        .project-item ul {
            margin-top: 5px;
            padding-left: 20px;
        }

        .project-item li {
            font-size: 12px;
            margin-bottom: 3px;
            color: #444;
        }

        /* Certificates Section */
        .certificate-item {
            margin-bottom: 10px;
        }

        .certificate-item .cert-name {
            font-weight: bold;
            font-size: 13px;
            color: #2c3e50;
        }

        .certificate-item .cert-issuer {
            font-size: 12px;
            color: #555;
        }

        .certificate-item .cert-date {
            font-size: 11px;
            color: #666;
            float: right;
        }

        /* Utility Classes */
        .clearfix::after {
            content: "";
            display: table;
            clear: both;
        }

        /* Print Optimization */
        @media print {
            body {
                padding: 20px;
                font-size: 12px;
            }
            
            .section {
                page-break-inside: avoid;
                margin-bottom: 20px;
            }
            
            .header {
                margin-bottom: 25px;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header">
        <h1>{{ name }}</h1>
        <div class="contact-info">{{ email }}</div>
        <div class="contact-info">{{ phone }}</div>
        {% if linkedin %}
        <div class="contact-info">{{ linkedin }}</div>
        {% endif %}
        {% if github %}
        <div class="contact-info">{{ github }}</div>
        {% endif %}
    </div>

    <!-- Profile Section -->
    {% if profile %}
    <div class="section">
        <h2 class="section-title">Profile</h2>
        <p class="profile-text">{{ profile }}</p>
    </div>
    {% endif %}

    <!-- Education Section -->
    <div class="section">
        <h2 class="section-title">Education</h2>
        {% for edu in education %}
        <div class="education-item">
            <div class="degree">{{ edu.degree }}, {{ edu.field }}</div>
            <div class="institution">{{ edu.institution }}</div>
            <div class="details">
                {% if edu.cgpa %}{{ edu.cgpa }}{% endif %}
                {% if edu.percentage %}{{ edu.percentage }}{% endif %}
                {% if edu.duration %} | {{ edu.duration }}{% endif %}
                {% if edu.location %} | {{ edu.location }}{% endif %}
            </div>
        </div>
        {% endfor %}
    </div>

    <!-- Professional Experience Section -->
    <div class="section">
        <h2 class="section-title">Professional Experience</h2>
        {% for exp in experience %}
        <div class="experience-item">
            <div class="role">{{ exp.role }}</div>
            <div class="company">{{ exp.company }}</div>
            <div class="duration">{{ exp.duration }}{% if exp.location %} | {{ exp.location }}{% endif %}</div>
            <div class="description">{{ exp.description }}</div>
            {% if exp.achievements %}
            <ul>
                {% for ach in exp.achievements %}
                <li>{{ ach }}</li>
                {% endfor %}
            </ul>
            {% endif %}
        </div>
        {% endfor %}
    </div>

    <!-- Skills Section -->
    <div class="section">
        <h2 class="section-title">Skills</h2>
        {% for skill_category in skills %}
        <div class="skills-category">
            <div class="category-title">{{ skill_category.category }} -</div>
            <div class="skills-list">{{ skill_category.skills }}</div>
        </div>
        {% endfor %}
    </div>

    <!-- Projects Section -->
    <div class="section">
        <h2 class="section-title">Projects</h2>
        {% for project in projects %}
        <div class="project-item">
            <div class="project-title">{{ project.name }}</div>
            <div class="project-tech">{{ project.technologies }}</div>
            {% if project.description %}
            <div class="project-description">{{ project.description }}</div>
            {% endif %}
            {% if project.highlights %}
            <ul>
                {% for highlight in project.highlights %}
                <li>{{ highlight }}</li>
                {% endfor %}
            </ul>
            {% endif %}
        </div>
        {% endfor %}
    </div>

    <!-- Certificates Section -->
    {% if certificates %}
    <div class="section">
        <h2 class="section-title">Certificates</h2>
        {% for cert in certificates %}
        <div class="certificate-item clearfix">
            <div class="cert-name">{{ cert.name }}</div>
            <div class="cert-issuer">{{ cert.issuer }}</div>
            <div class="cert-date">{{ cert.date }}</div>
        </div>
        {% endfor %}
    </div>
    {% endif %}
</body>
</html>'''


def get_input_list(prompt):
    """Get a list of inputs from user until they type 'done'."""
    items = []
    while True:
        entry = input(prompt)
        if entry.lower() == 'done':
            break
        items.append(entry)
    return items


def get_education():
    """Collect education information from user."""
    education = []
    print("\nEnter education details (type 'done' as degree to finish):")
    while True:
        degree = input("Degree: ")
        if degree.lower() == 'done':
            break
        field = input("Field of Study: ")
        institution = input("Institution: ")
        cgpa = input("CGPA (leave blank if not applicable): ")
        percentage = input("Percentage (leave blank if not applicable): ")
        duration = input("Duration (e.g., 2020-2024): ")
        location = input("Location: ")
        education.append({
            "degree": degree,
            "field": field,
            "institution": institution,
            "cgpa": cgpa,
            "percentage": percentage,
            "duration": duration,
            "location": location
        })
    return education


def get_experience():
    """Collect work experience information from user."""
    experience = []
    print("\nEnter experience details (type 'done' as role to finish):")
    while True:
        role = input("Role: ")
        if role.lower() == 'done':
            break
        company = input("Company: ")
        duration = input("Duration: ")
        location = input("Location: ")
        description = input("Short Description: ")
        print("Enter achievements (type 'done' to finish):")
        achievements = get_input_list("Achievement: ")
        experience.append({
            "role": role,
            "company": company,
            "duration": duration,
            "location": location,
            "description": description,
            "achievements": achievements
        })
    return experience


def get_skills():
    """Collect skills information from user."""
    skills = []
    print("\nEnter skill categories and corresponding skills.")
    while True:
        category = input("Skill Category (e.g., Programming Languages) (type 'done' to finish): ")
        if category.lower() == 'done':
            break
        skills_list = input("Enter skills for this category (comma-separated): ")
        skills.append({
            "category": category,
            "skills": skills_list
        })
    return skills


def get_projects():
    """Collect project information from user."""
    projects = []
    print("\nEnter project details (type 'done' as project name to finish):")
    while True:
        name = input("Project Name: ")
        if name.lower() == 'done':
            break
        technologies = input("Technologies Used: ")
        description = input("Project Description: ")
        print("Enter highlights (type 'done' to finish):")
        highlights = get_input_list("Highlight: ")
        projects.append({
            "name": name,
            "technologies": technologies,
            "description": description,
            "highlights": highlights
        })
    return projects


def get_certificates():
    """Collect certificate information from user."""
    certificates = []
    print("\nEnter certificate details (type 'done' as name to finish):")
    while True:
        name = input("Certificate Name: ")
        if name.lower() == 'done':
            break
        issuer = input("Issued By: ")
        date = input("Date (e.g., Jan 2024): ")
        certificates.append({
            "name": name,
            "issuer": issuer,
            "date": date
        })
    return certificates


def collect_resume_data():
    """Collect all resume data from user input."""
    print("=== Resume CLI Generator ===")
    print("Generate a professional resume in PDF format\n")
    
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    linkedin = input("LinkedIn URL (or leave blank): ")
    github = input("GitHub URL (or leave blank): ")
    profile = input("Profile Summary (or leave blank): ")

    education = get_education()
    experience = get_experience()
    skills = get_skills()
    projects = get_projects()
    certificates = get_certificates()

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "profile": profile,
        "education": education,
        "experience": experience,
        "skills": skills,
        "projects": projects,
        "certificates": certificates
    }


def render_to_pdf(data, output_filename="resume.pdf"):
    """Render resume data to PDF using the embedded template."""
    try:
        template_content = get_template_content()
        env = Environment(loader=StringTemplateLoader(template_content))
        template = env.get_template('')
        html_out = template.render(data)

        # Save HTML for debugging (optional)
        html_filename = output_filename.replace('.pdf', '.html')
        with open(html_filename, "w", encoding='utf-8') as f:
            f.write(html_out)

        # Generate PDF
        HTML(string=html_out).write_pdf(output_filename)
        
        print(f"\n✅ Resume generated successfully!")
        print(f"📄 PDF: {output_filename}")
        print(f"🌐 HTML: {html_filename}")
        
    except Exception as e:
        print(f"\n❌ Error generating resume: {str(e)}")
        print("Please ensure WeasyPrint dependencies are installed.")
        sys.exit(1)


def save_data_to_json(data, filename="resume_data.json"):
    """Save resume data to JSON file for future use."""
    try:
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"💾 Resume data saved to: {filename}")
    except Exception as e:
        print(f"⚠️  Warning: Could not save data to JSON: {str(e)}")


def main():
    """Main CLI entry point."""
    try:
        print("🚀 Welcome to Resume CLI Generator!")
        print("This tool will help you create a professional resume in PDF format.\n")
        
        # Collect resume data
        resume_data = collect_resume_data()
        
        # Save data to JSON
        save_data_to_json(resume_data)
        
        # Generate PDF
        render_to_pdf(resume_data)
        
        print("\n🎉 Resume generation completed!")
        print("You can now use your resume.pdf file for job applications.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Resume generation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()