<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-dialog v-model="dialog" width="400">
        <v-card>
          <v-card-title class="headline grey lighten-1" primary-title>
            Log in
          </v-card-title>

          <div style="margin: 15px;">
            <v-text-field
              v-model="account.emailId"
              label="e-mail"
              :rules="[rules.required]"
              hide-details="auto"
            ></v-text-field>
            <v-text-field
              v-model="account.emailPsw"
              label="Password"
              :rules="[rules.required, rules.min]"
              :error-messages="errorMessages"
              :append-icon="show ? 'visibility' : 'visibility_off'"
              :type="show ? 'text' : 'password'"
              @click:append="show = !show"
            >
            </v-text-field>
          </div>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="dialog = false">
              취소
            </v-btn>
            <v-btn color="primary" @click="login">
              로그인
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-if="userLogin && !adminOn && userType === 'A01'">
        <v-list-item
          v-for="item in angelRegdCpny"
          :key="item.title"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-if="userLogin && !adminOn && userType === 'A02'">
        <v-list-item
          v-for="item in angelNoRegdCpny"
          :key="item.title"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-if="userLogin && !adminOn && userType === 'H01'">
        <v-list-item
          v-for="item in humanRegdCpny"
          :key="item.title"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-if="userLogin && !adminOn && userType === 'H02'">
        <v-list-item
          v-for="item in humanNoRegdCpny"
          :key="item.title"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-if="!userLogin">
        <v-list-item
          v-for="(item, i) in guests"
          :key="item.title + i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-if="adminOn && userLogin">
        <v-list-item
          v-for="item in admin"
          :key="item.title"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <!-- 
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      -->
      <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>mdi-application</v-icon>
      </v-btn>
      <!-- 기능 확인 불가
      <v-btn icon @click.stop="fixed = !fixed">
        <v-icon>mdi-minus</v-icon>
      </v-btn>
       -->
      <v-toolbar-title
        style="cursor: pointer"
        @click="$router.push('/')"
        v-text="title"
      />
      <v-spacer />

      <v-card-actions>
        <div v-if="!userLogin" class="text-center">
          <v-btn class="ma-2" @click="dialog = !dialog">
            로그인
          </v-btn>

          <v-btn color="primary" nuxt to="/account/registAccount">
            회원가입
          </v-btn>
        </div>
        <div v-if="userLogin" class="text-center d-flex flex-row align-center">
          <v-avatar color="indigo" size="36">
            <v-icon dark>mdi-account-circle</v-icon>
          </v-avatar>

          <h5 class="ml-2">{{ account.emailId }} 님 로그인</h5>

          <v-btn class="ma-2" @click="logout">
            로그아웃
          </v-btn>

          <v-btn color="primary" nuxt to="/account/myPage">
            마이페이지
          </v-btn>
        </div>
      </v-card-actions>

      <!-- 우측메뉴 활성버튼
      <v-btn icon @click.stop="rightDrawer = !rightDrawer">
        <v-icon>mdi-menu</v-icon>
      </v-btn>
       -->
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <!-- 우측메뉴
    <v-navigation-drawer v-model="rightDrawer" :right="right" temporary fixed>
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light>
              mdi-repeat
            </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
     -->
    <v-footer :fixed="fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import {
  mdiClipboardText,
  mdiClipboardTextMultiple,
  mdiClipboardTextOutline,
  mdiClipboardTextMultipleOutline,
  mdiFileDocumentEdit,
  mdiFileDocumentEditOutline,
  mdiCreditCardMultiple,
  mdiSprout
} from '@mdi/js'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'

