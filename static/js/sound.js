const main = document.getElementsByTagName('main')[0]
const batmanSound = document.getElementById('batman_sound')

const toggleSound = () => {
  const { paused } = batmanSound
  if (paused) {
    batmanSound.play()
  } else {
    batmanSound.pause()
  }
}

main.addEventListener('click', toggleSound)
