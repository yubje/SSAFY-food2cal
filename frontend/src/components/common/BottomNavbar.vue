<template>
  <v-bottom-navigation
    :value="activeBtn"
    fixed
    color="#FF890E"
  >
    <v-btn>
      <span>Recents</span>
      <v-icon>mdi-history</v-icon>
    </v-btn>

    <v-btn>
      <span>Favorites</span>
      <v-icon>mdi-heart</v-icon>
    </v-btn>

    <v-btn>
      <span>Nearby</span>
      <v-icon>mdi-map-marker</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {
  name: 'BottomNavbar',
  data () {
    return {
      activeBtn: 1,
    }
  },
}
</script>

<style>

</style>