<template>
  <div class="complete">
    <h3>이용권 결제가 완료 되었습니다.</h3>
    <v-divider></v-divider>
    <div class="text-center">
      <v-btn class="ma-4" dark color="primary" @click="$router.push('/')"
        >메인 페이지로</v-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'Payment',
  data: () => ({
    dialog: false,
    payment: {}
  }),
  created() {
    const vm = this
    this.payment.emailId = localStorage.getItem('account')
    this.payment.payProduct = localStorage.getItem('payProduct')
    this.payment.pay = localStorage.getItem('pay')

    /* 접속자 정보 수집 (ex..)
     * city: "Yongsan-dong"
     * country: "KR"
     * ip: "119.196.13.124"
     * loc: "37.5016,126.9516"
     * org: "AS4766 Korea Telecom"
     * postal: "06970"
     * readme: "https://ipinfo.io/missingauth"
     * region: "Seoul"
     * timezone: "Asia/Seoul"
     */
    this.$axios
      .get('http://ipinfo.io')
      .then((res) => {
        vm.payment.payIp = res.data.ip
        if (this.payment.pay) this.init()
      })
      .catch((err) => {
        throw err
      })
  },
  methods: {
    popTest() {
      const page = 'http://119.196.13.124:80/payment/paymentResult'
      window.open(page, 'testPop', 'width=450,height=600,left=600')
    },
    init() {
      this.paymentSave()
    },
    paymentSave() {
      this.$axios
        .post('/api/account/payment', JSON.stringify(this.payment))
        .then((res) => {
          this.removeHistory()
        })
        .catch((err) => {
          console.error(err)
        })
    },
    removeHistory() {
      localStorage.removeItem('pay')
      localStorage.removeItem('payProduct')
      this.storeSet()
    },
    storeSet() {
      this.$store.commit('payOn/changePayment', true)
    }
  }
}
</script>

<style>
.complete {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
