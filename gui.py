import tkinter as tk
from tkinter import ttk
from urllib.parse import urlparse
import ipaddress

from analyzer import analyze_url as check_url_risk
from email_analyzer import analyze_email
from dashboard import open_dashboard
from history import save_analysis
from simulation import open_simulation
from ctf import open_ctf

def analyze_url():
    url = url_entry.get().strip()

    results.delete("1.0", tk.END)

    if not url:
        results.insert(tk.END, "Please enter a URL.")
        return

    analysis = check_url_risk(url)
    save_analysis(analysis["level"])

    score = analysis["score"]
    level = analysis["level"]
    warnings = analysis["warnings"]

    results.insert(tk.END, "CYBERSHIELD ANALYSIS\n")
    results.insert(tk.END, "--------------------------\n")
    results.insert(tk.END, f"URL: {url}\n")
    results.insert(tk.END, f"Risk Score: {score}/100\n")
    results.insert(tk.END, f"Risk Level: {level}\n\n")

    results.tag_configure("low", foreground="#22C55E")
    results.tag_configure("medium", foreground="#F59E0B")
    results.tag_configure("high", foreground="#EF4444")

    if score >= 60:
        color_tag = "high"
    elif score >= 25:
        color_tag = "medium"
    else:
        color_tag = "low"

    results.insert(
        tk.END,
        f"Risk Indicator: {level}\n",
        color_tag
    )
    if warnings:
        results.insert(tk.END, "Security Warnings:\n")
        for warning in warnings:
            results.insert(tk.END, f"- {warning}\n")
    else:
        results.insert(tk.END, "No basic warning indicators found.\n")

    results.insert(tk.END, "\nEducational analysis only.")
    results.insert(tk.END, "\nThis does not guarantee URL safety.")



    try:
        parsed = urlparse(url)

        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            results.insert(tk.END, "Invalid URL. Use http:// or https://")
            return

        hostname = parsed.hostname
        warnings = []

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

        results.insert(tk.END, "Hostname: " + hostname + "\n\n")

        if warnings:
            for warning in warnings:
                results.insert(tk.END, "Warning: " + warning + "\n")
        else:
            results.insert(tk.END, "No basic warning indicators found")

        results.insert(
            tk.END,
            "\n\nEducational analysis only.\n"
            "This does not guarantee URL safety."
        )

    except ValueError:
        results.insert(tk.END, "Invalid URL format")


root = tk.Tk()
root.title("CyberShield - URL Analyzer")
root.geometry("650x460")
root.configure(bg="#101827")

title = tk.Label(
    root, text="CYBERSHIELD",
    font=("Arial", 25, "bold"),
    fg="#60A5FA", bg="#101827"
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root, text="Cybersecurity URL Analyzer",
    font=("Arial", 12),
    fg="white", bg="#101827"
)
subtitle.pack(pady=5)

url_entry = ttk.Entry(root, font=("Arial", 13), width=55)
url_entry.pack(pady=20)
url_entry.insert(0, "https://example.com")

analyze_button = tk.Button(
    root, text="ANALYZE URL",
    command=analyze_url,
    bg="#2563EB", fg="white",
    font=("Arial", 12, "bold"),
    padx=25, pady=10
)
analyze_button.pack(pady=5)

results = tk.Text(
    root, height=9, width=65,
    bg="#1E293B", fg="white",
    font=("Consolas", 11),
    padx=12, pady=12
)
results.pack(pady=20)

def open_email_analyzer():
    window = tk.Toplevel(root)
    window.title("CyberShield - Email Analyzer")
    window.geometry("650x550")
    window.configure(bg="#1E293B")

    tk.Label(
        window,
        text="PHISHING EMAIL ANALYZER",
        font=("Arial", 18, "bold"),
        fg="#38BDF8",
        bg="#1E293B"
    ).pack(pady=15)

    email_input = tk.Text(window, height=8, width=65)
    email_input.pack(pady=10)

    output = tk.Text(window, height=10, width=65)
    output.pack(pady=15)

    def check_email():
        message = email_input.get("1.0", tk.END).strip()
        output.delete("1.0", tk.END)

        if not message:
            output.insert(tk.END, "Please enter an email message.")
            return

        result = analyze_email(message)

        output.insert(tk.END, "CYBERSHIELD EMAIL ANALYSIS\n")
        output.insert(tk.END, f"Risk Score: {result['score']}/100\n")
        output.insert(tk.END, f"Risk Level: {result['level']}\n\n")

        if result["warnings"]:
            for warning in result["warnings"]:
                output.insert(tk.END, f"- {warning}\n")
        else:
            output.insert(tk.END, "No basic phishing indicators found.")

        output.insert(tk.END, "\nEducational analysis only.")

    tk.Button(
        window,
        text="ANALYZE EMAIL",
        command=check_email,
        bg="#2563EB",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=5)


email_button = tk.Button(
    root,
    text="PHISHING EMAIL ANALYZER",
    command=open_email_analyzer,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold")
)
email_button.pack(pady=10)
dashboard_button = tk.Button(
    root,
    text="OPEN DASHBOARD",
    command=open_dashboard,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold")
)

dashboard_button.pack(pady=10)

simulation_button = tk.Button(
    root,
    text="ATTACK SIMULATION",
    command=open_simulation,
    bg="#0284C7",
    fg="white",
    font=("Arial", 12, "bold"),
    width=25
)

simulation_button.pack(pady=10)

ctf_button = tk.Button(
    root,
    text="CTF CHALLENGES",
    command=open_ctf,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=25
)
ctf_button.pack(pady=10)

root.mainloop()

