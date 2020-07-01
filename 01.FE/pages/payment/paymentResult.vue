<template>
  <div class="pop">
    <div class="content">
      <h3>결제를 진행 중 입니다.</h3>
      <v-progress-linear indeterminate color="green"></v-progress-linear>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.init()
  },
  methods: {
    init() {
      this.setStore()
        .then((res) => {
          this.closeWindow()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    setStore() {
      /* 
      console.log(process.client) : 클라이언트 상태 확인
      window.parent.__NUXT__.state.payState.payment : 부모창 스토어 확인 X
      window.parent.$nuxt.$root.$store.state.payState.payment : 부모창 스토어 확인 X
      window.opener.parent.$nuxt.$root.$store.state.payState.payment : 부모창 스토어 확인 O
       */
      return new Promise(function(resolve, reject) {
        /* 부모창 스토어 핸들링 */
        resolve(
          window.opener.parent.$nuxt.$root.$store.commit(
            'payState/changePayment'
          )
        )
        resolve(new Error('Store Commit is Falied'))
      })
    },
    closeWindow() {
      window.opener.parent.$nuxt.$root.$store.commit('payState/changePayment')
      window.close()
    }
  }
}
</script>

<style>
.pop {
  background: #f7e600;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  z-index: 100;
}
.content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;
}
</style>
