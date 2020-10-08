<template>
  <v-row class="mx-auto fill-height">
    <Loading v-if="isLoading" />
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
        >
          <!-- <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn> -->
          <div class="mx-auto d-flex align-center">
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="prev"
            >
              <v-icon small>
                mdi-chevron-left
              </v-icon>
            </v-btn>
            
            <v-toolbar-title v-if="$refs.calendar" @click="type = 'month'">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <!-- <v-toolbar-title v-else>
              {{ title }}
            </v-toolbar-title> -->

            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click.prevent="next"
            >
              <v-icon small>
                mdi-chevron-right
              </v-icon>
            </v-btn>
          </div>
          
          <!-- <v-menu
            bottom
            right
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                outlined
                color="grey darken-2"
                v-bind="attrs"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>
                  mdi-menu-down
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = '4day'">
                <v-list-item-title>4 days</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu> -->
        </v-toolbar>
      </v-sheet>
      <v-sheet height="400">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :type="type"
          :events="events"
          :event-color="getEventColor"
          @click:date="sendDate"
        ></v-calendar>
        
        
        <!-- @change="updateRange" :events="events" :event-color="getEventColor" @click:event="showEvent" @click:more="viewDay" @click:date="viewDay"-->
        <!-- <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent.details"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu> -->
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
// import SERVER from '@/libs/api'
import { mapState, mapActions } from 'vuex'
import Loading from '@/components/common/Loading'

export default {
  data: () => ({
    focus: '',
    type: 'month',
    typeToLabel: {
      month: 'Month',
      day: 'Day',
    },
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    title: null,
    isLoading: false,
    events: [
      {
        name: 'Sucess',
        start: '2020-10-07',
        color: 'green'
      },
      {
        name: 'Fail',
        start: '2020-10-06',
        color: 'red'
      }
    ],
  }),
  created () {
    this.isLoading = true
    setTimeout(() => {
      this.isLoading = false
    }, 1)
  },
  mounted () {
    this.$refs.calendar.checkChange()
    setTimeout(() => {
      this.title = this.$refs.calendar.title
      const yearMon = this.setYearMon(this.$refs.calendar.title)
      this.getMonthDiets(yearMon)
    }, 10)
    this.setCalendarEvent()
  },
  updated() {
    
  },
  computed: {
    ...mapState([
      'dietMonthInfo'
    ]),
    setTitle() {
      return this.$refs.calendar.title
    }
  },
  components: {
    Loading
  },
  methods: {
    ...mapActions([
      'getMonthDiets'
    ]),
    // viewDay({ date }) {
    //   this.focus = date
    //   this.type = 'day'
    // },
    getEventColor (event) {
      return event.color
    },
    // setToday() {
    //   this.focus = ''
    // },
    setYearMon(title) {
      const date = title.split(' ')
      let year = +date[1]
      let month = +date[0].slice(0, -1)
      month = month >= 10 ? month: '0' + month
      const yearMon = year + '-' + month
      return yearMon
    },
    prev() {
      this.$refs.calendar.prev()
      setTimeout(() => {
        const yearMon = this.setYearMon(this.$refs.calendar.title)
        this.getMonthDiets(yearMon)
      }, 10)
    },
    next() {
      this.$refs.calendar.next()
      setTimeout(() => {
        const yearMon = this.setYearMon(this.$refs.calendar.title)
        this.getMonthDiets(yearMon)
      }, 10)
    },
    sendDate() {
      setTimeout(() => {
        const arr = this.dietMonthInfo
        const date = this.$refs.calendar.value
        this.$emit('date', date)
        // this.$emit('food-info', arr[date])
        this.$emit('food-info', arr)
      }, 10)
    },
    setCalendarEvent() {
      const arr = Object.keys(this.dietMonthInfo)
      // const daily = window.sessionStorage.getItem('standard')
      const daily = 1800
      const events = []
      arr.forEach(el => {
        if (this.dietMonthInfo[el].calorie > daily) {
          events.push(
            {
              name: 'Fail',
              start: el,
              color: 'red'
            },
          )
        } else {
          events.push(
            {
              name: 'Sucess',
              start: el,
              color: 'green'
            },
          )
        }
      })
      this.events = events
    }
    // getMonthDiets() {
    //   const config = {
    //     headers: {
    //       Authorization: `Token ${this.$cookies.get(`auth-token`)}`
    //     }
    //   }
      
    //   const date = this.$refs.calendar.title.split(' ')
    //   let year = +date[1]
    //   let month = +date[0].slice(0, -1)
    //   month = month >= 10 ? month: '0' + month
    //   const yearMon = year + '-' + month

    //   this.$http.get(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.diets + `${yearMon}/`, config)
    //     .then(res => {
    //       this.dietMonthInfo = res.data
    //       // setTimeout(() => {
    //       //   this.getMonthDiets()
    //       // }, 10)
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },

    // showEvent ({ nativeEvent, event }) {
    //   const open = () => {
    //     this.selectedEvent = event
    //     this.selectedElement = nativeEvent.target
    //     setTimeout(() => {
    //       this.selectedOpen = true
    //     }, 10)
    //   }

    //   if (this.selectedOpen) {
    //     this.selectedOpen = false
    //     setTimeout(open, 10)
    //   } else {
    //     open()
    //   }

    //   nativeEvent.stopPropagation()
    // },


    // updateRange ({ start, end }) {
    //   const events = []

    //   const min = new Date(`${start.date}T00:00:00`)
    //   const max = new Date(`${end.date}T23:59:59`)
    //   const days = (max.getTime() - min.getTime()) / 86400000
    //   const eventCount = this.rnd(days, days + 20)

    //   for (let i = 0; i < eventCount; i++) {
    //     const allDay = this.rnd(0, 3) === 0
    //     const firstTimestamp = this.rnd(min.getTime(), max.getTime())
    //     const first = new Date(firstTimestamp - (firstTimestamp % 900000))
    //     const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
    //     const second = new Date(first.getTime() + secondTimestamp)

    //     events.push({
    //       name: this.names[this.rnd(0, this.names.length - 1)],
    //       start: first,
    //       end: second,
    //       color: this.colors[this.rnd(0, this.colors.length - 1)],
    //       timed: !allDay,
    //     })
    //   }

    //   this.events = events
    // },
    // rnd (a, b) {
    //   return Math.floor((b - a + 1) * Math.random()) + a
    // },
  },
}
</script>