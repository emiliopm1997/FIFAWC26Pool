# FIFA WC 2026 Pool

## 📌 Overview
This project provides a simple API to manage a FIFA World Cup 2026 prediction pool for a group of friends.

The API is responsible for handling match data, user predictions, and scoring. It allows users to submit predictions, update match results, and automatically maintain a leaderboard as the tournament progresses.

---

## ⚙️ Tech Stack
- **Python**
- **Flask**
- **SQLAlchemy** (for database management)

---

## 🎯 Purpose
The API is designed to:
- Store World Cup match data
- Store user predictions
- Update match results
- Automatically compute and update a leaderboard

This project is intended for **personal use within a small group of friends**.

---

## 🚀 Features
- Create users
- Submit match predictions
- Update match results
- Compute and update leaderboard
- Retrieve current standings

---

## 🧠 Scoring System
- Users predict the **winner of each match** (or a draw)
- Points are awarded for:
  - Correct match outcome (win/draw)

> Future extension (optional):
> - Predict exact score
> - Bonus points for exact score accuracy

---

## 📦 Project Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd fifa-wc-2026-pool
