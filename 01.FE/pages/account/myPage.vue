<template>
  <div>
    <div class="text-center">
      <img src="/angel_logo.png" alt="Vuetify.js" class="mb-5" />
    </div>
    <v-layout justify-center>
      <v-flex xs12 sm10 md8 lg6>
        <v-card ref="form">
          <!-- 텍스트 수 표시 할 때 사용
        <v-card-text>
          <v-text-field
            ref="address"
            v-model="address"
            :rules="[
              () => !!address || 'This field is required',
              () =>
                (!!address && address.length <= 25) ||
                'Address must be less than 25 characters',
              addressCheck
            ]"
            label="Address Line"
            placeholder="Snowy Rock Pl"
            counter="25"
            required
          ></v-text-field>
        </v-card-text>
        -->
          <v-card-text>
            <p>가입일 : {{ account.regDate }}</p>
            <v-text-field
              ref="emailId"
              v-model="account.emailId"
              :rules="[() => !!account.emailId || 'This field is required']"
              label="e-mail"
              required
              disabled
            ></v-text-field>
            <v-text-field
              ref="emailPsw"
              v-model="account.emailPsw"
              :append-icon="show1 ? 'visibility' : 'visibility_off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-2"
              label="비밀번호 (최소 6자리)"
              hint="At least 6 characters"
              value="wqfasds"
              class="input-group--focused"
              @click:append="show1 = !show1"
            ></v-text-field>
            <v-text-field
              ref="emailPswConfirm"
              v-model="account.emailPswConfirm"
              :append-icon="show2 ? 'visibility' : 'visibility_off'"
              :rules="[rules.required, rules.min]"
              :type="show2 ? 'text' : 'password'"
              :error-messages="pswErrorMessages"
              name="input-10-2"
              label="비밀번호 확인"
              hint="At least 6 characters"
              value="wqfasds"
              class="input-group--focused"
              @click:append="show2 = !show2"
              @blur="validPassword"
            ></v-text-field>
            <v-text-field
              ref="name"
              v-model="account.name"
              :rules="[() => !!account.name || 'This field is required']"
              :error-messages="errorMessages"
              label="이름"
              disabled
              required
            ></v-text-field>
            <v-text-field
              ref="nickName"
              v-model="account.nickName"
              :rules="[() => !!account.nickName || 'This field is required']"
              :error-messages="errorMessages"
              label="닉네임"
              required
            ></v-text-field>
            <v-text-field
              ref="belong"
              v-model="account.belong"
              :rules="[() => !!account.belong || 'This field is required']"
              :error-messages="errorMessages"
              label="소속 회사명"
              placeholder="Company Name"
              required
            ></v-text-field>
            <v-text-field
              ref="rank"
              v-model="account.rank"
              :rules="[() => !!account.rank || 'This field is required']"
              :error-messages="errorMessages"
              label="직위"
              placeholder="Rank"
              required
            ></v-text-field>

            <v-row class="d-flex align-baseline" no-gutters>
              <v-col cols="3"><h4>가입 유형</h4></v-col>
              <v-col
                ><v-select
                  ref="accountType"
                  v-model="account.accountType"
                  :rules="[
                    () => !!account.accountType || 'This field is required'
                  ]"
                  :items="accountType"
                  label="가입 유형"
                  placeholder="선택.."
                  required
                  solo
                ></v-select
              ></v-col>
            </v-row>

            <v-row
              v-if="account.accountType === '01'"
              no-gutters
              class="d-flex align-baseline"
            >
              <v-col cols="3"><h4>관심업체 분야</h4></v-col>
              <v-col
                ><v-select
                  ref="accountFCo"
                  v-model="account.accountFCo"
                  :rules="[
                    () => !!account.accountFCo || 'This field is required'
                  ]"
                  :items="largeField"
                  label="나의 관심업체 분야"
                  placeholder="선택.."
                  required
                  solo
                ></v-select
              ></v-col>
            </v-row>

            <v-row
              v-if="account.accountType === '02'"
              no-gutters
              class="d-flex align-baseline"
            >
              <v-col cols="3"><h4>희망 투자유형</h4></v-col>
              <v-col
                ><v-select
                  ref="accountFCo"
                  v-model="account.accountFCo"
                  :rules="[
                    () => !!account.accountFCo || 'This field is required'
                  ]"
                  :items="invCompType"
                  label="나의 관심 투자유치 유형"
                  placeholder="선택.."
                  required
                  solo
                ></v-select
              ></v-col>
            </v-row>

            <v-row
              v-if="account.accountType === '02'"
              no-gutters
              class="d-flex align-baseline"
            >
              <v-col cols="3"><h4>희망 융합기술</h4></v-col>
              <v-col
                ><v-select
                  ref="accountFTech"
                  v-model="account.accountFTech"
                  :rules="[
                    () => !!account.accountFTech || 'This field is required'
                  ]"
                  :items="tech"
                  label="나의 관심 융합기술"
                  placeholder="선택.."
                  required
                  solo
                ></v-select
              ></v-col>
            </v-row>

            <v-switch
              v-model="account.newsRx"
              class="ma-2"
              :label="`뉴스레터 수신 : ${newsRxVal}`"
            ></v-switch>
          </v-card-text>
          <v-divider class="mt-5"></v-divider>
          <v-card-actions>
            <v-btn nuxt to="/inspire">취소</v-btn>
            <v-spacer></v-spacer>
            <v-slide-x-reverse-transition>
              <v-tooltip v-if="formHasErrors" left>
                <template v-slot:activator="{ on }">
                  <v-btn icon class="my-0" @click="resetForm" v-on="on">
                    <v-icon>초기화</v-icon>
                  </v-btn>
                </template>
                <span>Refresh form</span>
              </v-tooltip>
            </v-slide-x-reverse-transition>
            <v-btn color="success" @click="submit">수정</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>

    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline"
          >회원정보 수정이 완료되었습니다.</v-card-title
        >

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog = false">
            돌아가기
          </v-btn>

          <v-btn color="primary" nuxt to="/inspire">
            메인으로
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import country from '~/pages/sample/country'
import category from '~/pages/sample/category'

