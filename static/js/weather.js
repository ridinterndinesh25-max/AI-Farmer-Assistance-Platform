document.addEventListener("DOMContentLoaded", function () {

    const video = document.getElementById("weatherVideo");
    const source = document.getElementById("weatherVideoSource");

    if (!video || !source) {
        return;
    }

    const condition = (
        video.dataset.condition || ""
    ).toLowerCase();

    const isDay = (
        video.dataset.isDay === "true"
    );


    let videoFile = "clouds.mp4";


    // =====================================================
    // CLEAR / SUNNY
    // =====================================================

    if (
        condition === "clear"
    ) {

        if (isDay) {
            videoFile = "sunny.mp4";
        } else {
            videoFile = "night.mp4";
        }

    }


    // =====================================================
    // CLOUDS
    // =====================================================

    else if (
        condition === "clouds"
    ) {

        videoFile = "clouds.mp4";

    }


    // =====================================================
    // RAIN
    // =====================================================

    else if (
        condition === "rain"
    ) {

        videoFile = "rain.mp4";

    }


    // =====================================================
    // DRIZZLE
    // =====================================================

    else if (
        condition === "drizzle"
    ) {

        videoFile = "rain.mp4";

    }


    // =====================================================
    // THUNDERSTORM
    // =====================================================

    else if (
        condition === "thunderstorm"
    ) {

        videoFile = "thunderstorm.mp4";

    }


    // =====================================================
    // FOG / MIST / HAZE
    // =====================================================

    else if (
        condition === "mist" ||
        condition === "fog" ||
        condition === "haze"
    ) {

        videoFile = "fog.mp4";

    }


    // =====================================================
    // SET VIDEO
    // =====================================================

    source.src = "/static/weather/videos/" + videoFile;

    video.load();

    video.play().catch(function () {
        console.log("Weather video autoplay blocked.");
    });

});