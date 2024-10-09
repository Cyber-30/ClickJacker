# ClickJacker

## Description
ClickJacker is a simple tool designed to check for clickjacking vulnerabilities in websites. It analyzes the HTTP headers of a specified URL to determine if protective measures against clickjacking, such as `X-Frame-Options` and `Content-Security-Policy`, are implemented. The tool provides clear output indicating whether a website is vulnerable or not.

## Features
- Checks for the presence of the `X-Frame-Options` header.
- Analyzes `Content-Security-Policy` for the presence of `frame-ancestors`.
- Placeholder functions for JavaScript frame busting and SameSite cookies checks.
- User-friendly command-line interface with colored output.

## Prerequisites
Make sure you have Python 3 installed on your machine. You will also need to install the required libraries listed in `requirements.txt`.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ClickJacker.git
   cd ClickJacker
2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```
## How to Use

1.Run the tool
```bash
python ClickJacker.py
```
2.When prompted, enter the URL you want to check for clickjacking vulnerabilities, including the ```http``` or ```https``` protocol.

3.The tool will display the HTTP headers and the results of the vulnerability check.

4.You can check another URL by typing ```yes``` when prompted, or type ```no``` to exit the tool.

## Example Usage
```bash
Enter a website URL (including http/https): https://example.com
```

### HTML Testing Page

The accompanying HTML file test.html can be used to visually test for clickjacking. It embeds a specified URL within an iframe.

# Steps to Use the HTML Page:

   1. Open ```test.html``` in a web browser.
   2. Modify the ```urlToTest``` variable in the ```<script>``` section of the HTML file to change the target URL for testing:
      ```bash
      const urlToTest = "https://example.com"; // Change this to the desired URL
      ```
3. Save the changes and refresh the page to see if the target URL can be embedded.
