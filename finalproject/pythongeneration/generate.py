"""
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Final Project Generator & Tester
________________________________________________________________________

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Author: Adrien Babet | GitHub: @babetcode | Email: adrienbabet1@gmail.com
_______________________________________________________________________________
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


site_name = 'FooBar'
site_pages = ['About', 'Contact', 'Employment', 'Locations']
about_content = """
<p>Enjoy all-you-can-eat French baked goods with our unique \
subscription model.</p>"""
contact_content = """
<p>Have a question? Reach out to us via email or visit one of \
our locations.</p>"""



page_contents = []

body


nav_header = f"""
<header id="main-header">
    <a href="../main.html">
        <img src="../images/logo2-1.png" alt="logo" id="mainheaderlogo">
    </a>
    <div id="hamburger">
        <div></div>
        <div></div>
        <div></div>
    </div>
    <div id="dropdown-menu">
        <a href="aboutpage.html">About</a>
        <a href="menupage.html">Menu</a>
        <a href="locationspage.html">Locations</a>
        <a href="employmentpage.html">Employment</a>
        <a href="contactpage.html">Contact</a>
        <a href="storypage.html">Our Story</a>
    </div>
    <ul>
        <li>
            <a href="aboutpage.html">About</a>
        </li>
        <li>
            <a href="menupage.html">Menu</a>
        </li>
        <li>
            <a href="locationspage.html">Locations</a>
        </li>
        <li>
            <a href="employmentpage.html">Employment</a>
        </li>
        <li>
            <a href="contactpage.html">Contact</a>
        </li>
        <li>
            <a href="storypage.html">Our Story</a>
        </li>
    </ul>
    <div id="socials">
        <a href="https://www.facebook.com" target="_blank">
            <img src="../images/fb.png" alt="facebook">
        </a>
        <a href="https://www.instagram.com" target="_blank">
            <img src="../images/instagram.png" alt="instagram">
        </a>
        <a href="https://www.twitter.com" target="_blank">
            <img src="../images/twitterx.png" alt="twitterx">
        </a>
    </div>
</header>"""

print(nav_header)

for page in site_pages:
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab 9 Homepage</title>
    <link rel="stylesheet" href="../css/navstyles.css">
    <link rel="stylesheet" href="../css/pagestyles.css">
</head>
<body>
    {nav_header}
    {body_content[page]}
</body>
</html>"""