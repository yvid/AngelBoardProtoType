<template>
  <body>
    <div class="complete">
      <v-card outlined>
        <v-card-text v-if="!exist">
          <div class="mb-7">| 엔젤보드 투자연결</div>
          <div v-if="inveParams.invType === 'h0'" class="text-center">
            <p class="display-1 text--primary mb-7">
              "투자사 {{ angel.coNameKor }}에 투자유치를 신청하시겠습니까?"
            </p>
          </div>

          <div v-if="inveParams.invType === 'a0'" class="text-center">
            <p class="display-1 text--primary mb-7">
              {{ human.coNameKor }}에 투자를 제안하시겠습니까?
            </p>
          </div>

          <div class="d-flex justify-center mb-7">
            투자 제안 및 신청 약관<br /><br />
            # 본 제안 및 신청은 엔젤보드가 중계 합니다.<br />
            # 투자 제안 및 신청 업체는 엔젤보드 담당자가 배정되며<br />
            # 요청 드리는 추가 자료를 제출 및 검토 후 오프라인 미팅으로
            진행됩니다.<br />
            # 엔젤보드는 본 투자계약의 자문 역할을 수행 할 수 있습니다.<br />
            # 위 약관에 동의 하시면 약관 동의 버튼을 눌러 주세요
          </div>

          <div class="d-flex justify-end">
            <v-btn
              v-if="!agreementTerms"
              color="light-blue darken-3"
              class="ma-2"
              @click="agreementTerms = !agreementTerms"
            >
              약관 동의
            </v-btn>
            <v-btn
              v-if="agreementTerms"
              color="teal"
              class="ma-2"
              @click="setInv(inveParams.invType)"
            >
              신청하기
            </v-btn>
            <v-btn color="grey darken-2" class="ma-2" @click="$router.go(-1)">
              취소
            </v-btn>
          </div>
        </v-card-text>

        <v-card-text v-if="exist">
          <div class="mb-7">| 엔젤보드 투자연결</div>
          <div class="text-center">
            <h2 class="mb-7">
              {{ message }}
            </h2>
            <h3>
              (잠시 후 페이지가 이동 됩니다.)
            </h3>
          </div>

          <div class="d-flex justify-end">
            <v-btn color="grey darken-2" class="ma-2" @click="$router.go(-1)">
              뒤로가기
            </v-btn>
          </div>
        </v-card-text>
      </v-card>
    </div>

    <div>ANGEL => {{ angel }}</div>
    <div>HUMAN => {{ human }}</div>
    <div>Investment => {{ inveParams }}</div>
  </body>
</template>

<script>
export default {
  data() {
    return {
      angel: null,
      human: null,
      inveParams: {},
      agreementTerms: false,
      exist: false,
      message: null
    }
  },
  created() {
    this.human = this.$route.query.human
    this.angel = this.$route.query.angel
    this.inveParams.invType = this.$route.query.invType
  },
  methods: {
    setInv(val) {
      if (!this.angel) {
        this.message = `잘못된 접근 입니다.`
        this.exist = true

        setTimeout(() => {
          this.$router.push({ path: '/human/humanList' })
        }, 2500)
        return
      }

      if (val === 'a0') {
        this.inveParams.invAserial = this.angel.accountCo
        this.inveParams.invHserial = this.human.hSerial
      }

      if (val === 'h0') {
        this.inveParams.invAserial = this.angel.aSerial
        this.inveParams.invHserial = this.human.accountCo
      }

      this.processInv(this.inveParams)
    },
    processInv(params) {
      this.$axios
        .post('/api/inv/register', JSON.stringify(params))
        .then((res) => {
          this.callbackInv(res.data)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    callbackInv(res) {
      if (res.includes('exist')) {
        this.message =
          '해당 기업에 이미 투자 제안 또는 신청이 등록되어 있습니다.'
        this.exist = true
      }

      if (res.includes('completed')) {
        this.message = `요청하신 투자 제안 또는 신청이 등록되었습니다.`
        this.exist = true
      }

      setTimeout(() => {
        this.$router.push({ path: '/investment/invList' })
      }, 2500)
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
