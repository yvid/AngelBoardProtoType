<template>
  <v-flex lg12 md12 sm12 style="min-width: 1190px">
    <v-row align="center">
      <!-- 
        <div class="text-center d-flex pb-4">
          <v-switch v-if="payOn" v-model="flap" label="전체 펼쳐보기"></v-switch>
        </div>
       -->

      <v-expansion-panels
        v-model="panel"
        :inset="inset"
        :multiple="multiple"
        :focusable="focusable"
        :flat="flat"
        :hover="hover"
      >
        <v-expansion-panel>
          <v-expansion-panel-header
            >기업 정보 (상세 보기 - 클릭)</v-expansion-panel-header
          >
          <v-expansion-panel-content dense>
            <v-row>
              <v-col cols="3">
                <h4>| 기본 정보</h4>
                <div style="margin: 25px;"></div>
                <v-text-field
                  v-model="human.coNameKor"
                  class="caption"
                  label="기업명(한글)"
                  placeholder="한글 기업명"
                  prepend-icon="mdi-city"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.coNameEng"
                  class="caption"
                  label="기업명(영문)"
                  placeholder="영문 기업명"
                  prepend-icon="mdi-city"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.foundedDate"
                  class="caption"
                  label="설립일"
                  placeholder="설립일"
                  prepend-icon="event"
                  dense
                  readonly
                ></v-text-field>

                <v-chip
                  v-for="item in humanDiv"
                  :key="item.coDiv"
                  class="ma-2"
                  color="primary"
                  small
                >
                  {{ item.coDiv | coDivFilter }}
                </v-chip>

                <v-chip class="ma-2" color="green" small>
                  {{ human.corpDiv }}
                </v-chip>
                <div style="margin: 25px;"></div>
                <a
                  style="cursor:pointer"
                  :href="human.coWeblink"
                  target="_blank"
                >
                  <v-text-field
                    v-model="human.coWeb"
                    class="caption"
                    label="웹사이트"
                    placeholder="기업 웹사이트"
                    style="cursor:pointer"
                    prepend-icon="mdi-dialpad"
                    dense
                    readonly
                  >
                  </v-text-field>
                </a>

                <div v-if="human.coLogo !== null" align="center">
                  <img
                    onerror="this.src='/null_logo.png'"
                    :src="human.coLogo"
                    alt="companyLogo"
                    style="max-heght: 120px; max-width: 120px;"
                  />
                </div>

                <v-row>
                  <v-textarea
                    v-model="human.coAddr"
                    class="caption"
                    placeholder="본사 주소"
                    prepend-icon="place"
                    dense
                    readonly
                    rows="2"
                  ></v-textarea>
                </v-row>
              </v-col>

              <v-col cols="3">
                <h4>| 대표자 정보</h4>
                <div style="margin: 25px;"></div>

                <v-text-field
                  v-model="human.representativeNameKor"
                  class="caption"
                  label="대표자명(한글)"
                  placeholder="대표자명(한글)"
                  :prepend-icon="icons.mdiAccount"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.representativeNameEng"
                  class="caption"
                  label="대표자명(영문)"
                  placeholder="대표자명(영문)"
                  :prepend-icon="icons.mdiAccount"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.representativeTel"
                  class="caption"
                  label="대표자 연락처"
                  placeholder="대표자 연락처"
                  :prepend-icon="icons.mdiCellphoneBasic"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.representativeNationality"
                  class="caption"
                  label="대표자 국적"
                  placeholder="대표자 국적"
                  prepend-icon="map"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.representativeGender"
                  class="caption"
                  label="대표자 성별"
                  placeholder="대표자 성별"
                  :prepend-icon="icons.mdiGenderMaleFemale"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-if="
                    human.founderNameKor !== null && human.founderNameKor !== ''
                  "
                  v-model="human.founderNameKor"
                  class="caption"
                  label="설립자명"
                  placeholder="설립자명"
                  :prepend-icon="icons.mdiWhiteBalanceIncandescent"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-if="
                    human.coRepresentativeNameKor !== null &&
                      human.coRepresentativeNameKor !== ''
                  "
                  v-model="human.coRepresentativeNameKor"
                  class="caption"
                  label="공동대표자명"
                  placeholder="공동대표자명"
                  :prepend-icon="icons.mdiAccountMultiple"
                  dense
                  readonly
                ></v-text-field>
              </v-col>

              <v-col v-if="payOn" cols="3">
                <h4>| 상태 정보</h4>
                <div style="margin: 25px;"></div>

                <v-text-field
                  v-model="human.invStage"
                  class="caption"
                  label="현재 투자 단계"
                  placeholder="현재 투자 단계"
                  :prepend-icon="icons.mdiArrangeSendBackward"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.invAttrTargetAmount"
                  class="caption"
                  label="현재 투자 유치 목표금액(억)"
                  placeholder="현재 투자 유치 목표금액(억)"
                  :prepend-icon="icons.mdiCurrencyKrw"
                  suffix="억원"
                  dense
                  readonly
                ></v-text-field>

                <v-textarea
                  v-model="human.problemsToSolve"
                  class="caption"
                  label="풀려고 하는 문제"
                  :prepend-icon="icons.mdiHeadQuestionOutline"
                  dense
                  outlined
                  readonly
                  rows="3"
                ></v-textarea>

                <v-textarea
                  v-model="human.ourSolution"
                  class="caption"
                  label="우리팀의 해결책"
                  :prepend-icon="icons.mdiHeadAlertOutline"
                  dense
                  outlined
                  readonly
                  rows="3"
                ></v-textarea>

                <v-textarea
                  v-model="human.aboutTeam"
                  class="caption"
                  label="팀 - 경력/자원/채널 위주 서술"
                  placeholder="팀 - 경력/자원/채널 위주 서술"
                  :prepend-icon="icons.mdiAccountSupervisor"
                  dense
                  outlined
                  readonly
                  rows="3"
                ></v-textarea>

                <v-text-field
                  v-model="human.numberOfEmp"
                  class="caption"
                  label="종업원수"
                  placeholder="종업원수"
                  :prepend-icon="icons.mdiAccountGroup"
                  suffix="명"
                  dense
                  readonly
                ></v-text-field>
              </v-col>

              <v-col v-if="payOn" cols="3">
                <h4>| 재무 정보</h4>
                <div style="margin: 25px;"></div>
                <v-text-field
                  v-model="human.prevYearSaleVolume"
                  class="caption"
                  label="전년도 매출 규모"
                  placeholder="전년도 매출 규모"
                  :prepend-icon="icons.mdiCurrencyKrw"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.capital"
                  class="caption"
                  label="자본금"
                  placeholder="자본금"
                  :prepend-icon="icons.mdiCurrencyKrw"
                  suffix="원"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.totalAssets"
                  class="caption"
                  label="총자산합계"
                  placeholder="총자산합계"
                  :prepend-icon="icons.mdiCurrencyKrw"
                  suffix="원"
                  dense
                  readonly
                ></v-text-field>

                <v-text-field
                  v-model="human.totalLiabilities"
                  class="caption"
                  label="총부채"
                  placeholder="총부채"
                  :prepend-icon="icons.mdiCurrencyKrw"
                  suffix="원"
                  dense
                  readonly
                ></v-text-field>

                <div class="chart">
                  <component
                    :is="componentIs1"
                    :width="250"
                    :height="250"
                    :chartdata="chartdata1"
                    :options="chartOptions1"
                  />
                </div>
              </v-col>

              <v-col v-show="!payOn" cols="6">
                <div class="message">
                  세부정보는 이용권 구매후 열람가능합니다.
                </div>
              </v-col>

              <v-btn
                v-show="payOn && cpnOn && angel.accountType === '01'"
                block
                color="#0D47A1"
                @click="prcsInvestment()"
              >
                {{ human.coNameKor }}에 투자하기
              </v-btn>

              <v-btn v-show="payOn && !cpnOn" block color="#0D47A1" disabled>
                업체 정보를 등록하시면 {{ human.coNameKor }}에 투자를 제안 할 수
                있습니다.
              </v-btn>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header>기업 아이템 정보</v-expansion-panel-header>
          <v-expansion-panel-content>
            <div class="ma-1"></div>
            <v-row align="center" class="ma-0">
              <v-col cols="6">
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="human.serviceNameKor"
                      class="caption"
                      label="서비스명(한글)"
                      :prepend-icon="icons.mdiLightbulbOn"
                      outlined
                      dense
                      readonly
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="human.serviceNameEng"
                      class="caption"
                      label="서비스명(영문)"
                      :prepend-icon="icons.mdiLightbulbOn"
                      dense
                      outlined
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="human.tech"
                      class="caption"
                      label="기술"
                      :prepend-icon="icons.mdiLightbulbOnOutline"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="human.o2o"
                      class="caption"
                      label="O2O"
                      :prepend-icon="icons.mdiLink"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="human.serviceType"
                      class="caption"
                      label="서비스형태"
                      :prepend-icon="icons.mdiSelectPlace"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="human.serviceStatus"
                      class="caption"
                      label="서비스상태"
                      :prepend-icon="icons.mdiSelectSearch"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="human.largeField"
                      class="caption"
                      label="대분야"
                      :prepend-icon="icons.mdiCheck"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="human.businessType"
                      class="caption"
                      label="사업형태"
                      :prepend-icon="icons.mdiSelect"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="human.smallField"
                      class="caption"
                      label="소분야"
                      :prepend-icon="icons.mdiCheckAll"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-text-field
                      v-model="human.similarService"
                      class="caption"
                      label="유사서비스"
                      :prepend-icon="icons.mdiSelectCompare"
                      dense
                      outlined
                      readonly
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-col>
              <v-col cols="6">
                <v-row align="center">
                  <v-col cols="4" align="center">
                    <img
                      onerror="this.src='/null_logo.png'"
                      :src="human.serviceLogo"
                      alt="serviceLogo"
                      style="max-heght: 120px; max-width: 120px;"
                    />
                    <h5>{{ serviceLogoText }}</h5>
                  </v-col>
                  <v-col>
                    <a
                      style="cursor:pointer"
                      :href="human.serviceURL"
                      target="_blank"
                    >
                      <v-text-field
                        v-model="human.serviceURL"
                        class="caption"
                        label="서비스 url"
                        prepend-icon="mdi-dialpad"
                        dense
                        readonly
                      ></v-text-field
                    ></a>
                  </v-col>
                </v-row>
                <div style="margin: 25px;"></div>

                <v-textarea
                  v-model="human.serviceSummary"
                  class="caption"
                  label="서비스 설명"
                  :prepend-icon="icons.mdiCommentTextMultiple"
                  dense
                  readonly
                  outlined
                  rows="4"
                ></v-textarea
                ><v-textarea
                  v-model="human.patent"
                  class="caption"
                  label="특허"
                  :prepend-icon="icons.mdiBookMultipleOutline"
                  dense
                  readonly
                  outlined
                  rows="4"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel v-if="payOn">
          <v-expansion-panel-header
            >기업 투자유치 정보</v-expansion-panel-header
          >
          <v-expansion-panel-content v-if="human.invInfo === '02'">
            <div style="margin: 15px;"></div>
            투자실적 정보가 없습니다.
          </v-expansion-panel-content>

          <v-expansion-panel-content
            v-if="human.invInfo === '01' && !human.invInfoAddIntention"
          >
            <div style="margin: 15px;"></div>
            총 {{ humanInv.length }}건의 투자실적이 있으며 투자실적 정보가
            비공개 입니다.
          </v-expansion-panel-content>

          <v-expansion-panel-content
            v-if="human.invInfo === '01' && human.invInfoAddIntention"
          >
            <div style="margin: 15px;"></div>
            <v-row v-for="(item, i) in humanInv" :key="i">
              <v-col>투자실적 #{{ item.preInvTime }}</v-col>
              <v-col>
                <v-text-field
                  v-model="item.preInvDate"
                  class="caption"
                  prepend-icon=""
                  label="투자 날짜"
                  dense
                  readonly
                  outlined
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="item.preInvStage"
                  class="caption"
                  prepend-icon=""
                  label="투자 단계"
                  dense
                  readonly
                  outlined
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="item.preInvAmount"
                  class="caption"
                  prepend-icon=""
                  suffix="억원"
                  label="투자금액(억)"
                  dense
                  readonly
                  outlined
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="item.preInvestor"
                  class="caption"
                  prepend-icon=""
                  dense
                  label="투자자"
                  readonly
                  outlined
                ></v-text-field>
              </v-col> </v-row
            ><v-divider></v-divider>
            <v-row justify="center" no-gutters>
              <div class="chart">
                <component
                  :is="componentIs2"
                  :height="300"
                  :width="300"
                  :chartdata="chartdata2"
                  :options="chartOptions2"
                />
              </div>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </v-flex>
