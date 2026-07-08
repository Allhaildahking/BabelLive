import { startRecording, stopRecording } from "/static/recorder.js";
import { uploadAudio } from "/static/api.js";

const recordBtn = document.getElementById("recordBtn");

let recording = false;

recordBtn.addEventListener("click", async () => {

    if (!recording) {

        await startRecording();

        recording = true;

        recordBtn.textContent = "⏹ Stop Recording";

        console.log("Recording started...");

    } else {

        const audioBlob = await stopRecording();

        recording = false;

        recordBtn.textContent = "🎤 Start Recording";

        console.log("Uploading...");

try {

    const result = await uploadAudio(audioBlob);

    console.log(result);

    alert(
        "Original:\n" +
        result.transcription +
        "\n\nSpanish:\n" +
        result.translation
    );

    const audio = new Audio("/audio");
    audio.play();

} catch (err) {

    console.error(err);
    alert("Translation failed.");

}

    }

});