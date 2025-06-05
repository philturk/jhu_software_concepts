from urllib import parse, robotparser

## This part of the script checks if a user agent can access specific paths on a website
agent = "phil"
url = "https://www.thegradcafe.com/"

parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(url, "robots.txt"))
parser.read()

paths = [
    "/",
    "/cgi-bin/",
    "/index-ad-test.php",
    "/admin/",
    "survey/"]

for path in paths:
    full_url = parse.urljoin(url, path)
    if parser.can_fetch(agent, full_url):
        print(f"{agent} can access {full_url}")
    else:
        print(f"{agent} cannot access {full_url}")

## phil can access https://www.thegradcafe.com/
## phil cannot access https://www.thegradcafe.com/cgi-bin/
## phil cannot access https://www.thegradcafe.com/index-ad-test.php
## phil can access https://www.thegradcafe.com/admin
## phil can access https://www.thegradcafe.com/survey