</template>

<script>
/* 항목별 아이콘 Import */
import {
  mdiAccount,
  mdiAccountMultiple,
  mdiWhiteBalanceIncandescent,
  mdiCellphoneBasic,
  mdiSmartCardOutline,
  mdiGenderMaleFemale,
  mdiArrangeSendBackward,
  mdiCurrencyKrw,
  mdiHeadQuestionOutline,
  mdiHeadAlertOutline,
  mdiAccountSupervisor,
  mdiAccountGroup,
  mdiLightbulbOn,
  mdiLightbulbOnOutline,
  mdiLink,
  mdiCheck,
  mdiCheckAll,
  mdiSelect,
  mdiSelectPlace,
  mdiSelectSearch,
  mdiSelectCompare,
  mdiCommentTextMultiple,
  mdiBookMultipleOutline
} from '@mdi/js'
/* 차트 컴포넌트 Import 도넛, Bar */
import statusChart from '../components/statusChart'
import invChart from '../components/invChart'
import category from '~/pages/sample/category'

export default {
  components: {
    // eslint-disable-next-line vue/no-unused-components
    statusChart,
    invChart
  },
  filters: {
    /* 기업분류 chip 표시하기 위한 필터 */
    coDivFilter(val) {
      let res = ''
      switch (val) {
        case '01':
          res = '개인사업자'
          break
        case '02':
          res = '중소기업'
          break
        case '03':
          res = '스타트업'
          break
        case '04':
          res = '이노비즈'
          break
        case '05':
          res = '메인비즈'
          break
        case '06':
          res = '혁신형중소기업'
          break
        case '07':
          res = '벤처인증'
          break
        case '08':
          res = '중견기업'
          break
        case '09':
          res = '대기업'
          break
        default:
          break
      }
      return res
    }
  },
  data() {
    return {
      payOn: false,
      cpnOn: false,
      componentIs1: null,
      componentIs2: null,
      icons: {
        mdiAccount,
        mdiAccountMultiple,
        mdiWhiteBalanceIncandescent,
        mdiCellphoneBasic,
        mdiSmartCardOutline,
        mdiGenderMaleFemale,
        mdiArrangeSendBackward,
        mdiCurrencyKrw,
        mdiHeadQuestionOutline,
        mdiHeadAlertOutline,
        mdiAccountSupervisor,
        mdiAccountGroup,
        mdiLightbulbOn,
        mdiLightbulbOnOutline,
        mdiLink,
        mdiCheck,
        mdiCheckAll,
        mdiSelect,
        mdiSelectPlace,
        mdiSelectSearch,
        mdiSelectCompare,
        mdiCommentTextMultiple,
        mdiBookMultipleOutline
      },
      inset: true,
      multiple: true,
      focusable: true,
      flat: true,
      hover: true,
      flap: false,
      panel: [],
      items: [
        { id: 'idA', name: '기업 기본 정보' },
        { id: 'idB', name: '기업 대표자 정보' },
        { id: 'idC', name: '기업 아이템 정보' },
        { id: 'idC', name: '기업 상태 정보' },
        { id: 'idD', name: '기업 투자유치 정보' }
      ],
      human: {
        regEMailID: null,
        regTel: null,
        regContPwd: null,
        coNameKor: null,
        coNameEng: null,
        foundedDate: null,
        coDiv: null,
        corpDiv: null,
        coStatus: null,
        coAddr: null,
        coEmail: null,
        coWeb: '웹사이트 정보가 없습니다.',
        coWeblink: null,
        coLogo: null,
        coTel: null,

        serviceLogo: null,

        hHDSerial: null,
        representativeNameKor: null,
        representativeNameEng: null,
        representativeTel: null,
        representativeNationality: null,
        representativeGender: null,
        representativeFounderSame: null,
        founderNameKor: null,
        coRepresentative: null,
        coRepresentativeNameKor: null,

        invTime: 0,
        invInfo: '01',
        invInfoAddIntention: 0
      },
      humanDiv: [],
      humanInv: [],

      /* 도넛차트 데이터 */
      chartdata1: {
        labels: ['자본', '자산', '부채'],
        datasets: [
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF'],
            data: [0, 0, 0]
          }
        ]
      },
      chartOptions1: {
        responsive: false,
        maintainAspectRatio: false
      },
      /* Bar차트 데이터 */
      chartdata2: {
        labels: [],
        datasets: [
          {
            label: '투자금(억)',
            backgroundColor: 'green',
            data: []
          }
        ]
      },
      chartOptions2: {
        responsive: false,
        maintainAspectRatio: false,
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }
          ],
          xAxes: [
            {
              gridLines: {
                display: true
              }
            }
          ]
        }
      },
      serviceLogoText: '<서비스 로고>',
      angel: {}
    }
  },
  computed: {
    tokenState() {
      return this.$store.state.payOn.payOn
    }
  },
  watch: {
    flap() {
      this.flap
        ? (this.panel = [...Array(this.items.length).keys()].map((k, i) => k))
        : (this.panel = [])
    },
    tokenState(newTokenState, oldTokenState) {
      this.payOn = newTokenState
    }
  },
  created() {
    let serial = 'c8dsXNN8tw430GF'

    /* 
      payOn 변수 값에 따라 유료정보 공개
      01. 로컬스토리지 확인 후 로그인 여부 확인
      02. 로컬스토리지 payOn Object 값에 따라 유료정보 유효성 검사
      비어있을경우 false, 결제정보가 있을 경우 false / true
      03. 결제보가 있을 경우 payOn.payOn 변수값이 true일 경우 유료정보 공개
    
    if (localStorage.getItem('payInfo') !== null) {
      const payInfo = JSON.parse(localStorage.getItem('payInfo'))
      this.payOn = this.isEmptyObject(payInfo) ? this.payOn : payInfo.payOn
    }
    */

    if (this.$route.query.hSerial) serial = this.$route.query.hSerial
    /* 
    ================================================================================================
      데이터 받아오기
    ================================================================================================
    */
    const hSerial = { hSerial: serial } /* TEST: 'c8dsXNN8tw430GF' */

    this.$axios
      .post('/api/human/detail', JSON.stringify(hSerial))
      .then((res) => {
        this.human = res.data[0][0]
        this.human.corpDiv = this.corpDivFilter(this.human.corpDiv)
        this.human.foundedDate = this.unixTimeFilter(this.human.foundedDate)
        this.human.representativeGender = this.genderFilter(
          this.human.representativeGender
        )
        this.humanDiv = res.data[1]

        this.hrefFilter()

        this.human.invStage = this.invStageFilter(this.human.invStage)
        this.human.prevYearSaleVolume = this.preSaleVolFilter(
          this.human.prevYearSaleVolume
        )

        const statusChartValue = [
          Number(this.human.capital.replace(/,/gi, '')),
          Number(this.human.totalAssets.replace(/,/gi, '')),
          Number(this.human.totalLiabilities.replace(/,/gi, ''))
        ]
        this.chartdata1.datasets[0].data = statusChartValue

        this.componentIs1 = statusChart

        if (res.data[3] !== null) {
          this.humanInv = res.data[3]
          console.log(this.humanInv)

          const labels = []
          const data = []

          for (const i in this.humanInv) {
            this.humanInv[i].preInvDate = this.unixTimeFilter(
              this.humanInv[i].preInvDate
            )

            this.humanInv[i].preInvStage = this.preInvStageFilter(
              this.humanInv[i].preInvStage
            )

            labels[i] = this.humanInv[i].preInvDate
            data[i] = this.humanInv[i].preInvAmount
          }

          this.chartdata2.labels = labels
          this.chartdata2.datasets[0].data = data
          this.componentIs2 = invChart
        }

        this.human.capital = this.cashTypeFiler(this.human.capital)
        this.human.totalAssets = this.cashTypeFiler(this.human.totalAssets)
        this.human.totalLiabilities = this.cashTypeFiler(
          this.human.totalLiabilities
        )

        this.human.tech = this.techFilter(this.human.tech)
        this.human.largeField = this.largeFieldFilter(this.human.largeField)
        this.human.o2o = this.o2oFilter(this.human.o2o)
        this.human.businessType = this.businessTypeFilter(
          this.human.businessType
        )
        this.human.serviceType = this.serviceTypeFilter(this.human.serviceType)
        this.human.serviceStatus = this.serviceStatusFilter(
          this.human.serviceStatus
        )

        this.confirmRegister(this.human.regEMailID)
      })
      .catch((err) => {
        console.error(err)
      })
  },
  mounted() {
    this.payOn = this.$store.state.payOn.payOn
    if (!this.setAdmin()) this.setInvestment()
  },
  methods: {
    setAdmin() {
      if (localStorage.getItem('account') !== null) {
        this.cpnOn = !!(localStorage.getItem('account') === 'admin')
      }
      return this.cpnOn
    },
    setInvestment() {
      if (localStorage.getItem('accountInfo') !== null) {
        const accountInfo = JSON.parse(localStorage.getItem('accountInfo'))
        this.cpnOn = !!accountInfo.accountCo
        this.angel = accountInfo
      }
    },
    confirmRegister(regEmaiId) {
      if (localStorage.getItem('accountInfo') !== null) {
        const accountInfo = JSON.parse(localStorage.getItem('accountInfo'))
        this.payOn = accountInfo.emailIdF === regEmaiId ? true : this.payOn
      }
    },
    prcsInvestment() {
      this.$router.push({
        path: '/investment/invReg',
        query: {
          angel: this.angel,
          human: this.human,
          invType: 'a0'
        }
      })
    },

    /* 
    ================================================================================================
      받아온 데이터 가공
    ================================================================================================
    */
    corpDivFilter(val) {
      const corpDivArr = category.corpDivArr

      let res = null
      for (const i in corpDivArr) {
        res = corpDivArr[i].value === val ? corpDivArr[i].text : res
      }

      return res
    },
    genderFilter(val) {
      if (val === 'm') {
        return '남자'
      } else {
        return '여자'
      }
    },
    unixTimeFilter(val) {
      const date = new Date(val + 1000)
        .toISOString()
        .slice(0, 19)
        .replace('T', ' ')
      return date.substring(0, 10)
    },
    hrefFilter() {
      const vm = this
      if (vm.human.coWeb) {
        if (vm.human.coWeb.includes('//')) {
          vm.human.coWeblink = vm.human.coWeb
        } else {
          vm.human.coWeblink = '//' + vm.human.coWeb
        }
      } else {
        vm.human.coWeblink = ''
        vm.human.coWeb = '웹사이트 정보가 없습니다.'
      }
    },
    invStageFilter(val) {
      const invStage = category.invStage

      let res = null
      for (const i in invStage) {
        res = invStage[i].value === val ? invStage[i].text : res
      }

      return res
    },
    preSaleVolFilter(val) {
      const prevYearSaleVolume = category.prevYearSaleVolume

      let res = null
      for (const i in prevYearSaleVolume) {
        res =
          prevYearSaleVolume[i].value === val ? prevYearSaleVolume[i].text : res
      }

      return res
    },
    techFilter(val) {
      const tech = category.tech

      let res = null
      for (const i in tech) {
        res = tech[i].value === val ? tech[i].text : res
      }

      return res
    },
    largeFieldFilter(val) {
      const largeField = category.largeField

      let res = null
      for (const i in largeField) {
        res = largeField[i].value === val ? largeField[i].text : res
      }

      return res
    },
    o2oFilter(val) {
      const o2o = category.o2o
      let res = null
      for (const i in o2o) {
        res = o2o[i].value === val ? o2o[i].text : res
      }

      return res
    },
    businessTypeFilter(val) {
      const businessType = category.businessType
      let res = null
      for (const i in businessType) {
        res = businessType[i].value === val ? businessType[i].text : res
      }

      return res
    },
    serviceTypeFilter(val) {
      const serviceType = category.serviceType
      let res = null
      for (const i in serviceType) {
        res = serviceType[i].value === val ? serviceType[i].text : res
      }

      return res
    },
    serviceStatusFilter(val) {
      const serviceStatus = category.serviceStatus
      let res = null
      for (const i in serviceStatus) {
        res = serviceStatus[i].value === val ? serviceStatus[i].text : res
      }

      return res
    },
    cashTypeFiler(val) {
      const str = val.toString()
      const pattern = /[^0-9]/

      let res = str.replace(pattern, '')
      res = res.replace(/,/g, '')
      res = res.replace(/\B(?=(\d{3})+(?!\d))/g, ',')

      return res
    },
    preInvStageFilter(val) {
      const preInvStage = category.preInvStage
      let res = null
      for (const i in preInvStage) {
        res = preInvStage[i].value === val ? preInvStage[i].text : res
      }

      return res
    },
    isEmptyObject(param) {
      return Object.keys(param).length === 0 && param.constructor === Object
    }
  }
}
</script>

<style>
.chart {
  display: block;
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  color: white;
}

.message {
  position: relative;
  top: 50%;
  left: 75%;
  transform: translate(-50%, -50%);
}
</style>
