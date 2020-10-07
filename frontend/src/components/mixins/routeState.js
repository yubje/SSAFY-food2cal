import constants from '@/libs/constants'

export const routeState = {
  methods: {
    goToLogin() {
      this.$router
        .push({ name: constants.URL_TYPE.USER.LOGIN })
        .catch(err => {
          if(err.name != "NavigationDuplicated" ) throw err
        })
    },
  }
}