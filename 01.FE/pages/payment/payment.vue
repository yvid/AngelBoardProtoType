<template>
  <div>
    <v-container>
      <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on }">
            <v-container class="pa-4 text-center">
              <v-row class="fill-height" align="center" justify="center">
                <template v-for="(item, i) in items">
                  <v-col :key="i" cols="12" md="4">
                    <v-hover v-slot:default="{ hover }">
                      <v-card
                        :elevation="hover ? 12 : 2"
                        :class="{ 'on-hover': hover }"
                      >
                        <v-card-title class="title white--text">
                          <v-row
                            class="fill-height flex-column"
                            justify="space-between"
                          >
                            <p class="mt-3 subheading text-left">
                              {{ item.title }}
                            </p>
                            <div>
                              <p class="mt-2 body-1 font-weight-bold text-left">
                                {{ item.text }}
                              </p>
                              <p
                                class="mt-3 caption font-weight-medium font-italic text-left"
                              >
                                {{ item.subtext }}
                              </p>
                            </div>
                          </v-row>
                        </v-card-title>
                      </v-card>
                    </v-hover>
                  </v-col>
                </template>
              </v-row>
            </v-container>
            <v-btn color="primary" outlined dark v-on="on">결제하기</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">결제 정보 입력 </span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-select
                      v-model="value"
                      :items="prices"
                      label="이용권 선택*"
                      required
                    ></v-select>
                  </v-col>
                </v-row>
              </v-container>
              <small>결제는 카카오페이로 진행됩니다 {{ message }} </small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="dialog = false"
                >취소</v-btn
              >
              <v-btn color="blue darken-1" text @click="pay">결제</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'Payment',
  data: () => ({
    items: [
      {
        title: '1개월 이용권 / 5,000원',
        text: '기업정보 상세보기 1개월 무제한 이용',
        subtext: `
          결제 시점으로 부터 1개월간 엔젤보드에 등록된 기업의 민감 상세정보를 열람 할 수 있습니다.`
      },
      {
        title: '3개월 이용권 /  10,000원',
        text: '기업정보 상세보기 3개월 무제한 이용',
        subtext: `
          결제 시점으로 부터 3개월간 엔젤보드에 등록된 기업의 민감 상세정보를 열람 할 수 있습니다.`
      },
      {
        title: '6개월 이용권 / 20,000원',
        text: '기업정보 상세보기 6개월 무제한 이용',
        subtext: `
          결제 시점으로 부터 6개월간 엔젤보드에 등록된 기업의 민감 상세정보를 열람 할 수 있습니다.`
      }
    ],
    transparent: 'rgba(255, 255, 255, 0)',
    dialog: false,
    prices: [
      { text: '5,000원 1개월', value: 5000 },
      { text: '10,000원 3개월', value: 10000 },
      { text: '20,000원 6개월', value: 20000 }
    ],
    value: null,
    message: ''
  }),
  computed: {
    payState() {
      return this.$store.state.payState.payment
    }
  },
  watch: {
    payState(newPayState, oldPayState) {
      console.log('Watch New Store payment Value :: ', newPayState)
      console.log('Watch old Store payment Value :: ', oldPayState)

      if (newPayState) {
        this.$router.push({ path: '/payment/paymentDone' })
      }
    }
  },
  methods: {
    pay() {
      if (this.value) {
        const param = { value: this.value }
        this.payProcess(param)
      } else {
        this.message = '( * 결제금액을 선택 해주세요 )'
      }
    },
    payProcess(param) {
      this.$axios
        .post('/api/account/kakaoPay', JSON.stringify(param))
        .then((res) => {
          const payUrl = res.data.next_redirect_pc_url
          this.localSave(this.payPageOpen(payUrl), () =>
            console.err('Local Save Error')
          )
        })
        .catch((e) => {
          console.error('error :: ', e)
        })
    },
    localSave(resolve, reject) {
      const vm = this
      return new Promise(function(resolve, reject) {
        localStorage.setItem('pay', vm.value)
        switch (vm.value) {
          case 5000:
            localStorage.setItem('payProduct', 'a')
            break
          case 10000:
            localStorage.setItem('payProduct', 'b')
            break
          case 20000:
            localStorage.setItem('payProduct', 'c')
            break
          default:
            localStorage.setItem('payProduct', 'e')
            break
        }
      })
    },
    payPageOpen(payUrl) {
      const sample = { name: 'sample' }
      window.data = sample
      window.open(payUrl, 'payPop', 'width=450,height=600,left=600')
    }
  }
}
</script>

<style scoped>
.v-card {
  transition: opacity 0.4s ease-in-out;
  padding: 20px;
}

.v-card:not(.on-hover) {
  opacity: 0.6;
}

.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}
</style>
