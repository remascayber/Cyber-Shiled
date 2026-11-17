def analyze_email(message):
    text = message.lower()
    score = 0
    warnings = []

    indicators = {
        "verify your account": "Account verification request",
        "password": "Password-related request",
        "urgent": "Urgency language",
        "click here": "Suspicious call to action",
        "account suspended": "Account suspension threat",
        "send your otp": "OTP disclosure request"
    }

    for phrase, warning in indicators.items():
        if phrase in text:
            score += 20
            warnings.append(warning)

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