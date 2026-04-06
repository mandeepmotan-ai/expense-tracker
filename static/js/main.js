// main.js — students will add JavaScript here as features are built

(function () {
  var texts = ['Free to use', 'No credit card needed'];
  var el = document.getElementById('typewriter-text');
  if (!el) return;

  var textIndex = 0;
  var charIndex = 0;
  var isDeleting = false;
  var isPaused = false;

  // speed settings (ms per character)
  var TYPE_SPEED_MIN = 100;
  var TYPE_SPEED_MAX = 100;
  var DELETE_SPEED = 50;
  var PAUSE_AFTER_TYPE = 1500;
  var PAUSE_AFTER_DELETE = 500;

  // cursor element
  var cursor = document.createElement('span');
  cursor.className = 'typewriter-cursor';
  cursor.textContent = '|';
  el.parentNode.insertBefore(cursor, el.nextSibling);

  function rand(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  function tick() {
    var current = texts[textIndex];

    if (!isDeleting) {
      el.textContent = current.substring(0, charIndex + 1);
      charIndex++;
      if (charIndex === current.length) {
        isDeleting = true;
        setTimeout(tick, PAUSE_AFTER_TYPE);
        return;
      }
      setTimeout(tick, rand(TYPE_SPEED_MIN, TYPE_SPEED_MAX));
    } else {
      el.textContent = current.substring(0, charIndex - 1);
      charIndex--;
      if (charIndex === 0) {
        isDeleting = false;
        textIndex = (textIndex + 1) % texts.length;
        // crossfade out → swap → fade in
        el.style.transition = 'opacity 180ms ease-out';
        el.style.opacity = '0';
        setTimeout(function () {
          el.style.transition = 'opacity 120ms ease-in';
          el.style.opacity = '1';
          setTimeout(tick, 120);
        }, 200);
        return;
      }
      setTimeout(tick, DELETE_SPEED);
    }
  }

  setTimeout(tick, 1200);
})();
