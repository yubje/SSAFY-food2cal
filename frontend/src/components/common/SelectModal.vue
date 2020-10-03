<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="370"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          text
          dark
          v-bind="attrs"
          v-on="on"
        >
          Save
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="headline">
          게시글을 등록하시겠습니까?
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false; goToHome()"
          >
            No
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false; goToPostCreate()"
          >
            Yes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import constants from '@/libs/constants'

export default {
  name: 'PostsModal',
  data () {
    return {
      dialog: false
    }
  },
  methods: {
    goToHome() {
      this.$router
        .push('/')
        .catch(err => {
          if(err.name != "NavigationDuplicated" ){
            throw err
          }
        })
    },
    goToPostCreate() {
      this.$router
        .push({ name: constants.URL_TYPE.POST.CREATE, params: { id: 0} })
        .catch(err => {
          if(err.name != "NavigationDuplicated" ){
            throw err
          }
        })
    }
  }
}
</script>