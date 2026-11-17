import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "email": "URGENT! Your bank account is blocked. Click the link and enter your password.",
        "phishing": True,
        "reason": "The message creates urgency and asks for a password."
    },
    {
        "email": "Hello student, your cybersecurity lecture starts tomorrow at 10 AM.",
        "phishing": False,
        "reason": "This example contains no obvious phishing indicators."
    },
    {
        "email": "You won $10,000! Send your OTP code to claim your prize.",
        "phishing": True,
        "reason": "Legitimate services should not ask you to share OTP codes."
    }
]


def open_simulation():
    window = tk.Toplevel()
    window.title("CyberShield - Attack Simulation")
    window.geometry("750x550")
    window.configure(bg="#111827")

    current = 0
    score = 0

    title = tk.Label(
        window,
        text="PHISHING ATTACK SIMULATION",
        font=("Arial", 22, "bold"),
        fg="#38BDF8",
        bg="#111827"
    )
    title.pack(pady=25)

    progress_label = tk.Label(
        window,
        text="",
        font=("Arial", 13),
        fg="white",
        bg="#111827"
    )
    progress_label.pack(pady=10)

    email_label = tk.Label(
        window,
        text="",
        font=("Arial", 15),
        fg="white",
        bg="#1F2937",
        wraplength=620,
        justify="center",
        padx=20,
        pady=25
    )
    email_label.pack(padx=35, pady=20, fill="x")

    feedback_label = tk.Label(
        window,
        text="",
        font=("Arial", 12),
        fg="#FACC15",
        bg="#111827",
        wraplength=620
    )
    feedback_label.pack(pady=15)

    def show_question():
        if current >= len(questions):
            progress_label.config(text="Simulation Completed")
            email_label.config(
                text=f"Final Score: {score}/{len(questions)}"
            )
            feedback_label.config(
                text="Great! Keep practicing cybersecurity awareness."
            )
            safe_button.pack_forget()
            phishing_button.pack_forget()
            next_button.pack_forget()
            return

        question = questions[current]
        progress_label.config(
            text=f"Question {current + 1} of {len(questions)}"
        )
        email_label.config(text=question["email"])
        feedback_label.config(text="")
        safe_button.config(state="normal")
        phishing_button.config(state="normal")
        next_button.pack_forget()

    def check_answer(answer):
        nonlocal score

        question = questions[current]

        if answer == question["phishing"]:
            score += 1
            result = "Correct Answer!"
        else:
            result = "Incorrect Answer!"

        feedback_label.config(
            text=result + "\n" + question["reason"]
        )

        safe_button.config(state="disabled")
        phishing_button.config(state="disabled")
        next_button.pack(pady=10)

    def next_question():
        nonlocal current
        current += 1
        show_question()

    safe_button = tk.Button(
        window,
        text="SAFE EMAIL",
        command=lambda: check_answer(False),
        bg="#16A34A",
        fg="white",
        font=("Arial", 13, "bold"),
        width=18
    )
    safe_button.pack(pady=8)

    phishing_button = tk.Button(
        window,
        text="PHISHING EMAIL",
        command=lambda: check_answer(True),
        bg="#DC2626",
        fg="white",
        font=("Arial", 13, "bold"),
        width=18
    )
    phishing_button.pack(pady=8)

    next_button = tk.Button(
        window,
        text="NEXT QUESTION",
        command=next_question,
        bg="#0284C7",
        fg="white",
        font=("Arial", 12, "bold")
    )

    show_question()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    open_simulation()
    root.mainloop()