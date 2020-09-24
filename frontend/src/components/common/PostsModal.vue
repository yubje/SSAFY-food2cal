<template>
  <v-row justify="center" class="mx-0">
    <v-dialog v-model="dialog" persistent class="m-0" max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#F84A0D"
          text
          large
          v-bind="attrs"
          v-on="on"
        >
          Submit
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Regist Your Diet</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Title*" required v-model="title"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Content*" v-model="content"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-select
                  :items="['아침', '점심', '저녁', '간식/기타']"
                  label="Category*"
                  required
                  v-model="category"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click.prevent="dialog = false; createPost();">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'PostsModal',
  data: () => ({
    dialog: false,
    title: null,
    content: null,
    category: null,
    diet_image_path: null
  }),
  computed: {
    ...mapState([
      'fileUrl',
      'foodInfo'
    ])
  },
  methods: {
    createPost() {
      const config = {
        headers: {
          Authorization: `jwt ${this.$cookies.get(`auth-token`)}`
        }
      }
      const postData = {
        post: {
          title: this.title,
          content: this.content,
          category: 'LU',
          diet_image_path: this.fileUrl
        },
        diet: {
          diet_image_path: this.fileUrl
        },
        food: [
          {
            food_name: this.foodInfo.food_name,
            amount: this.foodInfo.ammount,
            calorie: this.foodInfo.calorie,
            carbohydrate: this.foodInfo.carbohydrate,
            protein: this.foodInfo.protein,
            fat: this.foodInfo.fat
          }
        ]
      }
      this.$http
        .post(process.env.VUE_APP_SERVER_URL + 'posts/', postData, config)
        .then(res => {
          console.log(res.data)
        })
        .catch(err => console.log(err.response.data))
    }
  }
}
</script>