from urllib.parse import urlparse
import ipaddress

def analyze_url(url):
    url = url.strip()
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        return {
            "score": 0,
            "level": "Invalid URL",
            "warnings": ["Enter a valid HTTP or HTTPS URL"]
        }

    score = 0
    warnings = []

    if parsed.scheme != "https":
        score += 25
        warnings.append("URL does not use HTTPS")

    if "@" in parsed.netloc:
        score += 30
        warnings.append("URL contains @ symbol")

    try:
        ipaddress.ip_address(parsed.hostname)
        score += 25
        warnings.append("URL uses an IP address")
    except ValueError:
        pass

    if len(url) > 100:
        score += 20
        warnings.append("URL is unusually long")

    score = min(score, 100)

    if score >= 60:
        level = "High Risk"
    elif score >= 25:
        level = "Medium Risk"
    else:
        level = "Low Risk Indicators"

    return {
        "score": score,
        "level": level,
        "warnings": warnings
    }