export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Main',
          to: '/'
        }
      ],
      admin: [
        {
          icon: mdiClipboardText,
          title: '투자사 등록',
          to: '/angel/angel'
        },
        {
          icon: mdiClipboardTextMultiple,
          title: '투자사 목록',
          to: '/angel/angelList'
        },

        {
          icon: mdiClipboardTextOutline,
          title: '투자유치사 등록',
          to: '/human/human'
        },
        {
          icon: mdiClipboardTextMultipleOutline,
          title: '투자유치사 목록',
          to: '/human/humanList'
        },
        {
          icon: mdiCreditCardMultiple,
          title: '결제 상품',
          to: '/payment/payment'
        },
        {
          icon: 'mdi-chart-bubble',
          title: '투자사 상세',
          to: '/angel/angelView'
        },
        {
          icon: 'mdi-chart-bubble',
          title: '투자유치사 상세',
          to: '/human/humanView'
        },
        {
          icon: 'mdi-chart-bubble',
          title: '투자 연결',
          to: '/investment/invReg'
        },
        {
          icon: mdiSprout,
          title: '투자 현황',
          to: '/investment/invList'
        },
        {
          icon: 'mdi-chart-bubble',
          title: '결제 완료',
          to: '/payment/paymentDone'
        },
        {
          icon: 'mdi-chart-bubble',
          title: '테스트',
          to: '/sample/test'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Chart1',
          to: '/sample/chart1'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Chart2',
          to: '/sample/chart2'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Chart3',
          to: '/sample/chart3'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Chart4',
          to: '/sample/chart4'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Sparkline',
          to: '/sample/sparkline'
        }
      ],
      guests: [
        {
          icon: mdiClipboardTextMultiple,
          title: '투자사 목록',
          to: '/angel/angelList'
        },
        {
          icon: mdiClipboardTextMultipleOutline,
          title: '투자유치사 목록',
          to: '/human/humanList'
        }
      ],
      angelRegdCpny: [
        {
          icon: mdiFileDocumentEdit,
          title: '나의 기업정보',
          to: '/angel/angel'
        },
        {
          icon: mdiClipboardTextMultiple,
          title: '투자사 목록',
          to: '/angel/angelList'
        },
        {
          icon: mdiClipboardTextMultipleOutline,
          title: '투자유치사 목록',
          to: '/human/humanList'
        },
        {
          icon: mdiSprout,
          title: '투자 현황',
          to: '/investment/invList'
        },
        {
          icon: mdiCreditCardMultiple,
          title: '결제 상품',
          to: '/payment/payment'
        }
      ],
      angelNoRegdCpny: [
        {
          icon: mdiClipboardText,
          title: '나의 기업정보 등록',
          to: '/angel/angel'
        },
        {
          icon: mdiClipboardTextMultiple,
          title: '투자사 목록',
          to: '/angel/angelList'
        },
        {
          icon: mdiClipboardTextMultipleOutline,
          title: '투자유치사 목록',
          to: '/human/humanList'
        },
        {
          icon: mdiCreditCardMultiple,
          title: '결제 상품',
          to: '/payment/payment'
        }
      ],
      humanRegdCpny: [
        {
          icon: mdiFileDocumentEditOutline,
          title: '나의 기업정보',
          to: '/human/human'
        },
        {
          icon: mdiClipboardTextMultiple,
          title: '투자사 목록',
          to: '/angel/angelList'
        },
        {
          icon: mdiClipboardTextMultipleOutline,
          title: '투자유치사 목록',
          to: '/human/humanList'
        },
        {
          icon: mdiSprout,
          title: '투자 현황',
          to: '/investment/invList'
        },
        {
          icon: mdiCreditCardMultiple,
          title: '결제 상품',
          to: '/payment/payment'
        }
      ],
      humanNoRegdCpny: [
        {
          icon: mdiClipboardTextOutline,
          title: '나의 기업정보 등록',
          to: '/human/human'
        },
        {
          icon: mdiClipboardTextMultiple,
          title: '투자사 목록',
          to: '/angel/angelList'
        },
        {
          icon: mdiClipboardTextMultipleOutline,
          title: '투자유치사 목록',
          to: '/human/humanList'
        },
        {
          icon: mdiCreditCardMultiple,
          title: '결제 상품',
          to: '/payment/payment'
        }
      ],
      show: false,
      errorMessages: '',
      account: {
        emailId: null /*	이메일id	*/,
        emailPsw: null /*	비밀번호	*/
      },
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'ANGEL BOARD',
      dialog: false,
      userLogin: false,
      userType: null,
      rules: {
        required: (value) => !!value || 'Required.',
        min: (value) =>
          (value != null && value.length >= 6) || 'Min 6 characters'
      },
      isCooKie: false,
      adminOn: false
    }
  },

  computed: {
    form() {
      return {
        emailId: this.account.emailId,
        emailPsw: this.account.emailPsw
      }
    },
    storeUserType() {
      return this.$store.state.userType.userType
    }
  },
  watch: {
    storeUserType(newVal, oldVal) {
      console.log('userType Change')
      this.userType = newVal
    }
  },
  mounted() {
    /* 
      console.log('로컬스토리지 값 확인 :: ', Object.entries(localStorage))    
    */

    if (localStorage.getItem('account') !== null) {
      this.userLogin = true
      this.account.emailId = localStorage.getItem('account')
      this.adminOn = !!(localStorage.getItem('account') === 'admin')
    }
    if (!this.adminOn) {
      this.setLeftMenu(JSON.parse(localStorage.getItem('accountInfo')))
    }
    if (localStorage.getItem('payInfo') !== null) {
      const payInfo = JSON.parse(localStorage.getItem('payInfo'))
      this.setPayOn(payInfo.payOn)
    }
  },
  methods: {
    login() {
      if (this.adminLogin()) {
        this.adminLoginCallback()
      } else if (this.checkEmail(this.account.emailId)) {
        this.loginProcess()
      } else {
        this.errorMessages = '아이디를 확인해주세요'
      }
    },
    adminLogin() {
      let val = false
      val = !!(
        this.account.emailId === 'admin' && this.account.emailPsw === '123123'
      )
      return val
    },
    adminLoginCallback() {
      this.adminOn = true
      const accountInfo = {
        emailIdF: 'admin',
        accountType: '00',
        accountCo: 'UnQ0NWHnwL67mlO'
      }
      localStorage.setItem('account', this.account.emailId)
      localStorage.setItem('accountInfo', JSON.stringify(accountInfo))
      this.setPayOn(true)
      this.dialog = false
      this.userLogin = true
    },
    logout() {
      localStorage.removeItem('account')
      localStorage.removeItem('accountInfo')
      localStorage.removeItem('payInfo')
      this.adminOn = false
      this.setPayOn(false)
      this.userLogin = false
      this.$router.push({ path: '/' })
    },
    loginProcess() {
      /* res.data: 
        e0: 없는 계정
        e1: 있는 계정, 비밀번호 오류
        s1: 로그인 성공
      */
      this.$axios
        .post('/api/account/login', JSON.stringify(this.account))
        .then((res) => {
          const _LOGIN = res.data.res
          let payInfo = {}
          /* 
            결제 정보
            payExp: 결제만료일
            payDate: 결제일
            paidProduc: 결제상품
            payOn: 결제상품상태
          */
          if (res.data.payProduct) {
            const payDate = new Date(res.data.payDate)
              .toISOString()
              .substring(0, 10)
            const payExp = new Date(res.data.payExp)
              .toISOString()
              .substring(0, 10)
            const today = new Date().toISOString().substring(0, 10)
            const paidProduct = res.data.payProduct
            const payOn = payExp >= today

            this.setPayOn(payOn)

            payInfo = {
              payExp,
              payDate,
              paidProduct,
              payOn
            }
          }

          switch (_LOGIN) {
            case 'e0':
              this.errorMessages = '아이디를 확인해주세요'
              break
            case 'e1':
              this.errorMessages = '비밀번호를 확인해주세요'
              break
            case 's1':
              this.account.payRes = res.data.payRes
              this.errorMessages = ''
              break
            default:
              break
          }

          if (_LOGIN === 's1') {
            this.loginCallback(this.account, payInfo)
          }
        })
        .catch((err) => {
          throw err
        })
    },
    loginCallback(account, payInfo) {
      /* 로그인 계정 로컬스토리지 저장 */
      localStorage.setItem('account', account.emailId)
      /* 로그인 계정 결제정보 로컬스토리지 저장 */
      localStorage.setItem('payInfo', JSON.stringify(payInfo))
      this.getAccountCompSerial()

      this.dialog = false
      this.userLogin = true
    },
    getAccountCompSerial() {
      this.$axios
        .post('/api/account/getCpny', JSON.stringify(this.account))
        .then((res) => {
          localStorage.setItem(
            'accountInfo',
            JSON.stringify(res.data.accountInfo[0])
          )
          this.setLeftMenu(res.data.accountInfo[0])
        })
        .catch((err) => {
          console.error(err)
        })
    },
    setLeftMenu(accountInfo) {
      /* 
        유저타입에 따라 this.userType 변수에 값을 바인딩
        A01: 엔젤(업체정보 있음)
        A02: 엔젤(업체정보 없음)
        H01: 휴먼(업체정보 없음)
        H01: 휴먼(업체정보 있음)
      */
      if (accountInfo === null) return
      if (accountInfo.accountCo !== null) {
        this.userType = accountInfo.accountType === '01' ? 'A01' : 'H01'
      } else {
        this.userType = accountInfo.accountType === '01' ? 'A02' : 'H02'
      }
      console.log(this.userType)
    },
    setPayOn(val) {
      this.$store.commit('payOn/changePayment', val)
    },
    checkEmail(email) {
      /* 이메일 입력 유효성 확인 */
      const exptext = /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
      if (exptext.test(email) === false) {
        // 이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
        return false
      }
      return true
    },
    isEmptyObject(param) {
      return Object.keys(param).length === 0 && param.constructor === Object
    }
  }
}
</script>
