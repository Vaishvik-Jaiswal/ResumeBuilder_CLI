import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def get_input_list(prompt):
    items = []
    while True:
        entry = input(prompt)
        if entry.lower() == 'done':
            break
        items.append(entry)
    return items

def get_education():
    education = []
    print("\nEnter education details (type 'done' as degree to finish):")
    while True:
        degree = input("Degree: ")
        if degree.lower() == 'done':
            break
        institution = input("Institution: ")
        year = input("Year: ")
        education.append({"degree": degree, "institution": institution, "year": year})
    return education

def get_experience():
    experience = []
    print("\nEnter experience details (type 'done' as role to finish):")
    while True:
        role = input("Role: ")
        if role.lower() == 'done':
            break
        company = input("Company: ")
        duration = input("Duration: ")
        description = input("Description: ")
        experience.append({"role": role, "company": company, "duration": duration, "description": description})
    return experience

def collect_resume_data():
    print("=== Resume CLI ===")
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    education = get_education()
    experience = get_experience()
    skills = get_input_list("\nEnter a skill (type 'done' to finish): ")

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "education": education,
        "experience": experience,
        "skills": skills
    }

def render_to_pdf(data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    html_out = template.render(data)

    # Save optional HTML output
    with open("output.html", "w") as f:
        f.write(html_out)

    # Convert to PDF
    HTML(string=html_out).write_pdf("resume.pdf")
    print("\n✅ Resume generated: resume.pdf")

if __name__ == "__main__":
    resume_data = collect_resume_data()

    with open("data.json", "w") as f:
        json.dump(resume_data, f, indent=4)

    render_to_pdf(resume_data)