import tkinter as tk

challenges = [
    {
        "title": "Challenge 1 - Cryptography",
        "question": "Decode this Base64 message: Q1lCRVI=",
        "answer": "CYBER",
        "hint": "Base64 is an encoding method.",
        "points": 10
    },
    {
        "title": "Challenge 2 - Digital Forensics",
        "question": "Which file extension is commonly used for packet captures? (include the dot)",
        "answer": ".pcap",
        "hint": "Wireshark can open this file type.",
        "points": 20
    },
    {
        "title": "Challenge 3 - Web Security",
        "question": "What does HTTPS stand for?",
        "answer": "Hypertext Transfer Protocol Secure",
        "hint": "It is the secure version of HTTP.",
        "points": 30
    }
]


def open_ctf():
    window = tk.Toplevel()
    window.title("CyberShield - CTF Challenges")
    window.geometry("800x550")
    window.configure(bg="#111827")

    current = 0
    score = 0

    title_label = tk.Label(
        window, text="CYBERSHIELD CTF",
        font=("Arial", 24, "bold"),
        fg="#38BDF8", bg="#111827"
    )
    title_label.pack(pady=20)

    score_label = tk.Label(
        window, text="Score: 0",
        font=("Arial", 14),
        fg="white", bg="#111827"
    )
    score_label.pack()

    question_label = tk.Label(
        window, text="",
        font=("Arial", 14),
        fg="white", bg="#1F2937",
        wraplength=700, padx=20, pady=25
    )
    question_label.pack(pady=20, padx=30, fill="x")

    answer_entry = tk.Entry(
        window, font=("Arial", 14), width=40
    )
    answer_entry.pack(pady=10)

    feedback_label = tk.Label(
        window, text="",
        font=("Arial", 12),
        fg="#FACC15", bg="#111827",
        wraplength=700
    )
    feedback_label.pack(pady=10)

    def show_challenge():
        if current >= len(challenges):
            question_label.config(
                text=f"CTF Completed! Final Score: {score}/60"
            )
            answer_entry.pack_forget()
            submit_button.pack_forget()
            hint_button.pack_forget()
            next_button.pack_forget()
            feedback_label.config(
                text="Congratulations on completing the challenges!"
            )
            return

        challenge = challenges[current]
        question_label.config(
            text=challenge["title"] + "\n\n"
            + challenge["question"]
        )
        answer_entry.delete(0, tk.END)
        feedback_label.config(text="")
        submit_button.config(state="normal")
        next_button.pack_forget()

    def check_answer():
        nonlocal score

        user_answer = answer_entry.get().strip().lower()
        correct_answer = challenges[current]["answer"].lower()

        if user_answer == correct_answer:
            score += challenges[current]["points"]
            feedback_label.config(
                text="Correct! You earned points."
            )
        else:
            feedback_label.config(
                text="Incorrect. Correct answer: "
                + challenges[current]["answer"]
            )

        score_label.config(text=f"Score: {score}")
        submit_button.config(state="disabled")
        next_button.pack(pady=10)

    def show_hint():
        feedback_label.config(
            text="Hint: " + challenges[current]["hint"]
        )

    def next_challenge():
        nonlocal current
        current += 1
        show_challenge()

    submit_button = tk.Button(
        window, text="SUBMIT ANSWER",
        command=check_answer,
        bg="#0284C7", fg="white",
        font=("Arial", 12, "bold")
    )
    submit_button.pack(pady=8)

    hint_button = tk.Button(
        window, text="SHOW HINT",
        command=show_hint,
        bg="#374151", fg="white"
    )
    hint_button.pack(pady=5)

    next_button = tk.Button(
        window, text="NEXT CHALLENGE",
        command=next_challenge,
        bg="#16A34A", fg="white"
    )

    show_challenge()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    open_ctf()
    root.mainloop()