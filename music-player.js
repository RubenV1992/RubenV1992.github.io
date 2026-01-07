// Audio Source Configuration
const AUDIO_SOURCE_TYPE = "local"; // "local" | "remote"

// Audio source URLs - Update these with your actual file paths or remote URLs
const AUDIO_SOURCES = {
  local: {
    mozart: "assets/audio/mozart_symphony_40.mp3",
    beethoven: "assets/audio/beethoven_moonlight.mp3",
    bach: "assets/audio/bach_air.mp3",
    vivaldi: "assets/audio/vivaldi_four_seasons.mp3",
    chopin: "assets/audio/chopin_nocturne.mp3"
  },
  remote: {
    mozart: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    beethoven: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    bach: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    vivaldi: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    chopin: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
  }
};

// Album catalog data
const ALBUMS = [
  {
    id: 1,
    composer: "Wolfgang Amadeus Mozart",
    work: "Symphony No. 40 in G Minor",
    duration: "28:45",
    cover: "assets/images/mozart_album.jpg",
    audioKey: "mozart"
  },
  {
    id: 2,
    composer: "Ludwig van Beethoven",
    work: "Moonlight Sonata",
    duration: "15:30",
    cover: "assets/images/beethoven_album.jpg",
    audioKey: "beethoven"
  },
  {
    id: 3,
    composer: "Johann Sebastian Bach",
    work: "Air on the G String",
    duration: "5:20",
    cover: "assets/images/bach_album.jpg",
    audioKey: "bach"
  },
  {
    id: 4,
    composer: "Antonio Vivaldi",
    work: "The Four Seasons - Spring",
    duration: "10:15",
    cover: "assets/images/vivaldi_album.jpg",
    audioKey: "vivaldi"
  },
  {
    id: 5,
    composer: "Frédéric Chopin",
    work: "Nocturne in E-flat Major",
    duration: "4:30",
    cover: "assets/images/chopin_album.jpg",
    audioKey: "chopin"
  }
];

// Vinyl Player Manager
class VinylPlayer {
  constructor() {
    this.currentPlaying = null;
    this.currentAudio = null;
    this.init();
  }

  init() {
    this.renderAlbums();
    this.setCurrentYear();
  }

  // Get audio source based on configuration
  getAudioSource(audioKey) {
    const sources = AUDIO_SOURCES[AUDIO_SOURCE_TYPE];
    if (!sources || !sources[audioKey]) {
      console.warn(`Audio source not found for key: ${audioKey}`);
      return AUDIO_SOURCES.remote[audioKey] || AUDIO_SOURCES.local[audioKey];
    }
    return sources[audioKey];
  }

  // Render album cards
  renderAlbums() {
    const grid = document.getElementById('albums-grid');
    if (!grid) return;

    grid.innerHTML = ALBUMS.map(album => `
      <article class="album-card" data-album-id="${album.id}">
        <div class="now-playing">Now Playing</div>
        <div class="vinyl-player">
          <div class="sleeve">
            <img src="${album.cover}" alt="${album.composer} - ${album.work}" 
                 onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIwIiBoZWlnaHQ9IjIyMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMjIwIiBoZWlnaHQ9IjIyMCIgZmlsbD0iIzIyMWYxYyIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBmb250LWZhbWlseT0iR2VvcmdpYSIgZm9udC1zaXplPSIxMiIgZmlsbD0iI2Q0YWYzNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkNsYXNzaWNhbCBBbGJ1bTwvdGV4dD48L3N2Zz4='">
            <img class="vinyl-disc" src="assets/images/vinyl.png" alt="Vinyl Disc" 
                 onerror="this.style.display='none'; const fallback = this.nextElementSibling; if(fallback) fallback.style.display='block';">
            <div class="vinyl-disc-fallback"></div>
          </div>
          <div class="needle-arm"></div>
        </div>
        <div class="album-info">
          <div class="composer-name">${this.escapeHtml(album.composer)}</div>
          <div class="work-title">${this.escapeHtml(album.work)}</div>
          <div class="duration">${album.duration}</div>
        </div>
        <div class="controls">
          <button class="control-btn play" data-album-id="${album.id}" aria-label="Play ${album.work}">
            Play
          </button>
          <button class="control-btn stop" data-album-id="${album.id}" aria-label="Stop ${album.work}" disabled>
            Stop
          </button>
        </div>
        <audio class="audio-element" data-album-id="${album.id}" preload="metadata">
          <source src="${this.getAudioSource(album.audioKey)}" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>
      </article>
    `).join('');

    // Add event listeners
    document.querySelectorAll('.play').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const albumId = parseInt(btn.dataset.albumId);
        this.playAlbum(albumId);
      });
    });

    document.querySelectorAll('.stop').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const albumId = parseInt(btn.dataset.albumId);
        this.stopAlbum(albumId);
      });
    });

    // Handle audio ended event
    document.querySelectorAll('.audio-element').forEach(audio => {
      audio.addEventListener('ended', () => {
        const albumId = parseInt(audio.dataset.albumId);
        this.stopAlbum(albumId);
      });

      audio.addEventListener('error', (e) => {
        console.error('Audio loading error:', e);
        const albumId = parseInt(audio.dataset.albumId);
        const album = ALBUMS.find(a => a.id === albumId);
        if (album) {
          alert(`Failed to load audio for ${album.composer} - ${album.work}. Please check the audio file path.`);
        }
      });
    });
  }

  // Play album
  playAlbum(albumId) {
    // Stop currently playing track if any
    if (this.currentPlaying && this.currentPlaying !== albumId) {
      this.stopAlbum(this.currentPlaying);
    }

    const albumCard = document.querySelector(`[data-album-id="${albumId}"]`);
    const audio = albumCard.querySelector('.audio-element');
    const playBtn = albumCard.querySelector('.play');
    const stopBtn = albumCard.querySelector('.stop');

    if (!albumCard || !audio) return;

    // Update UI state
    albumCard.classList.add('playing');
    playBtn.classList.add('playing');
    playBtn.disabled = true;
    stopBtn.disabled = false;

    // Set current playing
    this.currentPlaying = albumId;
    this.currentAudio = audio;

    // Play audio
    audio.play().catch(err => {
      console.error('Playback error:', err);
      alert('Failed to play audio. Please check your audio source configuration.');
      this.stopAlbum(albumId);
    });
  }

  // Stop album
  stopAlbum(albumId) {
    const albumCard = document.querySelector(`[data-album-id="${albumId}"]`);
    if (!albumCard) return;

    const audio = albumCard.querySelector('.audio-element');
    const playBtn = albumCard.querySelector('.play');
    const stopBtn = albumCard.querySelector('.stop');

    // Stop audio
    if (audio) {
      audio.pause();
      audio.currentTime = 0;
    }

    // Update UI state
    albumCard.classList.remove('playing');
    playBtn.classList.remove('playing');
    playBtn.disabled = false;
    stopBtn.disabled = true;

    // Clear current playing if this was the active track
    if (this.currentPlaying === albumId) {
      this.currentPlaying = null;
      this.currentAudio = null;
    }
  }

  // Escape HTML to prevent XSS
  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Set current year in footer
  setCurrentYear() {
    const yearEl = document.getElementById('year');
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }
  }
}

// Initialize player when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  window.vinylPlayer = new VinylPlayer();
});

// Keyboard accessibility
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const player = window.vinylPlayer;
    if (player && player.currentPlaying) {
      player.stopAlbum(player.currentPlaying);
    }
  }
});
