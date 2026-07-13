import { startRecording, stopRecording } from "/static/recorder.js";
import { uploadAudio } from "/static/api.js";

const recordBtn = document.getElementById("recordBtn");

async function beginRecording() {

    recordBtn.textContent = "🎙 Recording...";

    await startRecording();

}

async function endRecording() {

    recordBtn.textContent = "⏳ Translating...";

    try {

        const audioBlob = await stopRecording();

        const result = await uploadAudio(audioBlob);

        document.getElementById("originalText").textContent =
            result.transcription;

        document.getElementById("translatedText").textContent =
            result.translation;

        const audio = new Audio("/audio");

        audio.play();

        audio.onended = () => {

            recordBtn.textContent = "🎤 Hold to Speak Again";

        };

    } catch (err) {

        console.error(err);

        recordBtn.textContent = "🎤 Hold to Speak";

        alert("Translation failed.");

    }

}

recordBtn.addEventListener("mousedown", beginRecording);
recordBtn.addEventListener("mouseup", endRecording);

recordBtn.addEventListener("touchstart", (e) => {

    e.preventDefault();

    beginRecording();

});

recordBtn.addEventListener("touchend", (e) => {

    e.preventDefault();

    endRecording();

});