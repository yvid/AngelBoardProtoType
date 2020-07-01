<template>
  <div>
    <!-- axios GET example -->
    <div>
      <v-btn @click="axiosGet">
        axios GET
      </v-btn>
      <span>{{ getResult }}</span>
    </div>

    <!-- axios POST example -->
    <div>
      <v-btn @click="axiosPost">
        axios POST
      </v-btn>
      <span>{{ postResult }}</span>
    </div>
  </div>
</template>

<style lang="sass" scoped></style>

<script>
export default {
  data() {
    return {
      getResult: 'result',
      postResult: 'result'
    }
  },
  methods: {
    axiosGet() {
      this.$axios
        .get('/api/environments/super')
        .then((res) => {
          this.getResult = res.data.language
          console.log('res : ' + res)
        })
        .catch((err) => {
          console.log('err : ' + err)
        })
    },
    axiosPost() {
      this.$axios
        .post('/api/userLogin', { name: 'yyb' })
        .then((res) => {
          this.postResult = res.data
          console.log('res : ' + res)
        })
        .catch((err) => {
          console.log('err : ' + err)
        })
    }
  }
}
</script>
