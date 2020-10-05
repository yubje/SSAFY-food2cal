<template>
  <v-card
    class="mx-auto mt-7"
    max-width="370"
  >
    <v-card-title class="pb-0">
      <div class="d-flex align-center">
        <v-icon>{{ category.icon }}</v-icon>
        <p class="ml-3 mb-0">{{ category.time }}</p>
      </div>
    </v-card-title>

    <v-card-actions>
      <v-btn text></v-btn>

      <v-btn
        color="purple"
        text
      >
        
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          food
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      show: false,
    }),
    props: {
      category: {
        type: Object
      }
    }
  }
</script>