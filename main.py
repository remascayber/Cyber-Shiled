from urllib.parse import urlparse
import ipaddress

print("Welcome to CyberShield")
print("Cybersecurity Educational URL Analyzer")

url = input("Enter a URL: ").strip()
parsed = urlparse(url)
hostname = parsed.hostname

warnings = []

if parsed.scheme not in ("http", "https") or not hostname:
    print("Invalid URL. Use http:// or https://")
else:
    if parsed.scheme != "https":
        warnings.append("URL does not use HTTPS")

    if "@" in parsed.netloc:
        warnings.append("URL contains @ symbol")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("URL uses an IP address")
    except ValueError:
        pass

    if len(url) > 100:
        warnings.append("URL is unusually long")

    print("\nAnalysis Results:")
    print("Hostname:", hostname)

    if warnings:
        for warning in warnings:
            print("Warning:", warning)
    else:
        print("No basic warning indicators found")

    print("Educational analysis only.")
    print("This does not guarantee URL safety.")
