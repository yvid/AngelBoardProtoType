<template>
  <body>
    <v-row>
      <v-col>
        <div>
          <v-btn class="mt-2" block @click="payTokenGet">
            결제토큰 GET
          </v-btn>
          <v-btn class="mt-2" block @click="payTokenSet">
            결제토큰 SET
          </v-btn>
          <v-btn class="mt-2" block @click="invSerialGet">
            투자관리번호 GET
          </v-btn>
          <v-btn class="mt-2" block @click="getAccountCompSerial">
            휴먼/엔젤 정보 GET
          </v-btn>
        </div>
      </v-col>
      <v-col>
        <div>
          <p>GET Store Token State: {{ token }}</p>
          <p>Computed Token State: {{ tokenStateValue }}</p>
          <p>GET Investment Serial No: {{ invSerial }}</p>
          <p>GET accountInfo: {{ accountInfo }}</p>
        </div>
      </v-col>
    </v-row>

    <v-select
      ref="coDiv"
      v-model="selected"
      :rules="[() => !!selected || '필수 입력!']"
      :items="selectArr"
      label="셀렉트 샘플"
      placeholder="선택..(다중선택 가능)"
      outlined
      multiple
      chips
      required
    >
    </v-select>
    <div>선택된 값: {{ selected }}</div>
  </body>
</template>

<script>
export default {
  data() {
    return {
      selected: null,
      selectArr: [
        { text: '선택01', value: '001' },
        { text: '선택02', value: '002' },
        { text: '선택03', value: '003' }
      ],
      token: true,
      tokenStateValue: null,
      invSerial: null,
      account: {
        emailId: 'xyvidx@gmail.com' /*	이메일id	*/,
        emailPsw: 123123 /*	비밀번호	*/
      },
      accountInfo: {}
    }
  },
  computed: {
    tokenState() {
      return this.$store.state.payOn.payOn
    }
  },
  watch: {
    tokenState(newTokenState, oldTokenState) {
      console.log('watch newTokenState :: ', newTokenState)
      this.tokenStateValue = newTokenState
    }
  },
  methods: {
    payTokenGet() {
      this.token = this.$store.state.payOn.payOn
      console.log('GET Store Pay Token :: ', this.token)
    },
    payTokenSet() {
      this.$store.commit('payOn/changePayment', !this.tokenState)
    },
    invSerialGet() {
      this.$axios
        .post('/api/inv/register')
        .then((res) => {
          this.invSerial = res.data
          console.log('GET Investment Serial :: ', res)
        })
        .catch((error) => console.err(error))
    },
    getAccountCompSerial() {
      this.$axios
        .post('/api/account/getCpny', JSON.stringify(this.account))
        .then((res) => {
          console.log('default 366 res ::', res)
          this.accountInfo = res.data.accountInfo[0]
        })
        .catch((err) => {
          console.error(err)
        })
    }
  }
}
</script>
