<template>
  <div>
    <v-progress-circular
      class="pro-circle"
      indeterminate
      color="red"
    ></v-progress-circular>
  </div>
</template>

<script>
export default {
  name: 'Loading'
}
</script>

<style>
.pro-circle {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>