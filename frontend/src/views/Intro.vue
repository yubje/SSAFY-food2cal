<template>
  <div class="intro">
    
  </div>
</template>

<script>
export default {
  name: 'Intro',
  created () {
    setTimeout(() => {
      this.$router.push('/home')
    }, 2000)
  }
}
</script>

<style>
.intro {
  position: fixed;
  top: 50%;
  left: 50%;
  /* transform: translate(-50%, -50%); */
  z-index: 10;
  background-color: #fff;
  width: 100vh;
  height: 100vh;
}
</style>