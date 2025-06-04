# Resume CLI Generator

A simple and elegant command-line tool to generate professional resumes in PDF format. No design skills required - just provide your information and get a beautifully formatted resume!

## Features

- 🎨 **Professional Design**: Clean, modern resume template
- 📝 **Interactive CLI**: Easy-to-use command-line interface
- 📄 **PDF Output**: Generates high-quality PDF resumes
- 💼 **Complete Sections**: Education, Experience, Skills, Projects, Certificates
- 🔧 **No Setup Required**: Template embedded in the package
- 💾 **Data Backup**: Saves your input as JSON for future edits

## Installation

### From PyPI (Recommended)

```bash
pip install resume-cli-generator
```

### System Dependencies

The tool uses WeasyPrint for PDF generation, which requires some system dependencies:

**Ubuntu/Debian:**
```bash
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

**macOS:**
```bash
brew install cairo pango gdk-pixbuf libffi
```

**Windows:**
- Install GTK3+ runtime from https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

## Usage

After installation, simply run:

```bash
resume-generator
```

The tool will guide you through entering your information:

1. **Personal Information**: Name, email, phone, LinkedIn, GitHub
2. **Profile Summary**: Brief professional summary (optional)
3. **Education**: Degrees, institutions, grades, duration
4. **Experience**: Job roles, companies, achievements
5. **Skills**: Categorized skill sets
6. **Projects**: Personal/professional projects with highlights
7. **Certificates**: Professional certifications

### Example Session

```
🚀 Welcome to Resume CLI Generator!

=== Resume CLI Generator ===
Full Name: John Doe
Email: john.doe@email.com
Phone: +1-234-567-8900
LinkedIn URL: https://linkedin.com/in/johndoe
GitHub URL: https://github.com/johndoe
Profile Summary: Experienced software developer with 5+ years...

Enter education details (type 'done' as degree to finish):
Degree: Bachelor of Science
Field of Study: Computer Science
Institution: University of Technology
...

✅ Resume generated successfully!
📄 PDF: resume.pdf
🌐 HTML: resume.html
💾 Resume data saved to: resume_data.json
```

## Output Files

The tool generates three files:

- **`resume.pdf`**: Your professional resume in PDF format
- **`resume.html`**: HTML version for web viewing
- **`resume_data.json`**: Your input data for future editing

## Template Preview

The generated resume includes:

- **Clean Header**: Name and contact information
- **Profile Section**: Professional summary
- **Education**: Academic background with grades and dates
- **Professional Experience**: Work history with achievements
- **Skills**: Categorized technical and soft skills
- **Projects**: Notable projects with technologies used
- **Certificates**: Professional certifications and courses

## Development

### Local Installation

```bash
git clone https://github.com/yourusername/resume-cli-generator.git
cd resume-cli-generator
pip install -e .
```

### Building for Distribution

```bash
python setup.py sdist bdist_wheel
```

### Publishing to PyPI

```bash
pip install twine
twine upload dist/*
```

## Requirements

- Python 3.7+
- Jinja2 >= 3.0.0
- WeasyPrint >= 54.0

## Troubleshooting

### WeasyPrint Installation Issues

If you encounter issues with WeasyPrint installation:

1. **Linux**: Ensure all system dependencies are installed
2. **macOS**: Install dependencies via Homebrew
3. **Windows**: Install GTK3+ runtime environment

### Common Issues

- **Permission Errors**: Run with appropriate permissions for file creation
- **Font Issues**: WeasyPrint will use system fonts automatically
- **PDF Generation Fails**: Check that all system dependencies are installed

## Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Contact the maintainer

## Changelog

### v1.0.0
- Initial release
- Interactive CLI interface
- PDF resume generation
- Professional template design
- JSON data backup feature