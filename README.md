# BabelLive

**Real-time speech translation for live broadcasts.**

BabelLive is an early-stage project exploring how AI can make live events more accessible across language barriers.

The initial use case is English-to-Spanish translation for church services and other live broadcasts, with OBS Studio as the intended broadcast workflow.

## Initial MVP direction

The first version is being planned around:

- Capturing live English speech
- Transcribing and translating speech into Spanish
- Generating Spanish speech audio
- Feeding translated audio into an OBS-based broadcast workflow

A **2–5 second end-to-end latency** is a design target, not a verified performance result.

## Intended use cases

- Church services
- Conferences and live events
- Webinars and online classes
- Community broadcasts

## Planned technology

The proposed stack includes Python, FastAPI, OBS Studio, FFmpeg, and AI services for speech recognition, translation, and text-to-speech. Supporting infrastructure such as Docker, PostgreSQL, and Redis may be introduced as the system develops.

These are planned components, not a claim that the full stack or feature set is already implemented.

## Project status

🚧 **Early development.** The project is currently at the architecture and MVP-planning stage. The features above describe the intended direction; they should not be read as a list of completed capabilities.

## License

Private Repository — All Rights Reserved.
