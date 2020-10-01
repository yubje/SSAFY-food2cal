<template>
  <v-card
    class="mx-auto mt-7"
    max-width="370"
  >
    <v-img
      :style="{ backgroundImage: 'url(https://cdn.vuetifyjs.com/images/cards/sunshine.jpg)' }"
      height="200px"
    ></v-img>

    <v-card-title>
      Top western road trips
    </v-card-title>

    <v-card-subtitle>
      1,000 miles of wonder
    </v-card-subtitle>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <!-- <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon> -->
        <v-icon>
          mdi-comment
        </v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          등록된 댓글이 없습니다.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<!-- <v-img
  :src="post.diet_image_path"
  :style="{ backgroundImage: 'url(https://cdn.vuetifyjs.com/images/cards/sunshine.jpg)' }"
  height="194"
></v-img> -->

<script>
  export default {
    name: 'PostsCard',
    props: {
      post: {
        type: Object
      }
    },
    data () {
      return {
        show: false
      }
    }
  }
</script>