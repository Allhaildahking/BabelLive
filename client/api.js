export async function uploadAudio(audioBlob) {

    const formData = new FormData();

    formData.append(
        "audio",
        audioBlob,
        "audio.webm"
    );

    const response = await fetch("/transcribe", {
        method: "POST",
        body: formData
    });

    if (!response.ok) {
        throw new Error("Upload failed");
    }

    return await response.json();
}