export default {
  data: () => ({
    countries: [],
    genOpt: ['Male', 'Female'],
    errorMessages: '',
    pswErrorMessages: '',
    formHasErrors: false,
    remote: null,
    account: {
      emailId: null /*	이메일id	*/,
      emailPsw: null /*	비밀번호	*/,
      emailPswConfirm: null /*	비밀번호 확인	*/,
      name: null /*	이름	*/,
      nickName: null /*	닉네임	*/,
      belong: null /*	소속	*/,
      rank: null /*	직위	*/,
      status: null /*	상태	*/,
      regDate: null /*	등록일시	*/,
      latelyDate: null /*	최근접속일	*/,
      regIP: null /*	등록시 접속 ip	*/,

      accountType: '01' /* 가입 유형 */,
      accountCo: null /* 나의 등록 업체 */,
      accountFCo: null /* 투자자: 관심업체 분야, * 투자 유치자: 희망 투자 유형 */,
      accountFTech: null /* 희망 융합 기술 */,
      newsRx: true /* 뉴스레터 알림 */
    },
    newsRx: '네',
    show1: false,
    show2: false,
    rules: {
      required: (value) => !!value || 'Required.',
      min: (value) =>
        (value != null && value.length >= 6) || 'Min 6 characters',
      emailMatch: () => "The email and password you entered don't match"
    },
    dialog: false,
    accountType: null,
    largeField: null,
    invCompType: null,
    tech: null
  }),

  computed: {
    form() {
      return {
        emailId: this.account.emailId,
        emailPsw: this.account.emailPsw,
        emailPswConfirm: this.account.emailPswConfirm,
        name: this.account.name,
        nickName: this.account.nickName
      }
    },
    newsRxVal() {
      return this.account.newsRx ? '네' : '아니오'
    }
  },

  watch: {
    name() {
      this.errorMessages = ''
    }
  },
  created() {
    /* 국가 select 데이터 바인딩 */
    this.countries = country.countries

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
        this.remote = res.data
      })
      .catch((err) => {
        throw err
      })

    /* 현재 날짜, 시간 MySQL형식으로 변수에 대입 */
    const d = new Date()
      .toISOString()
      .slice(0, 19)
      .replace('T', ' ')
    this.account.latelyDate = d
    this.account.regDate = d
    this.accountType = category.accountType
    this.largeField = category.largeField
    this.invCompType = category.invCompType
    this.tech = category.tech
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      this.account.emailId = localStorage.getItem('account')
      this.$axios
        .post('/api/account/myPage', JSON.stringify(this.account))
        .then((res) => {
          console.log(res)

          this.account = res.data[0][0]
          this.account.emailPswConfirm = res.data[0][0].emailPsw
          this.account.regDate = this.unixTimeFilter(this.account.regDate)
          this.account.latelyDate = this.unixTimeFilter(this.account.latelyDate)
        })
        .catch((err) => {
          throw err
        })
    },
    addressCheck() {
      this.errorMessages =
        this.address && !this.account.name ? "I'm required" : ''
      return true
    },
    resetForm() {
      this.errorMessages = []
      this.formHasErrors = false

      Object.keys(this.form).forEach((f) => {
        this.$refs[f].reset()
      })
    },
    submit() {
      /* 접속정보 변수에 대입 */
      if (!this.validPassword()) return
      if (this.remote.ip) this.account.modyIP = this.remote.ip

      this.formHasErrors = false

      for (const f in this.form) {
        if (!this.form[f]) return
      }

      this.submintProcess()
    },
    submintProcess() {
      this.$axios
        .post('/api/account/updater', JSON.stringify(this.account))
        .then((res) => {
          this.dialog = !this.dialog
        })
        .catch((err) => {
          throw err
        })
    },
    validPassword() {
      /* 비밀번호 입력 유효성 확인 */
      if (this.account.emailPswConfirm !== this.account.emailPsw) {
        this.pswErrorMessages = 'Password Does not match !'
        this.account.emailPswConfirm = ''
        return false
      } else {
        this.pswErrorMessages = ''
        return true
      }
    },
    unixTimeFilter(val) {
      const date = new Date(val + 1000)
        .toISOString()
        .slice(0, 19)
        .replace('T', ' ')
      return date.substring(0, 10)
    }
  }
}
</script>
