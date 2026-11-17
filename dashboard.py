import tkinter as tk
from history import get_statistics


def open_dashboard():
    window = tk.Toplevel()
    window.title("CyberShield - Dashboard")
    window.geometry("800x600")
    window.configure(bg="#101827")

    tk.Label(
        window,
        text="CYBERSHIELD DASHBOARD",
        font=("Arial", 23, "bold"),
        fg="#38BDF8",
        bg="#101827"
    ).pack(pady=25)

    tk.Label(
        window,
        text="Cybersecurity Threat Analysis Results",
        font=("Arial", 13),
        fg="white",
        bg="#101827"
    ).pack(pady=5)

    stats_frame = tk.Frame(
        window,
        bg="#101827"
    )
    stats_frame.pack(pady=15)

    def refresh_statistics():
        data = get_statistics()

        stats = [
            ("Total Analyzed", data["total"]),
            ("Low Risk", data["low"]),
            ("Medium Risk", data["medium"]),
            ("High Risk", data["high"])
        ]

        for widget in stats_frame.winfo_children():
            widget.destroy()

        for name, value in stats:
            tk.Label(
                stats_frame,
                text=f"{name}: {value}",
                font=("Arial", 16),
                fg="white",
                bg="#1E293B",
                width=35,
                pady=12
            ).pack(pady=7)

    refresh_statistics()

    tk.Button(
        window,
        text="REFRESH DASHBOARD",
        command=refresh_statistics,
        bg="#2563EB",
        fg="white",
        font=("Arial", 12, "bold"),
        padx=20,
        pady=10
    ).pack(pady=10)

    tk.Label(
        window,
        text="Educational analysis only.",
        font=("Arial", 11),
        fg="#94A3B8",
        bg="#101827"
    ).pack(pady=10)