Software Requirements Specification (SRS)

Project Name

BabelLive

Version

0.1.0 (MVP)

Purpose

BabelLive is an AI-powered real-time speech translation platform that converts live spoken language into natural-sounding translated speech with minimal delay.

The first MVP will focus on translating English speech into Spanish during live broadcasts.

---

Problem Statement

Many churches and organizations have international audiences but rely on a single spoken language during live broadcasts.

Hiring live interpreters is expensive and difficult to scale.

BabelLive aims to provide an AI-powered alternative that delivers high-quality live translation with low latency.

---

MVP Objective

The MVP must demonstrate:

- Live English speech input
- Real-time speech recognition
- English-to-Spanish translation
- Natural Spanish AI voice generation
- Integration with OBS Studio
- One live stream carrying Spanish audio
- Target latency of 2–5 seconds
- Stable operation for at least 20 minutes

---

Functional Requirements

The system shall:

1. Receive live microphone audio from OBS.
2. Convert speech to English text.
3. Translate English text into Spanish.
4. Generate natural Spanish speech.
5. Send the Spanish audio back into OBS.
6. Support continuous live translation.
7. Log system errors for debugging.

---

Non-Functional Requirements

- Low latency (2–5 seconds)
- High reliability
- Modular architecture
- Easy deployment
- Scalable design
- Secure API communication

---

Out of Scope (MVP)

- Multiple languages
- User accounts
- Billing system
- Church dashboard
- Mobile applications
- Voice cloning
- Speaker identification

These features will be added in future versions.

---

Success Criteria

The MVP is considered successful if:

- A speaker talks in English.
- The system translates into Spanish.
- The Spanish AI voice is streamed through OBS.
- The audience hears only Spanish.
- End-to-end delay remains within 2–5 seconds.
- The demo runs successfully for 10–20 minutes.