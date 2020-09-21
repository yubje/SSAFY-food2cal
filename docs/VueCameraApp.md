# Vue Camera App
---
## Summary
---
1. [Camera 연동](#1.-Camera-연동)
2. [Canvas 그리기](#2.-Canvas-그리기)
## Learning
---
## 1. Camera 연동
### 1-1. getUserMedia 메서드
  * `getUserMedia()`란?
    * MediaDevices 인터페이스의 getUserMedia()는 사용자에게 미디어 입력 장치 사용 권한을 요청하며, 사용자가 수락하면 요청한 미디어 종류의 트랙을 포함한 MediaStream을 반환하는 메서드이다.
### 1-2. `getUserMedia()`를 사용하여 웹에서 카메라 연동
  ```vue
  <template>
    <div class="camera">
      <video autoplay class="feed"></video>
      <button class="snap" @click="$emit('take-picture')">SNAP</button>
    </div>
  </template>

  <script>
  export default {
    name: 'camera',
    methods: {
      init() {
        if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
          navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
            const videoPlayer = document.querySelector('video');
            videoPlayer.srcObject = stream;
            videoPlayer.play();
          });
        } else {
          alert('Cannot get Media Devices')
        }
      }
    },
    beforeMount() {
      this.init();
    }
  }
  </script>

  <style lang="scss" scoped>
  .camera {
    z-index: 1;
    width: 100vw;
    height: 100vh;

    .feed {
      display: block;
      width: 100%;
      max-width: 1200px;
      padding: 25px;
      box-sizing: border-box;

      margin: 0 auto;

      background-color: #171717;
      box-shadow: 6px 6px 12px 8px rgba(0, 0, 0, 0.25);
    }

    .snap {
      display: block;
      width: 75px;
      height: 75px;
      border-radius: 50%;

      margin: 25px auto;

      background-color: transparentize($color: #ffCE00, $amount: 0.75);
      border: 1px solid #171717;
      outline: none;

      cursor: pointer;

      &:hover {
        background-color: #ffCE00;
      }
      &:active {
        background-color: darken($color: #FFCE00, $amount: .10);
      }
    }
  }
  </style>
  ```
## 2. Canvas 그리기
### 2-1. Canvas API
  * Canvas API
    * Canvas API는 JavaScript와 HTML <canvas> 엘리먼트를 통해 그래픽을 그리기위한 수단을 제공한다. 애니메이션, 게임 그래픽, 데이터 시각화, 사진 조작 및 실시간 비디오 처리를 위해 사용된다.
### 2-2. Snap Canvas 그리기
  ```vue
  <template>
    <div class="picture">
      <canvas></canvas>
    </div>  
  </template>

  <script>
  export default {
    name: 'gallery',
  }
  </script>

  <style lang="scss" scoped>
  .picture {
    display: block;
    width: 100vw;
    height: 100vh;

    padding: 25px;
    box-sizing: border-box;
    
    canvas {
      display: block;
      width: 100%;
      max-width: 1200px;

      margin: 0 auto;

      box-shadow: 4px 4px 12px 0px transparentize($color: #171717, $amount: 0.5);
    }
  }
  </style>
  ```
### 2-3. App.vue에 Camera, Gallery Components 연동
  ```vue
  <template>
    <div id="app">
      <Camera v-on:take-picture="this.takePicture"/>
      <Gallery />
      <button>save</button>
    </div>
  </template>

  <script>
  import Camera from './components/Camera';
  import Gallery from './components/Gallery';

  export default {
    name: 'App',
    components: {
      Camera,
      Gallery,
    },
    methods: {
      takePicture () {
        let ratio = (window.innerHeight < window.innerWidth) ? 16/9: 9/16;
        const picture = document.querySelector('canvas');
        picture.width = (window.innerWidth < 1200) ? window.innerWidth : 1200;
        picture.height = window.innerWidth / ratio;
        const ctx = picture.getContext('2d');
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(document.querySelector('video'), 0, 0, picture.width, picture.height);
      }
    }
  }
  </script>

  <style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #fefefe;
  }
  </style>
  ```
---
## References
* [How to create a CAMERA APP in VueJS](https://www.youtube.com/watch?v=HR97Uq2Ejks)
* [`MediaDevices.getUserMedia()`](https://developer.mozilla.org/ko/docs/Web/API/MediaDevices/getUserMedia)
* [Canvas API](https://developer.mozilla.org/ko/docs/Web/HTML/Canvas)
