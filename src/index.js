let file = "file:///C:/Users/Kai/Music/Songs/Other/Dammit.mp3";
let playing = false;
const audioPlayer = document.querySelector("#audioPlayer");
audioPlayer.src = URL.createObjectURL(file);
audioPlayer.load();

document.getElementById("playPauseButton").addEventListener("click", () => {

    if (playing) {

        playing = false;
        audioPlayer.pause();

    } else {

        playing = true;
        audioPlayer.play();

    }

});
