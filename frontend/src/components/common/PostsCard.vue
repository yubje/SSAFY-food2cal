<template>
  <v-card
    max-width="344"
    class="mx-auto mt-6"
  >
    <v-list-item>
      <v-list-item-avatar color="grey"></v-list-item-avatar>
      <v-list-item-content>
        <!-- <v-list-item-title class="headline">Our Changing Planet</v-list-item-title> -->
        <v-list-item-subtitle>by Kurt Wagner</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <!-- <v-img
      :src="post.diet_image_path"
      :style="{ backgroundImage: 'url( '+ require('../../assets/img/MAATKKUN.png') +' )' }"
      height="194"
    ></v-img> -->

    <v-img
      :src="post.diet_image_path"
      :style="{ backgroundImage: 'url(https://cdn.vuetifyjs.com/images/cards/sunshine.jpg)' }"
      height="194"
    ></v-img>



    <v-card-text>
      {{ post.content }}
    </v-card-text>

    <v-card-actions>
      <v-btn
        text
        color="deep-purple accent-4"
      >
        
      </v-btn>
      <v-btn
        text
        color="deep-purple accent-4"
      >
        
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-share-variant</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Card',
  props: {
    post: {
      type: Object
    }
  }
}
</script>