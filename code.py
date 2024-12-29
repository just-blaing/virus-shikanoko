import webbrowser
import time

url = "https://www.youtube.com/watch?v=bv__9O5CZok&autoplay=1"
for i in range(30):
    webbrowser.open(url)
    time.sleep(1)

volume_script = '''
javascript: (function() {
    var video = document.querySelector('video');
    if (video) {
        video.volume = 1;
    }
})();
'''

webbrowser.open(volume_script)
