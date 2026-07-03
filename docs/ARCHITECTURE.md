# BabelLive System Architecture

## Overview

BabelLive is a real-time AI speech translation platform.

The system captures live audio from OBS, converts it into text, translates it, generates natural speech, and sends the translated audio back into OBS for live streaming.

---

## High-Level Architecture

Preacher
↓
Microphone
↓
OBS Studio
↓
BabelLive Backend
↓
Speech Recognition
↓
Translation Engine
↓
Text-to-Speech Engine
↓
OBS Audio Output
↓
YouTube / Facebook / Website

---

## Core Components

### Audio Input Service
Receives live audio from OBS.

### Speech Recognition Service
Converts speech into English text.

### Translation Service
Translates English into Spanish.

### Text-to-Speech Service
Creates natural Spanish speech.

### Streaming Service
Returns Spanish audio to OBS.

### Logging Service
Tracks errors and system performance.

---

## Design Principles

- Modular
- Low Latency
- Scalable
- Fault Tolerant
- Cloud Ready
